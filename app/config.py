class Config:
	white = '#f2f2f2'
	light_gray = '#c2c2c2'
	black = '#121212'
	wpm_purple = '#7851a9'
	acc_cyan = '#23d5d5'
	green = '#1fc471'
	red = '#ff506e'
	correct_format = '<span class="correct" style="color: #1fc471;">{}</span>'
	wrong_format = '<span class="wrong" style="color: #ff506e;">{}</span>'

	app_light = """
		* {
			color: #121212;
			background: #f2f2f2;
		}
		QPushButton { border: none; }
		"""

	app_dark = """
		* {
			color: #c2c2c2;
			background: #121212;
		}
		QPushButton { border: none; }
		"""
	caret = '''<span style="margin-left: -2px;
			margin-right: -2px;
			font-family: Inter;">|</span>'''
