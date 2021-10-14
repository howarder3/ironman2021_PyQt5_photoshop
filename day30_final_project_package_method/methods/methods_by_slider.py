from .methods_interface import slider_method_interface
from .opencv_engine import opencv_engine 

class method_lightness(slider_method_interface):
    def __init__(self, slider, label, image_center):
        super().__init__(slider, label, image_center)
        self.prefix = "lightness: "
        self.update_img()

    def setimage(self, img):        
        return opencv_engine.modify_lightness(img, lightness=self.slider.value())

    # def update_img(self):
    #     img = self.setimage(self.tmp_origin_img)
    #     self.image_center.update_img(img)

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        # self.update_img() # for the efficiency reason, we don't let the picture change with our slider

class method_saturation(slider_method_interface):
    def __init__(self, slider, label, image_center):
        super().__init__(slider, label, image_center)
        self.prefix = "saturation: "
        self.update_img()

    def setimage(self, img):        
        return opencv_engine.modify_saturation(img, saturation=self.slider.value())

    # def update_img(self):
    #     img = self.setimage(self.tmp_origin_img)
    #     self.image_center.update_img(img)

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        # self.update_img() # for the efficiency reason, we don't let the picture change with our slider


class method_contrast(slider_method_interface):
    def __init__(self, slider, label, image_center):
        super().__init__(slider, label, image_center)
        self.prefix = "contrast: "
        self.update_img()

    def setimage(self, img):        
        return opencv_engine.modify_contrast_brightness(img, contrast=self.slider.value())

    # def update_img(self):
    #     img = self.setimage(self.tmp_origin_img)
    #     self.image_center.update_img(img)

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        # self.update_img()  # for the efficiency reason, we don't let the picture change with our slider



class method_brightness(slider_method_interface):
    def __init__(self, slider, label, image_center):
        super().__init__(slider, label, image_center)
        self.prefix = "brightness: "
        self.update_img()

    def setimage(self, img):        
        return opencv_engine.modify_contrast_brightness(img, brightness=self.slider.value())

    # def update_img(self):
    #     img = self.setimage(self.tmp_origin_img)
    #     self.image_center.update_img(img)

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        # self.update_img()  # for the efficiency reason, we don't let the picture change with our slider



class method_zoom(slider_method_interface):    
    def __init__(self, slider, label, image_center, label_img_shape):
        super().__init__(slider, label, image_center)
        self.prefix = "Zoom: "
        self.label_img_shape = label_img_shape
        self.ratio_rate = pow(10, (self.slider.value() - 100)/100) # 0.01 ~ 10
        self.image_center.set_zoom_value(self.get_zoom_value())
        self.set_label_img_shape()
        # self.update_img()

    def set_label_img_shape(self):
        current_image_shape = (self.image_center.qpixmap.width(), self.image_center.qpixmap.height())
        origin_image_shape = (self.image_center.origin_img_width, self.image_center.origin_img_height)
        self.label_img_shape.setText(f"Current image shape: {current_image_shape}, Origin image shape: {origin_image_shape}")

    def setsliderlabel(self):
        self.ratio_rate = pow(10, (self.slider.value() - 100)/100) # 0.01 ~ 10
        # print(self.ratio_rate) # 0.1 ~ 1.0
        self.label.setText(f"{self.prefix}{self.ratio_rate*1000:.0f} %")
        self.image_center.set_zoom_value(self.get_zoom_value())
        self.set_label_img_shape()
        self.update_img()  # for the efficiency reason, we don't let the picture change with our slider

    def get_zoom_value(self):
        return self.ratio_rate*10 # 0.01 ~ 1.0 ->　0.1 ~ 10.0

    

