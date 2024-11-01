from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from app.local_profile_page import LocalProfile
from app.test_page import TestPage


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.pages = QStackedWidget(self)  # add pages here

		# maximum resolution available
		self.setGeometry(QApplication.primaryScreen().availableGeometry())

		self.mode = True  # light mode by default

		self.pages.addWidget(TestPage(self.pages))
		self.pages.addWidget(LocalProfile(self.pages))

		self.pages.setCurrentIndex(0)  # test page

		self.pages.setGeometry(0, 0, 1920, 1080)

	def change_mode(self):
		self.mode = not self.mode
		for page in self.pages:
			page.change_mode()
