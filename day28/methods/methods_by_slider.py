from .methods_interface import slider_method_interface

# from method.opencv_engine import opencv_engine # from file import class


# in methods __init__.py, we have class opencv_engine, but here opencv_engine is in same level
from .opencv_engine import opencv_engine # from file import class

from utils import WongWongLogger
logger = WongWongLogger()

# @WongWongTimer
# print(f"{dir(self)}")

# print(dir(opencv_engine))

class method_lightness(slider_method_interface):
    def __init__(self, slider, label, image_center):
        super().__init__(slider, label, image_center)
        self.prefix = "Lightness: "
        self.update_img()

    def setimage(self, img):        
        return opencv_engine.modify_lightness_saturation(img, lightness=self.slider.value())

    def update_img(self):
        logger.info(f"get lightness slider value = {self.slider.value()}")
        img = self.setimage(self.origin_img)
        self.image_center.update_img(img)

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.get_origin_image() # change from origin
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        self.update_img()  
        # return NotImplemented


class method_zoom(slider_method_interface):    
    def __init__(self, slider, label, image_center):
        super().__init__(slider, label, image_center)
        self.prefix = "Zoom: "
        self.ratio_rate = pow(10, (self.slider.value() - 100)/100) # 0.01 ~ 10
        self.image_center.set_zoom_value(self.get_zoom_value())
        self.update_img()

    def setsliderlabel(self):
        logger.info(f"get zoom slider value = {self.slider.value()}")
        self.get_current_image()
        self.ratio_rate = pow(10, (self.slider.value() - 100)/100) # 0.01 ~ 10
        # print(self.ratio_rate) # 0.1 ~ 1.0
        self.label.setText(f"{self.prefix}{self.ratio_rate*1000:.0f} %")
        self.image_center.set_zoom_value(self.get_zoom_value())
        self.update_img()

    def get_zoom_value(self):
        return self.ratio_rate*10 # 0.01 ~ 1.0 ->　0.1 ~ 10.0

