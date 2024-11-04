from PyQt6.QtCore import QObject, QTimer


class StatsManager(QObject):
	def __init__(self, text_area, text_manager) -> None:
		super().__init__()
		self.text_area = text_area
		self.text_manager = text_manager

		self.test_time = 5
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.get_stats)
		self.timer.setInterval(1000)  # 1 second

	def start(self) -> None:
		self.reset_elapsed_time()
		self.timer.start()

	def reset(self) -> None:
		self.timer.stop()
		self.reset_elapsed_time()
		self.reset_wpm_arr()
		self.reset_acc_arr()

	def get_stats(self) -> None:
		correct_words = self.text_manager.get_correct_words()
		correct_chars = self.text_manager.get_correct_chars()
		wrong_chars = self.text_manager.get_wrong_chars()

		self.wpm_arr.append(self.calculate_wpm(correct_words))
		self.acc_arr.append(self.calculate_acc(correct_chars, wrong_chars))
		self.increment_elapsed_time()

	def calculate_wpm(self, correct_words: int) -> float:
		return correct_words * 60 / self.elapsed_time

	@staticmethod
	def calculate_acc(correct_chars: int, wrong_chars: int) -> int:
		return 100 * (correct_chars) // (correct_chars + wrong_chars)

	def reset_elapsed_time(self) -> None:
		self.elapsed_time = 1  # second

	def increment_elapsed_time(self) -> None:
		if self.elapsed_time == self.test_time:
			wpm_arr, acc_arr = self.wpm_arr, self.acc_arr
			self.text_area.parent().show_line_chart(wpm_arr, acc_arr)
		else:
			self.elapsed_time += 1  # second

	def reset_wpm_arr(self) -> None:
		self.wpm_arr = []

	def reset_acc_arr(self) -> None:
		self.acc_arr = []
