import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from app.config import Config


mpl.use('QtAgg')


class PlotCanvas(FigureCanvasQTAgg):
	def __init__(self, parent=None, width=500, height=4, dpi=100):
		self.figure = Figure(figsize=(width, height), dpi=dpi)
		self.ax1 = self.figure.add_subplot(111)
		self.ax2 = self.ax1.twinx()
		# self.ax1.xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
		super().__init__(self.figure)

	def clear_data(self) -> None:
		self.ax1.cla()
		self.ax2.cla()
		self.ax2.yaxis.set_label_position('right')

	def set_values(self, wpm_arr, acc_arr) -> None:
		self.clear_data()
		self.figure.gca().xaxis.set_major_locator(
			mpl.ticker.MaxNLocator(integer=True)
		)
		self.ax1.yaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
		self.ax2.yaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))

		self.ax1.set_ylim(
			-1,
			max(100, max(wpm_arr or [-1])) + 1
		)
		self.ax1.set_ylabel(
			'Words Per Minute',
			color=Config.wpm_purple
		)
		self.ax2.set_ylim(
			0,
			101
		)
		self.ax2.set_ylabel(
			'Accuracy',
			color=Config.acc_cyan,
			rotation=270,
			va='bottom'  # fix spacing
		)
		if not wpm_arr:
			self.ax1.set_xticks([])
			return

		# only one test was done
		if len(wpm_arr) == 1:
			self.ax1.set_xticks([1])
			wpm_arr *= 2
			acc_arr *= 2

		x_values = range(1, len(wpm_arr) + 1)

		self.ax1.plot(
			x_values,
			wpm_arr,
			color=Config.wpm_purple,
			linewidth=3,
			solid_capstyle='round',
		)
		self.ax2.set_ylim(
			0,
			101
		)
		self.ax2.set_ylabel(
			'Accuracy',
			color=Config.acc_cyan
		)
		self.ax2.plot(
			x_values,
			acc_arr,
			color=Config.acc_cyan,
			linewidth=3,
			solid_capstyle='round',
		)

	def set_mode(self, bg_color, text_color) -> None:
		self.figure.set_facecolor(bg_color)
		self.ax1.set_facecolor(bg_color)
		self.ax2.set_facecolor(bg_color)

		self.ax1.tick_params(axis='both', colors=text_color)
		self.ax2.tick_params(axis='both', colors=text_color)

		for spine in self.ax2.spines.values():
			spine.set_color(text_color)
		for spine in self.ax1.spines.values():
			spine.set_color(text_color)
		