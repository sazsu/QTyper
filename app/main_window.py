from PyQt6.QtWidgets import QMainWindow, QStackedWidget

from app.widgets.text_area import TextArea


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_language_words()
		self.initUI()

	def initUI(self):
		self.pages = QStackedWidget(self)  # add pages here

		self.setGeometry(0, 0, 500, 500)
		self.text_area_widget = TextArea(self)
		self.text_area_widget.setGeometry(
			300, 300, self.text_area_widget.width(), self.text_area_widget.height()
		)

	def load_language_words(self):
		with open('app/language_words/en.txt', 'r') as f:
			self.en_words = map(lambda s: s.strip(), f.readlines())
			
		with open('app/language_words/ru.txt', 'r') as f:
			self.ru_words = map(lambda s: s.strip(), f.readlines())
