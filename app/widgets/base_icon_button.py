from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QWidget


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
		self.btn.setGeometry(0, 0, 90, 90)
		self.set_icon()
		self.btn.setIconSize(QSize(90, 90))

	# self -> ParentClass -> QStackedWidget -> MainWindow
	def set_icon(self):
		pass

	def change_mode(self):
		pass
