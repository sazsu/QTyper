from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from app.scripts.get_app_path import get_app_path
from app.scripts.get_assets_path import get_assets_path


class BaseIconButton(QPushButton):
	def __init__(self, light_icon_name, dark_icon_name, parent):
		super().__init__(text=None, parent=parent)
		app_path = get_app_path()
		assets_path = get_assets_path(app_path)

		self.icon_paths = {
			True: QIcon(str(assets_path / light_icon_name)),
			False: QIcon(str(assets_path / dark_icon_name))
		}
		# prevent button from activating on keypress
		self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
		width, height = self.width(), self.height()
		self.setFixedSize(QSize(min(width, height), min(width, height)))
		self.set_icon(True)

	def resizeEvent(self, event) -> None:
		width, height = self.width(), self.height()
		self.setFixedSize(QSize(min(width, height), min(width, height)))
		self.adjust_icon_size()

	def adjust_icon_size(self) -> None:
		self.setIconSize(self.size())

	def set_icon(self, mode: bool):
		self.setIcon(self.icon_paths[mode])

	def set_mode(self, mode: bool):
		self.set_icon(mode)
