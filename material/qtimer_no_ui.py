# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from thread_test import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # QTimer
        self.timer = QTimer()

        # QPushButton
        self.ui.pushButton.clicked.connect(self.timeGo)
        self.ui.pushButton_2.clicked.connect(self.timeStop)

        # Other
        self.timer.timeout.connect(self.LCDEvent)
        self.s = 0

    def timeGo(self):
        self.timer.start(100)

    def timeStop(self):
        self.timer.stop()

    def LCDEvent(self):
        self.s += 1
        self.ui.lcdNumber.display(self.s)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())