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
# 中文乱码问题
class readThread(QThread):
    updated = pyqtSignal(str)
    def __init__(self):
        super(readThread, self).__init__()
        self.ser = None
        self.serial_message = None
        self.run_flag = True
    def setser(self, ser, serial_message):
        self.ser = ser
        self.serial_message = serial_message
        self.run_flag = True
        self.start()
    def threadStop(self):
        self.run_flag = False
    def run(self):
        print("Start Reading")
        self.run_flag = True
        while self.run_flag:
            try:
                if self.ser.in_waiting:
                    # read_str=self.ser.read(self.ser.in_waiting ).decode("gbk")
                    read_str=self.ser.read(self.ser.in_waiting ).hex()
                    self.updated.emit(str("[Read ] {}".format(read_str)))
                    time.sleep(0.05) # CPU占用过高
            except Exception as e:
                print(str(e))

# correct bind
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__() # 菱形继承
        self.setupUi(self)
        self.led_widget._layout = QtWidgets.QGridLayout(self.led_widget)
        self._create_leds()
        self._arrange_leds()
        self.serial_flag = False
        for i in range (1,21):
            exec('self.serial_port.addItem("/dev/ttyS{0}")'.format(i))

    def serial_connect(self): # button
        if not self.serial_flag:
            serial_port = self.serial_port.currentText()
            baud_rate = self.baud_rate.currentText()
            data_bit = int(self.data_bit.currentText())
            parity = self.parity.currentText()
            stop_bit = int(self.stop_bit.currentText())
            # port_list = list(serial.tools.list_ports.comports())
            try:
                self.ser=serial.Serial(port=serial_port,baudrate=baud_rate,bytesize=data_bit,parity=parity,stopbits=stop_bit,timeout=0.5)
                if self.ser.isOpen():
                    self._serial_state("connected")
                    self.serial_message.append("Seral connected")
                    self.serial_flag = True
                    self.readthread = readThread()
                    self.readthread.setser(self.ser, self.serial_message)
                    self.readthread.updated.connect(self.thread_append)
            except Exception as e:
                self.serial_message.append("Open {0} failed, make sure you open the device".format(serial_port))
                self._serial_state("failed")
            self.led_widget.led1.turn_on(True)
        else:
            self.serial_message.append("Serial already connected")

    def serial_disconnect(self):
        # self.readthread.quit()
        try:
            self.ser.flush()
            if self.ser.isOpen():
                self.readthread.threadStop()
                # self.readthread.wait()
                self.readthread.quit()
                self.readthread = None
                self.ser.close()
                self._serial_state("wait")
                self.serial_message.append("Serial disconnected")
            else:
                self._serial_state("failed")
                self.serial_message.append("Serial can not connected")
            self.serial_flag = self.ser.isOpen()
        except Exception as e:
            self.serial_message.append("Close serial connect failed")
            self._serial_state("wait")
    
    def send_test(self):
        # send = "Hi"
        # send = "01050000FF008C3A" # 1 on
        # send = "010F000000080100FE95" # 1-8off
        send = "010400000004F1C9" # dac 1
        # send = "0104000000040000" # dac 1
        # send = "01050001FF000000" # 3 on
        # send = "0105000100000000" # 1 3 oof
        if self.serial_flag and self.ser.isOpen():
            send = bytes.fromhex(send)
            result = self.ser.write(send)
            self.serial_message.append("[Write] {}".format(send))

    def thread_append(self, text):
        self.serial_message.append(text)

    def _serial_state(self,state):
        if state == 'failed':
            self.waitinglabel.setStyleSheet("color:red;font-weight:bold")
            self.waitinglabel.setText("Failed")
        if state == 'wait':
            self.waitinglabel.setStyleSheet("color:black;font-weight:bold")
            self.waitinglabel.setText("Waiting")
        if state == 'connected':
            self.waitinglabel.setStyleSheet("color:green;font-weight:bold")
            self.waitinglabel.setText("Connected")
        else:
            pass

    def _create_leds(self):
        for i in range (0,8):
            exec('self.led_widget.led{0} = Led(self.led_widget, on_color=Led.red, shape=Led.circle, build="debug")'.format(i))

    def _arrange_leds(self):
        for i in range (0,4):
            exec('self.led_widget._layout.addWidget(self.led_widget.led{0},0,{0}, 1, 1, QtCore.Qt.AlignCenter)'.format(i))
        for i in range (4,8):
            exec('self.led_widget._layout.addWidget(self.led_widget.led{0},1,{0}-4, 1, 1, QtCore.Qt.AlignCenter)'.format(i))

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)            #pyqt窗口必须在QApplication方法中使用
    myshow=MyWindow()                               #生成mywindow类的实例 myshow
    myshow.show()                                   #myshow调用show方法
    sys.exit(app.exec())                            #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序