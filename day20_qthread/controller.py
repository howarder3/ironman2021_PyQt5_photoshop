from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal

import time

from UI import Ui_MainWindow

class ThreadTask(QThread):
    qthread_signal = pyqtSignal(int)

    def start_progress(self):
        max_value = 100      
        for i in range(max_value):
            time.sleep(0.1)            
            self.qthread_signal.emit(i+1)

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        self.ui.progressBar.setMaximum(100)
        self.ui.pushButton.clicked.connect(self.ButtonClick) 
        
    def ButtonClick(self):
        self.qthread = ThreadTask()
        self.qthread.qthread_signal.connect(self.progress_changed) 
        self.qthread.start_progress()

    def progress_changed(self, value):        
        self.ui.progressBar.setValue(value)