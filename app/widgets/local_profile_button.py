from app.widgets.base_icon_button import BaseIconButton


class LocalProfileButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# open local profile
		self.parent().main_window.pages.setCurrentIndex(1)  # local profile
		self.parent().text_area.reset_test()
