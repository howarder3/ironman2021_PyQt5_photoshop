import abc
 
class method_interface(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        return NotImplemented

    @abc.abstractmethod
    def update_img(self):
        return NotImplemented

    @abc.abstractmethod
    def append_each_method_step(self):
        return NotImplemented
 

class slider_method_interface(method_interface):
    def __init__(self, slider, label, image_center):
        self.label = label
        self.slider = slider
        self.image_center = image_center
        self.tmp_origin_img = self.image_center.display_img
        self.slider.setRange(-100, 100)
        self.slider.setProperty("value", 0)
        self.slider.valueChanged.connect(self.setsliderlabel)
        self.slider.sliderPressed.connect(self.slider_press_event)
        self.slider.sliderReleased.connect(self.slider_release_event)
        self.prefix = ""

    # get first picture snapshot, 
    def slider_press_event(self):
        self.tmp_origin_img = self.image_center.display_img

    # final update back to image center (not necessary, for double check)
    def slider_release_event(self):
        img = self.setimage(self.tmp_origin_img)
        self.append_each_method_step() # append all the methods include variables in to method_steps_recoder
        self.image_center.update_img(img)

    # image do the method
    def setimage(self, img):        
        return img

    @property
    def getslidervalue(self):
        return self.slider.value()

    # trigger function, get your signal from here
    def setsliderlabel(self):
        self.label.setText(f"{self.prefix}{self.slider.value():+}")
        # self.update_img()  # for the efficiency reason, we don't let the picture change with our slider
        
    def update_img(self):
        # self.append_each_method_step() # append all the methods include variables in to method_steps_recoder
        self.image_center.update_img(self.tmp_origin_img) # default = origin_image no change, like zoom in/out
        
    def append_each_method_step(self):
        self.image_center.method_steps_recoder.add_each_method_step(self) # append all the methods include variables in to method_steps_recoder
