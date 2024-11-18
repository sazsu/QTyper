from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow

from app.config import Config
from app.managers.database_manager import DatabaseManager
from app.pages.local_profile_page import LocalProfilePage
from app.pages.test_page import TestPage
from app.scripts.get_app_path import get_app_path
from app.scripts.get_assets_path import get_assets_path
from app.ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self) -> None:
		super().__init__()
		app_path = get_app_path()
		assets_path = get_assets_path(app_path)
		self.icon_paths = {
			True: QIcon(str(assets_path / 'logo_light.svg')),
			False: QIcon(str(assets_path / 'logo_dark.svg'))
		}
		self.setupUi(self)

		self.db_manager = DatabaseManager('app.sqlite3')
		self.interface_mode = self.db_manager.get_interface_mode()

		test_page = TestPage(self.db_manager, self)
		local_profile_page = LocalProfilePage(self.db_manager, self)

		self.pages.addWidget(test_page)
		self.pages.addWidget(local_profile_page)

		self.pages.setCurrentWidget(test_page)

		self.set_interface_mode()

	def set_interface_mode(self) -> None:
		self.setStyleSheet(
			Config.app_light if self.interface_mode else Config.app_dark
		)
		self.setWindowIcon(self.icon_paths[self.interface_mode])
		self.pages.widget(0).set_mode(self.interface_mode)
		self.pages.widget(1).set_mode(self.interface_mode)

	def change_interface_mode_db(self) -> None:
		self.interface_mode = not self.interface_mode
		self.db_manager.set_interface_mode(int(self.interface_mode))
