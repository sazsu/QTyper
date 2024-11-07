from PyQt6.QtWidgets import QLabel, QWidget, QButtonGroup

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
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		print([(w.objectName(), w.geometry() )for w in self.children()])
		print(self.ui.reset_button.geometry())
		self.ui.mode_button.setVisible(True)
		self.initUI()
		# self.setLayout(self.ui.verticalLayout)
		self.update()

	def initUI(self):
		
		# print(self.ui.reset_button.geometry(), self.ui.reset_button.isVisible())
		# self.ui.reset_button.move(500, 500)
		# self.ui.reset_button.setVisible(True)
		# print(self.ui.reset_button.geometry(), self.ui.reset_button.isVisible())

		# self.ui.mode_button.setVisible(True)
		# self.ui.local_profile_button.setVisible(True)
		# self.ui.settings_button.setVisible(True)
		# self.ui.reset_button = ResetButton(
		# 	'app/assets/reset_light.svg', 'app/assets/reset_dark.svg', self
		# )
		# self.ui.mode_button = ModeButton(
		# 	'app/assets/mode_light.svg', 'app/assets/mode_dark.svg', self
		# )
		# self.ui.local_profile_button = LocalProfileButton(
		# 	'app/assets/local_profile_light.svg',
		# 	'app/assets/local_profile_dark.svg',
		# 	self,
		# )
		# self.ui.settings_button = SettingsButton(
		# 	'app/assets/settings_light.svg', 'app/assets/settings_dark.svg', self
		# )
		# self.ui.reset_button.move(200, 0)
		# self.ui.mode_button.move(300, 0)
		# self.ui.local_profile_button.move(400, 0)
		# self.ui.settings_button.move(500, 0)

		self.ui.buttonGroup = QButtonGroup(self)
		# self.ui.buttonGroup.addButton(self.ui.reset_button)
		# self.ui.buttonGroup.addButton(self.ui.mode_button)
		# self.ui.buttonGroup.addButton(self.ui.local_profile_button)
		# self.ui.buttonGroup.addButton(self.ui.settings_button)

		# self.ui.main_container.addWidget(TextArea(self, self))

	def change_mode(self, mode: bool):
		# print(self.ui.reset_button.__class__.__name__)
		for b in self.ui.buttonGroup.buttons():
			print(b.__class__.__name__)
			print(b.isVisible(), b.geometry())
			b.change_mode(mode)
		# for i in range(self.ui.main_container.count()):
			# self.ui.main_container.widget(i).change_mode(mode)

	def show_line_chart(self, wpm_arr, acc_arr) -> None:
		self.text_area.setVisible(False)
		self.text_area.reset_test()

		self.chart.set_values(wpm_arr, acc_arr)
		self.chart.setVisible(True)
