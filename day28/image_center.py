from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap

# import utils # not defined
from utils import WongWongDebugger
from methods import opencv_engine # in methods __init__.py, we have class opencv_engine
import numpy as np
import logging
# import sys

from utils import WongWongLogger
logger = WongWongLogger()

# logger = logging.getLogger("root")

class image_center(object):
    _instance = None
    # Singleton mode: 單例模式 (only one instance), be sure all method change the only one "same instance"
    def __new__(cls, *args, **kwargs):
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, img_path, label_img):
        self.img_path = img_path
        self.label_img = label_img
        self.label_mouse_controller = label_mouse_controller(self.label_img)
        self.zoom_value = 1
        self.read_file_and_init()

    def read_file_and_init(self):
        try:
            self.origin_img = opencv_engine.read_image(self.img_path) # if cancel, no error !!!!
            self.origin_img_height, self.origin_img_width, self.origin_img_channel = self.origin_img.shape # need this to make error !!!
        except:
            self.origin_img = opencv_engine.read_image('./demo_materials/sad.png')
            self.origin_img_height, self.origin_img_width, self.origin_img_channel = self.origin_img.shape
        
        self.display_img = np.copy(self.origin_img) # make a clone
        self.__update_label_img()

    def update_img(self, img):
        self.display_img = img # default = not change, like zoom
        self.__update_label_img()

    def set_zoom_value(self, value):
        self.zoom_value = value

    def __update_img_zoom(self):        
        qpixmap_height = self.origin_img_height * self.zoom_value
        self.qpixmap = self.qpixmap.scaledToHeight(qpixmap_height)

    def __update_label_img(self):       
        bytesPerline = 3 * self.origin_img_width
        qimg = QImage(self.display_img, self.origin_img_width, self.origin_img_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)
        self.__update_img_zoom()
        self.label_img.setPixmap(self.qpixmap)
        self.label_img.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)




class label_mouse_controller(object):
    def __init__(self, label_img):
        self.label_img = label_img
        self.label_img.mousePressEvent = self.mouse_press_event
        self.label_img.mouseReleaseEvent = self.mouse_release_event
        self.label_img.mouseMoveEvent = self.mouse_moving_event
        # self.logger = WongWongLogger(level=logging.WARN)
    
    def mouse_press_event(self, event):
        msg = f"{event.x()=}, {event.y()=}, {event.button()=}"
        logger.info(msg)
        # print(msg)

    def mouse_release_event(self, event):
        msg = f"{event.x()=}, {event.y()=}, {event.button()=}"
        logger.info(msg)
        # print(msg)

    def mouse_moving_event(self, event):
        msg = f"{event.x()=}, {event.y()=}, {event.button()=}"
        logger.info(msg)
        # print(msg)

    def set_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.__update_text_clicked_position(x, y)
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        self.draw_point((norm_x, norm_y))
        self.__update_text_point_roi((norm_x, norm_y))

    # @property
    # def zoom_value(self):
    #     return self._zoom_value
        
    # @zoom_value.setter
    # def zoom_value(self, zoom_value):
    #     self._zoom_value = zoom_value
