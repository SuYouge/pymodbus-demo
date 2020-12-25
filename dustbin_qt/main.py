"""
继承调试类：debug，设置界面及默认参数
"""

import debug
import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt

class MyWindow(debug.MyWindow):
    def __init__(self):
        super(MyWindow,self).__init__() # 菱形继承
        self.gui_tab.setWindowFlags (Qt.Window|Qt.FramelessWindowHint)
        self.gui_tab.showFullScreen()
        self.serial_connect() # 直接开启任务
    
    def read_param(self):
        self.serial_port = "/dev/ttyS3"
        self.modbus_port = "/dev/ttyS1"
        self.baud_rate = 9600
        self.data_bit = 8
        self.parity = 'N'
        self.stop_bit = 1

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    # myshow.show()
    # myshow.setWindowFlags(Qt.FramelessWindowHint)
    # myshow.showMaximized()
    # myshow.showFullScreen()
    sys.exit(app.exec())
    
