import sys
import time
import random
import sqlite3

import login
import line_module

from course_work.app.colors import BColors
from course_work.app.button import MyButton
from course_work.db.db_user import add_user_to_db, pk

from PyQt5 import QtWidgets, QtGui, QtCore

start_time = time.time()
colors = [BColors.OKCYAN, BColors.OKBLUE, BColors.OKGREEN]


class SignUpWidget(QtWidgets.QWidget):
    """
        Класс SignUpWidget является настледником класса QtWidgets.QWidget в котором прописывается логика для добавления
        пользоваетелей в базу данных
    """

    def __init__(self):
        """
            Метод конструктор который не принимает никаких аргументов кроме аргумента self что указывает на сам
            экземпляр класса,  в кострукторе мы вызываем метод __init__() суперкласса и создаем атрбуты
            экземпляра класса которые являются экземплярами других классов с которыми мы сможем взаимодействовать
            с помощью их методов и свойствЫ
        """
        super().__init__()

        self.setWindowTitle('SignUp')
        self.setWindowIcon(QtGui.QIcon(login.resource_path('icons/add-user.png')))
        self.setMaximumHeight(120)
        self.setMinimumWidth(320)
        self.setMaximumWidth(380)

        self.setStyleSheet('background-color: #A4A3A3;')

        self.first_name_line = line_module.MyLine()
        self.first_name_line.setPlaceholderText('Name')

        self.last_name_line = line_module.MyLine()
        self.last_name_line.setPlaceholderText('Surname')

        self.email_line = line_module.MyLine()
        self.email_line.setPlaceholderText('Email')

        self.password_line = line_module.PasswordEdit()
        self.password_line.setPlaceholderText('Password')
        self.password_line.change_font_color('#fff')

        self.password_check_line = line_module.PasswordEdit()
        self.password_check_line.setPlaceholderText('Confirm password')
        self.password_check_line.change_font_color('#fff')

        self.first_name_btn = MyButton()
        self.first_name_btn.setIcon(QtGui.QIcon(login.resource_path(r'icons/login.png')))
        self.first_name_btn.without_hover('#A4A3A3')

        self.last_name_btn = MyButton()
        self.last_name_btn.setIcon(QtGui.QIcon(login.resource_path('icons/login.png')))
        self.last_name_btn.without_hover('#A4A3A3')

        self.email_btn = MyButton()
        self.email_btn.setIcon(QtGui.QIcon(login.resource_path('icons/login.png')))
        self.email_btn.without_hover('#A4A3A3')

        self.password_btn = MyButton()
        self.password_btn.setIcon(QtGui.QIcon(login.resource_path('icons/login.png')))
        self.password_btn.without_hover('#A4A3A3')

        self.password_check_btn = MyButton()
        self.password_check_btn.setIcon(QtGui.QIcon(login.resource_path('icons/login.png')))
        self.password_check_btn.without_hover('#A4A3A3')

        self.label = QtWidgets.QLabel('all widgets need fill correct')
        self.label.hide()

        self.acceptButton = MyButton('Signup')
        self.acceptButton.change_hover('#198754')
        self.acceptButton.setMinimumWidth(130)
        self.acceptButton.clicked.connect(self.register)

        self.vbox = QtWidgets.QVBoxLayout()

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox4 = QtWidgets.QHBoxLayout()
        self.hbox5 = QtWidgets.QHBoxLayout()

        self.hbox1.addWidget(self.first_name_line)
        self.hbox1.addWidget(self.first_name_btn)

        self.hbox2.addWidget(self.last_name_line)
        self.hbox2.addWidget(self.last_name_btn)

        self.hbox3.addWidget(self.email_line)
        self.hbox3.addWidget(self.email_btn)

        self.hbox4.addWidget(self.password_line)
        self.hbox4.addWidget(self.password_btn)

        self.hbox5.addWidget(self.password_check_line)
        self.hbox5.addWidget(self.password_check_btn)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        self.vbox.addWidget(self.acceptButton, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(self.vbox)

    def register(self):
        """
        Метод register проверяет валидность введенных данных со стороны пользователя и после проверки в случаи их
        валидности добавляет и в базу данных, в противном сучае возвращает сообщение о причине ошибки
        :return None:
        """
        try:
            if self.first_name_line.text() == '' or self.last_name_line.text() == '' \
                    or '@' not in self.email_line.text() or len(self.password_line.text()) < 8 \
                    or self.password_line.text() != self.password_check_line.text():
                self.first_name_line.setText('')
                self.last_name_line.setText('')
                self.email_line.setText('')
                self.password_line.setText('')
                self.password_check_line.setText('')
                self.label.show()
            else:
                add_user_to_db(
                    pk(), self.first_name_line.text(), self.last_name_line.text(),
                    self.email_line.text(), self.password_line.text()
                )
                self.first_name_line.setText('')
                self.last_name_line.setText('')
                self.email_line.setText('')
                self.password_line.setText('')
                self.password_check_line.setText('')

                self.hide()
        except sqlite3.IntegrityError:
            self.email_line.setPlaceholderText('this email already using')
            self.email_line.setStyleSheet('background-color: #E14F60;')
            self.password_line.setStyleSheet('background-color: #E14F60;')
            self.password_check_line.setStyleSheet('background-color: #E14F60;')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = SignUpWidget()
    final_time = time.time() - start_time
    if int(str(final_time)[0]) < 1:
        print(f"{BColors.BOLD}{random.choice(colors)}--- {final_time} секунд ---")
    elif int(str(final_time)[0]) == 1:
        print(f"{BColors.BOLD}{BColors.WARNING}--- {final_time} секунд ---")
    else:
        print(f"{BColors.BOLD}{BColors.FAIL}--- {final_time} секунд ---")
    widget.show()
    sys.exit(app.exec())
