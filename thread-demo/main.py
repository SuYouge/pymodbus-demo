import sys
from panel import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
from pyqt_led.pyqt_led import Led # From https://github.com/Neur1n/pyqt_led

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

import os
import yaml

class switch:
    def __init__(self, addr, port, master):
        self.addr = addr
        self.port = port
        self.master = master
        self.state = -1
        print("Init switch at {0} {1}".format(addr,port))
    def check_on(self):
        self.state = self.master.execute(self.addr, cst.READ_DISCRETE_INPUTS, self.port-1, 1)[0]
        return self.state

class motor:
    def __init__(self, addr, bridge, master):
        self.addr = addr
        self.bridge = bridge
        self.master = master
        (h1,h2,l1,l2) = bridge
        print("Init motor at {0} {1}".format(addr, bridge))
    def stop(self):
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, h1-1, output_value=0)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, h2-1, output_value=0)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, l1-1, output_value=0)
        res = self.master.execute(io_port, cst.WRITE_SINGLE_COIL, l2-1, output_value=0)
        pass
    def forward(self):
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, h1-1, output_value=1)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, h2-1, output_value=0)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, l1-1, output_value=0)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, l2-1, output_value=1)
        pass
    def reverse(self):
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, h1-1, output_value=0)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, h2-1, output_value=1)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, l1-1, output_value=1)
        res = self.master.execute(addr, cst.WRITE_SINGLE_COIL, l2-1, output_value=0)
        pass

class entranceThread(QThread):
    updated = pyqtSignal(str)
    start_work = pyqtSignal(bool)
    def __init__(self):
        super(entranceThread, self).__init__()
        self.ser = None
        self.run_flag = False
    def setser(self, ser):
        self.ser = ser
        self.run_flag = True
        self.start()
    def threadStop(self):
        self.run_flag = False
    def run(self):
        print("Start Reading Entrance")
        self.run_flag = True
        while self.run_flag:
            try:
                if self.ser.in_waiting:
                    read_str=self.ser.read(self.ser.in_waiting )
                    # read_str=self.ser.read(self.ser.in_waiting ).hex()
                    self.updated.emit(str("[Read ] {}".format(read_str)))
                    if str(read_str,'utf-8').split("'")[0] == "ABCD":
                        self.start_work.emit(bool(True))
                    time.sleep(0.1) # CPU占用过高
            except Exception as e:
                print(str(e))

