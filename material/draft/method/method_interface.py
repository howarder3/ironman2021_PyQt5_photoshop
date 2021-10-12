import abc
from utils import WongWongTimer, WongWongDebugger

# @WongWongTimer
# print(f"{dir(self)}")

class method_interface(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        return NotImplemented

    @abc.abstractmethod
    def setimage(self, img):
        return NotImplemented
 

class slider_method_interface(method_interface):
    def __init__(self, slider, label):
        self.label = label
        self.slider = slider
        self.slider.setRange(-100, 100)
        self.slider.setProperty("value", 0)
        self.slider.valueChanged.connect(self.setsliderlabel)
        self.prefix = ""

    def getslidervalue(self):
        return self.slider.value()

    def setsliderlabel(self):
        self.label.setText(f"{self.prefix}{self.slider.value()}")
    
    def setimage(self, img):
        return NotImplemented



class method_lightness(slider_method_interface):
    
    # @WongWongTimer
    @WongWongDebugger
    def __init__(self, slider, label):
        super().__init__(slider, label)
        self.prefix = "Lightness: "

    def setimage(self, img):
        return img


class method_zoom(slider_method_interface):
    
    @WongWongDebugger
    def __init__(self, slider, label):
        super().__init__(slider, label)
        self.prefix = "Zoom: "

    def setsliderlabel(self):
        self.ratio_rate = pow(10, (self.slider.value() - 100)/100) # 0.01 ~ 10
        # print(self.ratio_rate) # 0.1 ~ 1.0
        self.label.setText(f"{self.prefix}{self.ratio_rate*1000:.0f} %")

    def get_zoom_value(self):
        return self.ratio_rate*10 # 0.01 ~ 1.0 ->　0.1 ~ 10.0

    def setimage(self, img):
        return img



