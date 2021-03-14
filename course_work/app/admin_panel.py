import sys
from PyQt5 import QtWidgets

from course_work.app import button


class PanelApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMaximumHeight(60)

        self.search_line = QtWidgets.QLineEdit()
        self.search_btn = button.MyButton('search')
        self.refresh_btn = button.MyButton('refresh')

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.search_line)
        self.hbox.addWidget(self.search_btn)
        self.hbox.addWidget(self.refresh_btn)
        self.setLayout(self.hbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = PanelApp()
    widget.show()
    sys.exit(app.exec())
