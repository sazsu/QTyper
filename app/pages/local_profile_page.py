from PyQt6.QtWidgets import QWidget

from app.ui.local_profile_page_ui import Ui_Form


class LocalProfilePage(QWidget, Ui_Form):
	def __init__(self, db_manager, parent):
		super().__init__(parent=parent)
		self.main_window = parent
		self.db_manager = db_manager
		self.setupUi(self)

		self.cancel_cross_button.clicked.connect(
			lambda s: self.main_window.pages.setCurrentIndex(0)
		)

	def set_mode(self, mode: bool) -> None:
		for button in self.buttonGroup.buttons():
			button.set_mode(mode)
		self.chart.set_mode(mode)

	def display_values(self) -> None:
		wpm_arr, acc_arr = self.db_manager.fetch_all_test_stats()
		self.chart.set_values(wpm_arr, acc_arr)
		self.chart.render()
