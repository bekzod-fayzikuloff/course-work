import sys
from PyQt5 import QtGui, QtWidgets

class QCustomQWidget (QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)

        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel    = QtWidgets.QLabel()
        self.textDownQLabel  = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)

        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.iconQLabel      = QtWidgets.QLabel()

        self.iconQLabel.setMinimumSize(80, 80)                   # +++
        self.iconQLabel.setMaximumSize(80, 80)                   # +++

        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)


    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath).scaled(80, 80))  # + scaled(80, 80)


class exampleQMainWindow (QtWidgets.QListWidget):    #QMainWindow):     # +++ / ---
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        #self.myQListWidget = QtWidgets.QListWidget(self)

        # +++
        self.resize(420, 300)
        self.setFrameShape(self.NoFrame) # Нет границы
        self.setFlow(self.LeftToRight)   # Слева направо
        self.setWrapping(True)           # Эти 3 комбинации могут достичь того же эффекта, что и FlowLayout
        self.setResizeMode(self.Adjust)

        for index, name, icon in [
            ('No.1', 'Лена', 'icons/login_ico.png'),
            ('No.2', 'Петя', 'icons/login_ico.png'),
            ('No.3', 'Вася', 'icons/login_ico.png'),
            ('No.4', 'Петя', 'icons/login_ico.png'),
            ('No.5', 'Вася', 'icons/login_ico.png'),
            ('No.6', 'Лена', 'icons/login_ico.png'),
            ('No.7', 'Петя', 'icons/login_ico.png'),
            ('No.8', 'Вася', 'icons/login_ico.png'),
            ('No.9', 'Петя', 'icons/login_ico.png'),
            ('No.10', 'Вася', 'icons/login_ico.png'),
            ]:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setIcon(icon)
            myQListWidgetItem = QtWidgets.QListWidgetItem(self)  #.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            #self.myQListWidget.addItem(myQListWidgetItem)
            self.addItem(myQListWidgetItem)
            #self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            self.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        #self.setCentralWidget(self.myQListWidget)

app = QtWidgets.QApplication([])
window = exampleQMainWindow()
window.show()
sys.exit(app.exec_())