#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://iter01.com/445923.html
Created on 2019年1月16日
@author: yiluo
@site: https://github.com/bingshilei
@email: 786129166@qq.com
@file: QThreadDemo2
@description: 使用多執行緒動態新增控制元件
"""
import time

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QWidget, QLineEdit, QListWidget, QPushButton,\
    QVBoxLayout, QLabel

'''
宣告執行緒類
'''

class addItemThread(QThread):
    add_item = pyqtSignal(str)
    show_time = pyqtSignal(str)

    '''
            新增控制元件
    '''
    def __init__(self,*args, **kwargs):
        super(addItemThread, self).__init__(*args, **kwargs)
        self.num = 0

    def run(self, *args, **kwargs):
        while True:
            file_str = 'File index{0}'.format(self.num,*args, **kwargs)
            self.num +=1

            #傳送新增訊號
            self.add_item.emit(file_str)

            date = QDateTime.currentDateTime()
            currtime = date.toString('yyyy-MM-dd hh:mm:ss')
            print(currtime)
            self.show_time.emit(str(currtime))

            time.sleep(1)

class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowTitle('多執行緒動態新增控制元件')
        # x,y,w,h
        self.setGeometry(800, 100, 500, 750)
        #建立QListWidget控制元件
        self.listWidget = QListWidget()
        #建立按鈕控制元件
        self.btn = QPushButton('開始',self)
        self.lb = QLabel('顯示時間',self)
        #建立佈局控制元件
        self.vlayout = QVBoxLayout()
        #將按鈕和列表控制元件新增到佈局
        self.vlayout.addWidget(self.btn)
        self.vlayout.addWidget(self.lb)
        self.vlayout.addWidget(self.listWidget)
        #設定窗體的佈局
        self.setLayout(self.vlayout)

        #繫結按鈕槽函式
        self.btn.clicked.connect(self.startThread)

        #宣告執行緒例項
        self.additemthread = addItemThread()

        #繫結增加控制元件函式
        self.additemthread.add_item.connect(self.addItem)

        #繫結顯示時間函式

        self.additemthread.show_time.connect(self.showTime)

    '''
    @description:按鈕開始，啟動執行緒
    '''
    def startThread(self):
        #按鈕不可用
        self.btn.setEnabled(False)
        #啟動執行緒
        self.additemthread.start()

    '''
    @description:為listwidget增加項
    @param:項的值 
    '''
    def addItem(self,file_str):
        self.listWidget.addItem(file_str)

    '''
    @description:顯示時間
    @param:項的值 
    '''
    def showTime(self,time):
        self.lb.setText(time)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())