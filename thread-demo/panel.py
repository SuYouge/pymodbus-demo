# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.IO_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.IO_label_2.setObjectName("IO_label_2")
        self.gridLayout_3.addWidget(self.IO_label_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 1)
        self.led_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_widget.sizePolicy().hasHeightForWidth())
        self.led_widget.setSizePolicy(sizePolicy)
        self.led_widget.setMinimumSize(QtCore.QSize(360, 120))
        self.led_widget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.led_widget.setObjectName("led_widget")
        self.gridLayout_3.addWidget(self.led_widget, 0, 1, 2, 1)
        self.IO_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.IO_label_3.setObjectName("IO_label_3")
        self.gridLayout_3.addWidget(self.IO_label_3, 1, 0, 1, 1)
        self.serial_message = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_message.sizePolicy().hasHeightForWidth())
        self.serial_message.setSizePolicy(sizePolicy)
        self.serial_message.setMinimumSize(QtCore.QSize(420, 150))
        self.serial_message.setReadOnly(True)
        self.serial_message.setObjectName("serial_message")
        self.gridLayout_3.addWidget(self.serial_message, 3, 0, 1, 2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 2, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setRowStretch(2, 2)
        self.gridLayout_3.setRowStretch(3, 16)
        self.gridLayout_3.setRowStretch(4, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_2.setObjectName("title_2")
        self.gridLayout_2.addWidget(self.title_2, 0, 0, 1, 1)
        self.serial_port = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_port.sizePolicy().hasHeightForWidth())
        self.serial_port.setSizePolicy(sizePolicy)
        self.serial_port.setObjectName("serial_port")
        self.serial_port.addItem("")
        self.gridLayout_2.addWidget(self.serial_port, 0, 1, 1, 1)
        self.title_6 = QtWidgets.QLabel(self.centralwidget)
        self.title_6.setObjectName("title_6")
        self.gridLayout_2.addWidget(self.title_6, 5, 0, 1, 1)
        self.connect_click = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_click.sizePolicy().hasHeightForWidth())
        self.connect_click.setSizePolicy(sizePolicy)
        self.connect_click.setObjectName("connect_click")
        self.gridLayout_2.addWidget(self.connect_click, 6, 0, 1, 1)
        self.waitinglabel = QtWidgets.QLabel(self.centralwidget)
        self.waitinglabel.setObjectName("waitinglabel")
        self.gridLayout_2.addWidget(self.waitinglabel, 6, 1, 1, 1)
        self.baud_rate = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baud_rate.sizePolicy().hasHeightForWidth())
        self.baud_rate.setSizePolicy(sizePolicy)
        self.baud_rate.setObjectName("baud_rate")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.gridLayout_2.addWidget(self.baud_rate, 2, 1, 1, 1)
        self.data_bit = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_bit.sizePolicy().hasHeightForWidth())
        self.data_bit.setSizePolicy(sizePolicy)
        self.data_bit.setObjectName("data_bit")
        self.data_bit.addItem("")
        self.data_bit.addItem("")
        self.data_bit.addItem("")
        self.data_bit.addItem("")
        self.gridLayout_2.addWidget(self.data_bit, 3, 1, 1, 1)
        self.disconnect_click = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnect_click.sizePolicy().hasHeightForWidth())
        self.disconnect_click.setSizePolicy(sizePolicy)
        self.disconnect_click.setObjectName("disconnect_click")
        self.gridLayout_2.addWidget(self.disconnect_click, 7, 0, 1, 1)
        self.stop_bit = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_bit.sizePolicy().hasHeightForWidth())
        self.stop_bit.setSizePolicy(sizePolicy)
        self.stop_bit.setObjectName("stop_bit")
        self.stop_bit.addItem("")
        self.stop_bit.addItem("")
        self.stop_bit.addItem("")
        self.gridLayout_2.addWidget(self.stop_bit, 5, 1, 1, 1)
        self.title_4 = QtWidgets.QLabel(self.centralwidget)
        self.title_4.setObjectName("title_4")
        self.gridLayout_2.addWidget(self.title_4, 3, 0, 1, 1)
        self.title_3 = QtWidgets.QLabel(self.centralwidget)
        self.title_3.setObjectName("title_3")
        self.gridLayout_2.addWidget(self.title_3, 2, 0, 1, 1)
        self.parity = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parity.sizePolicy().hasHeightForWidth())
        self.parity.setSizePolicy(sizePolicy)
        self.parity.setObjectName("parity")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.gridLayout_2.addWidget(self.parity, 4, 1, 1, 1)
        self.title_5 = QtWidgets.QLabel(self.centralwidget)
        self.title_5.setObjectName("title_5")
        self.gridLayout_2.addWidget(self.title_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.modbus_port = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modbus_port.sizePolicy().hasHeightForWidth())
        self.modbus_port.setSizePolicy(sizePolicy)
        self.modbus_port.setObjectName("modbus_port")
        self.modbus_port.addItem("")
        self.gridLayout_2.addWidget(self.modbus_port, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setRowStretch(6, 1)
        self.gridLayout_2.setRowStretch(7, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 3)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 5)
        self.gridLayout_4.setColumnStretch(2, 5)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 7)
        self.gridLayout_4.setRowStretch(2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 20))
        self.menubar.setObjectName("menubar")
        self.menuSerialPannel = QtWidgets.QMenu(self.menubar)
        self.menuSerialPannel.setObjectName("menuSerialPannel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSerialPannel.menuAction())

        self.retranslateUi(MainWindow)
        self.baud_rate.setCurrentIndex(1)
        self.data_bit.setCurrentIndex(3)
        self.connect_click.clicked.connect(MainWindow.serial_connect)
        self.disconnect_click.clicked.connect(MainWindow.serial_disconnect)
        self.pushButton.clicked.connect(MainWindow.clean_log)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IO_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">IO_IN</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Clean"))
        self.IO_label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">IO_OUT</span></p></body></html>"))
        self.title_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Entrance</span></p></body></html>"))
        self.serial_port.setItemText(0, _translate("MainWindow", "/dev/ttyTHS1"))
        self.title_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Stop Bit</span></p></body></html>"))
        self.connect_click.setText(_translate("MainWindow", "Connect"))
        self.waitinglabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Not Connected</span></p></body></html>"))
        self.baud_rate.setItemText(0, _translate("MainWindow", "4800"))
        self.baud_rate.setItemText(1, _translate("MainWindow", "9600"))
        self.baud_rate.setItemText(2, _translate("MainWindow", "14400"))
        self.baud_rate.setItemText(3, _translate("MainWindow", "19200"))
        self.baud_rate.setItemText(4, _translate("MainWindow", "38400"))
        self.baud_rate.setItemText(5, _translate("MainWindow", "56000"))
        self.baud_rate.setItemText(6, _translate("MainWindow", "57600"))
        self.baud_rate.setItemText(7, _translate("MainWindow", "115200"))
        self.data_bit.setCurrentText(_translate("MainWindow", "8"))
        self.data_bit.setItemText(0, _translate("MainWindow", "5"))
        self.data_bit.setItemText(1, _translate("MainWindow", "6"))
        self.data_bit.setItemText(2, _translate("MainWindow", "7"))
        self.data_bit.setItemText(3, _translate("MainWindow", "8"))
        self.disconnect_click.setText(_translate("MainWindow", "Disconnect"))
        self.stop_bit.setItemText(0, _translate("MainWindow", "1"))
        self.stop_bit.setItemText(1, _translate("MainWindow", "1.5"))
        self.stop_bit.setItemText(2, _translate("MainWindow", "2"))
        self.title_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Data Bit</span></p></body></html>"))
        self.title_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Baud Rate</span></p></body></html>"))
        self.parity.setItemText(0, _translate("MainWindow", "N"))
        self.parity.setItemText(1, _translate("MainWindow", "E"))
        self.parity.setItemText(2, _translate("MainWindow", "O"))
        self.title_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Parity</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">485Module</span></p></body></html>"))
        self.modbus_port.setItemText(0, _translate("MainWindow", "/dev/ttyS0"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Serial Pannel</span></p></body></html>"))
        self.menuSerialPannel.setTitle(_translate("MainWindow", "SerialPannel"))
