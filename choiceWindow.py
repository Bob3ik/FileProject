from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog


class ChoiceWidget(QDialog):
    def __init__(self, text_buttons, index_buttons):
        super().__init__()
        uic.loadUi('documentsWindow.ui', self)
        self.index = ''

        # приминение характеристик к кнопкам
        # BD - именование кнопок с выбором файла
        self.BD1.setText(text_buttons[0])
        self.BD1_index = index_buttons[0]
        self.BD1.clicked.connect(self.BD_choice_index_one)

        self.BD2.setText(text_buttons[1])
        self.BD2_index = index_buttons[1]
        self.BD2.clicked.connect(self.BD_choice_index_two)

    # метод для первой кнопки
    def BD_choice_index_one(self):
        self.index = self.BD1_index
        self.close()

    # метод для второй кнопки
    def BD_choice_index_two(self):
        self.index = self.BD2_index
        self.close()

    # оба метода вызывают одну и ту же функцию
    # в основном скрипте и закрывают данное окно,
    # но передают разные характеристики
