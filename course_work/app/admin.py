import sys

from PyQt5.QtCore import QDate

import button
from PyQt5 import QtWidgets, QtGui, QtCore
from course_work.db.models import *


def date_convert(data: tuple):
    pass


class AdminApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin Panel')
        self.resize(480, 340)
        self.setStyleSheet('background-color: #ADADAD;')

        self.profession_name = QtWidgets.QLineEdit()
        self.profession_name.setPlaceholderText('Названия профессии в вашей аптеке')
        self.experience = QtWidgets.QLineEdit()
        self.experience.setPlaceholderText('Назвние опыта в нужной в вашей аптеке')
        self.wage = QtWidgets.QLineEdit()
        self.wage.setPlaceholderText('Заработная плата данной профессии')
        self.button = button.MyButton('Добавить профессию')

        self.button.clicked.connect(self.add_employee_func)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.profession_name)
        self.vbox.addWidget(self.experience)
        self.vbox.addWidget(self.wage)
        self.vbox.addWidget(self.button)

        # -------------------------------

        self.person_name = QtWidgets.QLineEdit()
        self.person_name.setPlaceholderText('Имя сотрудника в аптеке')
        self.person_lastname = QtWidgets.QLineEdit()
        self.person_lastname.setPlaceholderText('Фамилия сотрудника в аптеке')
        self.person_profession_id = QtWidgets.QComboBox()

        for profession in Profession.select():
            self.person_profession_id.addItem(profession.profession)

        self.add_staff = button.MyButton('Добавить сотрудника')
        self.add_staff.clicked.connect(self.add_staff_person)

        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox1.addWidget(self.person_name)
        self.vbox1.addWidget(self.person_lastname)
        self.vbox1.addWidget(self.person_profession_id)
        self.vbox1.addWidget(self.add_staff)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.hbox.addLayout(self.vbox1)

        self.vbox2 = QtWidgets.QVBoxLayout()
        self.vbox2.addLayout(self.hbox)

        self.medicine_name_line = QtWidgets.QLineEdit()
        self.medicine_name_line.setPlaceholderText('Названия лекарства')
        self.medicine_description = QtWidgets.QTextEdit()
        self.medicine_description.setMinimumHeight(175)
        self.medicine_description.setPlaceholderText('Описания лекарства')
        self.medicine_price = QtWidgets.QDoubleSpinBox()
        self.medicine_price.setMaximum(1000000)
        self.medicine_date_of_manufacture = QtWidgets.QDateEdit()
        self.medicine_shelf_life = QtWidgets.QDateEdit()
        self.medicine_date_of_manufacture.setDate(QDate(2020, 1, 1))
        self.medicine_shelf_life.setDate(QDate(2020, 1, 1))
        self.maker_medicine_id = QtWidgets.QComboBox()

        for maker in Maker.select():
            self.maker_medicine_id.addItem(maker.company_name)

        self.add_medicine = button.MyButton('Добавить лекарство')
        self.add_medicine.clicked.connect(self.add_medicine_method)

        self.vbox2.addWidget(self.medicine_name_line)
        self.vbox2.addWidget(self.medicine_description)
        self.vbox2.addWidget(self.medicine_price)
        self.vbox2.addWidget(self.medicine_date_of_manufacture)
        self.vbox2.addWidget(self.medicine_shelf_life)
        self.vbox2.addWidget(self.maker_medicine_id)
        self.vbox2.addWidget(self.add_medicine)

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.addLayout(self.vbox2)
        self.icon_btn = button.MyButton()
        self.icon_btn.setIcon(QtGui.QIcon('icons/caduceus.png'))
        self.icon_btn.setIconSize(QtCore.QSize(50, 50))
        self.icon_btn.without_hover('#ADADAD')
        self.hbox1.addWidget(self.icon_btn)

        self.setLayout(self.hbox1)

    def add_employee_func(self):
        try:
            with db:
                Profession(
                    profession=self.profession_name.text(),
                    experience=int(self.experience.text()),
                    wage=float(self.wage.text())
                ).save()
            self.profession_name.setText('')
            self.experience.setText('')
            self.wage.setText('')
        except ValueError:
            self.experience.setText('')
            self.wage.setText('')
            self.experience.setPlaceholderText('Your need write numeric type')
            self.wage.setPlaceholderText('Your need write numeric type')

    def add_staff_person(self):
        try:
            with db:
                # id_ = Profession.profession == self.person_profession_id.currentText()
                Staff(
                    firs_name=self.person_name.text(),
                    last_name=self.person_lastname.text(),
                    profession_id=Profession.select(Profession.id).where(Profession.profession == self.person_profession_id.currentText())
                ).save()

                self.person_name.setText('')
                self.person_lastname.setText('')
            print('ok...')
            print(self.person_profession_id.currentText())

        except Exception as e:
            print(e)

    def add_medicine_method(self):
        try:
            with db:
                Medicine(
                    name=self.medicine_name_line.text(),
                    description=self.medicine_description.toPlainText(),
                    price=float(self.medicine_price.text().replace(',', '.')),
                    date_of_manufacture=self.medicine_date_of_manufacture.text(),
                    shelf_life=self.medicine_shelf_life.text(),
                    maker_id=Maker.select(Maker.id).where(Maker.company_name == self.maker_medicine_id.currentText())
                ).save()
            self.medicine_name_line.setText('')
            self.medicine_description.setText('')
            self.medicine_price.setValue(0.)
            self.medicine_date_of_manufacture.setDate(QDate(2020, 1, 1))
            self.medicine_shelf_life.setDate(QDate(2020, 1, 1))

            print('OK...')

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = AdminApp()
    widget.show()
    sys.exit(app.exec())
