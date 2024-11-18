from PyQt6.QtWidgets import QWidget

from app.config import Config
from app.ui.line_chart_ui import Ui_Form


class LineChart(QWidget, Ui_Form):
	def __init__(self, parent) -> None:
		super().__init__(parent)
		self.setupUi(self)

	def set_values(self, wpm_arr, acc_arr) -> None:
		self.canvas.set_values(wpm_arr, acc_arr)

	def set_mode(self, mode: bool) -> None:
		if mode:
			bg_color = Config.white
			text_color = Config.black
		else:
			bg_color = Config.black
			text_color = Config.white

		self.setStyleSheet(f'background: {bg_color}')

		# set bg color of the plot
		self.canvas.set_mode(bg_color, text_color)
		# re-render
		self.render()

	def render(self) -> None:
		self.canvas.draw()
