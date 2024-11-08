from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from app.config import Config
from app.local_profile_page import LocalProfile
from app.test_page import TestPage
from app.ui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		test_page = TestPage(self)
		self.ui.pages.addWidget(test_page)
		self.ui.pages.setCurrentWidget(test_page)
		self.mode = False
		self.change_mode()

	def change_mode(self) -> None:
		self.mode = not self.mode
		self.setStyleSheet(Config.app_light if self.mode else Config.app_dark)
		self.ui.pages.widget(0).change_mode(self.mode)
		# self.ui.pages.widget(1).change_mode(mode)
