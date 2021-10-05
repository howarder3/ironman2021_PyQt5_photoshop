from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow, QColorDialog

from UI import Ui_MainWindow

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.label.setText("QColorDialog")
        self.ui.pushButton.clicked.connect(self.set_label_color)


    def set_label_color(self):
        color = QColorDialog.getColor() # OpenColorDialog
        if color.isValid():
            print(color.name()) #ff5b87
            print(color.red(), color.green(), color.blue()) # 255 91 135


        r, g, b = color.red(), color.green(), color.blue()        
        strRGB = ('{}, {}, {}'.format(r, g, b)) # ^ = middle
        print(f"{strRGB=}")

        self.ui.label.setStyleSheet('background-color:rgb({});'.format(strRGB))
