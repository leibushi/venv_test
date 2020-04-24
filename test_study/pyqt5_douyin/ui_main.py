# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/2.txt 15:55
# @Author  : Mqz
# @FileName: ui_main.py

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.txt.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_fullInterface = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_fullInterface.setEnabled(True)
        self.tabWidget_fullInterface.setGeometry(QtCore.QRect(20, 0, 841, 561))
        self.tabWidget_fullInterface.setStyleSheet("font: 12pt \"Arial\";")
        self.tabWidget_fullInterface.setObjectName("tabWidget_fullInterface")
        self.tab_startInterface = QtWidgets.QWidget()
        self.tab_startInterface.setObjectName("tab_startInterface")
        self.pushButton_startRun = QtWidgets.QPushButton(self.tab_startInterface)
        self.pushButton_startRun.setGeometry(QtCore.QRect(90, 430, 131, 51))
        self.pushButton_startRun.setStyleSheet(
            "font: 87 14pt \"Arial\";color: white;background-color: rgb(218,181,150)")
        self.pushButton_startRun.setObjectName("pushButton_startRun")
        self.label_37 = QtWidgets.QLabel(self.tab_startInterface)
        self.label_37.setGeometry(QtCore.QRect(40, 395, 81, 21))
        self.label_37.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_37.setObjectName("label_37")
        self.line_5 = QtWidgets.QFrame(self.tab_startInterface)
        self.line_5.setGeometry(QtCore.QRect(10, 485, 821, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_7 = QtWidgets.QFrame(self.tab_startInterface)
        self.line_7.setGeometry(QtCore.QRect(120, 390, 711, 31))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton_stopRun = QtWidgets.QPushButton(self.tab_startInterface)
        self.pushButton_stopRun.setGeometry(QtCore.QRect(290, 430, 131, 51))
        self.pushButton_stopRun.setStyleSheet("font: 87 14pt \"Arial\";color: white;background-color: rgb(218,181,150)")
        self.pushButton_stopRun.setObjectName("pushButton_stopRun")
        self.line_6 = QtWidgets.QFrame(self.tab_startInterface)
        self.line_6.setGeometry(QtCore.QRect(-20, 405, 61, 101))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_8 = QtWidgets.QFrame(self.tab_startInterface)
        self.line_8.setGeometry(QtCore.QRect(10, 395, 31, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_11 = QtWidgets.QFrame(self.tab_startInterface)
        self.line_11.setGeometry(QtCore.QRect(820, 410, 20, 101))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.spinBox_maxThreadNum = QtWidgets.QSpinBox(self.tab_startInterface)
        self.spinBox_maxThreadNum.setGeometry(QtCore.QRect(670, 440, 61, 22))
        self.spinBox_maxThreadNum.setMinimum(1)
        self.spinBox_maxThreadNum.setMaximum(10)
        self.spinBox_maxThreadNum.setProperty("value", 3)
        self.spinBox_maxThreadNum.setObjectName("spinBox_maxThreadNum")
        self.label_41 = QtWidgets.QLabel(self.tab_startInterface)
        self.label_41.setGeometry(QtCore.QRect(580, 440, 81, 21))
        self.label_41.setObjectName("label_41")
        self.textEditLog = QtWidgets.QTextEdit(self.tab_startInterface)
        self.textEditLog.setGeometry(QtCore.QRect(0, 10, 781, 371))
        self.textEditLog.setObjectName("textEditLog")
        self.tabWidget_fullInterface.addTab(self.tab_startInterface, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_fullInterface.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "抖音短视频下载"))
        self.pushButton_startRun.setText(_translate("MainWindow", "开始运行"))
        self.label_37.setText(_translate("MainWindow", "运行控制"))
        self.pushButton_stopRun.setText(_translate("MainWindow", "停止运行"))
        self.label_41.setText(_translate("MainWindow", "线程个数"))
        self.tabWidget_fullInterface.setTabText(self.tabWidget_fullInterface.indexOf(self.tab_startInterface),
                                                _translate("MainWindow", "启动界面"))
