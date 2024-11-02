from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtCore import Qt


class BaseIconButton(QWidget):
	def __init__(self, light_icon_path, dark_icon_path, parent):
		super().__init__(parent=parent)
		self.icon_paths = {
			True: QIcon(light_icon_path),
			False: QIcon(dark_icon_path)
		}
		self.initUI()

	def initUI(self):
		self.btn = QPushButton('', self)
		self.btn.setGeometry(0, 0, 75, 75)
		self.set_icon(True)
		self.btn.setIconSize(QSize(75, 75))
		# prevent button from activating on keypress
		self.btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

	def set_icon(self, mode: bool):
		self.btn.setIcon(self.icon_paths[mode])

	def change_mode(self, mode: bool):
		self.set_icon(mode)
