# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day18.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_in.setGeometry(QtCore.QRect(190, 840, 101, 31))
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.btn_zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out.setGeometry(QtCore.QRect(330, 840, 91, 31))
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(60, 40, 1121, 771))
        self.label_img.setObjectName("label_img")
        self.btn_open_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_file.setGeometry(QtCore.QRect(60, 840, 101, 31))
        self.btn_open_file.setObjectName("btn_open_file")
        self.label_img_shape = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape.setGeometry(QtCore.QRect(490, 850, 361, 21))
        self.label_img_shape.setObjectName("label_img_shape")
        self.label_file_path = QtWidgets.QLabel(self.centralwidget)
        self.label_file_path.setGeometry(QtCore.QRect(60, 890, 1131, 31))
        self.label_file_path.setObjectName("label_file_path")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_zoom_in.setText(_translate("MainWindow", "zoom in"))
        self.btn_zoom_out.setText(_translate("MainWindow", "zoom out"))
        self.label_img.setText(_translate("MainWindow", "img"))
        self.btn_open_file.setText(_translate("MainWindow", "Open file"))
        self.label_img_shape.setText(_translate("MainWindow", "current img shape ="))
        self.label_file_path.setText(_translate("MainWindow", "file path: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

