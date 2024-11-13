from app.widgets.base_icon_button import BaseIconButton


class CancelCrossButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		# close current window
		self.parent().close()
