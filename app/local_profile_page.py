from PyQt6.QtWidgets import QWidget


class LocalProfilePage(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self) -> None:
        pass

    def set_mode(self, mode: bool) -> None:
        pass
