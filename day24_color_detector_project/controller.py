from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QApplication
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtCore import QTimer

from UI import Ui_MainWindow

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.label.setText("")
        timer = QTimer(self)
        timer.timeout.connect(self.get_current_cursor_color)
        timer.start(20)


    def get_current_cursor_color(self):
        x = QCursor.pos().x()
        y = QCursor.pos().y()
        self.ui.text_pos.setText(f"X:{x:^4d} Y:{y:^4d}")
        pixmap = QApplication.primaryScreen().grabWindow(
            QApplication.desktop().winId(), x, y, 1, 1)
        image = pixmap.toImage()
        color = QColor(image.pixel(0, 0))
        self.set_label_color(color)


    def set_label_color(self, color):
        # color = QColorDialog.getColor() # OpenColorDialog
        # if color.isValid():
        #     print(color.name()) #ff5b87
        #     print(color.red(), color.green(), color.blue()) # 255 91 135

        r, g, b = color.red(), color.green(), color.blue()        
        strRGB = (f"{r:^3d}, {g:^3d}, {b:^3d}")
        # print(f"{strRGB=}")

        self.ui.label.setStyleSheet('background-color:rgb({});'.format(strRGB))
        self.ui.text_rgb.setText(f"({strRGB})")
        self.ui.text_hex.setText(color.name().upper())
