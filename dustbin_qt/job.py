"""
流程类：
    read_id_list: 读取excel表格中的ID，生成user列表和admin列表 
    init_hardware：读取配置列表
    entranceThread：门禁线程，循环读取串口上的ID，判断是否与user/admin中的一致
    userThread：用户倒垃圾的工作线程
    adminThread：管理员处理线程
"""

from PyQt5.QtCore import QThread, pyqtSignal
import time
from device import adc, motor, switch, output_switch
import os
import yaml
import xlrd
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import sys

def read_id_list(): # 读取用户名单
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    xlPath = os.path.join(fileNamePath,'./user_list.xlsx')
    data = xlrd.open_workbook(xlPath)
    table = data.sheet_by_name('Sheet1')
    user = []
    admin = []
    for i in range (0,table.ncols):
        if table.cell(0,i).value=="ID":
            id_col = i
        elif table.cell(0,i).value=="GROUP":
            group_col = i
    for i in range (1, table.nrows):
        if table.cell(i, group_col).value.lower() == "user":
            user.append(table.cell(i,id_col).value)
        elif table.cell(i, group_col).value.lower() == "admin":
            admin.append(table.cell(i,id_col).value)
    return user,admin

def init_hardware(): # 读取设备配置
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath,'./config.yaml')
    with open(yamlPath,'r',encoding='utf-8') as f:
        result = f.read()
        config = yaml.load(result,Loader=yaml.FullLoader)
        print(config)
    return config

class entranceThread(QThread):
    log = pyqtSignal(str) # 日志
    start_user = pyqtSignal(bool) # 开始用户工作流程
    start_admin = pyqtSignal(bool) # 开始管理员工作流程

    def __init__(self, ser, user, admin):
        super(entranceThread, self).__init__()
        self.ser = None
        self.ser = ser
        self.run_flag = False
        self.admin = admin
        self.user = user
        self.working = False

    def threadStop(self):
        self.run_flag = False

    def release(self): # 工作结束后调用realse放开读卡器读数
        self.working = False

    def run(self):
        print("Start Reading Entrance")
        self.run_flag = True
        while self.run_flag:
            time.sleep(0.1) # CPU占用过高
            try:
                if self.ser.in_waiting:
                    read_str=self.ser.read(self.ser.in_waiting)
                    # read_str=self.ser.read(self.ser.in_waiting ).hex()
                    # self.log.emit(str("[Read ] {}".format(read_str))) #
                    if not self.working: # 防止二次刷卡
                        self.working = True
                        input_id = str(read_str,'utf-8').split("'")[0]
                        if input_id in self.user:
                            # self.start_user.emit(bool(True)) # 
                            # self.log.emit(str("[ENTER] Valid user {}".format(input_id))) #
                            print("Valid user")
                        elif input_id in self.admin:
                            # self.start_admin.emit(bool(True)) # 
                            # self.log.emit(str("[ENTER] Valid admin {}".format(input_id))) # 
                            print("Valid admin")
                        else:
                            # self.working = False # 
                            # self.log.emit(str("[ENTER] Invalid user {}".format(input_id))) #
                            print("Invalid user")
                    else:
                        # self.log.emit(str("[ENTER] Don`t scan twice {}".format(input_id))) # 
                        print("Dont scan twice")
            except Exception as e:
                print(str(e))
        print("Thread died")

class userThread(QThread):
    log = pyqtSignal(str) # 日志
    end = pyqtSignal(bool)
    def __init__(self,master):
        super(userThread, self).__init__()
        self.master = master
        config = init_hardware()
        for i in range (1,4):
            exec("print(tuple(config['digital_device']['output']['d0{}']))".format(i))
            exec("self.motor_{0} = motor(config['digital_device']['addr'],tuple(config['digital_device']['output']['d0{0}']), self.master)".format(i))
            print("motor_{} init".format(i))
        for i in range (4,8):
            exec("self.output_switch_{0} = output_switch(config['digital_device']['addr'],config['digital_device']['output']['d0{0}'], self.master)".format(i))
            print("output_switch_{} init".format(i))
        for i in range (1,11):
            exec("self.switch_{0} = switch(config['digital_device']['addr'],config['digital_device']['input']['td0{0}'], self.master)".format(i))
        self.adc = adc(config['analog_device']['addr'],config['analog_device']['input']['force'],self.master)
    
    def test(self):
        self.test()
    
    def run(self):
        print("Start User thread")
        # while True:
        for i in range (1,4):
            time.sleep(0.5)
            exec("self.motor_{}.forward()".format(i))
            time.sleep(1.5)
            exec("self.motor_{}.stop()".format(i))
            time.sleep(1.5)
            exec("self.motor_{}.reverse()".format(i))
        time.sleep(0.5)

        for i in range (4,8):
            time.sleep(0.5)
            exec("print(self.output_switch_{}.set_state(0))".format(i))
            time.sleep(1.5)
            exec("print(self.output_switch_{}.set_state(1))".format(i))
            time.sleep(1.5)

        for i in range (1,11):
            time.sleep(1.5)
            exec("print(self.switch_{}.check_on())".format(i))
        time.sleep(0.5)
        print(self.adc.get_value())
        # self.log.emit(str("[Read ] switch at {0}, state = {1}".format(self.switch_1.port, self.switch_1.check_on())))
        print("user thread died")

def test_entrance():
    print("Start test entrance")
    config = init_hardware() # 测试配置读取
    user,admin  = read_id_list()
    try:
        ser=serial.Serial(port="/dev/ttyS1",baudrate=9600,bytesize=8,parity='N',stopbits=1)
    except Exception as e:
        print("Test failed, check modbus device and serial comm")
        sys.exit()
    print("Start test entrance thread")
    thread_1 = entranceThread(ser, user, admin)
    thread_1.start()
    cnt = 0
    while cnt<1:
        cnt+=1
        time.sleep(10.0)
        print("Release scanner")
        thread_1.release() # 释放门禁
    ser.flush()
    if ser.isOpen():
        thread_1.threadStop()
        thread_1.quit()
        while not thread_1.wait(): # run结束后通过wait判断线程是否成功退出
            time.sleep(0.1)
        ser.close()
        print("Serial and thread quit safely")

def test_user():
    print("Start test user thread")
    config = init_hardware() # 测试配置读取
    user,admin  = read_id_list()
    try:
        ser=serial.Serial(port="/dev/ttyS1",baudrate=9600,bytesize=8,parity='N',stopbits=1)
    except Exception as e:
        print("Test failed, check modbus device and serial comm")
        sys.exit()
    master = modbus_rtu.RtuMaster(ser)
    master.set_timeout(5.0) # 需要设置，否则可能没有返回值
    thread_2 = userThread(master)
    thread_2.start()
    while not thread_2.wait():
        time.sleep(1.0)


if __name__ == "__main__":
    config = init_hardware() # 测试配置读取
    user,admin  = read_id_list() # 测试user/admin名单
    # test_entrance() # 测试门禁线程
    test_user() # 测试用户线程
    
