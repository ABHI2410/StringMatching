
import sys

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import *
from form import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.openFileNameDialog)
        self.ui.pushButton_4.clicked.connect(self.openFileNamesDialog)
        self.ui.pushButton_9.clicked.connect(self.clear)
        self.stdout = ''
        self.style_for_success = "<span style=\" font-weight:bold; color:#4bb543;\" >"
        self.style_for_error = "<span style=\" font-weight:bold; color:#ff3333;\" >"
        self.style_for_highlighter = "<span style=\" font-weight:bold; background-color:ff3333;\" >"
        self.style_close = "</span>"

    
    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)")
        if fileName:
            try:
                file = open(fileName, encoding='UTF-8')
                doc = file.readlines()
                text = "".join(doc)
                self.ui.textEdit.append(text)
                self.stdout = f"File imported Successfully....{self.style_for_success}OK{self.style_close}"
                self.ui.textEdit_2.append(self.stdout)
            except:
                self.stdout = f"Something went wrong when writing to the file{self.style_for_error}ERROR{self.style_close}"
                self.ui.textEdit_2.append(self.stdout)
    
    def openFileNamesDialog(self):
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Text Files (*.txt)")
        print(type(files))
        if files:
            print(files)

    def clear(self):
        self.ui.textEdit.clear()
        self.ui.lineEdit.clear()
        self.ui.textEdit_2.clear()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(app.exec())