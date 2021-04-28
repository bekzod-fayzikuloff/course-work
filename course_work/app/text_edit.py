from PyQt5 import QtWidgets, QtGui
from course_work.app import main


class BaseStyle:
    """
        Некий базовый класс со своими атрибутами которые мы будем использовать для наших классов
        которые будут наследоваться от него
    """
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
    """
        Класс TextArea наследуется от класса QtWidgets.QTextEdit и BaseStyle в котором мы протсо вызываем методы
        класса QtWidgets.QTextEdit(setStyleSheet() и setFont()) передаем и артбут базового класса и атрибут с модуля
        main который мы импортируем
    """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style)
        self.setFont(QtGui.QFont(main.font_family))


class ComboBox(QtWidgets.QComboBox, BaseStyle):
    """
        Класс ComboBox наследуется от класса QtWidgets.QComboBox и BaseStyle в котором мы протсо вызываем методы
        класса QtWidgets.QTextEdit(setStyleSheet() и setFont()) передаем и артбут базового класса и атрибут с модуля
        main который мы импортируем
    """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style_edit)
        self.setFont(QtGui.QFont(main.font_family))

    def change_font_color(self, color):
        """
        Метод который изменяет цвет текста экземпляра класса
        :param color:
        :return None:
        """
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


class DateEdit(QtWidgets.QDateEdit, BaseStyle):
    """
        Класс DateEdit наследуется от класса QtWidgets.QDateEdit и BaseStyle в котором мы протсо вызываем методы
        класса QtWidgets.QDateEdit(setStyleSheet() ) передаем и артбут базового класса
    """

    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style_edit)

    def change_font_color(self, color):
        """
        Метод который изменяет цвет текста экземпляра класса
        :param color:
        :return None:
        """
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


class DoubleSpinBox(QtWidgets.QDoubleSpinBox, BaseStyle):
    """
        Класс DoubleSpinBox наследуется от класса QtWidgets.QDoubleSpinBox и BaseStyle в
        котором мы протсо вызываем методы класса
        QtWidgets.QDoubleSpinBox(setStyleSheet() ) передаем и артбут базового класса
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet(super()._style_edit)

    def change_font_color(self, color):
        """
        Метод который изменяет цвет текста экземпляра класса
        :param color:
        :return None:
        """
        self.setStyleSheet(self.styleSheet() + f'color: {color}')


if __name__ == '__main__':
    pass
