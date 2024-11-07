from app.widgets.base_icon_button import BaseIconButton


class ModeButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# change mode of whole app
		# self -> TestPage -> QStackedWidget -> MainWindow
		self.parent().parent().parent().change_mode()
