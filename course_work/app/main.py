import random
import sys

import admin_panel

from PyQt5 import QtWidgets, QtGui, QtCore
from course_work.db.models import *

med_icons = [r'icons/med.png', r'icons/med1.png', r'icons/med2.png']
font_family = 'Century Gothic'


def spaces(count: int):
    return ' ' * count


class MedicineAppWidget(QtWidgets.QWidget):

    __css_label = """
        QLabel {
            border: 2px solid #CFA0E9;
            background-color: #fff;
        }
        QLabel:hover {
            border: 2px solid #E1E1E1;
            background-color: #F5F5F5;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('background-color: #91ADCD;')

        self.textVbox = QtWidgets.QVBoxLayout()

        self.text_title = QtWidgets.QLabel()
        self.text_title.setMargin(10)
        self.text_title.setStyleSheet('background-color: #fff;')

        self.text_title.setContentsMargins(0, 0, 0, -20)
        self.text_description = QtWidgets.QLabel()
        self.text_description.setWordWrap(True)
        self.text_description.setMargin(20)
        self.text_description.setStyleSheet(self.__class__.__css_label)

        self.text_info = QtWidgets.QLabel()
        self.text_info.setMargin(10)
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
        self.text_title.setFont(QtGui.QFont(font_family, 13, QtGui.QFont.Bold))
        self.text_title.setText(text)

    def set_text_description(self, text: str):
        self.text_description.setFont(QtGui.QFont(font_family, 12, QtGui.QFont.Bold))
        self.text_description.setText(text)

    def set_price(self, price):
        self.text_info.setFont(QtGui.QFont(font_family, 10, QtGui.QFont.Bold))
        self.text_info.setText(str(price))

    def set_icon(self, path: str):
        self.iconLabel.setPixmap(QtGui.QPixmap(path).scaled(100, 100))


class MainAppWindow(QtWidgets.QListWidget):

    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.setMinimumSize(800, 500)
        self.setStyleSheet('background-color: #fff;')
        self.setFrameShape(self.NoFrame)
        # self.setFlow(self.LeftToRight)
        # self.setWrapping(True)
        self.setResizeMode(self.Adjust)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.clearSelection()
        self.unit_ui()

    def unit_ui(self, filter_=None):
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
            medicine = Medicine.select().where(
                (Medicine.name.contains(filter_) | (Medicine.description.contains(filter_)))
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

    def refresh(self):
        for j in range(self.count()):
            self.takeItem(0)
        self.unit_ui()


class MainApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('background-color: #3C3F41;')
        self.setWindowTitle('Pharmacy')
        self.setWindowIcon(QtGui.QIcon(r'icons/caduceus.png'))
        self.main_panel = admin_panel.PanelApp()

        self.main_panel.search_line.setFont(QtGui.QFont(font_family))
        self.main_panel.search_btn.setFont(QtGui.QFont(font_family, weight=QtGui.QFont.Bold))
        self.main_panel.refresh_btn.setFont(QtGui.QFont(font_family, weight=QtGui.QFont.Bold))
        self.main_panel.take_parent_bg(parent=self)

        self.main_panel.refresh_btn.clicked.connect(self.medicine_refresh)
        self.main_panel.search_btn.clicked.connect(self.medicine_search)

        self.main_app = MainAppWindow()

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.main_panel)
        self.vbox.addWidget(self.main_app)
        self.setLayout(self.vbox)

    def medicine_refresh(self):
        self.main_app.refresh()

    def medicine_search(self):
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
