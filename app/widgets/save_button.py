from app.widgets.base_icon_button import BaseIconButton
from app.widgets.save_dialog import SaveDialog


class SaveButton(BaseIconButton):
	def __init__(self, light_icon_name: str, dark_icon_name: str, parent):
		super().__init__(light_icon_name, dark_icon_name, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self) -> None:
		file_name = SaveDialog(self).getSaveFileName()
		if not file_name:  # canceled
			return
		self.export_stats(file_name)

	def export_stats(self, file_name: str) -> None:
		with open(file_name, 'w') as f:
			f.write('wpm,accuracy\n')
			for wpm, acc in zip(*self.parent().db_manager.fetch_all_test_stats()):
				f.write(f'{wpm},{acc}\n')
