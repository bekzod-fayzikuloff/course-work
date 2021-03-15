import sys
import time
import random

import button

from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets, QtGui, QtCore

from course_work.app import main
from course_work.app.colors import BColors
from course_work.db.models import *

start_time = time.time()
colors = [BColors.OKCYAN, BColors.OKBLUE, BColors.OKGREEN]


class AdminApp(QtWidgets.QWidget):
    """
    Класс AdminApp  является наследником класса QtWidgets.QWidget в ней я страюсь реализовать функционал главного окна
    админ панели с помощбю которого можно манипкулировать базой данных с помощью GUI состовляющец программы
    """

    def __init__(self):
        """
        Метод коструктор класса AdminApp который не принимает никаких аргументов а просто вызывает коструктор сурекласса
        и последующем просто создает атрибуты класса AdminApp которые являются экземплярами других классов и происходит
        процесс манипуляции с этими экземплярами с помощью их методов и свойст.
        """
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(r'icons/admin.png'))
        self.setWindowTitle('Admin Panel')
        self.resize(620, 340)
        self.setStyleSheet('background-color: #A9AFCD;')
        self.maker_app = main.MainApp()

        self.profession_name = QtWidgets.QLineEdit()
        self.profession_name.setPlaceholderText('Названия профессии в вашей аптеке')
        self.experience = QtWidgets.QLineEdit()
        self.experience.setPlaceholderText('Назвние опыта в нужной в вашей аптеке')
        self.wage = QtWidgets.QLineEdit()
        self.wage.setPlaceholderText('Заработная плата данной профессии')

        self.button = button.MyButton('Добавить профессию')
        self.button.change_hover('#38CD54')
        self.button.setMinimumWidth(190)

        self.button.clicked.connect(self.add_employee_func)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.profession_name)
        self.vbox.addWidget(self.experience)
        self.vbox.addWidget(self.wage)
        self.vbox.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)

        # -------------------------------

        self.person_name = QtWidgets.QLineEdit()
        self.person_name.setPlaceholderText('Имя сотрудника в аптеке')
        self.person_lastname = QtWidgets.QLineEdit()
        self.person_lastname.setPlaceholderText('Фамилия сотрудника в аптеке')
        self.person_profession_id = QtWidgets.QComboBox()

        for profession in Profession.select():
            self.person_profession_id.addItem(profession.profession)

        self.add_staff = button.MyButton('Добавить сотрудника')
        self.add_staff.change_hover('#38CD54')
        self.add_staff.setMinimumWidth(190)
        self.add_staff.clicked.connect(self.add_staff_person)

        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox1.addWidget(self.person_name)
        self.vbox1.addWidget(self.person_lastname)
        self.vbox1.addWidget(self.person_profession_id)
        self.vbox1.addWidget(self.add_staff, alignment=QtCore.Qt.AlignCenter)

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
        self.add_medicine.change_hover('#38CD54')
        self.add_medicine.setMinimumWidth(250)
        self.add_medicine.clicked.connect(self.add_medicine_method)

        self.vbox2.addWidget(self.medicine_name_line)
        self.vbox2.addWidget(self.medicine_description)
        self.vbox2.addWidget(self.medicine_price)
        self.vbox2.addWidget(self.medicine_date_of_manufacture)
        self.vbox2.addWidget(self.medicine_shelf_life)
        self.vbox2.addWidget(self.maker_medicine_id)
        self.vbox2.addWidget(self.add_medicine, alignment=QtCore.Qt.AlignCenter)

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.addLayout(self.vbox2)

        self.icon_btn = button.MyButton()
        self.icon_btn.setIcon(QtGui.QIcon('icons/caduceus.png'))
        self.icon_btn.setIconSize(QtCore.QSize(50, 50))
        self.icon_btn.without_hover('#A9AFCD')
        self.icon_btn.clicked.connect(self.add_maker)

        self.hbox1.addWidget(self.icon_btn)
        self.setLayout(self.hbox1)

    def add_employee_func(self):
        """
            Метод экземпляра в котором мы с помощью условного оператора и конструкции try/except выполняем процесс
            занесения информации об професии в вашей аптеке в базу данных
        """
        if all((self.profession_name.text(), self.experience.text(), self.wage.text())):
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
        else:
            self.profession_name.setText('')
            self.experience.setText('')
            self.wage.setText('')
            self.profession_name.setPlaceholderText('Все поля должны быть заполнены')
            self.experience.setPlaceholderText('Все поля должны быть заполнены')
            self.wage.setPlaceholderText('Все поля должны быть заполнены')

    def add_staff_person(self):
        """
            Метод экземпляра в котором мы с помощью условного оператора и конструкции try/except выполняем процесс
            занесения информации об сотруднике в базу данных
        """
        if all((self.person_name.text(), self.person_lastname.text(), self.person_profession_id.currentText())):
            try:
                with db:
                    staff_profession_id = self.person_profession_id.currentText()
                    Staff(
                        firs_name=self.person_name.text(),
                        last_name=self.person_lastname.text(),
                        profession_id=Profession.select(Profession.id).where(
                            Profession.profession == staff_profession_id
                        )
                    ).save()

                    self.person_name.setText('')
                    self.person_lastname.setText('')
                print('ok...')

            except Exception as e:
                print(e)
        else:
            self.person_name.setPlaceholderText('Все поля должны быть заполнены')
            self.person_lastname.setPlaceholderText('Все поля должны быть заполнены')

    def add_medicine_method(self):
        """
            Метод экземпляра в котором мы с помощью условного оператора и конструкции try/except выполняем процесс
            занесения информации об лекарствах в базу данных
        """
        med_name = self.medicine_name_line.text()
        med_description = self.medicine_description.toPlainText()
        med_price = self.medicine_price.text()
        date_of_manuf = self.medicine_date_of_manufacture.text()
        med_shelf_life = self.medicine_shelf_life.text()
        med_maker_id = self.maker_medicine_id.currentText()

        if all((med_name, med_description, med_price, date_of_manuf, med_shelf_life, med_maker_id)):
            try:
                with db:
                    Medicine(
                        name=self.medicine_name_line.text(),
                        description=self.medicine_description.toPlainText(),
                        price=float(self.medicine_price.text().replace(',', '.')),
                        date_of_manufacture=self.medicine_date_of_manufacture.text(),
                        shelf_life=self.medicine_shelf_life.text(),
                        maker_id=Maker.select(Maker.id).where(
                            Maker.company_name == self.maker_medicine_id.currentText()
                        )
                    ).save()
                self.medicine_name_line.setText('')
                self.medicine_description.setText('')
                self.medicine_price.setValue(0.)
                self.medicine_date_of_manufacture.setDate(QDate(2020, 1, 1))
                self.medicine_shelf_life.setDate(QDate(2020, 1, 1))

                print('OK...')

            except Exception as e:
                print(e)
        else:
            self.medicine_name_line.setPlaceholderText('Все поля должны быть заполнены')
            self.medicine_description.setPlaceholderText('Все поля должны быть заполнены')

    def add_maker(self):
        self.maker_app.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = AdminApp()
    final_time = time.time() - start_time
    if int(str(final_time)[0]) < 1:
        print(f"{BColors.BOLD}{random.choice(colors)}--- {final_time} секунд ---")
    elif int(str(final_time)[0]) == 1:
        print(f"{BColors.BOLD}{BColors.WARNING}--- {final_time} секунд ---")
    else:
        print(f"{BColors.BOLD}{BColors.FAIL}--- {final_time} секунд ---")
    widget.show()
    sys.exit(app.exec())
