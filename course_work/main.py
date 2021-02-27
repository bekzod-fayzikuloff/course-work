import sys

from PyQt5 import QtWidgets, QtGui
from course_work.db import email_is_valid, password_id_valid
from qtwidgets import PasswordEdit


class MyButton(QtWidgets.QPushButton):
    __stylesheet__ = '''
        QPushButton{
            background-color: #3C3F41;
            color: #E1E1E1;
            border-radius: 10px;        
        }
        QPushButton:hover {
        background-color: #A648C7;
        }
        QPushButton:pressed {
        background-color: #A648C7;
        }
    '''

    def __init__(self, text_on_btn=None):
        super().__init__()
        self.text_on_btn = text_on_btn
        self.setMinimumHeight(20)
        self.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))
        self.setText(self.text_on_btn)
        self.setStyleSheet(MyButton.__stylesheet__)


class Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.resize(320, 120)
        self.setStyleSheet('background-color: #3C3F41;')
        self.setWindowTitle('authenticator app')
        self.setWindowIcon(QtGui.QIcon(r'icons/login.png'))

        self.lineEdit_email = QtWidgets.QLineEdit()
        self.lineEdit_email.setMinimumHeight(22)
        self.lineEdit_email.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))

        self.lineEdit_password = PasswordEdit()
        # self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setMinimumHeight(22)
        self.lineEdit_password.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))

        self.acceptButton = MyButton(' login')
        self.acceptButton.setIcon(QtGui.QIcon(r'icons/login.png'))
        self.acceptButton.clicked.connect(self.user_login)

        self.emailIconButton = MyButton()
        self.emailIconButton.setIcon(QtGui.QIcon(r'icons/at.png'))

        self.passwordIconButton = MyButton()
        self.passwordIconButton.setIcon(QtGui.QIcon(r'icons/password.png'))
        self.passwordIconButton.setObjectName('view')

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox2 = QtWidgets.QHBoxLayout()

        self.vbox = QtWidgets.QVBoxLayout()

        self.hbox1.addWidget(self.lineEdit_email)
        self.hbox1.addWidget(self.emailIconButton)

        self.hbox2.addWidget(self.lineEdit_password)
        self.hbox2.addWidget(self.passwordIconButton)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.acceptButton)

        self.setLayout(self.vbox)

    def user_login(self):
        try:
            result, id_ = email_is_valid(self.lineEdit_email.text())
            if result:
                if password_id_valid(user_id=id_, password=self.lineEdit_password.text()):
                    print('successful login')
                else:
                    self.lineEdit_password.setStyleSheet('background-color: #F03C39;')
                    self.lineEdit_password.setText('')
        except:
            self.lineEdit_password.setStyleSheet('background-color: #F03C39;')
            self.lineEdit_password.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())