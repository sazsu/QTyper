from PyQt6.QtWidgets import QWidget

from app.config import Config
from app.ui.line_chart_ui import Ui_Form


class LineChart(QWidget):
	def __init__(self, parent) -> None:
		super().__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

	def set_values(self, wpm_arr, acc_arr) -> None:
		self.ui.canvas.ax1.set_xlabel('Test')

		self.ui.canvas.ax1.set_ylabel(
			'Words Per Minute',
			color=Config.wpm_purple
		)
		self.ui.canvas.ax1.plot(
			range(len(wpm_arr)),
			wpm_arr,
			color=Config.wpm_purple
		)

		self.ui.canvas.ax2.set_ylabel('Accuracy', color=Config.acc_cyan)
		self.ui.canvas.ax2.plot(range(len(acc_arr)), acc_arr, color=Config.acc_cyan)

	def set_mode(self, mode: bool) -> None:
		if mode:
			bg_color = Config.white
			text_color = Config.black
		else:
			bg_color = Config.black
			text_color = Config.white

		self.setStyleSheet(f'background: {bg_color}')

		# set bg color
		self.ui.canvas.figure.set_facecolor(bg_color)
		self.ui.canvas.ax1.set_facecolor(bg_color)

		self.ui.canvas.ax1.tick_params(axis='both', colors=text_color)
		self.ui.canvas.ax2.tick_params(axis='both', colors=text_color)

		for spine in self.ui.canvas.ax1.spines.values():
			spine.set_color(text_color)
		for spine in self.ui.canvas.ax2.spines.values():
			spine.set_color(text_color)
		# re-render
		self.ui.canvas.draw()
