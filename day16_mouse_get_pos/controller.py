from PyQt5 import QtCore 
# from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
# from PyQt5.QtCore import QThread, pyqtSignal

import time
import os


from UI import Ui_MainWindow
from img_controller import img_controller

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
        self.file_path = ''
        self.img_controller = img_controller(img_path=self.file_path,
                                             label_img=self.ui.label_img,
                                             label_file_path=self.ui.label_file_name,
                                             label_ratio=self.ui.label_ratio,
                                             label_img_shape=self.ui.label_img_shape,
                                             label_click_pos=self.ui.label_click_pos,
                                             label_norm_pos=self.ui.label_norm_pos,
                                             label_real_pos=self.ui.label_real_pos)

        self.ui.btn_open_file.clicked.connect(self.open_file)         
        self.ui.btn_zoom_in.clicked.connect(self.img_controller.set_zoom_in)
        self.ui.btn_zoom_out.clicked.connect(self.img_controller.set_zoom_out)
        self.ui.slider_zoom.valueChanged.connect(self.getslidervalue)        

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file", "./") # start path        
        self.init_new_picture(filename)

    def init_new_picture(self, filename):
        self.ui.slider_zoom.setProperty("value", 50)
        self.img_controller.set_path(filename)        


    def getslidervalue(self):        
        self.img_controller.set_slider_value(self.ui.slider_zoom.value()+1)

    # def getPos(self , event):
    #     x = event.pos().x()
    #     y = event.pos().y() 
    #     print(f"(x, y) = ({x}, {y})")


