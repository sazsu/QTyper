from random import sample
from typing import List, Tuple

from app.config import Config


class TextManager:
	def __init__(self, words_en: List[str], words_ru: List[str]) -> None:
		self.lang_words = {0: words_en, 1: words_ru}
		self.curr_words_lang = 0  # pull from db
		self.correct_format = Config.correct_format
		self.wrong_format = Config.wrong_format
		self.KEYS_TO_LISTEN = Config.keys_to_listen
		self.reset()

	def reset(self):
		self.target_text = sample(
			self.lang_words[self.curr_words_lang],
			200,  # length is always 200
		)  # multiply by coeff (mode selected)
		self.user_text = {i: [] for i in range(len(self.target_text))}
		self.highlighted_text = [list(word) for word in self.target_text]
		self.current_word_index = 0
		self.current_char_index = -1
		self.correct_words = set()

	def get_coords(self) -> Tuple[int, int]:
		return self.current_word_index, self.current_char_index

	def update_coords(self, new_word_index: int, new_char_index: int) -> None:
		self.current_word_index = new_word_index
		self.current_char_index = new_char_index

	def handle_backspace(self) -> None:
		word_idx, char_idx = self.get_coords()

		if char_idx >= 0:
			self.user_text[word_idx].pop()
			self.remove_correct_word(word_idx)
			self.update_coords(word_idx, char_idx - 1)
		# do not backspace if previous word was correctly typed
		elif (
			char_idx == -1
			and word_idx > 0
			and word_idx - 1 not in self.correct_words
		):
			self.update_coords(word_idx - 1, len(self.user_text[word_idx - 1]) - 1)
		# do not change anything if caret is at first word's first symbol

	def handle_space(self) -> None:
		word_idx, char_idx = self.get_coords()
		if char_idx >= 0:  # not an empty word
			is_word_correct = self.check_is_word_correct(word_idx)
			if is_word_correct:
				self.correct_words.add(word_idx)
			self.update_coords(word_idx + 1, -1)

	def handle_char(self, char: str) -> None:
		word_idx, char_idx = self.get_coords()
		self.user_text[word_idx].append(char)
		self.update_coords(word_idx, char_idx + 1)

	def update_highlighted_text(self) -> None:
		word_idx, _ = self.get_coords()
		self.highlighted_text[word_idx] = self.highlight_word(word_idx)

	def highlight_word(self, word_idx: int) -> List[str]:
		word = self.user_text[word_idx].copy()
		target_word = self.target_text[word_idx]

		# color (green or red) all symbol in word in one loop
		for i in range(len(word)):
			if i < len(target_word) and target_word[i] == word[i]:
				word[i] = self.correct_format.format(word[i])
			else:
				word[i] = self.wrong_format.format(word[i])

		# word is not fully typed -> add missing characters (placeholder color)
		for i in range(len(word), len(target_word)):
			word.append(target_word[i])
		return word

	def add_caret(self) -> None:
		word_idx, char_idx = self.get_coords()
		self.highlighted_text[word_idx].insert(char_idx + 1, '|')

	def remove_caret(self) -> None:
		word_idx, char_idx = self.get_coords()
		self.highlighted_text[word_idx].pop(char_idx + 1)

	def generate_display_text(self) -> str:
		return ' '.join(''.join(word) for word in self.highlighted_text)

	def get_correct_words(self) -> int:
		return len(self.correct_words)

	def check_is_word_correct(self, word_idx: int) -> bool:
		word = self.user_text[word_idx]
		target_word = self.target_text[word_idx]
		return (
			len(word) == len(target_word)
			and all(word[i] == target_word[i] for i in range(len(word)))
		)

	def add_correct_word(self, word_idx: int) -> None:
		self.correct_words.add(word_idx)

	def remove_correct_word(self, word_idx: int) -> None:
		if word_idx in self.correct_words:
			self.correct_words.remove(word_idx)
