# import sys
# sys.path.append('./method/') 

# from method_interface import method_interface, method_rotate
# from opencv_engine import opencv_engine

# from .methods_interface import *
from .methods_by_slider import *
from .opencv_engine import * # from file import class

__all__ = ['methods_interface', 'method_rotate', 'method_zoom', 'opencv_engine'] # in methods __init__.py, we have class opencv_engine



