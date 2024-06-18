#!/home/bendix/Documents/programming/python/numi-application/venv/bin/python

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys
from subprocess import check_output


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("/home/bendix/Documents/programming/python/numi-application/icon.png"))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet("border-radius: 50px")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        screen = app.primaryScreen()
        self.size = (screen.size().width(), screen.size().height())

        self.setGeometry(int(self.size[0]/2-200), int(self.size[1]/2-50), 400, 100)

        # Def Widgets
        self.label1_data = ""

        # Widgets
        self.label1 = QtWidgets.QLabel(self.label1_data, self)
        self.label1.move(0, 50)
        self.label1.resize(400, 50)
        self.label1.setStyleSheet("font-size: 35px; background-color: #2A2E32; border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; font-weight: bold;")
        self.label1.setAlignment(QtCore.Qt.AlignHCenter)

        self.input1 = QtWidgets.QLineEdit(self)
        self.input1.textChanged.connect(self.numi_func)
        self.input1.returnPressed.connect(self.enter_func)
        self.input1.resize(400, 50)
        self.input1.setStyleSheet("font-size: 25px; background-color: #23262a; border-top-left-radius: 10px; border-top-right-radius: 10px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; ")
        self.input1.setAlignment(QtCore.Qt.AlignHCenter)

        self.show()
        sys.exit(app.exec())

    def keyPressEvent(self, key):
        if key.key() == QtCore.Qt.Key_Escape:
            self.close()

    def numi_func(self):
        input = f"{self.input1.text()}"
        output = check_output(["numi-cli", str(input)])
        self.label1.setText(output.decode("utf-8"))

    def enter_func(self):
        input = f"{self.input1.text()}"
        if input=="exit" or input=="Exit" or input=="EXIT":
            self.close()
        if input=="help":
            # TODO HELP
            pass
        output = check_output(["numi-cli", str(input)])
        output = output.decode("utf-8")

        self.input1.setText(output)


app = QApplication(sys.argv)
window = Window()
