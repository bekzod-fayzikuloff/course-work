import sys
import line_module
from PyQt5 import QtWidgets


from course_work.app import button


class PanelApp(QtWidgets.QWidget):

    def __init__(self, parent_=None):
        super().__init__()
        self.setMaximumHeight(60)

        self.search_line = line_module.MyLine()

        self.search_btn = button.MyButton('search')
        self.search_btn.change_hover('#38CD54')
        self.search_btn.setMinimumWidth(60)
        self.search_btn.setMaximumHeight(21)

        self.refresh_btn = button.MyButton('refresh')
        self.refresh_btn.setMinimumWidth(60)
        self.refresh_btn.change_hover('#38CD54')
        self.refresh_btn.setMaximumHeight(21)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.search_line)
        self.hbox.addWidget(self.search_btn)
        self.hbox.addWidget(self.refresh_btn)
        self.setLayout(self.hbox)

    def take_parent_bg(self, parent):
        parent.styleSheet()
        self.setStyleSheet(parent.styleSheet())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = PanelApp()
    widget.show()
    sys.exit(app.exec())
