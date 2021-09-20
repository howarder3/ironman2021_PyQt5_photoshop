from PyQt5 import QtWidgets, QtGui, QtCore

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.button_line.clicked.connect(self.buttonClicked_line)
        self.ui.button_text.clicked.connect(self.buttonClicked_text)
        self.ui.button_plain.clicked.connect(self.buttonClicked_plain)

    def buttonClicked_line(self):
        msg = self.ui.box_line.text()
        self.ui.label_line.setText(msg)

    def buttonClicked_text(self):
        msg = self.ui.box_text.toPlainText()
        self.ui.label_text.setText(msg)

    def buttonClicked_plain(self):
        msg = self.ui.box_plain.toPlainText()
        self.ui.label_plain.setText(msg)

