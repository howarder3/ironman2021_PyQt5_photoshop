# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ps.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1282, 871)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material/wongwong.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img_shape = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape.setGeometry(QtCore.QRect(880, 780, 641, 21))
        self.label_img_shape.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_img_shape.setObjectName("label_img_shape")
        self.btn_open_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_file.setGeometry(QtCore.QRect(50, 670, 89, 25))
        self.btn_open_file.setObjectName("btn_open_file")
        self.label_click_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_click_pos.setGeometry(QtCore.QRect(940, 710, 191, 20))
        self.label_click_pos.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_click_pos.setObjectName("label_click_pos")
        self.label_real_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_real_pos.setGeometry(QtCore.QRect(940, 750, 191, 20))
        self.label_real_pos.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_real_pos.setObjectName("label_real_pos")
        self.label_norm_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_norm_pos.setGeometry(QtCore.QRect(940, 730, 191, 20))
        self.label_norm_pos.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_norm_pos.setObjectName("label_norm_pos")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 801, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 797, 597))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_image = QtWidgets.QLabel()
        self.label_image.setGeometry(QtCore.QRect(0, 0, 851, 661))
        self.label_image.setObjectName("label_image")
        self.scrollArea.setWidget(self.label_image)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(1120, 660, 150, 150))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("day26_video_player_add_slider_project/wongwong.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.label_filepath = QtWidgets.QLabel(self.centralwidget)
        self.label_filepath.setGeometry(QtCore.QRect(70, 760, 841, 71))
        self.label_filepath.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_filepath.setObjectName("label_filepath")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(910, 60, 341, 174))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Adjustments = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.Adjustments.setFont(font)
        self.Adjustments.setStyleSheet("color:rgb(255, 170, 0);")
        self.Adjustments.setObjectName("Adjustments")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Adjustments)
        self.label_lightness = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_lightness.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_lightness.setObjectName("label_lightness")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_lightness)
        self.slider_lightness = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.slider_lightness.setProperty("value", 50)
        self.slider_lightness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lightness.setObjectName("slider_lightness")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.slider_lightness)
        self.label_brightness = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_brightness.setAutoFillBackground(False)
        self.label_brightness.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_brightness.setObjectName("label_brightness")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_brightness)
        self.slider_brightness = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.slider_brightness.setProperty("value", 50)
        self.slider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brightness.setObjectName("slider_brightness")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.slider_brightness)
        self.label_contrast = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_contrast.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_contrast.setObjectName("label_contrast")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_contrast)
        self.slider_contrast = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.slider_contrast.setProperty("value", 50)
        self.slider_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.slider_contrast.setObjectName("slider_contrast")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.slider_contrast)
        self.label_saturation = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_saturation.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_saturation.setObjectName("label_saturation")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_saturation)
        self.slider_saturation = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.slider_saturation.setProperty("value", 50)
        self.slider_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturation.setObjectName("slider_saturation")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.slider_saturation)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(910, 267, 341, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.slider_Rvalue = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider_Rvalue.setProperty("value", 50)
        self.slider_Rvalue.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Rvalue.setObjectName("slider_Rvalue")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.slider_Rvalue)
        self.label_Gvalue = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_Gvalue.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_Gvalue.setObjectName("label_Gvalue")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Gvalue)
        self.slider_Gvalue = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider_Gvalue.setProperty("value", 50)
        self.slider_Gvalue.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Gvalue.setObjectName("slider_Gvalue")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.slider_Gvalue)
        self.label_Bvalue = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_Bvalue.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_Bvalue.setObjectName("label_Bvalue")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_Bvalue)
        self.slider_Bvalue = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider_Bvalue.setProperty("value", 50)
        self.slider_Bvalue.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Bvalue.setObjectName("slider_Bvalue")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.slider_Bvalue)
        self.label_warm = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_warm.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_warm.setObjectName("label_warm")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_warm)
        self.slider_warm = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider_warm.setProperty("value", 50)
        self.slider_warm.setOrientation(QtCore.Qt.Horizontal)
        self.slider_warm.setObjectName("slider_warm")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.slider_warm)
        self.label_cold = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_cold.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_cold.setObjectName("label_cold")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_cold)
        self.slider_cold = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider_cold.setProperty("value", 50)
        self.slider_cold.setOrientation(QtCore.Qt.Horizontal)
        self.slider_cold.setObjectName("slider_cold")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.slider_cold)
        self.label_Rvalue = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_Rvalue.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_Rvalue.setObjectName("label_Rvalue")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Rvalue)
        self.ColorBalance = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.ColorBalance.setFont(font)
        self.ColorBalance.setAutoFillBackground(False)
        self.ColorBalance.setStyleSheet("color:rgb(255, 170, 0);")
        self.ColorBalance.setObjectName("ColorBalance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ColorBalance)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1541, 951))
        self.Background.setMaximumSize(QtCore.QSize(1541, 951))
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("background-color:rgb(50, 50,50); color:rgb(255, 170, 0);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(910, 570, 341, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.Zoom = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.Zoom.setFont(font)
        self.Zoom.setAutoFillBackground(False)
        self.Zoom.setStyleSheet("color:rgb(255, 170, 0);")
        self.Zoom.setObjectName("Zoom")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Zoom)
        self.label_zoom = QtWidgets.QLabel(self.layoutWidget)
        self.label_zoom.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_zoom.setObjectName("label_zoom")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_zoom)
        self.slider_zoom = QtWidgets.QSlider(self.layoutWidget)
        self.slider_zoom.setProperty("value", 50)
        self.slider_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.slider_zoom.setObjectName("slider_zoom")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.slider_zoom)
        self.Background.raise_()
        self.label_img_shape.raise_()
        self.btn_open_file.raise_()
        self.label_click_pos.raise_()
        self.label_real_pos.raise_()
        self.label_norm_pos.raise_()
        self.verticalLayoutWidget.raise_()
        self.Logo.raise_()
        self.label_filepath.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.layoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1282, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenfile = QtWidgets.QAction(MainWindow)
        self.actionOpenfile.setObjectName("actionOpenfile")
        self.menuMenu.addAction(self.actionOpenfile)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Photoshop by WongWong"))
        self.label_img_shape.setText(_translate("MainWindow", "Current image shape: (0,0), Origin image shape: (0,0)"))
        self.btn_open_file.setText(_translate("MainWindow", "Open file"))
        self.label_click_pos.setText(_translate("MainWindow", "clicked position = (x, y)"))
        self.label_real_pos.setText(_translate("MainWindow", "real position = (x, y)"))
        self.label_norm_pos.setText(_translate("MainWindow", "normalized position = (x, y)"))
        self.label_image.setText(_translate("MainWindow", "image"))
        self.label_filepath.setText(_translate("MainWindow", "file path:"))
        self.Adjustments.setText(_translate("MainWindow", "Adjustments"))
        self.label_lightness.setText(_translate("MainWindow", "Lightness: +0"))
        self.label_brightness.setText(_translate("MainWindow", "Brightness: +0"))
        self.label_contrast.setText(_translate("MainWindow", "Contrast: +0"))
        self.label_saturation.setText(_translate("MainWindow", "Saturation: +0"))
        self.label_Gvalue.setText(_translate("MainWindow", "G value: +0"))
        self.label_Bvalue.setText(_translate("MainWindow", "B value: +0"))
        self.label_warm.setText(_translate("MainWindow", "Warm : +0"))
        self.label_cold.setText(_translate("MainWindow", "Cold: +0"))
        self.label_Rvalue.setText(_translate("MainWindow", "R value: +0"))
        self.ColorBalance.setText(_translate("MainWindow", "Color Balance"))
        self.Zoom.setText(_translate("MainWindow", "Zoom"))
        self.label_zoom.setText(_translate("MainWindow", "zoom: 100%"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpenfile.setText(_translate("MainWindow", "Openfile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
