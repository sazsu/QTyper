from PyQt6.QtWidgets import QWidget

from app.ui.local_profile_page_ui import Ui_Form


class LocalProfilePage(QWidget):
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.main_window = parent
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.ui.cancel_cross_button.clicked.connect(
			lambda s: self.main_window.ui.pages.setCurrentIndex(0)
		)

	def initUI(self) -> None:
		pass

	def set_mode(self, mode: bool) -> None:
		for button in self.ui.buttonGroup.buttons():
			button.set_mode(mode)
