import random
import sys

import admin_panel
import line_module
# import sidebar_panel

from PyQt5 import QtWidgets, QtGui, QtCore
from course_work.db.models import *

med_icons = [r'icons/med.png', r'icons/cad.png', r'icons/Medicine.png']
font_family = 'Century Gothic'


def spaces(count: int):
    return ' ' * count


class MedicineAppWidget(QtWidgets.QWidget):
    """
    Класс MedicineAppWidget наследуется от класса QtWidgets.QWidget в нутри которого мы создаем экземпляры класса
    QtWidgets.QLabel и методы которые позволяют нам изменять содержимое наших экземпляров
    """

    __css_label = """
            border: 2px solid #CFA0E9;
            background-color: #fff;
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('background-color: #91ADCD;')

        self.textVbox = QtWidgets.QVBoxLayout()

        self.text_title = QtWidgets.QLabel()
        self.text_title.setMargin(10)
        self.text_title.setMaximumHeight(40)
        self.text_title.setStyleSheet('background-color: #fff;')

        self.text_title.setContentsMargins(0, 0, 0, -20)
        self.text_description = QtWidgets.QLabel()
        self.text_description.setWordWrap(True)
        self.text_description.setMargin(20)
        self.text_description.setStyleSheet(self.__class__.__css_label)

        self.text_info = QtWidgets.QLabel()
        self.text_info.setMargin(5)
        self.text_info.setMaximumHeight(30)
        self.text_info.setStyleSheet(self.__class__.__css_label)

        self.hbox_med = QtWidgets.QHBoxLayout()
        self.hbox_med.setContentsMargins(0, 0, 0, 0)
        self.hbox_med.addWidget(self.text_info)

        self.textVbox.addWidget(self.text_title, alignment=QtCore.Qt.AlignCenter)
        self.textVbox.addWidget(self.text_description)
        self.textVbox.addLayout(self.hbox_med)

        self.allHBox = QtWidgets.QHBoxLayout()
        self.iconLabel = QtWidgets.QLabel()
        self.iconLabel.setFixedSize(100, 100)

        self.allHBox.addWidget(self.iconLabel, stretch=0)
        self.allHBox.addLayout(self.textVbox, stretch=1)

        self.setLayout(self.allHBox)

    def set_text_title(self, text: str):
        """
        Метод который принемает параметр text и перезаписывает содержимое нашего атрибута self.text_title
        :param text: --> строковой тип данных
        :return None:
        """
        self.text_title.setFont(QtGui.QFont(font_family, 13, QtGui.QFont.Bold))
        self.text_title.setText(text)

    def set_text_description(self, text: str):
        """
        Метод который принемает параметр text и перезаписывает содержимое нашего атрибута self.text_description
        :param text: --> строковой тип данных
        :return None:
        """
        self.text_description.setFont(QtGui.QFont(font_family, 12, QtGui.QFont.Bold))
        self.text_description.setText(text)

    def set_price(self, price):
        """
        Метод который принемает параметр text и перезаписывает содержимое нашего атрибута self.text_info
        :param price: --> строковой тип данных или (int, float)
        :return None:
        """
        self.text_info.setFont(QtGui.QFont(font_family, 10, QtGui.QFont.Bold))
        self.text_info.setText(str(price))

    def set_icon(self, path: str):
        """
        Метод который принемает параметр text и перезаписывает содержимое нашего атрибута self.iconLabel то есть
        ставит иконку для нашего экземпляра класса QLabel
        :param path: --> строковой тип данных(который должен быть относительным или абсолютным путем до файла)
        :return None:
        """
        self.iconLabel.setPixmap(QtGui.QPixmap(path).scaled(100, 100))


class MainAppWindow(QtWidgets.QListWidget):

    """
        Класс MainAppWindow наследуется от класса QtWidgets.QListWidget -> внутри него мы реализуем отображение
        всех элементов из БД а также методы реализации поиска по ключевым словам и значениям из этих данных
        и проведем некоторые манипуляии позволяющие изменить внешний вид нашего приложения
    """

    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.setMinimumSize(800, 500)
        self.setStyleSheet('background-color: #fff;')
        self.setFrameShape(self.NoFrame)
        self.setFlow(self.TopToBottom)
        self.setWrapping(False)
        self.setResizeMode(self.Adjust)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.clearSelection()
        self.custom_scroll = line_module.ScrollBar()
        self.setVerticalScrollBar(self.custom_scroll)
        self.unit_ui()

    def unit_ui(self, filter_=None):
        """
        Метод который ренализует основную часть всей выпоняемой нами работы так как он принемает на себя роль регулятора
        который при передаче аргумента filter_ должен производить логику выборки информации из базы данных а так же его
        роль нельзя переоценит при моменте когда нам нужно обновить содержание(информацию из БД) так как мы просто
        вызываем данную функцию не передавая никаких параметров
        :param filter_: -> параметр выборки данных из базы данных если он не передан то его значение по умолчанию ->None
        :return None:
        """
        if not filter_:
            medicine = Medicine.select().order_by()
            for med in medicine:
                my_app_widget = MedicineAppWidget()
                my_app_widget.set_text_title(f' {med.name} ({med.maker_id.company_name})')
                my_app_widget.set_text_description(f'{str(med.description).capitalize()}')
                my_app_widget.set_price(
                    f'{med.price} ${spaces(20)}Произведен: '
                    f'{med.date_of_manufacture}{spaces(20)} Годен до: {med.shelf_life}'
                )
                my_app_widget.set_icon(random.choice(med_icons))

                list_widget_item = QtWidgets.QListWidgetItem(self)
                list_widget_item.setSizeHint(my_app_widget.sizeHint())
                self.addItem(list_widget_item)
                self.setItemWidget(list_widget_item, my_app_widget)
        else:
            try:
                medicine = Medicine.select().join(Maker).where(
                    (Medicine.name.contains(filter_) | (Medicine.description.contains(filter_))) |
                    (Medicine.shelf_life.contains(filter_)) | (Medicine.price.contains(filter_)) |
                    (Medicine.maker_id.company_name.contains(filter_))
                )
                if len(medicine) == 0:
                    self.setFont(QtGui.QFont(font_family, 14, QtGui.QFont.Bold))
                    self.addItem('По данному запросу нету пододящих результатов')
                for med in medicine:
                    my_app_widget = MedicineAppWidget()
                    my_app_widget.set_text_title(f' {med.name} ({med.maker_id.company_name})')
                    my_app_widget.set_text_description(f'{str(med.description).capitalize()}')
                    my_app_widget.set_price(
                        f'{med.price} ${spaces(20)}Произведен: '
                        f'{med.date_of_manufacture}{spaces(20)} Годен до: {med.shelf_life}'
                    )
                    my_app_widget.set_icon(random.choice(med_icons))

                    list_widget_item = QtWidgets.QListWidgetItem(self)
                    list_widget_item.setSizeHint(my_app_widget.sizeHint())
                    self.addItem(list_widget_item)
                    self.setItemWidget(list_widget_item, my_app_widget)
            except Exception as e:
                print(e)

    def refresh(self):
        """
        Метод который очищает содержимое Внешнего окна и просто вызывает метод self.unit_ui() -> без аргуменнов что
        позволит нам просто обновить страницу с информацией о лекарствах
        :return None:
        """
        for j in range(self.count()):
            self.takeItem(0)
        self.unit_ui()


class MainApp(QtWidgets.QWidget):
    """
        Главное окно нашего приложения в нем мы компануем все элементы нашего главного окна в одно приложение
        в котором есть панель для поиска по ключевым словам а также есть возможность внесения различной информации
    """
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('background-color: #3C3F41;')
        self.setWindowTitle('Pharmacy')
        self.setWindowIcon(QtGui.QIcon(r'icons/caduceus.png'))
        self.main_panel = admin_panel.PanelApp()

        self.main_panel.search_line.setFont(QtGui.QFont(font_family))
        self.main_panel.search_btn.setFont(QtGui.QFont(font_family, weight=1100))
        self.main_panel.refresh_btn.setFont(QtGui.QFont(font_family, weight=1100))
        self.main_panel.take_parent_bg(parent=self)

        self.main_panel.refresh_btn.clicked.connect(self.medicine_refresh)
        self.main_panel.search_btn.clicked.connect(self.medicine_search)

        self.main_app = MainAppWindow()

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.main_panel)
        self.vbox.addWidget(self.main_app)
        # self.hbox = QtWidgets.QHBoxLayout()
        # self.hbox.addWidget(sidebar_panel.SideBar())
        # self.hbox.addLayout(self.vbox)
        # self.setLayout(self.hbox)
        self.setLayout(self.vbox)

    def medicine_refresh(self):
        """
        Обнавляем содержимое нашего главного окна
        :return None:
        """
        self.main_app.refresh()

    def medicine_search(self):
        """
        Производим удаление и всех элементов и производим поиск по ключевому слову
        :return None:
        """
        filter_ = self.main_panel.search_line.text()
        for med in range(self.main_app.count()):
            self.main_app.takeItem(0)
        self.main_app.unit_ui(filter_=filter_)
        self.main_panel.search_line.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    id_ = QtGui.QFontDatabase.addApplicationFont(r'font/my_font.ttf')
    widget = MainApp()
    widget.show()
    sys.exit(app.exec())
