import main
import qtwidgets
from PyQt5 import QtWidgets, QtGui


class MyLine(QtWidgets.QLineEdit):
    __style = """
        QLineEdit {
            background-color: #3C3F41;
            border: 2px solid #fff;
            border-radius: 8px;
            position: absolute;
            font-size: 14px;
            color: #fff;
            font-style: oblique;
            font-size-adjust: 0.7;
            font-weight: 700;
        }
        QLineEdit:hover {
            border: 2px solid #black;
            background-color: #fff;
            color: black;
        }
    """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(MyLine.__style)
        self.setFixedHeight(21)
        self.setFont(QtGui.QFont(main.font_family))

    def change_font_size(self, size: int):
        _style = """
            QLineEdit {
                background-color: #3C3F41;
                border: 2px solid #fff;
                border-radius: 8px;
                position: absolute;
                font-size: %spx;
                color: #fff;
                font-style: oblique;
                font-size-adjust: 0.7;
                font-weight: 700;
            }
            QLineEdit:hover {
                border: 2px solid #000;
                background-color: #fff;
                color: black;
            }  
        """ % size
        self.setStyleSheet(_style)


class PasswordEdit(qtwidgets.PasswordEdit):

    __style = """
        border: 2px solid #fff;
        border-radius: 7px;
        background-color: #3C3F41;
        color: #9E9FA0;
        font-size: 12px;
        font-style: oblique;
        font-size-adjust: 0.7;
        font-weight: 700; 
        """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.__class__.__style)

    def change_font_color(self, color):
        self.setStyleSheet(self.styleSheet() + f'color: {color}')
