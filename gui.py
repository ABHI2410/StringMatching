
import sys

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import *
from form import Ui_Form
from RabinKarp import RabinKarp

class MyHighlighter(QtGui.QSyntaxHighlighter):

    def highlightBlock(self,pattern,position):
        myClassFormat = QtGui.QTextCharFormat()
        myClassFormat.setBackground(QtGui.QColor('yellow'))
        length = len(pattern)
        self.setFormat(position, length, myClassFormat)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.openFileNamesDialog)
        self.ui.pushButton_4.clicked.connect(self.clear)
        self.ui.pushButton_5.clicked.connect(self.rabinkarp_search)
        self.stdout = ''
        self.style_for_success = "<span style=\" font-weight:bold; color:#4bb543;\" >"
        self.style_for_error = "<span style=\" font-weight:bold; color:#ff3333;\" >"
        self.style_for_highlighter = "<span style=\" font-weight:bold; background-color:ff3333;\" >"
        self.style_close = "</span>"
    
    def openFileNamesDialog(self):
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Text Files (*.txt)")
        if files:
            try:
                for file in files:
                    with open(file, 'r', encoding= 'UTF-8') as f:
                        doc = f.readlines()
                        text = "".join(doc)
                        self.ui.textEdit.append(text)
                self.stdout = f"All Files imported Successfully....{self.style_for_success}OK{self.style_close}"
                self.ui.textEdit_2.append(self.stdout)
            except Exception as e:
                print(e)
                self.stdout = f"Something went wrong when reading to the file {self.style_for_error}ERROR{self.style_close}"
                self.ui.textEdit_2.append(self.stdout)
                

    def clear(self):
        self.ui.textEdit.clear()
        self.ui.lineEdit.clear()
        self.ui.textEdit_2.clear()

    def rabinkarp_search(self):
        text = self.ui.textEdit.toPlainText()
        pattern = self.ui.lineEdit.text()
        if text != "" and pattern != "":
            SM = RabinKarp(text,pattern)
            out = SM.search()
            self.ui.textEdit_2.append(f"Pattern found {out[0]:,} times.")
            self.ui.textEdit_2.append(f"Total number of loop iterations: {out[1]:,}.")
            self.ui.textEdit_2.append(f"Expected Best or Average case time complexity: {out[2]:,}.")
            self.ui.textEdit_2.append(f"Expected Worst case time complexity: {out[3]:,}.")
            self.stdout = f"Successfull....{self.style_for_success}OK{self.style_close}"
            positions = out[4]
            highlight = MyHighlighter(self.ui.textEdit)
            for item in positions:
                highlight.highlightBlock(pattern, item)
                
                

        else:
            if text == "" and pattern == "":
                self.stdout = f"Empty Text and Pattern provided....{self.style_for_error}ERROR{self.style_close}"
            elif text == "":
                self.stdout = f"Empty Text....{self.style_for_error}ERROR{self.style_close}"
            elif pattern == "":
                self.stdout = f"Empty Pattern....{self.style_for_error}ERROR{self.style_close}"
            else:
                self.stdout =f"Something went wrong {self.style_for_error}ERROR{self.style_close}"
        self.ui.textEdit_2.append(self.stdout)             

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(app.exec())