import os
import sys

import tables

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('desine.ui', self)

        self.createrFileButton.clicked.connect(self.CreateFile)
        self.comboFormatBox.addItems(tables.FILE_FORMATS)
        self.comboTasksBox.addItems(tables.AREAS_OF_ACTIVITY)

    def CreateFile(self):
        task = self.comboTasksBox.currentText()
        format = self.comboFormatBox.currentText()

        folder = self.CreateFolder(task)

        file_name = f'{task}.{format}'
        with open(f'{folder}\\{file_name}', 'w') as file:
            file.write('Test text.')

    def CreateFolder(self, task):
        main_folder = r'C:\Users\Admin\Desktop\DocumentsPy'
        task_folder = main_folder + '\\' + task

        if not os.path.exists(main_folder):
            os.makedirs(main_folder)
        if not os.path.exists(task_folder):
            os.makedirs(task_folder)

        return task_folder


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
