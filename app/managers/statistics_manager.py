from PyQt6.QtCore import QObject, QTimer


class StatsManager(QObject):
	def __init__(self, text_manager) -> None:
		super().__init__()
		self.text_manager = text_manager

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.get_stats)
		self.timer.setInterval(1000)  # 1 second

	def start(self) -> None:
		self.reset_elapsed_time()
		self.timer.start()

	def stop(self) -> None:
		self.timer.stop()
		self.get_stats()
		self.reset_elapsed_time()

	def get_stats(self) -> None:
		self.increment_elapsed_time()

		correct_words = self.text_manager.get_correct_words()
		self.calculate_wpm(correct_words)

	def calculate_wpm(self, correct_words: int) -> int:
		print(f'WPM: {correct_words * (60 / self.elapsed_time)}')

	def reset_elapsed_time(self) -> None:
		self.elapsed_time = 0  # seconds

	def increment_elapsed_time(self) -> None:
		self.elapsed_time += 1  # second
