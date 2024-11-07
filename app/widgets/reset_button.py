from app.widgets.base_icon_button import BaseIconButton


class ResetButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		if self.parent().text_area.isVisible() is True:
			self.parent().text_area.reset_test()
		else:  # showing a chart -> test was reseted chart was shown
			self.parent().chart.setVisible(False)
			self.parent().text_area.setVisible(True)
