from PyQt5 import QtWidgets


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
