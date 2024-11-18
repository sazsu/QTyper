from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton


class BaseIconButton(QPushButton):
	def __init__(self, light_icon_path, dark_icon_path, parent):
		super().__init__(text=None, parent=parent)
		self.icon_paths = {
			True: QIcon(light_icon_path),
			False: QIcon(dark_icon_path)
		}
		# prevent button from activating on keypress
		self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
		width, height = self.width(), self.height()
		self.setFixedSize(QSize(min(width, height), min(width, height)))
		self.set_icon(True)
	
	def resizeEvent(self, event) -> None:
		# super().resizeEvent(event)
		width, height = self.width(), self.height()
		self.setFixedSize(QSize(min(width, height), min(width, height)))
		self.adjust_icon_size()
	
	def adjust_icon_size(self) -> None:
		self.setIconSize(self.size())

	def set_icon(self, mode: bool):
		self.setIcon(self.icon_paths[mode])

	def set_mode(self, mode: bool):
		self.set_icon(mode)
