import os.path
import sys

from PyQt5 import QtGui


def set_gradient(instance):
    p = QtGui.QPalette()
    gradient = QtGui.QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.0, QtGui.QColor(240, 230, 200))
    gradient.setColorAt(1.0, QtGui.QColor(220, 170, 150))
    p.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
    instance.setPalette(p)


def get_path(path: str = None):
    if path:
        return os.path.abspath(path=path)
    return False


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)