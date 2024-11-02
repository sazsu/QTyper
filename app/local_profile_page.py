from PyQt6.QtWidgets import QWidget


class LocalProfile(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self) -> None:
        pass

    def change_mode(self, mode: bool) -> None:
        pass
