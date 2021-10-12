import abc
from utils import WongWongTimer, WongWongDebugger

class method_interface(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        return NotImplemented

    @abc.abstractmethod
    def update_img(self):
        return NotImplemented
 

class slider_method_interface(method_interface):
    def __init__(self, slider, label, image_center):
        self.label = label
        self.slider = slider
        self.image_center = image_center
        self.origin_img = self.image_center.display_img
        self.slider.setRange(-100, 100)
        self.slider.setProperty("value", 0)
        self.slider.valueChanged.connect(self.setsliderlabel)
        self.prefix = ""

    @property
    def getslidervalue(self):
        return self.slider.value()

    def get_current_image(self):
        self.origin_img = self.image_center.display_img

    def get_origin_image(self):
        self.origin_img = self.image_center.origin_img

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.get_current_image()
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        self.update_img()  
        # return NotImplemented
        
    def update_img(self):
        self.image_center.update_img(self.origin_img) # default = origin_image no change, like zoom in/out

