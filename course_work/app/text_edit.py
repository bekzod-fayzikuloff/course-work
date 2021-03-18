import sys
from PyQt5 import QtWidgets, QtGui
import main


class BaseStyle:
    _style = """
        border: 2px solid black; 
        font-size:13px;
        font-weight: 540;
        background-color: #FCFCFC;
        """

    _style_edit = """
         border: 2px solid #fff;
         border-radius: 7px;
         background-color: #3C3F41;
         color: #9E9FA0;
         font-size: 12px;
         font-style: oblique;
         font-size-adjust: 0.7;
         font-weight: 700;
    """


class TextArea(QtWidgets.QTextEdit, BaseStyle):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style)
        self.setFont(QtGui.QFont(main.font_family))


class ComboBox(QtWidgets.QComboBox, BaseStyle):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style_edit)
        self.setFont(QtGui.QFont(main.font_family))

    def change_font_color(self, color):
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


class DateEdit(QtWidgets.QDateEdit, BaseStyle):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style_edit)

    def change_font_color(self, color):
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


class DoubleSpinBox(QtWidgets.QDoubleSpinBox, BaseStyle):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style_edit)

    def change_font_color(self, color):
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = TextArea()
    widget.show()
    sys.exit(app.exec())
