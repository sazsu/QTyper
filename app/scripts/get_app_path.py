from pathlib import Path
import sys


def get_app_path():
	if getattr(sys, 'frozen', False):
		return Path(sys._MEIPASS).parent
	return Path(__file__).parent.parent
