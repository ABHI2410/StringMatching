import sys
import os
try:
    from PyQt6.QtWidgets import *
except ModuleNotFoundError:
    os.system("python3 -m pip install PyQt6")
else:
    os.system("python -m pip install PyQt6")


from .UI.gui import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(app.exec())