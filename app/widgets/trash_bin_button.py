from app.widgets.base_icon_button import BaseIconButton
from app.widgets.clear_data_pop_up import ClearDataPopUp


class TrashBinButton(BaseIconButton):
	def __init__(self, light_icon_name: str, dark_icon_name: str, parent):
		super().__init__(light_icon_name, dark_icon_name, parent)
		self.clicked.connect(self.btn_handler)

	def btn_handler(self):
		ClearDataPopUp(self.parent()).exec()
