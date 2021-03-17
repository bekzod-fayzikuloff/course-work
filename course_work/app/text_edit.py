import sys
from PyQt5 import QtWidgets, QtGui
import main


class TextArea(QtWidgets.QTextEdit):

    __style = """
        QTextEdit {
            border: 2px solid black; 
            font-size:13px;
            font-weight: 540;
            background-color: #FCFCFC;
        }
    """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.__class__.__style)
        self.setFont(QtGui.QFont(main.font_family))


class ComboBox(QtWidgets.QComboBox):

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
        self.setFont(QtGui.QFont(main.font_family))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = TextArea()
    widget.show()
    sys.exit(app.exec())
