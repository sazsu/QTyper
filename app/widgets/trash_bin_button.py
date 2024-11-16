from app.widgets.base_icon_button import BaseIconButton
from app.widgets.clear_data_pop_up import ClearDataPopUp


class TrashBinButton(BaseIconButton):
	def __init__(self, light_icon_path: str, dark_icon_path: str, parent):
		super().__init__(light_icon_path, dark_icon_path, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		ClearDataPopUp(self.parent()).exec()
