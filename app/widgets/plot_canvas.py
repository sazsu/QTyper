import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('QtAgg')


class PlotCanvas(FigureCanvasQTAgg):
	def __init__(self, parent=None, width=500, height=4, dpi=100):
		self.figure = Figure(figsize=(width, height), dpi=dpi)
		self.ax1 = self.figure.add_subplot(111)
		self.ax2 = self.ax1.twinx()
		super().__init__(self.figure)
