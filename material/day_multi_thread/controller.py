from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal

import time

from UI import Ui_MainWindow

class External(QThread):
    res_signal = pyqtSignal(dict)

    def __init__(self, label, progress_bar):
        super().__init__()
        self.label = label
        self.progress_bar = progress_bar
        self.res_dict = {}

    def run(self):
        max_value = 100
        for i in range(max_value):
            time.sleep(0.1)
            self.res_dict['progress_bar'] = self.progress_bar
            self.res_dict['count'] = i+1
            self.res_dict['label'] = self.label
            self.res_dict['msg'] = f"{i+1}/{max_value}"
            self.res_signal.emit(self.res_dict)

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        self.ui.progressBar.setMaximum(100)
        self.ui.pushButton.clicked.connect(lambda: self.ButtonClick(self.ui.pushButton, self.ui.label, self.ui.progressBar))

        # self.ui.pushButton_2.clicked.connect(self.ButtonClick2)
        # self.ui.pushButton_3.clicked.connect(self.ButtonClick3)

    def ButtonClick(self, button, label, progress_bar):
        button.setDown(True)
        button.setEnabled(False)
        self.qthread = External(label, progress_bar)
        # self.qthread.res_signal.connect(self.progress_changed)
        self.qthread.res_signal.connect(lambda: self.progress_changed(self.qthread.res_dict, label, progress_bar))
        self.qthread.start()


    def progress_changed(self, res, label, progress_bar):
        label.setText(res['msg'])
        progress_bar.setValue(res['count'])

    def progress_changed2(self, value):        
        self.ui.progressBar_2.setValue(value)

    def progress_changed3(self, value):        
        self.ui.progressBar_3.setValue(value)