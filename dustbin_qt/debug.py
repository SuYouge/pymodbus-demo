"""
主界面调试类： 完成程序主体逻辑
"""

import sys
from panel import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

import os
import yaml

from device import adc, motor, switch
# from job import entranceThread, workThread
from job import init_hardware, read_id_list
import job

class entranceThread(job.entranceThread): # 重载
    def run(self):
        self.run_flag = True
        while self.run_flag:
            time.sleep(0.1) # CPU占用过高
            try:
                if self.ser.in_waiting:
                    read_str=self.ser.read(self.ser.in_waiting)
                    # read_str=self.ser.read(self.ser.in_waiting ).hex()
                    if not self.working: # 防止二次刷卡
                        self.working = True
                        input_id = str(read_str,'utf-8').split("'")[0]
                        self.log.emit(str("[Read] {}".format(input_id))) #
                        if input_id in self.user:
                            self.start_user.emit(bool(True)) # 
                            self.log.emit(str("[Door] Valid user {}".format(input_id))) #
                        elif input_id in self.admin:
                            self.start_admin.emit(bool(True)) # 
                            self.log.emit(str("[Door] Valid admin {}".format(input_id))) # 
                        else:
                            self.working = False # 
                            self.log.emit(str("[Door] Invalid user {}".format(input_id))) #
                    else:
                        self.log.emit(str("[Door] Don`t scan twice {}".format(input_id))) # 
            except Exception as e:
                print(str(e))

class userThread(job.userThread): # 重载
    def run(self):
        self.log.emit("Start User thread")
        # while True:
        for i in range (1,4):
            time.sleep(0.5)
            exec("self.motor_{}.forward()".format(i))
            time.sleep(0.5)
            exec("self.motor_{}.stop()".format(i))
            time.sleep(0.5)
            exec("self.motor_{}.reverse()".format(i))
            exec("self.log.emit('motor_{0} test done')".format(i))
        time.sleep(0.5)
        for i in range (1,11):
            exec("self.log.emit(str(self.switch_{}.check_on()))".format(i))
        time.sleep(0.5)
        self.log.emit(str(self.adc.get_value()))
        self.log.emit("user thread died")
        self.end.emit(True)

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        # set UI
        super(MyWindow,self).__init__() # 菱形继承
        self.setupUi(self)
        # self.gui_tab.setWindowFlags (Qt.Window|Qt.FramelessWindowHint)
        # self.gui_tab.showFullScreen()

        self.serial_flag = False
        self.user,self.admin  = read_id_list()

        for i in range (1,21):
            exec('self.serial_port.addItem("/dev/ttyS{0}")'.format(i))
        for i in range (1,21):
            exec('self.modbus_port.addItem("/dev/ttyS{0}")'.format(i))

    def read_param(self):
        self.serial_port = self.serial_port.currentText()
        self.modbus_port = self.modbus_port.currentText()
        self.baud_rate = self.baud_rate.currentText()
        self.data_bit = int(self.data_bit.currentText())
        self.parity = self.parity.currentText()
        self.stop_bit = int(self.stop_bit.currentText())

    def serial_connect(self):
        # self.frame.setStyleSheet("border-image: url(:/layer/source/2.jpg);")
        if not self.serial_flag:
            self.read_param()
            try:
                # modbus串口
                self.mod=serial.Serial(port=self.modbus_port,baudrate=self.baud_rate,bytesize=self.data_bit,parity=self.parity,stopbits=self.stop_bit)
                self.master = modbus_rtu.RtuMaster(self.mod)
                self.master.set_timeout(0.5)
                self.userThread = userThread(self.master)
                self.userThread.log.connect(self._log_append)
                self.userThread.end.connect(self._release_enter)
                # 门禁串口
                self.ser=serial.Serial(port=self.serial_port,baudrate=self.baud_rate,bytesize=self.data_bit,parity=self.parity,stopbits=self.stop_bit)
                if self.ser.isOpen():
                    self.serial_message.append("[State] Seral connected")
                    self.serial_flag = True
                    self.entranceThread = entranceThread(self.ser, self.user, self.admin)
                    self.entranceThread.log.connect(self._log_append)
                    self.entranceThread.start_user.connect(self._user_thread)
                    self.entranceThread.start_user.connect(self._admin_thread)
                    self.entranceThread.start()
            except Exception as e:
                self.serial_message.append("Open {0} failed, make sure you open the device".format(serial_port))
        else:
            self.serial_message.append("[State] Serial already connected")

    def serial_disconnect(self):
        pass

    def _user_thread(self, flag):
        self.frame.setStyleSheet("border-image: url(:/layer/source/2.jpg);") # 修改背景
        self.userThread.start()

    def _admin_thread(self, flag):
        pass
    
    def _log_append(self, text):
        self.serial_message.append(text)

    def _release_enter(self, flag):
        self.entranceThread.working = False
        self.frame.setStyleSheet("border-image: url(:/layer/source/1.jpg);") # 修改背景

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    # myshow.setWindowFlags(Qt.FramelessWindowHint)
    # myshow.showMaximized()
    # myshow.showFullScreen()
    sys.exit(app.exec())