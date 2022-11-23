
import sys

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import *
from form import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    