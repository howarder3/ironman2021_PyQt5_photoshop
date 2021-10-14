from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap

from methods import opencv_engine # in methods __init__.py, we have class opencv_engine
import numpy as np
import logging

class method_steps_recoder(object):
    def __init__(self, text_recordsteps):
        self.method_steps = []
        self.text_recordsteps = text_recordsteps

    def add_each_method_step(self, each_method_step):
        self.method_steps.append(each_method_step)

    def update_recordsteps(self):
        msg = f"All saved steps: \n"
        for idx, ele in enumerate(self.method_steps):
            msg +=(f"{idx+1}: {ele}\n")
        self.text_recordsteps.setText(msg)


class label_mouse_controller(object):
    def __init__(self, image_center):
        self.image_center = image_center
        self.ui = self.image_center.ui # new pointer point to self.image_center.ui
        self.ui.label_img.mousePressEvent = self.mouse_press_event
        self.ui.label_img.mouseReleaseEvent = self.mouse_release_event
        self.ui.label_img.mouseMoveEvent = self.mouse_moving_event

    def mouse_press_event(self, event):
        msg = f"{event.x()=}, {event.y()=}, {event.button()=}"
        x = event.x()
        y = event.y()
        norm_x = x/self.image_center.qpixmap.width()
        norm_y = y/self.image_center.qpixmap.height()
        real_x = int(norm_x*self.image_center.origin_img_width)
        real_y = int(norm_y*self.image_center.origin_img_height)
        self.ui.label_click_pos.setText(f"Clicked postion = ({x}, {y})")
        self.ui.label_norm_pos.setText(f"Normalized postion = ({norm_x:.3f}, {norm_y:.3f})")
        self.ui.label_real_pos.setText(f"Real postion = ({real_x}, {real_y})")

    def mouse_release_event(self, event):
        msg = f"{event.x()=}, {event.y()=}, {event.button()=}"

    def mouse_moving_event(self, event):
        msg = f"{event.x()=}, {event.y()=}, {event.button()=}"


class image_center(object):
    def __init__(self, img_path, ui):
        self.img_path = img_path
        self.ui = ui
        self.label_mouse_controller = label_mouse_controller(self)
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
        self.method_steps_recoder = method_steps_recoder(self.ui.text_recordsteps) # record steps
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
        self.method_steps_recoder.update_recordsteps()
        bytesPerline = 3 * self.origin_img_width
        qimg = QImage(self.display_img, self.origin_img_width, self.origin_img_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)
        self.__update_img_zoom()
        self.ui.label_img.setPixmap(self.qpixmap)
        self.ui.label_img.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

