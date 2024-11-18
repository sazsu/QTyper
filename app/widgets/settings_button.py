from app.widgets.base_icon_button import BaseIconButton


class SettingsButton(BaseIconButton):
	def __init__(self, light_icon_name: str, dark_icon_name: str, parent):
		super().__init__(light_icon_name, dark_icon_name, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# open test settings
		# block event loop
		self.parent().test_settings.exec()
