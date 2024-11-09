from PyQt6.QtWidgets import QWidget

from app.ui.test_page_ui import Ui_Form
from app.widgets.line_chart import LineChart
from app.widgets.text_area import TextArea


class TestPage(QWidget):
	def __init__(self, db_manager, parent):
		super().__init__(parent=parent)
		self.main_window = parent
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.text_area = TextArea(db_manager, self)
		self.chart = LineChart(self)

		self.ui.main_container.addWidget(self.text_area)
		self.ui.main_container.addWidget(self.chart)

	def set_mode(self, mode: bool):
		for button in self.ui.buttonGroup.buttons():
			button.set_mode(mode)
		self.chart.set_mode(mode)

	def show_line_chart(self, wpm_arr, acc_arr) -> None:
		self.ui.main_container.setCurrentWidget(self.chart)
		self.text_area.reset_test()

		self.chart.set_values(wpm_arr, acc_arr)
