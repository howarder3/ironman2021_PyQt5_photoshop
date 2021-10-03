# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_Dialog
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.ui.label.setFont(QtGui.QFont('Arial', 10))
        self.ui.label.setText('Nothing')
        
        self.ui.lineEdit.setText('Welcome!')

        self.ui.pushButton.setText('Display')
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        text = self.ui.lineEdit.text()
        self.ui.label.setText(text)
        self.ui.lineEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())