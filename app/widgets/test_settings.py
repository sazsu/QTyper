from typing import Tuple

from PyQt6.QtWidgets import QDialog

from app.config import Config
from app.ui.test_settings import Ui_Form


class TestSettings(QDialog):
	def __init__(self, db_manager, test_page) -> None:
		super().__init__()
		self.text_area = test_page.text_area
		self.text_manager = test_page.text_area.text_manager
		self.stats_manager = test_page.text_area.stats_manager
		self.db_manager = db_manager

		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.cancelCrossButton.clicked.connect(lambda c: self.close())
		
		mode, lang = self.text_manager.get_test_settings()
		self.ui.langComboBox.setCurrentText(lang)
		self.ui.modeComboBox.setCurrentText(str(mode))

		self.finished.connect(self.on_closed)  # update db only when window is closed

	def on_closed(self):
		new_test_settings = self.get_new_test_settings()
		if new_test_settings != self.text_manager.get_test_settings():
			self.text_manager.set_test_settings(*new_test_settings)
			self.stats_manager.set_test_time(new_test_settings[0])
			self.text_area.reset_test()
			self.db_manager.set_test_settings(*new_test_settings)

	def get_new_test_settings(self) -> Tuple[int, str]:
		return (
			int(self.ui.modeComboBox.currentText()),
			self.ui.langComboBox.currentText()
		)

	def set_mode(self, mode: bool) -> None:
		if mode:
			bg_color = Config.white
			text_color = Config.black
		else:
			bg_color = Config.black
			text_color = Config.white
		self.setStyleSheet(f'background: {bg_color}; color: {text_color}')
		self.ui.cancelCrossButton.set_mode(mode)
