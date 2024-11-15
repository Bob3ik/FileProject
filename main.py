import os
import sys
from playsound import playsound

import errorWindow
import helpWindow
import choiceWindow
import sounds
import tables

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


# создание основного рабочего окна программы
class MainWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainWindow.ui', self)

        # привязка функций к методам
        self.createrFileButton.clicked.connect(self.create_file)
        self.helpButton.clicked.connect(self.open_help_window)
        self.choiceDocument.clicked.connect(self.choice_file)

        # установление значений для окон с выбором вариантов
        self.comboFormatBox.addItems(tables.FILE_FORMATS)
        self.comboTasksBox.addItems(tables.AREAS_OF_ACTIVITY)

        # индекс выбранного документа
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.index_file = '00-000'
        self.documentName.setPlainText(tables.ALL_DOCUMENTS[self.index_file])

    def create_file(self):
        no_choice = 'не выбранно'
        task = self.comboTasksBox.currentText()
        format = self.comboFormatBox.currentText()
        file = self.documentName.toPlainText()

        if task == no_choice:
            # playsound(sounds.common_path + sounds.sound_error_window)
            self.open_error_window('Пожалуйста, выберите\nсферу')
        elif format == no_choice:
            # playsound(sounds.common_path + sounds.sound_error_window)
            self.open_error_window('Пожалуйста, выберите\nформат файла')
        # elif file == 'Документ не выбран':
        elif self.index_file == '00-000':
            self.open_error_window('Пожалуйста, выберите\nдокумент')
        else:
            folder = self.create_folder(task)

            file_name = f'{task}.{format}'
            with open(f'{folder}\\{file_name}', 'w') as file:
                file.write('Test text.')

    def create_folder(self, task):
        main_folder = r'C:\Users\Admin\Desktop\DocumentsPy'
        task_folder = main_folder + '\\' + task

        if not os.path.exists(main_folder):
            os.makedirs(main_folder)
        if not os.path.exists(task_folder):
            os.makedirs(task_folder)

        return task_folder

    # открытие окна для выбора документа
    def choice_file(self):
        print(self.index_file)
        text_buttons = None
        index_buttons = None

        # установка характеристик для объектов
        if self.comboTasksBox.currentText() == 'Юрист':
            pass
        elif self.comboTasksBox.currentText() == 'Педагог':
            text_buttons = ['Договор об \nоказании платных \nобразовательных \nуслуг',
                            'Договор оказания \nобразовательных \nуслуг по программе \nповышения \nквалификации']
            index_buttons = ['02-001', '02-002']
        elif self.comboTasksBox.currentText() == 'Бугалтер':
            pass
        elif self.comboTasksBox.currentText() == 'Другое':
            pass
        else:
            self.open_error_window('Пожалуйста, выберите\nсферу')
            return

        # создание и открытие окна
        choice_window = choiceWindow.ChoiceWidget(text_buttons, index_buttons)
        choice_window.exec()

    def update_document(self, new_index):
        self.index_file = new_index
        # изменения вроде применяются, но
        # при выходе из метода возвращаются назад
        print(self.index_file)

        self.documentName.setPlainText(tables.ALL_DOCUMENTS[self.index_file])

    def open_error_window(self, name_error):
        error_window = errorWindow.ErrorWidget(name_error)
        error_window.exec()

    def open_help_window(self):
        help_window = helpWindow.HelpWidget()
        help_window.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
