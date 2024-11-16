import os

from PyQt6.QtWidgets import QFileDialog, QMessageBox


class SaveDialog(QFileDialog):
	def __init__(self, parent) -> None:
		super().__init__(parent)
		self.setStyleSheet('font-size: 16px')

	def getSaveFileName(self):
		file_name, _ = super().getSaveFileName(
			self,
			'Select Output File',
			filter='.csv'
		)
		if file_name and not file_name.endswith('.csv'):
			file_name = self.generate_correct_file_name(file_name)
			reply = QMessageBox.question(
				self,
				'Confirm File Extension?',
				f'Selected file does not have a .csv extension, '
				f'do you want to save it as {os.path.split(file_name)[-1]}?',
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
			)
			if reply == QMessageBox.StandardButton.No:
				return ''
		return file_name

	@staticmethod
	def generate_correct_file_name(file_name: str) -> str:
		head = file_name.rsplit('.', maxsplit=1)[0]
		return f'{head}.csv'
