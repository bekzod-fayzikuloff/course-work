import sys
import login
import line_module
from PyQt5 import QtWidgets, QtGui

from course_work.app import button


class PanelApp(QtWidgets.QWidget):
    """
    Класс PanelApp является классом наследником класса QtWidgets.QWidget в котором мы описываем некоторый функцианал и
    разделяем класса на несколько модулей что позволяет легче разобраться в написанном коде
    """
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(60)

        self.search_line = line_module.MyLine()

        self.search_btn = button.MyButton('Search')
        self.search_btn.setIcon(QtGui.QIcon(login.resource_path(r'icons/search.png')))
        self.search_btn.change_hover('#38CD54')
        self.search_btn.setMinimumWidth(70)
        self.search_btn.setMaximumHeight(21)

        self.refresh_btn = button.MyButton('Refresh')
        self.refresh_btn.setIcon(QtGui.QIcon(login.resource_path(r'icons/refreshing.png')))
        self.refresh_btn.setMinimumWidth(70)
        self.refresh_btn.change_hover('#38CD54')
        self.refresh_btn.setMaximumHeight(21)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.search_line)
        self.hbox.addWidget(self.search_btn)
        self.hbox.addWidget(self.refresh_btn)
        self.setLayout(self.hbox)

    def take_parent_bg(self, parent):
        """
        Метод при вызове которого мы получаем стиль передоваемого параметра
        и зададим этот стиль нашему экземпляру класса
        :return None:
        """
        try:
            parent.styleSheet()
            self.setStyleSheet(parent.styleSheet())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = PanelApp()
    widget.show()
    sys.exit(app.exec())
