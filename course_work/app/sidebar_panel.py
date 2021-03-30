import sys
import button
from PyQt5 import QtWidgets


def foo():
    print('s')


class SideBar(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.setMaximumWidth(20)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle('sdsd')

        self.admin_btn = button.MyButton('admin')
        self.catalog_btn = button.MyButton('catalog')

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.addWidget(self.admin_btn)
        self.vbox.addWidget(self.catalog_btn)
        self.vbox.setStretch(100, 1)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = SideBar()
    widget.show()
    sys.exit(app.exec())
