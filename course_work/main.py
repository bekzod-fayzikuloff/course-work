import sys

from PyQt5 import QtWidgets


class MyMainApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyMainApp()
    widget.show()
    sys.exit(app.exec())