from app.widgets.base_icon_button import BaseIconButton


class ModeButton(BaseIconButton):
	def __init__(
		self, light_icon_name: str, dark_icon_name: str, parent, main_window
	):
		super().__init__(light_icon_name, dark_icon_name, parent)
		self.main_window = main_window
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# set mode of whole app
		self.main_window.change_interface_mode_db()
		self.main_window.set_interface_mode()
