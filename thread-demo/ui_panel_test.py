# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_testBLsgQJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import gui_source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(881, 627)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.gui_tab = QWidget()
        self.gui_tab.setObjectName(u"gui_tab")
        self.gridLayout_5 = QGridLayout(self.gui_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.gui_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-image: url(:/layer/source/1.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.gui_tab, "")
        self.back_tab = QWidget()
        self.back_tab.setObjectName(u"back_tab")
        self.back_tab.setMaximumSize(QSize(840, 500))
        self.gridLayout = QGridLayout(self.back_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setVerticalSpacing(6)
        self.title_2 = QLabel(self.back_tab)
        self.title_2.setObjectName(u"title_2")

        self.gridLayout_2.addWidget(self.title_2, 0, 0, 1, 1)

        self.serial_port = QComboBox(self.back_tab)
        self.serial_port.addItem("")
        self.serial_port.setObjectName(u"serial_port")
        sizePolicy.setHeightForWidth(self.serial_port.sizePolicy().hasHeightForWidth())
        self.serial_port.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.serial_port, 0, 1, 1, 1)

        self.title_6 = QLabel(self.back_tab)
        self.title_6.setObjectName(u"title_6")

        self.gridLayout_2.addWidget(self.title_6, 5, 0, 1, 1)

        self.connect_click = QPushButton(self.back_tab)
        self.connect_click.setObjectName(u"connect_click")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.connect_click.sizePolicy().hasHeightForWidth())
        self.connect_click.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.connect_click, 6, 0, 1, 1)

        self.waitinglabel = QLabel(self.back_tab)
        self.waitinglabel.setObjectName(u"waitinglabel")

        self.gridLayout_2.addWidget(self.waitinglabel, 6, 1, 1, 1)

        self.baud_rate = QComboBox(self.back_tab)
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.setObjectName(u"baud_rate")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.baud_rate.sizePolicy().hasHeightForWidth())
        self.baud_rate.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.baud_rate, 2, 1, 1, 1)

        self.data_bit = QComboBox(self.back_tab)
        self.data_bit.addItem("")
        self.data_bit.addItem("")
        self.data_bit.addItem("")
        self.data_bit.addItem("")
        self.data_bit.setObjectName(u"data_bit")
        sizePolicy3.setHeightForWidth(self.data_bit.sizePolicy().hasHeightForWidth())
        self.data_bit.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.data_bit, 3, 1, 1, 1)

        self.disconnect_click = QPushButton(self.back_tab)
        self.disconnect_click.setObjectName(u"disconnect_click")
        sizePolicy2.setHeightForWidth(self.disconnect_click.sizePolicy().hasHeightForWidth())
        self.disconnect_click.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.disconnect_click, 7, 0, 1, 1)

        self.stop_bit = QComboBox(self.back_tab)
        self.stop_bit.addItem("")
        self.stop_bit.addItem("")
        self.stop_bit.addItem("")
        self.stop_bit.setObjectName(u"stop_bit")
        sizePolicy3.setHeightForWidth(self.stop_bit.sizePolicy().hasHeightForWidth())
        self.stop_bit.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.stop_bit, 5, 1, 1, 1)

        self.title_4 = QLabel(self.back_tab)
        self.title_4.setObjectName(u"title_4")

        self.gridLayout_2.addWidget(self.title_4, 3, 0, 1, 1)

        self.title_3 = QLabel(self.back_tab)
        self.title_3.setObjectName(u"title_3")

        self.gridLayout_2.addWidget(self.title_3, 2, 0, 1, 1)

        self.parity = QComboBox(self.back_tab)
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.setObjectName(u"parity")
        sizePolicy3.setHeightForWidth(self.parity.sizePolicy().hasHeightForWidth())
        self.parity.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.parity, 4, 1, 1, 1)

        self.title_5 = QLabel(self.back_tab)
        self.title_5.setObjectName(u"title_5")

        self.gridLayout_2.addWidget(self.title_5, 4, 0, 1, 1)

        self.label = QLabel(self.back_tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.modbus_port = QComboBox(self.back_tab)
        self.modbus_port.addItem("")
        self.modbus_port.setObjectName(u"modbus_port")
        sizePolicy.setHeightForWidth(self.modbus_port.sizePolicy().hasHeightForWidth())
        self.modbus_port.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.modbus_port, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setRowStretch(6, 1)
        self.gridLayout_2.setRowStretch(7, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.IO_label_3 = QLabel(self.back_tab)
        self.IO_label_3.setObjectName(u"IO_label_3")

        self.gridLayout_3.addWidget(self.IO_label_3, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.back_tab)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 1)

        self.serial_message = QTextEdit(self.back_tab)
        self.serial_message.setObjectName(u"serial_message")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.serial_message.sizePolicy().hasHeightForWidth())
        self.serial_message.setSizePolicy(sizePolicy4)
        self.serial_message.setMinimumSize(QSize(420, 150))
        self.serial_message.setReadOnly(True)

        self.gridLayout_3.addWidget(self.serial_message, 2, 0, 1, 2)

        self.IO_label_2 = QLabel(self.back_tab)
        self.IO_label_2.setObjectName(u"IO_label_2")

        self.gridLayout_3.addWidget(self.IO_label_2, 0, 0, 1, 1)

        self.led_widget = QWidget(self.back_tab)
        self.led_widget.setObjectName(u"led_widget")
        sizePolicy4.setHeightForWidth(self.led_widget.sizePolicy().hasHeightForWidth())
        self.led_widget.setSizePolicy(sizePolicy4)
        self.led_widget.setMinimumSize(QSize(360, 60))
        self.led_widget.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_3.addWidget(self.led_widget, 0, 1, 2, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setRowStretch(2, 200)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 50)

        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.tabWidget.addTab(self.back_tab, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 20))
        self.menuSerialPannel = QMenu(self.menubar)
        self.menuSerialPannel.setObjectName(u"menuSerialPannel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSerialPannel.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.baud_rate.setCurrentIndex(1)
        self.data_bit.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gui_tab), QCoreApplication.translate("MainWindow", u"GUI", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Entrance</span></p></body></html>", None))
        self.serial_port.setItemText(0, QCoreApplication.translate("MainWindow", u"/dev/ttyTHS1", None))

        self.title_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Stop Bit</span></p></body></html>", None))
        self.connect_click.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.waitinglabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Not Connected</span></p></body></html>", None))
        self.baud_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"4800", None))
        self.baud_rate.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.baud_rate.setItemText(2, QCoreApplication.translate("MainWindow", u"14400", None))
        self.baud_rate.setItemText(3, QCoreApplication.translate("MainWindow", u"19200", None))
        self.baud_rate.setItemText(4, QCoreApplication.translate("MainWindow", u"38400", None))
        self.baud_rate.setItemText(5, QCoreApplication.translate("MainWindow", u"56000", None))
        self.baud_rate.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.baud_rate.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))

        self.data_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.data_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"6", None))
        self.data_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))
        self.data_bit.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))

        self.data_bit.setCurrentText(QCoreApplication.translate("MainWindow", u"8", None))
        self.disconnect_click.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.stop_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.stop_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.stop_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.title_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Data Bit</span></p></body></html>", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Baud Rate</span></p></body></html>", None))
        self.parity.setItemText(0, QCoreApplication.translate("MainWindow", u"N", None))
        self.parity.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))
        self.parity.setItemText(2, QCoreApplication.translate("MainWindow", u"O", None))

        self.title_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Parity</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">485Module</span></p></body></html>", None))
        self.modbus_port.setItemText(0, QCoreApplication.translate("MainWindow", u"/dev/ttyS0", None))

        self.IO_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">IO_OUT</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.IO_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">IO_IN</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.back_tab), QCoreApplication.translate("MainWindow", u"DEBUG", None))
        self.menuSerialPannel.setTitle(QCoreApplication.translate("MainWindow", u"SerialPannel", None))
    # retranslateUi

