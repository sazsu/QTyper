from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton


class BaseIconButton(QPushButton):
	def __init__(self, light_icon_path, dark_icon_path, parent):
		super().__init__(text=None, parent=parent)
		self.icon_paths = {
			True: QIcon(light_icon_path),
			False: QIcon(dark_icon_path)
		}
		self.initUI()
		# prevent button from activating on keypress
		self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

	def initUI(self):
		self.set_icon(True)

	def set_icon(self, mode: bool):
		self.setIcon(self.icon_paths[mode])

	def set_mode(self, mode: bool):
		self.set_icon(mode)
