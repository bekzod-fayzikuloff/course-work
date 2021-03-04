from PyQt5 import QtWidgets, QtGui


class MyButton(QtWidgets.QPushButton):
    __stylesheet__ = '''
        QPushButton{
            background-color: #3C3F41;
            color: #E1E1E1;
            border-radius: 10px;        
        }
        QPushButton:hover {
        background-color: #A648C7;
        }
        QPushButton:pressed {
        background-color: #A648C7;
        }
    '''

    def __init__(self, text_on_btn=None):
        super().__init__()
        self.text_on_btn = text_on_btn
        self.setMinimumHeight(20)
        self.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))
        self.setText(self.text_on_btn)
        self.setStyleSheet(MyButton.__stylesheet__)

    def change_hover(self, color):
        __stylesheet__ = '''
            QPushButton{
                background-color: #3C3F41;
                color: #E1E1E1;
                border-radius: 10px;        
            }
            QPushButton:hover {
            background-color: %s ;
            }
            QPushButton:pressed {
            background-color: %s;
            }
        ''' % (color, color)

        self.setStyleSheet(__stylesheet__)

    def without_hover(self, color):
        __stylesheet__ = '''
            QPushButton{
                background-color: %s;
                color: #E1E1E1;
                border-radius: 10px;        
            }

        ''' % color

        self.setStyleSheet(__stylesheet__)