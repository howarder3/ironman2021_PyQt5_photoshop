# http://sammypython.blogspot.com/2019/01/pyqt5-qtimer.htm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage,QFont
from PyQt5.QtCore import QTimer

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setGeometry(200,100,200,200)
        self.label.setFont(QFont("Roman times",100,QFont.Bold)) #設訂字體
        self.setGeometry(500,300,700,500)
        self.setWindowTitle("PyQT Timer Demo")

        self.timer=QTimer() # 呼叫 QTimer
        self.timer.timeout.connect(self.run) #當時間到時會執行 run
        # self.timer.start(1000) #啟動 Timer .. 每隔1000ms 會觸發 run
        self.timer.start(10) #啟動 Timer .. 每隔1000ms 會觸發 run
        self.total = 0 #初始 total


    def run(self):

        self.label.setText(str(self.total)) # 顯示 total
        self.total+=1 #Total 加 1 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_()) 