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
        super(MyWindow,self).__init__() # 菱形继承
        self.setupUi(self)

        self.led_widget._layout = QtWidgets.QGridLayout(self.led_widget)
        self._create_leds()
        self._arrange_leds()

        self.serial_flag = False

        for i in range (1,21):
            exec('self.serial_port.addItem("/dev/ttyS{0}")'.format(i))

        self.logger = modbus_tk.utils.create_logger("console")

        for i in range (1,17):
            exec('self.io_read_from.addItem("{0}")'.format(i))
            exec('self.io_write_from.addItem("{0}")'.format(i))
            exec('self.io_read_to.addItem("{0}")'.format(i))
            exec('self.io_write_to.addItem("{0}")'.format(i))
    
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
            baud_rate = self.baud_rate.currentText()
            data_bit = int(self.data_bit.currentText())
            parity = self.parity.currentText()
            stop_bit = int(self.stop_bit.currentText())
            try:
                self.ser=serial.Serial(port=serial_port,baudrate=baud_rate,bytesize=data_bit,parity=parity,stopbits=stop_bit)
                self.master = modbus_rtu.RtuMaster(self.ser)
                self.master.set_timeout(0.5)
                self.master.set_verbose(True)
                self.logger.info("connected")
                if self.ser.isOpen():
                    self._serial_state("connected")
                    self.serial_message.append("[State] Seral connected")
                    self.serial_flag = True

                    self.readthread = readThread()
                    self.readthread.setser(self.ser, self.serial_message)
                    self.readthread.updated.connect(self._thread_append)

            except Exception as e:
                self.serial_message.append("Open {0} failed, make sure you open the device".format(serial_port))
                self._serial_state("failed")
        else:
            self.serial_message.append("[State] Serial already connected")

    def serial_disconnect(self):
        try:
            self.ser.flush()
            if self.ser.isOpen():
                self.readthread.threadStop()
                # self.readthread.wait()
                self.readthread.quit()
                self.readthread = None

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

    """
    io_read_click_callback:
        input:
            io_port
            io_read_from
            io_read_to
            io_read_state
        output:
            self.serial_message
    """
    def io_read_click_callback(self):
        if self.serial_flag:
            io_port = int(self.io_port.currentText())
            io_read_from = int(self.io_read_from.currentText())
            io_read_to = self.io_read_to.currentText()
            io_read_state = self.io_read_state.currentText()
            read_num = 0
            res = None
            if io_read_to == "None":
                read_num = 1
            else :
                io_read_to = int(io_read_to)
                if io_read_to < io_read_from:
                    io_read_from,io_read_to = io_read_to,io_read_from
                read_num = io_read_to - io_read_from + 1
            try:
                if io_read_state == "Input": # 02 READ_DISCRETE_INPUTS
                    res = self.master.execute(io_port, cst.READ_DISCRETE_INPUTS, io_read_from-1, read_num)
                elif io_read_state == "Output": # 01 READ_COILS
                    res = self.master.execute(io_port, cst.READ_COILS, io_read_from-1, read_num)
                loginfo = ""
                for i in range(len(res)):
                    loginfo = loginfo + str(res[i]) + " "
                    if res[i] == 1:
                        exec('self.led_widget.led_{0}{1}.turn_on(True)'.format(io_read_state.lower(),i))
                    elif res[i] == 0:
                        exec('self.led_widget.led_{0}{1}.turn_on(False)'.format(io_read_state.lower(),i))
                self.serial_message.append("[Read] {1}[{2}-{3}]: {0}".format(loginfo, io_read_state,io_read_from,io_read_to))
            except Exception as e:
                self.serial_message.append("[State] Undefined Read config")
        else:
            self.serial_message.append("[State] Read serial failed")
            self._serial_state("wait")
        
    """
    io_write_click_callback:
        input:
            analog_port
            io_write_from
            io_write_to
            io_write_state
        output:
    """
    def io_write_click_callback(self):
        if self.serial_flag:
            io_port = int(self.io_port.currentText())
            io_write_from = int(self.io_write_from.currentText())
            io_write_to = self.io_write_to.currentText()
            io_write_state = self.io_write_state.currentText()
            write_num = 0
            res = None
            if io_write_to == "None":
                write_num = 1
            else :
                io_write_to = int(io_write_to)
                if io_write_to < io_write_from:
                    io_write_from,io_write_to = io_write_to,io_write_from
                write_num = io_write_to - io_write_from + 1
            try:
                if write_num == 1: # 05
                    if io_write_state == "On":
                        res = self.master.execute(io_port, cst.WRITE_SINGLE_COIL, io_write_from-1, output_value=1)
                    elif io_write_state == "Off":
                        res = self.master.execute(io_port, cst.WRITE_SINGLE_COIL, io_write_from-1, output_value=0)
                elif write_num >1: # 15
                    if io_write_state == "On":
                        res = self.master.execute(io_port, cst.WRITE_MULTIPLE_COILS, io_write_from-1, output_value=[1 for i in range(0,write_num)])
                    elif io_write_state == "Off":
                        res = self.master.execute(io_port, cst.WRITE_MULTIPLE_COILS, io_write_from-1, output_value=[0 for i in range(0,write_num)])
                self.serial_message.append("[Write] {1}[{2}-{3}]: {0}".format(res[1], "Output",io_write_from,io_write_to))
            except Exception as e:
                self.serial_message.append("[State] Undefined Write config")
        else:
            self.serial_message.append("[State] Write serial failed")
            self._serial_state("wait")

    """
    analog_read_click_callback:
        input:
            analog_port
            analog_read_from
            analog_read_unit
        output:
            serial_message
    """
    def analog_read_click_callback(self):
        if self.serial_flag:
            analog_port = self.analog_port.currentText()
            analog_read_from = int(self.analog_read_from.currentText())
            analog_read_unit = self.analog_read_unit.currentText()
            res = None
            if analog_read_unit == "V":
                start = 0
                interval = 10
            elif analog_read_unit == "mA":
                start = 0
                interval = 20
            try:
                res = self.master.execute(1, cst.READ_INPUT_REGISTERS, analog_read_from-1, 1) # 
                self.serial_message.append("[Read] {0}[{1}]: {2} {3}".format("input",analog_read_from , res[0]/4000*interval+start,analog_read_unit))
            except Exception as e:
                self.serial_message.append("[State] Undefined Analog Read config")
        else:
            self.serial_message.append("[State] Read serial failed")
            self._serial_state("wait")
    
    """
    analog_write_click_callback:
        input:
            analog_port
            analog_write_to
            analog_wirte_value
            analog_write_unit
        output:
            serial_message
    """
    def analog_write_click_callback(self):
        if self.serial_flag:
            analog_port = self.analog_port.currentText()
            analog_write_to = int(self.analog_write_to.currentText())
            analog_wirte_value =self.analog_wirte_value.text()
            if analog_wirte_value == "":
                analog_wirte_value = 0
            else:
                analog_wirte_value = float(analog_wirte_value)
            analog_write_unit = self.analog_write_unit.currentText()
            res = None
            try:
                if analog_write_unit == "V":
                    start = 0
                    interval = 10
                elif analog_write_unit == "mA":
                    start = 4
                    interval = 16
                if analog_wirte_value-start < 0:
                    pass
                output_value = int((analog_wirte_value-start)/interval*4096)
                res = self.master.execute(1, cst.WRITE_SINGLE_REGISTER, analog_write_to-1, output_value=output_value)
                self.serial_message.append("[Write] {0}[{1}]: {2}".format("Output", analog_write_to, res[1]))
            except Exception as e:
                self.serial_message.append("[State] Undefined Analog Write config")
        else:
            self.serial_message.append("[State] Write serial failed")
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
if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec())