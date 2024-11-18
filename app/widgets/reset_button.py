from app.widgets.base_icon_button import BaseIconButton


class ResetButton(BaseIconButton):
	def __init__(self, light_icon_name: str, dark_icon_name: str, parent):
		super().__init__(light_icon_name, dark_icon_name, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		if self.parent().main_container.currentIndex() == 0:  # textarea
			self.parent().text_area.reset_test()
		else:
			self.parent().main_container.setCurrentIndex(0)
