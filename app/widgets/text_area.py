from random import sample

from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QFont, QTextDocument
from PyQt6.QtWidgets import QLabel, QWidget

from app.config import Config


class TextArea(QWidget):
	def __init__(self, parent) -> None:
		super().__init__(parent=parent)
		self.KEYS_TO_LISTEN = {
			Qt.Key.Key_A,
			Qt.Key.Key_B,
			Qt.Key.Key_C,
			Qt.Key.Key_D,
			Qt.Key.Key_E,
			Qt.Key.Key_F,
			Qt.Key.Key_G,
			Qt.Key.Key_H,
			Qt.Key.Key_I,
			Qt.Key.Key_J,
			Qt.Key.Key_K,
			Qt.Key.Key_L,
			Qt.Key.Key_M,
			Qt.Key.Key_N,
			Qt.Key.Key_O,
			Qt.Key.Key_P,
			Qt.Key.Key_Q,
			Qt.Key.Key_R,
			Qt.Key.Key_S,
			Qt.Key.Key_T,
			Qt.Key.Key_U,
			Qt.Key.Key_V,
			Qt.Key.Key_W,
			Qt.Key.Key_X,
			Qt.Key.Key_Y,
			Qt.Key.Key_Z,
			Qt.Key.Key_1,
			Qt.Key.Key_2,
			Qt.Key.Key_3,
			Qt.Key.Key_4,
			Qt.Key.Key_5,
			Qt.Key.Key_6,
			Qt.Key.Key_7,
			Qt.Key.Key_8,
			Qt.Key.Key_9,
			Qt.Key.Key_0,
			Qt.Key.Key_Backspace,
			Qt.Key.Key_Space,
		}
		self.green_format = '<span style="color: #5cb200;">{}</span>'
		self.red_format = '<span style="color: #ff506e;">{}</span>'

		self.setGeometry(0, 0, 500, 500)
		self.load_language_words()
		self.load_base_words()

		# set focus to listen keyboard
		self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

		self.initUI()
		self.reset_test()

	def load_base_words(self) -> None:
		self.base_words = list(self.en_words)

	def initUI(self) -> None:
		font = QFont()
		font.setPointSize(12)

		self.document = QTextDocument()
		self.document.setDefaultFont(font)

		self.display = QLabel('', self)
		self.display.setGeometry(0, 0, 500, 500)
		self.reset_test()

	def get_coords(self):
		return self.current_word_index, self.current_char_index

	def update_coords(self, new_word_index: int, new_char_index: int):
		self.current_word_index = new_word_index
		self.current_char_index = new_char_index

	def handle_backspace(self) -> None:
		word_idx, char_idx = self.get_coords()

		if char_idx >= 0:
			self.user_text[word_idx].pop()
			self.update_coords(word_idx, char_idx - 1)
		elif char_idx == -1 and word_idx > 0:
			self.update_coords(
				word_idx - 1,
				len(self.user_text[word_idx - 1]) - 1
			)
		# do not change anything if caret is at first word's first symbol

	def handle_space(self) -> None:
		word_idx, char_idx = self.get_coords()
		if char_idx >= 0:  # not an empty word
			self.update_coords(word_idx + 1, -1)

	def handle_symbol(self, symbol: str) -> None:
		word_idx, char_idx = self.get_coords()
		self.user_text[word_idx].append(symbol)
		self.update_coords(word_idx, char_idx + 1)

	def update_display(self) -> None:
		word_idx, char_idx = self.get_coords()

		self.update_highlighted_text(word_idx)

		# add caret symbol
		self.add_caret(word_idx, char_idx)

		self.document.setHtml(
			' '.join(
				''.join(word) for word in self.highlighted_text
				)
			)

		# remove caret symbol
		self.remove_caret(word_idx, char_idx)

		self.display.setText(self.document.toHtml())

	def update_highlighted_text(self, word_idx: int) -> None:
		self.highlighted_text[word_idx] = self.highlight_word(word_idx)

	def highlight_word(self, word_idx: int) -> list[str]:
		word = self.user_text[word_idx].copy()
		target_word = self.target_text[word_idx]

		# color (green or red) all symbol in word in one loop
		for i in range(len(word)):
			if i < len(target_word) and target_word[i] == word[i]:
				word[i] = self.green_format.format(word[i])
			else:
				word[i] = self.red_format.format(word[i])

		# word is not fully typed -> add missing characters (placeholder color)
		for i in range(len(word), len(target_word)):
			word.append(target_word[i])
		return word

	def add_caret(self, word_idx: int, char_idx: int) -> None:
		self.highlighted_text[word_idx].insert(char_idx + 1, '|')

	def remove_caret(self, word_idx: int, char_idx: int) -> None:
		self.highlighted_text[word_idx].pop(char_idx + 1)

	def keyPressEvent(self, event: QEvent) -> None:
		if event.key() not in self.KEYS_TO_LISTEN:
			return
		if event.key() == Qt.Key.Key_Backspace:
			self.handle_backspace()
		elif event.key() == Qt.Key.Key_Space:
			self.handle_space()
		else:
			self.handle_symbol(event.text())
		self.update_display()

	def reset_test(self) -> None:
		self.current_word_index = 0
		self.current_char_index = -1

		self.generate_text()

		self.update_display()

	def generate_text(self) -> None:
		self.target_text = sample(self.base_words, len(self.base_words))
		self.user_text = {i: [] for i in range(len(self.target_text))}
		self.highlighted_text = [list(word) for word in self.target_text]

	def change_mode(self) -> None:
		# self -> TestPage -> QStackedWidget -> MainWindow
		pass

	def load_language_words(self) -> None:
		self.en_words = Config.en_words
		self.ru_words = Config.ru_words
