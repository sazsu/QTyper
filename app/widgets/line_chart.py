import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from app.config import Config


matplotlib.use('QtAgg')


class PlotCanvas(FigureCanvasQTAgg):
	def __init__(self, parent=None, width=500, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.ax1 = fig.add_subplot(111)
		self.ax2 = self.ax1.twinx()
		super().__init__(fig)


class LineChart(QWidget):
	def __init__(self, parent) -> None:
		super().__init__(parent)

		layout = QVBoxLayout(self)
		self.canvas = PlotCanvas(self, width=500, height=4, dpi=100)

		layout.addWidget(self.canvas)
		self.setLayout(layout)

	def set_values(self, wpm_arr, acc_arr) -> None:
		self.canvas.ax1.set_xlabel('Test')

		self.canvas.ax1.set_ylabel('Words Per Minute', color=Config.wpm_purple)
		self.canvas.ax1.plot(range(len(wpm_arr)), wpm_arr, color=Config.wpm_purple)

		self.canvas.ax2.set_ylabel('Accuracy', color=Config.acc_cyan)
		self.canvas.ax2.plot(range(len(acc_arr)), acc_arr, color=Config.acc_cyan)

	def change_mode(self, mode: bool) -> None:
		if mode:
			bg_color = Config.white
			text_color = Config.black
		else:
			bg_color = Config.black
			text_color = Config.white

		self.setStyleSheet(f'background: {bg_color}')
		self.canvas.ax1.set_facecolor(bg_color)
		self.canvas.ax1.tick_params(axis='both', colors=text_color)
		self.canvas.ax2.tick_params(axis='both', colors=text_color)

		# re-render
		self.canvas.draw()
