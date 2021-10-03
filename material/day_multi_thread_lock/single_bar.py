from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import time

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        self.ui.pushButton.clicked.connect(self.start_progress) 
        
    def start_progress(self):
        max_value = 100
        self.ui.progressBar.setMaximum(max_value)

        for i in range(max_value):
            time.sleep(0.1)
            self.ui.progressBar.setValue(i+1)