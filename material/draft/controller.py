from PyQt5 import QtCore 
# from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
# from PyQt5.QtCore import QThread, pyqtSignal

import time
import os


from UI import Ui_MainWindow
# from img_controller import img_controller

# from method import method_interface, method_rotate  # method_rotate()
# import method # method.method_rotate()

from method import method_lightness, method_zoom



class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_control_setinput()
        self.ui_control_setoutput()
        # test_method = method.method_rotate()
        # img = "test"
        # img = test_method.set(img)

    def set_ui_control(self):
        self.method_zoom = method_zoom(self.ui.slider_zoom, self.ui.label_zoom)
        self.method_lightness = method_lightness(self.ui.slider_lightness, self.ui.label_lightness)
    
