#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年7月2日
@author: Irony
@site: https://pyqt5.com https://github.com/PyQt5
@email: 892768447@qq.com
@file: QPushButton.SignalsExample
@description: button信号例子
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit

# 有中文显示乱码问题

__Author__ = "Irony"
__Copyright__ = "Copyright (c) 2019"
__Version__ = "Version 1.0"


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)

        btn1 = QPushButton('button click signal', self)
        btn1.setObjectName('ClickBtn')
        btn1.clicked.connect(self.onClicked)

        layout.addWidget(btn1)
        layout.addWidget(QPushButton(
            'button push signal', self, objectName='PressBtn', pressed=self.onPressed))
        layout.addWidget(QPushButton(
            'button release signal', self, objectName='ReleaseBtn', released=self.onReleased))
        layout.addWidget(QPushButton(
            'button selected signal', self, checkable=True, objectName='ToggleBtn', toggled=self.onToggled))

        self.resultView = QPlainTextEdit(self)
        self.resultView.setReadOnly(True)
        layout.addWidget(self.resultView)

    def onClicked(self):
        self.resultView.appendPlainText(
            'button {0} clicked'.format(self.sender().objectName()))

    def onPressed(self):
        self.resultView.appendPlainText(
            'button {0} pushed'.format(self.sender().objectName()))

    def onReleased(self):
        self.resultView.appendPlainText(
            'button {0} released'.format(self.sender().objectName()))

    def onToggled(self, checked):
        self.resultView.appendPlainText(
            'button {0} selected : {1}'.format(self.sender().objectName(), checked))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
