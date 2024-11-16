from PyQt6.QtWidgets import QWidget

from app.ui.local_profile_page_ui import Ui_Form


class LocalProfilePage(QWidget, Ui_Form):
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.main_window = parent
		self.setupUi(self)

		self.cancel_cross_button.clicked.connect(
			lambda s: self.main_window.pages.setCurrentIndex(0)
		)

	def initUI(self) -> None:
		pass

	def set_mode(self, mode: bool) -> None:
		for button in self.buttonGroup.buttons():
			button.set_mode(mode)
