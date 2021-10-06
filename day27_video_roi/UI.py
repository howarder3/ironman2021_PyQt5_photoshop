# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day27.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_videoframe = QtWidgets.QLabel(self.centralwidget)
        self.label_videoframe.setGeometry(QtCore.QRect(40, 50, 800, 450))
        self.label_videoframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_videoframe.setObjectName("label_videoframe")
        self.button_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.button_openfile.setGeometry(QtCore.QRect(20, 550, 113, 32))
        self.button_openfile.setObjectName("button_openfile")
        self.label_framecnt = QtWidgets.QLabel(self.centralwidget)
        self.label_framecnt.setGeometry(QtCore.QRect(700, 560, 171, 21))
        self.label_framecnt.setObjectName("label_framecnt")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(750, 600, 113, 32))
        self.button_play.setObjectName("button_play")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(490, 600, 113, 32))
        self.button_stop.setObjectName("button_stop")
        self.label_filepath = QtWidgets.QLabel(self.centralwidget)
        self.label_filepath.setGeometry(QtCore.QRect(40, 790, 841, 41))
        self.label_filepath.setObjectName("label_filepath")
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setGeometry(QtCore.QRect(620, 600, 113, 32))
        self.button_pause.setObjectName("button_pause")
        self.slider_videoframe = QtWidgets.QSlider(self.centralwidget)
        self.slider_videoframe.setGeometry(QtCore.QRect(150, 560, 531, 22))
        self.slider_videoframe.setOrientation(QtCore.Qt.Horizontal)
        self.slider_videoframe.setObjectName("slider_videoframe")
        self.text_save_points = QtWidgets.QTextEdit(self.centralwidget)
        self.text_save_points.setGeometry(QtCore.QRect(90, 660, 241, 101))
        self.text_save_points.setObjectName("text_save_points")
        self.text_output_rois = QtWidgets.QTextEdit(self.centralwidget)
        self.text_output_rois.setGeometry(QtCore.QRect(490, 660, 231, 101))
        self.text_output_rois.setObjectName("text_output_rois")
        self.button_clear_points = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_points.setGeometry(QtCore.QRect(350, 730, 113, 32))
        self.button_clear_points.setObjectName("button_clear_points")
        self.button_generate_rois = QtWidgets.QPushButton(self.centralwidget)
        self.button_generate_rois.setGeometry(QtCore.QRect(750, 730, 113, 32))
        self.button_generate_rois.setObjectName("button_generate_rois")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_videoframe.setText(_translate("MainWindow", "video_player"))
        self.button_openfile.setText(_translate("MainWindow", "Openfile"))
        self.label_framecnt.setText(_translate("MainWindow", "current_frame/total_frame"))
        self.button_play.setText(_translate("MainWindow", "Play"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.label_filepath.setText(_translate("MainWindow", "file path:"))
        self.button_pause.setText(_translate("MainWindow", "Pause"))
        self.button_clear_points.setText(_translate("MainWindow", "Clear Points"))
        self.button_generate_rois.setText(_translate("MainWindow", "Generate Rois"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
