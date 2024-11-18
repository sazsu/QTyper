from random import sample
from typing import List, Tuple

from app.config import Config
from app.word_dictionary import WordDict


class TextManager:
	def __init__(self, db_manager) -> None:
		self.correct_format = Config.correct_format
		self.wrong_format = Config.wrong_format
		self.WORDS_PER_ROW = 12
		self.lang_words = {
			'english': WordDict.en_words,
			'russian': WordDict.ru_words,
		}

		self.db_manager = db_manager
		self.mode, self.language = self.db_manager.get_test_settings()

	def reset(self):
		mode, language = self.get_test_settings()
		self.target_text = []
		for _ in range(3):
			self.target_text.extend(self.generate_new_row())

		self.user_text = [
			[[] for _ in range(self.WORDS_PER_ROW)] for _ in range(3)
		]
		self.highlighted_text = [
			[
				list(word)
				for word in self.target_text[
					i * self.WORDS_PER_ROW:i * self.WORDS_PER_ROW
					+ self.WORDS_PER_ROW
				]
			]
			for i in range(3)
		]
		self.curr_row_index = 0
		self.current_word_index = 0
		self.current_char_index = -1
		self.correct_words = set()

		self.correct_chars = set()
		self.wrong_chars = set()

	def are_words_needed(self) -> bool:
		# if next row is last row, then add more words
		return len(self.user_text) - self.curr_row_index <= 2

	def generate_new_row(self) -> List[str]:
		words = self.lang_words[self.language]
		new_row = [
			*sample(words[6], 2),
			*sample(words[5], 2),
			*sample(words[4], 3),
			*sample(words[3], 3),
			*sample(words[2], 2),
		]
		return sample(new_row, self.WORDS_PER_ROW)

	def add_words(self) -> None:
		self.target_text.extend(self.generate_new_row())
		self.user_text.extend([[[] for _ in range(self.WORDS_PER_ROW)]])
		self.highlighted_text.extend(
			[
				list(word)
				for word in self.target_text[
					i * self.WORDS_PER_ROW:i * self.WORDS_PER_ROW
					+ self.WORDS_PER_ROW
				]
			]
			for i in range(
				(len(self.target_text) - self.WORDS_PER_ROW)
				// self.WORDS_PER_ROW,
				len(self.target_text) // self.WORDS_PER_ROW,
			)
		)

	def get_test_settings(self) -> Tuple[int, str]:
		return self.mode, self.language

	def set_test_settings(self, mode: int, language: str) -> None:
		self.mode, self.language = mode, language

	def get_coords(self) -> Tuple[int, int, int]:
		return (
			self.curr_row_index,
			self.current_word_index,
			self.current_char_index,
		)

	def update_coords(
		self, new_row_index: int, new_word_index: int, new_char_index: int
	) -> None:
		self.curr_row_index = new_row_index
		self.current_word_index = new_word_index
		self.current_char_index = new_char_index

	def handle_backspace(self) -> None:
		row_idx, word_idx, char_idx = self.get_coords()

		if char_idx >= 0:
			self.user_text[row_idx][word_idx].pop()
			self.update_coords(row_idx, word_idx, char_idx - 1)
		# first word of the row
		# backtrack to the last word of the previous row
		# if it wasn't correctly typed and current row isn't the first row
		elif (
			char_idx == -1
			and word_idx == 0
			and row_idx > 0
			and self.is_user_word_correct(row_idx - 1, self.WORDS_PER_ROW - 1)
			is False
		):
			self.update_coords(
				row_idx - 1,
				self.WORDS_PER_ROW - 1,
				len(self.user_text[row_idx - 1][self.WORDS_PER_ROW - 1]) - 1,
			)
		# not a first word of the row
		# backtrack to the previous word
		# if it wasn't correctly typed
		elif (
			char_idx == -1
			and word_idx > 0
			and (row_idx, word_idx - 1) not in self.correct_words
		):
			self.update_coords(
				row_idx,
				word_idx - 1,
				len(self.user_text[row_idx][word_idx - 1]) - 1,
			)
		# do not change anything if caret is at first word's first symbol

	def handle_space(self) -> None:
		row_idx, word_idx, char_idx = self.get_coords()
		if char_idx >= 0:  # not an empty word
			is_word_correct = self.is_user_word_correct(row_idx, word_idx)
			if is_word_correct:
				self.add_correct_word_coords((row_idx, word_idx))
			if word_idx == self.WORDS_PER_ROW - 1:  # last word of the row
				self.update_coords(row_idx + 1, 0, -1)
			else:
				self.update_coords(row_idx, word_idx + 1, -1)

	def handle_char(self, char: str) -> None:
		row_idx, word_idx, char_idx = self.get_coords()
		user_word = self.get_user_word(row_idx, word_idx)
		target_word = self.get_target_word(row_idx, word_idx)
		if len(user_word) < len(target_word) + 5:  # set boundary
			user_word.append(char)
			self.update_coords(row_idx, word_idx, char_idx + 1)

	def update_highlighted_text(self) -> None:
		row_idx, word_idx, _ = self.get_coords()
		self.highlighted_text[row_idx][word_idx] = self.highlight_word(
			row_idx, word_idx
		)

	def highlight_word(self, row_idx: int, word_idx: int) -> List[str]:
		# copy to not mess up the original word
		word = self.get_user_word(row_idx, word_idx).copy()
		target_word = self.get_target_word(row_idx, word_idx)
		# color (green or red) all symbol in word in one loop
		for i in range(len(word)):
			if i < len(target_word) and target_word[i] == word[i]:
				word[i] = self.correct_format.format(word[i])
				self.add_correct_char((row_idx, word_idx, i))
			else:
				word[i] = self.wrong_format.format(word[i])
				self.add_wrong_char((row_idx, word_idx, i))
				self.remove_correct_char((row_idx, word_idx, i))

		# word is not fully typed -> add missing characters (placeholder color)
		for i in range(len(word), len(target_word)):
			word.append(target_word[i])
		return word

	def add_caret(self) -> None:
		row_idx, word_idx, char_idx = self.get_coords()
		self.highlighted_text[row_idx][word_idx].insert(
			char_idx + 1, Config.caret
		)

	def remove_caret(self) -> None:
		row_idx, word_idx, char_idx = self.get_coords()
		self.highlighted_text[row_idx][word_idx].pop(char_idx + 1)

	def generate_display_text(self) -> Tuple[str, str, str]:
		# return ' '.join(''.join(word) for word in self.highlighted_text)
		(
			row_idx,
			_,
			_,
		) = self.get_coords()
		first_idx, second_idx, third_idx = row_idx, row_idx + 1, row_idx + 2

		if row_idx > 0:
			first_idx -= 1
			second_idx -= 1
			third_idx -= 1
		return (
			' '.join(
				''.join(chars_of_word)
				for chars_of_word in self.highlighted_text[first_idx]
			),
			' '.join(
				''.join(chars_of_word)
				for chars_of_word in self.highlighted_text[second_idx]
			),
			' '.join(
				''.join(chars_of_word)
				for chars_of_word in self.highlighted_text[third_idx]
			),
		)

	def add_correct_char(self, coords: Tuple[int, int, int]) -> None:
		self.correct_chars.add(coords)

	def remove_correct_char(self, coords: Tuple[int, int, int]) -> None:
		if coords in self.correct_chars:
			self.correct_chars.remove(coords)

	def get_correct_chars(self) -> int:
		return len(self.correct_chars)

	def add_wrong_char(self, coords: Tuple[int, int, int]) -> None:
		self.wrong_chars.add(coords)

	def get_wrong_chars(self) -> int:
		return len(self.wrong_chars)

	def get_correct_words(self) -> int:
		return len(self.correct_words)

	def is_user_word_correct(self, row_idx: int, word_idx: int) -> bool:
		if (row_idx, word_idx) in self.correct_words:
			return True

		user_word = self.get_user_word(row_idx, word_idx)
		target_word = self.get_target_word(row_idx, word_idx)
		return len(user_word) == len(target_word) and all(
			user_word[i] == target_word[i] for i in range(len(user_word))
		)

	def add_correct_word_coords(self, coords: Tuple[int, int]) -> None:
		self.correct_words.add(coords)

	def remove_correct_word_coords(self, coords: Tuple[int, int]) -> None:
		if coords in self.correct_words:
			self.correct_words.remove(coords)

	def get_user_word(self, row_idx: int, word_idx: int) -> List[str]:
		return self.user_text[row_idx][word_idx]

	def get_target_word(self, row_idx: int, word_idx: int) -> str:
		return self.target_text[row_idx * self.WORDS_PER_ROW + word_idx]
