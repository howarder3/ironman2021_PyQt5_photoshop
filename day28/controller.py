from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow, QFileDialog

import time
import os

from UI import Ui_MainWindow
from image_center import image_center
from methods import method_lightness, method_zoom

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_init_ui()
        
    def set_init_ui(self):
        self.ui.btn_open_file.clicked.connect(self.open_file)     

    def image_wait_for_trigger(self):
        self.methods_library = methods_library(self.ui, self.image_center)      
    
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file Window", "./") # start path       
        # filename, filetype = QFileDialog.getOpenFileName(self, "Open file Window", "./", "Video Files(*.mp4 *.avi)") # start path   
        self.ui.label_filepath.setText(f"File path = {filename}")      
        self.image_center = image_center(filename, self.ui.label_image)        
        self.image_wait_for_trigger()
         
class methods_library(object):
    def __init__(self, ui, image_center):
        self.ui = ui
        self.image_center = image_center
        self.method_zoom = method_zoom(self.ui.slider_zoom, self.ui.label_zoom, self.image_center)
        self.method_lightness = method_lightness(self.ui.slider_lightness, self.ui.label_lightness, self.image_center)

