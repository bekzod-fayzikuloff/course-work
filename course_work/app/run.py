import sys
import login
from PyQt5 import QtWidgets


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    main = login.Widget()
    main.show()
    sys.exit(application.exec())
