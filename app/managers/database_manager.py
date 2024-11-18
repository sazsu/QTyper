import sqlite3
from typing import Tuple


class DatabaseManager:
	def __init__(self, db_name: str) -> None:
		self.conn = sqlite3.connect(db_name)  # will be created if doesn't exist
		self.on_startup()

	def on_startup(self) -> None:
		with open('app/startup.sql', 'r') as f:
			startup_script = f.read()

		with self.conn as conn:
			conn.executescript(startup_script)

	def add_test_stats(self, wpm: int, acc: float) -> None:
		with self.conn as conn:
			conn.execute(
				"""
				INSERT INTO Stats (wpm, accuracy)
				VALUES (?, ?)
				""",
				(wpm, acc),
			)

	def get_interface_mode(self) -> bool:
		with self.conn as conn:
			res = conn.execute("""
			SELECT interfaceMode FROM Settings""").fetchone()[0]
		return bool(res)

	def set_interface_mode(self, mode: int) -> None:
		with self.conn as conn:
			conn.execute(
				"""
				UPDATE Settings
				SET interfaceMode = ?""",
				(mode,),
			)

	def fetch_all_test_stats(self) -> (Tuple[int], Tuple[int]):
		with self.conn as conn:
			wpm_stats = tuple(map(
				lambda x: x[0],
				conn.execute("""
					SELECT wpm FROM Stats""").fetchall(),
			))
			acc_stats = tuple(map(
				lambda x: x[0],
				conn.execute("""
					SELECT accuracy FROM Stats""").fetchall(),
			))
		return wpm_stats, acc_stats

	def clear_data(self) -> None:
		with self.conn as conn:
			conn.execute("""
				DROP TABLE Stats""")
		self.on_startup()

	def get_test_settings(self) -> Tuple[int, str]:
		with self.conn as conn:
			res = conn.execute('''
				SELECT (
					SELECT mode FROM Modes
					WHERE id=Settings.mode
				),
				(
					SELECT language FROM Languages
					WHERE id=Settings.language
				) FROM Settings''').fetchone()
		return res

	def set_test_settings(self, mode: int, language: str) -> None:
		with self.conn as conn:
			conn.execute('''
				UPDATE Settings
				SET mode=(
					SELECT id FROM Modes WHERE mode=?
				),
				language=(
					SELECT id FROM Languages WHERE language=?
				)''', (mode, language))
