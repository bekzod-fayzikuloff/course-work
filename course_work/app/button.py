from PyQt5 import QtWidgets, QtGui


class MyButton(QtWidgets.QPushButton):
    """
        Класс MyButton который служит для изменения стандартого внешего вида кнопки путем наследования от класса
        QtWidgets.QPushButton и вызова различных его методов которые изменяют стандартное поведение `страндартной`
        кнопки
    """
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
        """
        Метод конструктор нашего класса принипющий один не обезтельный параметр `text_on_btn` что по умолчанию равен
        None, а при передаче аргумента он будет отображаться на кнопке, а в самом констукторе происходит маленькое
        изменение стандартных значений свойств класса QPushButton
        :param text_on_btn:
        """
        super().__init__()
        self.text_on_btn = text_on_btn
        self.setMinimumHeight(20)
        self.setFont(QtGui.QFont('SansSerif', 10, QtGui.QFont.Bold))
        self.setText(self.text_on_btn)
        self.setStyleSheet(MyButton.__stylesheet__)

    def change_hover(self, color):
        """
        Метод класса служащий для изменения заднего фона(hover эффекта) кнопки который принимает один обязательный
        аргумент color который должен служить цветом для передачи, и этот метод ничего не принимает, а просто изменяет
        состояние экземпляра класса
        :param color:
        :return None:
        """
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
        """
        Метод класса служащий для изменения заднего фона и убирает(hover effect) кнопки который принимает один
        обязательный аргумент color который должен служить цветом для передачи, и этот метод ничего не принимает,
        а просто изменяет состояние экземпляра класса
        :param color:
        :return:
        """
        __stylesheet__ = '''
            QPushButton{
                background-color: %s;
                color: #E1E1E1;
                border-radius: 10px;        
            }

        ''' % color

        self.setStyleSheet(__stylesheet__)
