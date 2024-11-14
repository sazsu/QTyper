from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QFont, QTextDocument
from PyQt6.QtWidgets import QWidget

from app.managers.statistics_manager import StatsManager
from app.managers.text_manager import TextManager
from app.ui.text_area_ui import Ui_Form


class TextArea(QWidget):
	def __init__(self, db_manager, parent) -> None:
		super().__init__(parent=parent)
		self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		# init text manager
		self.text_manager = TextManager(db_manager)

		# init stats manager
		self.stats_manager = StatsManager(db_manager, parent)

		self.text_manager.stats_manager = self.stats_manager
		self.stats_manager.text_manager = self.text_manager
		self.stats_manager.set_test_time(self.text_manager.mode)
		self.initUI()

	def initUI(self) -> None:
		font = QFont('monospace')
		font.setPointSize(24)

		self.document = QTextDocument()
		self.document.setDefaultFont(font)

		self.reset_test()

	def keyPressEvent(self, event: QEvent) -> None:
		if not self.isVisible():
			return
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
		(
			first_row_text,
			second_row_text,
			third_row_text
		) = self.text_manager.generate_display_text()

		self.document.setHtml(first_row_text)
		self.ui.first_row_display.setText(self.document.toHtml())

		self.document.setHtml(second_row_text)
		self.ui.second_row_display.setText(self.document.toHtml())

		self.document.setHtml(third_row_text)
		self.ui.third_row_display.setText(self.document.toHtml())

		self.text_manager.remove_caret()

	def reset_test(self):
		self.started = False
		self.text_manager.reset()
		self.stats_manager.reset()
		self.update_display()
