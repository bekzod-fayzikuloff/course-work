import sys

from PyQt5 import QtWidgets

from course_work.app import login


def start_app():
    application = QtWidgets.QApplication(sys.argv)
    app = login.Widget()
    app.show()
    sys.exit(application.exec())


if __name__ == '__main__':
    start_app()
