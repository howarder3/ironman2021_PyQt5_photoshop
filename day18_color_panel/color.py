# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *


class colorSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Color Selector')
        self.setGeometry(600, 500, 400, 200)

        # OpenColorDialog
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())


if __name__ == '__main__':
    app = QApplication([])
    window = colorSelector()
    window.show()
    sys.exit(app.exec_())