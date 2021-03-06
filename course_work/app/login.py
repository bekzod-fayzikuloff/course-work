import os
import sys
import time
import random

# from qtwidgets import PasswordEdit
from PyQt5 import QtWidgets, QtGui, QtCore

from course_work.app import main
from course_work.app import admin

from course_work.app import signup
from course_work.app.button import MyButton
from course_work.app.colors import BColors
from course_work.db.db_user import email_is_valid, password_id_valid


start_time = time.time()

colors = [BColors.OKCYAN, BColors.OKBLUE, BColors.OKGREEN]


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


class Widget(QtWidgets.QWidget):
    """
        Класс QWidget который наследуется от класса QtWidget.QWidget(будет содержать логику аутентификации).
        В методе контруктор вызываем конструктор родительского класса и взаимодействуем с атрибутами нашего класса,
        которые являются экземлярами различных классов и производим над ними нужные нам манипуляцию
    """

    def __init__(self):
        """
            Конструктор нашего класса в котором будет происходить все события созадния инстэнсов дригх классо и работа
            с их свойствами и методами
        """
        super().__init__()
        self.resize(320, 100)
        self.setMaximumWidth(400)
        self.setMaximumHeight(110)
        self.setStyleSheet('background-color: #3C3F41;')
        self.setWindowTitle('authenticator app')
        self.setWindowIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/login_ico.png')))
        self.setContentsMargins(0, 0, 0, -10)

        self.admin_app = admin.AdminApp()

        # -------------------------------------
        self.main_app = main.MainApp()
        # -------------------------------------

        self.lineEdit_email = QtWidgets.QLineEdit()
        self.lineEdit_email.setMinimumHeight(22)
        self.lineEdit_email.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))
        self.lineEdit_email.setStyleSheet('background-color: #FFFFFF;')

        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setMinimumHeight(22)
        self.lineEdit_password.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))
        self.lineEdit_password.setStyleSheet('background-color: #FFFFFF;')

        self.acceptButton = MyButton(' login')
        self.acceptButton.setMinimumWidth(160)
        self.acceptButton.setMaximumWidth(220)
        self.acceptButton.setIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/login.png')))
        self.acceptButton.clicked.connect(self.user_login)

        self.sign_up = signup.SignUpWidget()

        self.signUpButton = MyButton(' Sign Up')
        self.signUpButton.setMinimumWidth(160)
        self.signUpButton.setMaximumWidth(220)
        self.signUpButton.setIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/add-user.png')))
        self.signUpButton.change_hover('#198754')
        self.signUpButton.clicked.connect(self.signup)

        self.emailIconButton = MyButton()
        self.emailIconButton.setIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/at.png')))
        self.emailIconButton.without_hover('#E1E1E1')

        self.passwordIconButton = MyButton()
        self.passwordIconButton.setIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/password.png')))
        self.passwordIconButton.setObjectName('view')
        self.passwordIconButton.without_hover('#E1E1E1')

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox3 = QtWidgets.QHBoxLayout()

        self.vbox = QtWidgets.QVBoxLayout()

        self.hbox1.addWidget(self.lineEdit_email)
        self.hbox1.addWidget(self.emailIconButton)

        self.hbox2.addWidget(self.lineEdit_password)
        self.hbox2.addWidget(self.passwordIconButton)

        self.hbox3.addWidget(self.acceptButton, alignment=QtCore.Qt.AlignCenter)
        self.hbox3.addWidget(self.signUpButton, alignment=QtCore.Qt.AlignCenter)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

        self.setLayout(self.vbox)

    def user_login(self):
        """
        Метод класс в котором проиходит логика проверки совпадения значений занесенные пользователем со значениями
        которые есть в базе данных с помощью условного оператора и конструкции try/except:
        """
        if self.lineEdit_password.text() and self.lineEdit_email.text() == 'admin':
            self.lineEdit_password.setText('')
            self.lineEdit_email.setText('')
            self.admin_app.show()
        else:
            try:
                result, id_ = email_is_valid(self.lineEdit_email.text())
                if result:
                    if password_id_valid(user_id=id_, password=self.lineEdit_password.text()):
                        print('successful login')
                        self.hide()
                        self.main_app.show()
                    else:
                        self.lineEdit_password.setStyleSheet('background-color: #E14F60;')
                        self.lineEdit_password.setText('')
            except Exception as e:
                self.lineEdit_password.setStyleSheet('background-color: #E14F60;')
                self.lineEdit_password.setText('')
                print(e)

    def signup(self):
        """
        Метод служуший для октрытия окна регистрации
        :return None:
        """
        self.sign_up.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    final_time = time.time() - start_time
    if int(str(final_time)[0]) < 1:
        print(f"{BColors.BOLD}{random.choice(colors)}--- {final_time} секунд ---")
    elif int(str(final_time)[0]) == 1:
        print(f"{BColors.BOLD}{BColors.WARNING}--- {final_time} секунд ---")
    else:
        print(f"{BColors.BOLD}{BColors.FAIL}--- {final_time} секунд ---")
    widget.show()
    sys.exit(app.exec())
