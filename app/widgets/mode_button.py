from app.widgets.base_icon_button import BaseIconButton


class ModeButton(BaseIconButton):
	def __init__(
		self, light_icon_path: str, dark_icon_path: str, parent, main_window
	):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.main_window = main_window
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# set mode of whole app
		# self -> TestPage -> QStackedWidget -> MainWindow
		self.main_window.change_interface_mode_db()
		self.main_window.set_interface_mode()
