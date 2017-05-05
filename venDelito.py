import sys
import pypyodbc
from PyQt5.QtWidgets import *#QApplication, QMainWindow,QDialog,QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import time
from  tkinter import *

from PyQt5.QtCore import pyqtSlot


class Delito(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('Delitoform.ui',self)

