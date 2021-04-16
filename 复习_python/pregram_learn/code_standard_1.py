# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 15:01
# @Author  : Mqz
# @FileName: code_standard_1.py

import time

timestamp_tens = int(time.time())
timestamp_thirteen = int(time.time()) * 13

prict_unit = ["分", "角", "元"]
number = (1, 3, 5, 7, 9)

MAX_NUMBER_THRESHOLD = 50000


import abc
class Save(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass


class MySQLSave(Save):
    def __init__(self):
        # 分类
        self.classify = "mysql"
        pass

    def insert(self):
        pass

    def update(self):
        pass

class Excel(Save):
    def __init__(self):
        self.classify = "excel"

    def insert(self):
        pass

    def update(self):
        pass

class Business:
    def __init__(self, saver):
        self.saver = saver

    def insert(self):
        self.saver.insert()

    def update(self):
        self.saver.update()

if __name__ == '__main__':
    mysql_saver = MySQLSave()
    excel_saver = Excel()
    business = Business(mysql_saver)


import abc
class Save(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass


class MySQLSave(Save):
    def __init__(self):
        self.classify = "mysql"
        pass

    def insert(self):
        pass

    def update(self):
        pass


class Excel(Save):
    def __init__(self):
        self.classify = "excel"

    def insert(self):
        pass

    def update(self):
        pass


class Business:
    def __init__(self, saver):
        self.saver = saver

    def insert(self):
        self.saver.insert()

    def update(self):
        self.saver.update()


if __name__ == '__main__':
    mysql_saver = MySQLSave()
    excel_saver = Excel()
    business = Business(mysql_saver)






