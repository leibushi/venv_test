# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 18:54
# @Author  : Mqz
# @FileName: qt5_4_alert.py

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 调用setTooltip()创建提示框可以使用富文本格式的内容。
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 创建一个按钮，并且为按钮添加了一个提示框。
        # 调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()
        # 方法提供了一个默认的按钮大小。
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())