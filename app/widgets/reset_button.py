from app.widgets.base_icon_button import BaseIconButton


class ResetButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		if self.parent().main_container.currentIndex() == 0:  # textarea
			self.parent().text_area.reset_test()
		else:
			self.parent().main_container.setCurrentIndex(0)
