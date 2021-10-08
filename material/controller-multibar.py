from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal

import time

from UI import Ui_MainWindow

class External(QThread):
    qthread_signal = pyqtSignal(int)
    qthread_msg = pyqtSignal(str)

    def run(self):
        max_value = 100      
        for i in range(max_value):
            time.sleep(0.1)            
            self.qthread_signal.emit(i+1)
            self.qthread_msg.emit(f"{i+1}/{max_value}")

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        self.ui.progressBar.setMaximum(100)
        self.ui.pushButton.clicked.connect(self.ButtonClick) 
        self.ui.pushButton_2.clicked.connect(self.ButtonClick2) 
        self.ui.pushButton_3.clicked.connect(self.ButtonClick3) 
        
    def ButtonClick(self):
        self.ui.pushButton.setDown(True)
        self.ui.pushButton.setEnabled(False)
        self.qthread = External()
        self.qthread.qthread_signal.connect(self.progress_changed) 
        self.qthread.qthread_msg.connect(self.msg_changed) 
        self.qthread.start()

    def ButtonClick2(self):
        self.qthread = External()
        self.qthread.qthread_signal.connect(self.progress_changed2) 
        self.qthread.start()

    def ButtonClick3(self):
        self.qthread = External()
        self.qthread.qthread_signal.connect(self.progress_changed3) 
        self.qthread.start()


    def progress_changed(self, value):        
        self.ui.progressBar.setValue(value)

    def msg_changed(self, s):        
        self.ui.label.setText(s)

    def progress_changed2(self, value):        
        self.ui.progressBar_2.setValue(value)

    def progress_changed3(self, value):        
        self.ui.progressBar_3.setValue(value)