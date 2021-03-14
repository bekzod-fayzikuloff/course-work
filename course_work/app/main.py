import random
import sys
import admin_panel

from PyQt5 import QtWidgets, QtGui, QtCore
from course_work.db.models import *

med_icons = [r'icons/med.png', r'icons/med1.png', r'icons/med2.png']


def spaces(cout: int):
    return ' ' * cout


class MedicineAppWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('background-color: #91ADCD;')
        self.textVbox = QtWidgets.QVBoxLayout()

        self.text_title = QtWidgets.QLabel()
        self.text_title.setMargin(10)
        self.text_title.setContentsMargins(0, 0, 0, -20)
        self.text_description = QtWidgets.QLabel()
        self.text_description.setWordWrap(True)
        self.text_description.setMargin(20)

        self.text_info = QtWidgets.QLabel()
        self.text_info.setMargin(10)

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
        self.text_title.setFont(QtGui.QFont('SansSerif', 12, QtGui.QFont.Bold))
        self.text_title.setText(text)

    def set_text_description(self, text: str):
        self.text_description.setFont(QtGui.QFont('SansSerif', 11, QtGui.QFont.Bold))
        self.text_description.setText(text)

    def set_price(self, price):
        self.text_info.setFont(QtGui.QFont('SansSerif', 9, QtGui.QFont.Bold))
        self.text_info.setText(str(price))

    def set_icon(self, path: str):
        self.iconLabel.setPixmap(QtGui.QPixmap(path).scaled(100, 100))


class MainAppWindow(QtWidgets.QListWidget):

    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.setMinimumSize(800, 500)
        self.setStyleSheet('background-color: #91ADCD;')
        self.setFrameShape(self.NoFrame)
        # self.setFlow(self.LeftToRight)
        # self.setWrapping(True)
        self.setResizeMode(self.Adjust)
        self.admin_panel = admin_panel.PanelApp()

        self.unit_ui()

    def unit_ui(self):
        medicine = Medicine.select().order_by(Medicine.name)
        for med in medicine:
            my_app_widget = MedicineAppWidget()
            my_app_widget.set_text_title(f' {med.name} ({med.maker_id.company_name})')
            my_app_widget.set_text_description(f'{str(med.description).capitalize()}')
            my_app_widget.set_price(
                f'{med.price} ${spaces(20)}Произведен: {med.date_of_manufacture}{spaces(20)} Годен до: {med.shelf_life}'
            )
            my_app_widget.set_icon(random.choice(med_icons))

            list_widget_item = QtWidgets.QListWidgetItem(self)
            list_widget_item.setSizeHint(my_app_widget.sizeHint())
            self.addItem(list_widget_item)
            self.setItemWidget(list_widget_item, my_app_widget)


class MainApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.main_panel = admin_panel.PanelApp()
        self.main_panel.refresh_btn.clicked.connect(self.medicine_refresh)

        self.main_app = MainAppWindow()

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.main_panel)
        self.vbox.addWidget(self.main_app)
        self.setLayout(self.vbox)

    def medicine_refresh(self):
        print('ok')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MainApp()
    widget.show()
    sys.exit(app.exec())