class workThread(QThread):
    updated = pyqtSignal(str)
    def __init__(self):
        super(workThread, self).__init__()
        self.motor_1 = None
        self.switch_1 = None

    def setdevice(self, motor_1, switch_1):
        self.motor_1 = motor_1
        self.switch_1 = switch_1
        self.start()

    def run(self):
        print("Start Working thread")
        # while True:
        print(self.switch_1.check_on())
        print("Working thread died")

    

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    """
    init:
        set UI
        set led
        set self.serial_flag
        add serial_port item
        set logger
        set io_read/write_from,io_read/write_to 
    """
    def __init__(self):
        # set UI
        super(MyWindow,self).__init__() # 菱形继承
        self.setupUi(self)
        self.led_widget._layout = QtWidgets.QGridLayout(self.led_widget)
        self._create_leds()
        self._arrange_leds()
        for i in range (1,21):
            exec('self.serial_port.addItem("/dev/ttyS{0}")'.format(i))
        for i in range (1,21):
            exec('self.modbus_port.addItem("/dev/ttyS{0}")'.format(i))
        self.logger = modbus_tk.utils.create_logger("console")
        self.serial_flag = False

    #call after serial&master init
    def init_hardware(self):
        fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        yamlPath = os.path.join(fileNamePath,'./config.yaml')
        config = None
        try:
            with open(yamlPath,'r',encoding='utf-8') as f:
                result = f.read()
                config = yaml.load(result,Loader=yaml.FullLoader)
                # init motor
                self.motor_1 = motor(config['digital_device']['addr'],tuple(config['digital_device']['output']['d01']), self.master)
                # init switches
                self.switch_1 = switch(config['digital_device']['addr'],config['digital_device']['input']['td01'], self.master)
        except Exception as e:
            self.serial_message.append("Read config at {} failed".format(yamlPath))
            print(x['digital_device']['addr'])

    """
    onclick:serial_connect
    input:
        self.serial_port.currentText()
        self.baud_rate.currentText()
        self.data_bit.currentText()
        self.parity.currentText()
        self.stop_bit.currentText()
    output:
        self.ser
        self.master
        self.serial_message
        self.serial_flag
    """
    def serial_connect(self):
        if not self.serial_flag:
            serial_port = self.serial_port.currentText()
            modbus_port = self.modbus_port.currentText()
            baud_rate = self.baud_rate.currentText()
            data_bit = int(self.data_bit.currentText())
            parity = self.parity.currentText()
            stop_bit = int(self.stop_bit.currentText())
            try:
                self.ser=serial.Serial(port=serial_port,baudrate=baud_rate,bytesize=data_bit,parity=parity,stopbits=stop_bit)
                self.mod=serial.Serial(port=modbus_port,baudrate=baud_rate,bytesize=data_bit,parity=parity,stopbits=stop_bit)
                self.master = modbus_rtu.RtuMaster(self.mod)
                self.master.set_timeout(0.5)
                self.master.set_verbose(True)
                self.logger.info("connected")
                if self.ser.isOpen():
                    self._serial_state("connected")
                    self.serial_message.append("[State] Seral connected")
                    self.serial_flag = True
                    self.init_hardware()
                    # Start entrance thread
                    self.entranceThread = entranceThread()
                    self.entranceThread.setser(self.ser)
                    self.entranceThread.updated.connect(self._thread_append)
                    self.entranceThread.start_work.connect(self._workthread)
            except Exception as e:
                self.serial_message.append("Open {0} failed, make sure you open the device".format(serial_port))
                self._serial_state("failed")
        else:
            self.serial_message.append("[State] Serial already connected")

    def serial_disconnect(self):
        try:
            self.ser.flush()
            if self.ser.isOpen():
                self.entranceThread.threadStop()
                self.entranceThread.quit()
                self.entranceThread = None

                self.master.close()
                self.ser.close()
                self._serial_state("wait")
                self.serial_message.append("[State] Serial disconnected")
            else:
                self._serial_state("failed")
                self.serial_message.append("[State] Serial can not connected")
            self.serial_flag = self.ser.isOpen()
        except Exception as e:
            self.serial_message.append("[State] Close serial connect failed")
            self._serial_state("wait")

    def _serial_state(self,state):
        if state == 'failed':
            self.waitinglabel.setStyleSheet("color:red;font-weight:bold")
            self.waitinglabel.setText("Failed")
        if state == 'wait':
            self.waitinglabel.setStyleSheet("color:black;font-weight:bold")
            self.waitinglabel.setText("Not Connected")
        if state == 'connected':
            self.waitinglabel.setStyleSheet("color:green;font-weight:bold")
            self.waitinglabel.setText("Connected")
        else:
            pass

    def clean_log(self):
        self.serial_message.clear()
        pass

    def _create_leds(self):
        for i in range (0,16):
            exec('self.led_widget.led_input{0} = Led(self.led_widget, on_color=Led.red, shape=Led.circle, build="debug")'.format(i))
        for i in range (0,16):
            exec('self.led_widget.led_output{0} = Led(self.led_widget, on_color=Led.red, shape=Led.circle, build="debug")'.format(i))
    
    def _arrange_leds(self):
        for i in range (0,16):
            exec('self.led_widget._layout.addWidget(self.led_widget.led_input{0},0,{0}, 1, 1, QtCore.Qt.AlignCenter)'.format(i))
        for i in range (0,16):
            exec('self.led_widget._layout.addWidget(self.led_widget.led_output{0},1,{0}, 1, 1, QtCore.Qt.AlignCenter)'.format(i))

    def _thread_append(self, text):
        self.serial_message.append(text)

    def _workthread(self, flag):
        if flag == True:
            self.workThread = workThread()
            self.workThread.setdevice(self.motor_1,self.switch_1)
            self.workThread.updated.connect(self._thread_append)
            pass

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec())