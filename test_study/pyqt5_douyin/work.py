# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/2.txt 15:54
# @Author  : Mqz
# @FileName: work.py
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from ui_main import Ui_MainWindow

import threading
import time
import os
import inspect
import ctypes
import re
from tools import *
from douyin import *

gMaxThreadNum = 2  # 最大线程数目
gWorkingThreadNum = 0

gThreadsList = []  # 存放线程ID

gThreadLock = threading.Lock()  # 获取发帖内容时，需要加锁
gTotalLink = []
gThreadCountLock = threading.Lock()


# @函数介绍：启动多个线程进行发帖
# @返回值： True/False
# @data: 20180803
def mainTask():
    global gMaxThreadNum  # 最大线程个数
    global gWorkingThreadNum  # 正在运行的工作线程的个数
    global gThreadCountLock  # 全局锁
    global gTotalLink
    gWorkingThreadNum = 0

    ipublishIndex = 1
    while True:
        if gWorkingThreadNum < gMaxThreadNum:

            if ipublishIndex > len(gTotalLink):
                printStr('所有任务完成，等待各个子线程完成后，退出........')
                break;
            ipublishIndex = ipublishIndex + 1
            # 启动一个线程
            t = threading.Thread(target=workThread)
            t.start()
            gThreadsList.append(t)

            gThreadCountLock.acquire()
            gWorkingThreadNum = gWorkingThreadNum + 1
            gThreadCountLock.release()

        time.sleep(0.1)
    return True


# @函数介绍： 退出线程
# @返回值： true/false, 成功/失败
# @data: 20180806
def stop_thread(thread):
    tid = thread.ident
    exctype = SystemExit
    ret = True
    """raises the exception, performs cleanup if needed"""

    tid = ctypes.c_long(tid)

    if not inspect.isclass(exctype):
        exctype = type(exctype)

    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))

    if res == 0:
        ret = False
        # raise ValueError("invalid thread id")
        strs = '%s子线程已经退出' % tid
        printStr(strs)

    elif res != 1:

        # """if it returns a number greater than one, you're in trouble,

        # and you should call it again with exc=NULL to revert the effect"""
        ret = False

        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)

        raise SystemError("PyThreadState_SetAsyncExc failed")
    else:
        ret = True
        strs = '%s 线程被Kill' % tid
        printStr(strs)
    return ret


def workThread():
    global gTotalLink
    global gThreadLock
    global gWorkingThreadNum

    gThreadCountLock.acquire()
    video_url = gTotalLink.pop()
    gThreadCountLock.release()

    printStr('video_url:%s' % video_url)
    # video_url = 'http://v.douyin.com/dU2Dsn/'
    handle = douyin()
    downloadUrl, name = handle.downloadUrlGet(video_url)

    if True == os.path.exists(name + '.mp4'):
        name = name + str(randomInt(2)) + '.mp4'
    handle.video_downloader(downloadUrl, name + '.mp4')

    gThreadCountLock.acquire()
    gWorkingThreadNum = gWorkingThreadNum + 1
    gThreadCountLock.release()


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))
    # @类介绍：主类


# @返回值：
# @data: 20180801
class mainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainForm, self).__init__()
        self.setupUi(self)
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # 禁止调整窗口大小
        self.setFixedWidth(848)
        self.setFixedHeight(588)
        # 信号槽，点击开始会去连接startTask
        self.pushButton_startRun.clicked.connect(self.startTask)
        # 信号槽，暂停
        self.pushButton_stopRun.clicked.connect(self.stopTask)
        self.spinBox_maxThreadNum.valueChanged['int'].connect(self.threadNumSet)
        # 编辑内容
        # self.pushButton_editFileContent.clicked.connect(self.editContent)
        # 下面将输出重定向到textEdit中
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
        self.initPara()

    # 编辑内容
    def editContent(self):
        dig = QFileDialog()
        dig.getOpenFileName(self, 'Open file', '', "")

    def initPara(self):
        global gTotalLink
        file = open('需要下载的的链接.txt', 'a+')
        file.close()

        # 读取内容
        file = open('需要下载的的链接.txt', 'r')
        strContent = file.read()
        file.close()
        resultList = re.findall('(?<=###).+?(?=###)', strContent, re.S)
        for item in resultList:
            if '\n' == item:
                pass
            else:
                p = item.find('http')
                item = item[p: item.find(' 复', p)]
                if item == '':
                    continue
                gTotalLink.append(item)
        printStr('gTotalLink:%s' % gTotalLink)

    # @data: 20180801
    def startTask(self):
        global gThreadsList

        if len(gThreadsList) != 0:
            for t in gThreadsList:
                stop_thread(t)
        # 运行主任务

        printStr('开启工作任务...')
        t = threading.Thread(target=mainTask)
        t.start()
        gThreadsList.append(t)

    # @函数介绍： 主函数入口
    # @返回值： 无
    # @data: 20180801
    def stopTask(self):
        global gThreadsList

        for t in gThreadsList:
            stop_thread(t)

        # 清空gThreadsList
        gThreadsList = []

    def threadNumSet(self):
        global gMaxThreadNum
        gMaxThreadNum = self.spinBox_maxThreadNum.value()
        printStr('设置参数->线程个数:%s' % gMaxThreadNum)

        # @函数介绍：接收信号str的信号槽

    # @返回值： 无
    # @data: 20180803
    def outputWritten(self, text):

        self.textEditLog.setReadOnly(True)
        cursor = self.textEditLog.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEditLog.setTextCursor(cursor)
        self.textEditLog.ensureCursorVisible()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainHandle = mainForm()
    mainHandle.show()
    sys.exit(app.exec())

# 原文链接：https: // blog.csdn.net / stefan1240 / article / details / 83185946