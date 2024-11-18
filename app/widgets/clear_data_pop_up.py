from PyQt6.QtWidgets import QMessageBox

from app.config import Config


class ClearDataPopUp(QMessageBox):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setWindowTitle('Clear All Data Pop Up')
        self.setStyleSheet('font-size: 24px')
        self.setText('Clear all data? This action cannot be undone')
        yes_btn = self.addButton('Yes', QMessageBox.ButtonRole.YesRole)
        yes_btn.setStyleSheet(
            f'background-color: {Config.green};'
            f'color: {Config.white};'
            'font-size: 24px'
        )
        yes_btn.clicked.connect(self.yes_btn_handler)

        no_btn = self.addButton('No', QMessageBox.ButtonRole.NoRole)
        no_btn.setStyleSheet(
            f'background-color: {Config.red};'
            f'color: {Config.white};'
            'font-size: 24px'
        )

    def yes_btn_handler(self) -> None:
        self.parent().db_manager.clear_data()
        self.parent().display_values()
