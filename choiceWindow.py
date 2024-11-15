from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

import main


class ChoiceWidget(QDialog):
    def __init__(self, text_buttons, index_buttons):
        super().__init__()
        uic.loadUi('documentsWindow.ui', self)

        # приминение характеристик к кнопкам
        # BD - именование кнопок с выбором файла
        for i in range(len(index_buttons)):
            self.BD1.setText(text_buttons[0])
            self.BD1_index = index_buttons[0]
            self.BD1.clicked.connect(self.BD_choice_index_one)

            self.BD2.setText(text_buttons[1])
            self.BD2_index = index_buttons[1]
            self.BD2.clicked.connect(self.BD_choice_index_two)

    # метод для первой кнопки
    def BD_choice_index_one(self):
        main.MainWidget().update_document(self.BD1_index)
        self.close()

    # метод для второй кнопки
    def BD_choice_index_two(self):
        main.MainWidget().update_document(self.BD2_index)
        self.close()

    # оба метода вызывают одну и ту же функцию
    # в основном скрипте и закрывают данное окно,
    # но передают разные характеристики

