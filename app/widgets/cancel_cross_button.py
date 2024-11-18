from app.widgets.base_icon_button import BaseIconButton


class CancelCrossButton(BaseIconButton):
	def __init__(self, light_icon_name: str, dark_icon_name: str, parent):
		super().__init__(light_icon_name, dark_icon_name, parent)
