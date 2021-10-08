from PyQt5 import QtCore 
# from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer #QThread, pyqtSignal

import time
import os


from UI import Ui_MainWindow

# set: big change
# update: simple update for info, no calculation... (format: update_type_name)

# private function: We do NOT want user directly call this function 

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.timer=QTimer() # init QTimer
        self.timer.timeout.connect(self.run) # when timeout, do run one
        self.timer.start(1) # start Timer, here we set '1ms' while timeout one time
        self.time_counter =  # init time counter # for testing: 3599000

    def run(self):
        self.ui.label.setText(str(self.set_time_counter_format(self.time_counter))) # show time_counter (by format)
        self.time_counter += 1 # time_counter + 1


    def set_time_counter_format(self, time_counter):
        ms = time_counter % 1000
        total_sec = max(0, (time_counter - ms)//1000)
        hour = max(0, total_sec//3600)
        minute = max(0, total_sec//60 - hour * 60)
        sec = max(0, (total_sec - (hour * 3600) - (minute * 60)))
        return f"{hour}:{minute:0>2}:{sec:0>2}.{ms:0>3}"