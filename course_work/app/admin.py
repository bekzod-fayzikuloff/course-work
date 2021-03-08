import sys
import button
from PyQt5 import QtWidgets
from course_work.db.models import *


class AdminApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.profession_name = QtWidgets.QLineEdit()
        self.experience = QtWidgets.QLineEdit()
        self.wage = QtWidgets.QLineEdit()
        self.button = button.MyButton('add employee')

        self.button.clicked.connect(self.add_employee_func)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.profession_name)
        self.vbox.addWidget(self.experience)
        self.vbox.addWidget(self.wage)
        self.vbox.addWidget(self.button)

        # -------------------------------

        self.person_name = QtWidgets.QLineEdit()
        self.person_lastname = QtWidgets.QLineEdit()
        self.person_profession_id = QtWidgets.QLineEdit()
        self.add_staff = button.MyButton('add employee')
        self.add_staff.clicked.connect(self.add_staff_person)

        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox1.addWidget(self.person_name)
        self.vbox1.addWidget(self.person_lastname)
        self.vbox1.addWidget(self.person_profession_id)
        self.vbox1.addWidget(self.add_staff)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.hbox.addLayout(self.vbox1)

        self.setLayout(self.hbox)

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
                Staff(
                    firs_name=self.person_name.text(),
                    last_name=self.person_lastname.text(),
                    profession_id=int(self.person_profession_id.text())
                ).save()

                self.person_name.setText('')
                self.person_lastname.setText('')
                self.person_profession_id.setText('')
            print('ok...')

        except ValueError:
            self.person_profession_id.setText('')
            self.person_profession_id.setPlaceholderText('Your need write numeric type')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = AdminApp()
    widget.show()
    sys.exit(app.exec())
