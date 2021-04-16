# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 14:41
# @Author  : Mqz
# @FileName: code_standard_2.py
import time
from typing import List, Tuple, Dict

coupons: Tuple[str, str, int] = ("折扣", "新用户", 12)
# message: List[str, str, str, str, str] = ["test", "test2", "test3", "test4", "test5"]
# information: Dict[str: int] = {"writer": 16, "name": 19}

import requests
try:
    resp = requests.get("", timetout=10)
except Exception as e:
    print(e)
else:
    print(resp.status_code)

import math

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def fool(x):
    if x >= 0:
        return math.sqrt(x)
    return None

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

import re
import requests

FILE = "./information.fet"

def open_file(file):
    fil = open(file, "r")
    content = fil.read()
    fil.close()
    return content

def re_extract(content):
    find_object = re.search(r"url=\d+", content)
    find = find_object.group(1)
    return find

def requetst_data(find):
    text = requests.get(find)
    return text

def extract(FILE):
    content = open_file(FILE)
    find = re_extract(content)
    text = requetst_data(find)
    return text

if __name__ == '__main__':
    print(extract(FILE))