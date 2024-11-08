from PyQt6.QtWidgets import QLabel, QWidget, QButtonGroup
from PyQt6.QtGui import QIcon

from app.widgets.line_chart import LineChart
from app.widgets.local_profile_button import LocalProfileButton
from app.widgets.mode_button import ModeButton
from app.widgets.reset_button import ResetButton
from app.widgets.settings_button import SettingsButton
from app.widgets.text_area import TextArea

from app.ui.test_page_ui import Ui_Form


class TestPage(QWidget):
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.main_window = parent
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.text_area = TextArea(self, self)
		self.chart = LineChart(self)
		
		self.ui.main_container.addWidget(self.text_area)
		self.ui.main_container.addWidget(self.chart)

	def change_mode(self, mode: bool):
		for button in self.ui.buttonGroup.buttons():
			button.change_mode(mode)
		self.chart.change_mode(mode)

	def show_line_chart(self, wpm_arr, acc_arr) -> None:
		self.ui.main_container.setCurrentWidget(self.chart)
		self.text_area.reset_test()

		self.chart.set_values(wpm_arr, acc_arr)
