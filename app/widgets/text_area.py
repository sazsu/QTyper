from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QFont, QTextDocument
from PyQt6.QtWidgets import QLabel, QWidget

from app.config import Config
from app.managers.statistics_manager import StatsManager
from app.managers.text_manager import TextManager


class TextArea(QWidget):
	def __init__(self, parent) -> None:
		super().__init__(parent=parent)
		self.setGeometry(0, 0, self.parent().width(), 500)

		# set focus to listen keyboard
		self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

		# init text manager
		self.text_manager = TextManager(Config.en_words, Config.ru_words)

		# init stats manager
		self.stats_manager = StatsManager(self.text_manager)
		self.initUI()

	def initUI(self) -> None:
		font = QFont()
		font.setPointSize(24)

		self.document = QTextDocument()
		self.document.setDefaultFont(font)

		self.display = QLabel('', self)
		self.display.setGeometry(0, 0, self.width(), self.height())
		self.reset_test()

	def keyPressEvent(self, event: QEvent) -> None:
		if event.key() not in self.text_manager.KEYS_TO_LISTEN:
			return
		if event.key() == Qt.Key.Key_Backspace:
			self.text_manager.handle_backspace()
		elif event.key() == Qt.Key.Key_Space:
			self.text_manager.handle_space()
		else:
			if not self.started:
				self.started = True
				self.stats_manager.start()  # start gathering stats
			self.text_manager.handle_char(event.text())
		self.update_display()

	def update_display(self) -> None:
		self.text_manager.update_highlighted_text()
		self.text_manager.add_caret()
		self.document.setHtml(self.text_manager.generate_display_text())
		self.text_manager.remove_caret()
		self.display.setText(self.document.toHtml())

	def reset_test(self):
		self.started = False
		self.text_manager.reset()
		self.update_display()
