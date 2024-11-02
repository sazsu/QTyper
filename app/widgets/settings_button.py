from app.widgets.base_icon_button import BaseIconButton


class SettingsButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.btn.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# open test settings
		pass