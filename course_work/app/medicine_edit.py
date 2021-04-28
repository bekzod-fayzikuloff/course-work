import sys
import datetime

from PyQt5 import QtWidgets, QtGui, QtCore

from course_work.app import text_edit
from course_work.app.conf_app import resource_path
from course_work.app import line_module
from course_work.app import button
from course_work.db import models
from course_work.app.conf_app import set_gradient


def date_convert(date_arr: list):
    """
    Функция которая принемает список даты в формате ['day <-- строка в формате ['01'-'31']',
                                                    'month <-- строка в формате ['01'-'12']',
                                                    'year <-- строка в формате ['1000'-'2070']'
                                                    ]
    и проводит его конвертацию в объект date модуля datetime и возвращает этот объект
    :param date_arr: --> Принемает обязательный параметр с типом list
    :return datetime.date(int(year), int(month), int(day)): --> Возвращает объект типа datetime.date
    """
    day, month, year = date_arr
    return datetime.date(int(year), int(month), int(day))


class MedicineEdit(QtWidgets.QWidget):
    """
        Класс MedicineEdit является наследником класса QtWidgets.QWidget в котором мы определяем логику и внешний вид
        взаимодествия для изменения данных хранящихся в базе данных (удаление и изменение)
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edition')
        self.setWindowIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/admin.png')))
        self.setMinimumWidth(400)
        self.setMaximumWidth(720)
        self.setMaximumHeight(100)
        set_gradient(self)

        self.edit_window = None
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.medicine_name = text_edit.ComboBox()
        for j in models.Medicine.select():
            self.medicine_name.addItem(j.name)

        self.delete_button = button.MyButton('Delete')
        self.delete_button.change_hover('#F72C36')
        # self.delete_button.setFixedWidth(100)
        self.delete_button.clicked.connect(self.delete_med)

        self.edit_button = button.MyButton('Edit')
        self.edit_button.clicked.connect(self.edit_med)
        # self.edit_button.setFixedWidth(100)
        self.edit_button.change_hover('#38CD54')

        self.hbox.addWidget(self.delete_button)
        self.hbox.addWidget(self.edit_button)

        self.vbox.addWidget(self.medicine_name)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def delete_med(self):
        """ Метод который удаляет занчение из таблицы в базе данных """
        try:
            query_text = self.medicine_name.currentText()
            record = models.Medicine.get(models.Medicine.name == query_text)
            if models.Medicine.delete_by_id(record):
                self.medicine_name.clear()
                for i in models.Medicine.select():
                    self.medicine_name.addItem(i.name)
            else:
                print('not ok')
        except models.Medicine.DoesNotExist:
            pass

    def edit_med(self):
        """
            Метод который переопределяет атрибут self.edit_window делая его экземпляром класса EditWindow
            данного модуля и передает ему в конструктор объязательный параметр для получения информации о
            нужной нам поля в таблице базы данных
        """
        self.edit_window = EditWindow(models.Medicine.get(models.Medicine.name == self.medicine_name.currentText()))
        self.edit_window.show()


class EditWindow(QtWidgets.QWidget):
    """
        Класса EditWindow наследуется от класса QtWidgetsQWidget в котором мы определяем функционал взаимодествия с
        БД для того чтобы мы смогли редактировать ее содержание
    """

    def __init__(self, pk):
        """
            Метод __init__ принемает в как обязательнный аргумент параметр pk <- и его помощью
            обращается к нужной записи в Базе Данных
        :param pk:
        """
        super().__init__()
        self.setMinimumWidth(560)
        self.setMaximumHeight(560)
        self.setWindowTitle('Change Medicine Data')
        self.setWindowIcon(QtGui.QIcon(resource_path(r'course_work/app/icons/admin.png')))
        set_gradient(self)

        # --------- elements ui ---------#

        self.pk = pk
        self.__record = models.Medicine.get(models.Medicine.id == self.pk)
        self.med_name = line_module.MyLine()
        self.med_name.setText(self.__record.name)

        self.med_description = text_edit.TextArea()
        self.med_description.setText(self.__record.description)

        self.med_price = text_edit.DoubleSpinBox()
        self.med_price.setMaximum(10000)
        self.med_price.setValue(self.__record.price)

        date_of_manufacture = self.__record.date_of_manufacture.split('.')
        shelf_life_date = self.__record.shelf_life.split('.')

        self.med_date_of_manufacture = text_edit.DateEdit()
        self.med_date_of_manufacture.setDate(date_convert(date_of_manufacture))

        self.med_shelf_life = text_edit.DateEdit()
        self.med_shelf_life.setDate(date_convert(shelf_life_date))

        self.change_info_btn = button.MyButton('Change information')
        self.change_info_btn.setMinimumWidth(200)
        self.change_info_btn.setMaximumWidth(320)
        self.change_info_btn.change_hover('#38CD54')
        self.change_info_btn.clicked.connect(self.set_new_data)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.med_name)
        self.vbox.addWidget(self.med_description)
        self.vbox.addWidget(self.med_price)
        self.vbox.addWidget(self.med_date_of_manufacture)
        self.vbox.addWidget(self.med_shelf_life)
        self.vbox.addWidget(self.change_info_btn, alignment=QtCore.Qt.AlignCenter)
        self.setLayout(self.vbox)

    def set_new_data(self):
        """
            Метод set_new_data в момент вызыва получает значения полей нащего окна и сохраняет их в базе данных
        :return None:
        """
        try:
            with models.db:
                models.Medicine.update(
                    name=self.med_name.text(),
                    description=self.med_description.toPlainText(),
                    price=float(self.med_price.text().replace(',', '.')),
                    date_of_manufacture=self.med_date_of_manufacture.text(),
                    shelf_life=self.med_shelf_life.text(),
                ).where(
                    models.Medicine.id == self.pk
                ).execute()
            print('ok')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MedicineEdit()
    window.show()
    sys.exit(app.exec())
