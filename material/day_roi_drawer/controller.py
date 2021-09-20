from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal

import time
import cv2


from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btn_open_file.clicked.connect(self.open_file)         
        self.ui.btn_zoom_in.clicked.connect(self.func_zoom_in) 
        self.ui.btn_zoom_out.clicked.connect(self.func_zoom_out)
        self.file_path = 'cat.jpg'
        self.display_img()

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                  "Open file",
                  "./")                 # start path
        print(filename)
        self.file_path = filename
        self.display_img()

    def display_img(self):
        self.img = cv2.imread(self.file_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.label_img.setPixmap(QPixmap.fromImage(self.qimg))
        self.ui.label_file_path.setText(f"File path = {self.file_path}")
        self.ui.label_img.mousePressEvent = self.getPos
        

    def func_zoom_in(self):
        self.qpixmap_height -= 100
        self.resize_image()

    def func_zoom_out(self):
        self.qpixmap_height += 100
        self.resize_image()

    def resize_image(self):
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        # print(f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.label_img_shape.setText(f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.label_img.setPixmap(scaled_pixmap)

    def getPos(self , event):
        x = event.pos().x()
        y = event.pos().y() 
        print(f"(x, y) = ({x}, {y})")