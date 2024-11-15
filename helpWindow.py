import smtplib
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog


class HelpWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('helpWindow.ui', self)

        self.sendMessageButton.clicked.connect(self.send_message)

    def send_message(self):
        user_message = self.userTextEdit.toPlainText()
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login('fileprojectemail@gmail.com', '#File_work758')
        smtpObj.sendmail("fileprojectemail@gmail.com",
                         "frolovroman20008@gmail.com", user_message)
        smtpObj.quit()
