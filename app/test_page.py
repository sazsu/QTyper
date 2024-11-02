from PyQt6.QtWidgets import QLabel, QWidget

from app.widgets.local_profile_button import LocalProfileButton
from app.widgets.mode_button import ModeButton
from app.widgets.reset_button import ResetButton
from app.widgets.settings_button import SettingsButton
from app.widgets.text_area import TextArea


class TestPage(QWidget):
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.initUI()

	def initUI(self):
		self.setGeometry(0, 0, self.parent().width(), self.parent().height())
		self.text_area = TextArea(self)

		self.reset_button = ResetButton(
			'app/assets/reset_light.svg', 'app/assets/reset_dark.svg', self
		)
		self.mode_button = ModeButton(
			'app/assets/mode_light.svg', 'app/assets/mode_dark.svg', self
		)
		self.local_profile_button = LocalProfileButton(
			'app/assets/local_profile_light.svg',
			'app/assets/local_profile_dark.svg',
			self,
		)
		self.settings_button = SettingsButton(
			'app/assets/settings_light.svg', 'app/assets/settings_dark.svg', self
		)

		self.mode_button.move(90, 0)
		self.local_profile_button.move(180, 0)
		self.settings_button.move(270, 0)

	def change_mode(self, mode: bool):
		for child in self.children():
			if not isinstance(child, (QLabel, TextArea)):  # ignore logo, text_area
				child.change_mode(mode)
