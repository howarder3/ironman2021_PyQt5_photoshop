import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWnd(QWidget):
    def __init__(self, parent=None):
        super (MainWnd, self).__init__(parent)
        self.initUI()
        timer = QTimer(self)
        timer.timeout.connect(self.slotPickColor)
        timer.start(20)

    def initUI(self):
        mainLayout = QGridLayout(self)
        self.labColor = QLabel()
        self.labColor.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.labColor.setMinimumSize(80, 80)
        mainLayout.addWidget(self.labColor, 0, 0, 3, 1)

        labs = list(map(lambda text: QLabel(text), ['RGB: ', 'CSS: ', 'position: ']))
        list(map(lambda lab: lab.setAlignment(Qt.AlignRight | Qt.AlignVCenter), labs))
        list(map(lambda lab, row: mainLayout.addWidget(lab, row, 1, 1, 1), labs, range(3)))

        self.txtRGB, self.txtCSS, self.txtXY = txts = list(map(lambda i: QLineEdit(), range(3)))
        list(map(lambda txt: txt.setStyleSheet(
            'background-color:rgb(0, 0, 0); color:rgb(255, 170, 0);'), txts))
        list(map(lambda txt, row: mainLayout.addWidget(txt, row, 2, 1, 1), txts, range(3)))

        self.resize(285, 120)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)

        self.setWindowTitle('Color Picker v1.0')
        # self.setWindowIcon(QIcon)


    def slotPickColor(self):
        x = QCursor.pos().x()
        y = QCursor.pos().y()
        self.txtXY.setText(('X:{:^4d} Y:{:^4d}').format(x, y))

        pixmap = QApplication.primaryScreen().grabWindow(
            QApplication.desktop().winId(), x, y, 1, 1)
        image = pixmap.toImage()
        color = QColor(image.pixel(0, 0))
        r, g, b = color.red(), color.green(), color.blue()

        strRGB = ('{:^3d}, {:^3d}, {:^3d}'.format(r, g, b))
        self.txtRGB.setText(strRGB)
        self.labColor.setStyleSheet('background-color:rgb({});'.format(strRGB))

        hexs = list(map(lambda x: str(hex(x)).replace('0x', '').upper(), [r ,g, b]))
        print(hexs)
        strCSS = '#{:0>2s}{:0>2s}{:0>2s}'.format(*hexs)
        self.txtCSS.setText(strCSS)


def main():
    app = QApplication(sys.argv)
    w = MainWnd()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()









