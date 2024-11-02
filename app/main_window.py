from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from app.config import Config
from app.local_profile_page import LocalProfile
from app.test_page import TestPage


class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.initUI()

	def initUI(self) -> None:
		# maximum resolution available
		self.setGeometry(QApplication.primaryScreen().availableGeometry())

		self.pages = QStackedWidget(self)  # add pages here
		self.pages.setGeometry(0, 0, self.width(), self.height())
		
		self.pages.addWidget(TestPage(self.pages))
		self.pages.addWidget(LocalProfile(self.pages))

		self.pages.setCurrentIndex(0)  # test page

		self.pages.widget(0).setGeometry(0, 0, self.width(), self.height())

		self.mode = False  # light mode by default
		self.change_mode()

	def change_mode(self) -> None:
		self.mode = not self.mode
		self.setStyleSheet(Config.app_light if self.mode else Config.app_dark)
		for i in range(self.pages.count()):
			self.pages.widget(i).change_mode(self.mode)
