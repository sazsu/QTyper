from app.widgets.base_icon_button import BaseIconButton


class LocalProfileButton(BaseIconButton):
	def __init__(self, light_icon_name: str, dark_icon_name: str, parent):
		super().__init__(light_icon_name, dark_icon_name, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# open local profile
		self.parent().main_window.pages.setCurrentIndex(1)  # local profile
		self.parent().main_window.pages.widget(1).display_values()
		# display text area
		self.parent().main_window.pages.widget(0).main_container.setCurrentIndex(0)
