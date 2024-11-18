from PyQt6.QtWidgets import QWidget

from app.ui.test_page_ui import Ui_Form
from app.widgets.line_chart import LineChart
from app.widgets.test_settings import TestSettings
from app.widgets.text_area import TextArea


class TestPage(QWidget, Ui_Form):
	def __init__(self, db_manager, parent) -> None:
		super().__init__(parent=parent)
		self.main_window = parent
		self.setupUi(self)

		self.text_area = TextArea(db_manager, self)
		self.chart = LineChart(self)

		self.test_settings = TestSettings(db_manager, self)

		self.main_container.addWidget(self.text_area)
		self.main_container.addWidget(self.chart)

	def set_mode(self, mode: bool) -> None:
		for button in self.buttonGroup.buttons():
			button.set_mode(mode)
		self.chart.set_mode(mode)
		self.test_settings.set_mode(mode)

	def show_line_chart(self, wpm_arr, acc_arr) -> None:
		self.main_container.setCurrentWidget(self.chart)
		self.text_area.reset_test()
		self.chart.set_values(wpm_arr, acc_arr)
		self.chart.render()
