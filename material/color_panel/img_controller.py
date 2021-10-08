from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap

from opencv_engine import opencv_engine



class img_controller(object):
    def __init__(self, img_path, ui):
        self.img_path = img_path
        self.ui = ui
        self.ratio_value = 50
        self.read_file_and_init()

    def read_file_and_init(self):
        try:
            self.origin_img = opencv_engine.read_image(self.img_path)
            self.origin_height, self.origin_width, self.origin_channel = self.origin_img.shape
        except:
            self.origin_img = opencv_engine.read_image('sad.png')
            self.origin_height, self.origin_width, self.origin_channel = self.origin_img.shape

        self.display_img = self.origin_img
        self.__update_text_file_path()
        self.ratio_value = 50 # re-init
        self.__update_img()

    def set_path(self, img_path):
        self.img_path = img_path
        self.read_file_and_init()


    def __update_img_ratio(self):
        self.ratio_rate = pow(10, (self.ratio_value - 50)/50)
        qpixmap_height = self.origin_height * self.ratio_rate
        self.qpixmap = self.qpixmap.scaledToHeight(qpixmap_height)
        self.__update_text_ratio()
        self.__update_text_img_shape()

    def __update_img(self):       
        bytesPerline = 3 * self.origin_width
        qimg = QImage(self.display_img, self.origin_width, self.origin_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)
        self.__update_img_ratio()
        self.ui.label_img.setPixmap(self.qpixmap)
        self.ui.label_img.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.ui.label_img.mousePressEvent = self.set_clicked_position

    def __update_text_file_path(self):
        self.ui.label_file_name.setText(f"File path = {self.img_path}")

    def __update_text_ratio(self):
        self.ui.label_ratio.setText(f"{int(100*self.ratio_rate)} %")

    def __update_text_img_shape(self):
        current_text = f"Current img shape = ({self.qpixmap.width()}, {self.qpixmap.height()})"
        origin_text = f"Origin img shape = ({self.origin_width}, {self.origin_height})"
        self.ui.label_img_shape.setText(current_text+"\t"+origin_text)

    def __update_text_clicked_position(self, x, y):
        # give me qpixmap point
        self.ui.label_click_pos.setText(f"Clicked postion = ({x}, {y})")
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({norm_x}, {norm_y})")
        self.ui.label_norm_pos.setText(f"Normalized postion = ({norm_x:.3f}, {norm_y:.3f})")
        self.ui.label_real_pos.setText(f"Real postion = ({int(norm_x*self.origin_width)}, {int(norm_y*self.origin_height)})")


    def set_zoom_in(self):
        self.ratio_value = max(0, self.ratio_value - 1)
        self.__update_img()

    def set_zoom_out(self):
        self.ratio_value = min(100, self.ratio_value + 1)
        self.__update_img()

    def set_slider_value(self, value):
        self.ratio_value = value
        self.__update_img()

    def set_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.__update_text_clicked_position(x, y)
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        self.draw_point((norm_x, norm_y))
        self.__update_text_point_roi((norm_x, norm_y))

    def draw_point(self, point):
        # give me normalized point, i will help you to transform to origin cv image position
        cv_image_x = point[0]*self.origin_width
        cv_image_y = point[1]*self.origin_height
        self.display_img = opencv_engine.draw_point(self.display_img, (cv_image_x, cv_image_y))
        self.__update_img()

    def __update_text_point_roi(self, point):
        # give me normalized point, i will help you to transform to origin cv image position
        cv_image_x = point[0]*self.origin_width
        cv_image_y = point[1]*self.origin_height
        self.ui.text_ratio_roi.append(f"[{point[0]:.6f}, {point[1]:.6f}]")
        self.ui.text_real_roi.append(f"[{int(cv_image_x)}, {int(cv_image_y)}]")




