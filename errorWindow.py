from PyQt6 import uic
from PyQt6.QtWidgets import QDialog


class ErrorWidget(QDialog):
    def __init__(self, name_error):
        super().__init__()
        uic.loadUi('errorWindow.ui', self)

        self.errorText.setText(name_error)
