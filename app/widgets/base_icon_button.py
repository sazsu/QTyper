from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QWidget


class BaseIconButton(QPushButton):
	def __init__(self, light_icon_path, dark_icon_path, parent):
		super().__init__(text=None, parent=parent)
		self.icon_paths = {
			True: QIcon(light_icon_path),
			False: QIcon(dark_icon_path)
		}
		self.initUI()
		self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

	def initUI(self):
		self.setGeometry(0, 0, 75, 75)
		self.set_icon(True)
		self.setIconSize(QSize(75, 75))
		# prevent button from activating on keypress

	def set_icon(self, mode: bool):
		self.setIcon(self.icon_paths[mode])

	def change_mode(self, mode: bool):
		self.set_icon(mode)
