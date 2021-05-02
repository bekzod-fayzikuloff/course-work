import sys
from PyQt5 import QtWidgets
from course_work.app import admin

app = QtWidgets.QApplication(sys.argv)
widget = admin.AdminApp()
widget.show()
sys.exit(app.exec())
