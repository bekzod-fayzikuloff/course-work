import main
import qtwidgets
from PyQt5 import QtWidgets, QtGui


class MyLine(QtWidgets.QLineEdit):
    """
        Класс MyLine явсляется наследником класса QLineEdit в котором мы стилизуем экземпляры нашего класса
    """
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
        """
        Метод в котором мы изменяем размер шрифта нашего текстового поля
        :param size: --> принемает параметр size который является целым числом
        :return None: ничего не возвращает
        """
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
    """
        Класс PasswordEdit явсляется наследником класса qtwidgets.PasswordEdit
        в котором мы стилизуем экземпляры нашего класса
    """

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

    def change_font_color(self, color: str):
        """
        Метод в котором мы изменяем цвет шрифта нашего текстового поля
        :param color: --> принемает параметр color который является строковым типом данных
        :return None: ничего не возвращает
        """
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


class ScrollBar(QtWidgets.QScrollBar):

    """
        Класс ScrollBar явсляется наследником класса QtWidgets.QScrollBar
        в котором мы стилизуем экземпляры нашего класса
    """

    __style = """
            QScrollBar {
                width: 15px;
                margin: 45px 0 45px 0;
                background: #fff;
            }

            QScrollBar::handle {
                border: 2px solid grey;
                background: white;
                max-height: 7px;
            }

            QScrollBar::add-line:vertical {
                border: 2px solid grey;
                background: none;
                height: 45px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                border: 2px solid grey;
                background: none;
                height: 45px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::up-arrow:vertical {
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {upArrow}
            }

            QScrollBar::down-arrow:vertical {
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {downArrow}
            }

            QScrollBar::left-arrow:vertical {
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {leftArrow}
            }

            QScrollBar::right-arrow:vertical {
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {rightArrow}
            }
    """

    def __init__(self):
        super().__init__()
        # self.setSingleStep(7)
        self.setMaximum(1)
        self.setMinimum(1)
        self.setPageStep(1)
        self.setStyleSheet(self.__class__.__style)
