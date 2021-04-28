import sys
# from course_work.app import admin

from PyQt5 import QtWidgets
from course_work.app import button


class SideBar(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMaximumWidth(40)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle('sdsd')

        self.admin_btn = button.MyButton('admin')
        self.admin_btn.clicked.connect(self.foo)

        self.verticalSpacer = QtWidgets.QSpacerItem(
                20, 500, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding
        )

        self.catalog_btn = button.MyButton('exit')
        self.catalog_btn.clicked.connect(self.foo)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.addSpacerItem(QtWidgets.QSpacerItem(20, 10))
        self.vbox.addWidget(self.admin_btn)
        self.vbox.addSpacerItem(self.verticalSpacer)
        self.vbox.addWidget(self.catalog_btn)
        self.setLayout(self.vbox)

    def foo(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = SideBar()
    widget.show()
    sys.exit(app.exec())
