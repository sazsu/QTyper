from PyQt6.QtWidgets import QMainWindow

from app.config import Config
from app.local_profile_page import LocalProfilePage
from app.managers.database_manager import DatabaseManager
from app.test_page import TestPage
from app.ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.db_manager = DatabaseManager('app.sqlite3')
		self.interface_mode = self.db_manager.get_interface_mode()

		test_page = TestPage(self.db_manager, self)

		self.ui.pages.addWidget(test_page)
		self.ui.pages.setCurrentWidget(test_page)

		self.set_interface_mode()

	def set_interface_mode(self) -> None:
		self.setStyleSheet(
			Config.app_light if self.interface_mode else Config.app_dark
		)
		self.ui.pages.widget(0).set_mode(self.interface_mode)

	def change_interface_mode_db(self) -> None:
		self.interface_mode = not self.interface_mode
		self.db_manager.set_interface_mode(int(self.interface_mode))
