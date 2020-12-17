import os
import sys
from serial_panel import Ui_MainWindow
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtWidgets,QtCore
from pyqt_led.pyqt_led import Led # From https://github.com/Neur1n/pyqt_led

from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtCore import QThread, pyqtSignal

import serial
# import serial.tools.list_ports
import time

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__() # 菱形继承
        self.setupUi(self)
    def serial_connect(self): # button
        pass

    def serial_disconnect(self):
        pass
    
    def send_test(self):
        pass

    def test_click(self):
        pass

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)            #pyqt窗口必须在QApplication方法中使用
    myshow=MyWindow()                               #生成mywindow类的实例 myshow
    myshow.show()                                   #myshow调用show方法
    sys.exit(app.exec())                            #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序