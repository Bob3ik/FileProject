import smtplib
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog


# вспомогательное окно
class HelpWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('helpWindow.ui', self)

        self.sendMessageButton.clicked.connect(self.send_message)

    def send_message(self):
        user_message = self.userTextEdit.toPlainText()
        message = f'''Subject: FilePY Предложка\n
                                {user_message}'''
        message = message.encode('utf-8')

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('fileprojectemail@gmail.com', 'rbax ymlc miso zlic')

        smtp.sendmail('fileprojectemail@gmail.com', 'frolovroman20008@gmail.com', message)
        smtp.quit()

        self.userTextEdit.setText('Сообщение отправленно')

