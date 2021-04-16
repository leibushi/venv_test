# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 11:10
# @Author  : Mqz
# @FileName: code_standard.py
# 代码规范
import time
# 变量名
import requests

timestamp_tens = int(time.time())
timestamp_thirteen = int(time.time()) * 13
price_unit = ["分", "角", "元"]
numbers = (1, 3, 5, 7, 9)

#  常量名
MAX_NUMBER_THRESHOLD = 50000
EXPIRE = 3600
PRICE_UNIT = ("分", "角", "元")

# 函数名称
def get(): pass
def set(): pass
def take_tickets(): pass
def extract_author(): pass

# 类名
class UserModels(): pass
class ParseException(): pass

# 文件名
# file_storage.py
# components.py

timestamp_thirteen = int(time.time()) * 1000  # 获取 13 位时间戳

# 函数注释
def send(message, host, name):
    """
    将消息推送到指定服务器的指定队列中
    :param message：消息体
    :param host: 服务器地址
    :param name: 队列名称
    :return: 推送消息
    """
    # 消息类型检查与转换
    if isinstance(message, str):
        message = message.encode('utf-8')
    if not isinstance(message, bytes):
        return False
    # result = _send(message, host, name)
    # return result

#     Python 的类型注释以 : 符号为标记，符号前为对象名称，符号后为对象类型，例如：
number: int
name: str
number: int = 1003
name: str = 3600

from typing import Tuple, List, Dict

class FileStorage:
    pass

class DataStorage:
    pass

coupons: Tuple[str, str, int] = ("折扣","新用户专享", 5)
message: List[str, str, str, str, str] = ["大家", "关注", "公众号", "Python 编程", "获取新资料"]
information: Dict[str: str] = {"作者": "haha", "公众号": "Python编程"}
file_storage: FileStorage
data_storage: DataStorage
storage: Dict[str: FileStorage]

# 函数添加类型注释
class FileStorage:
    pass

# 添加了类型注释的代码看起来和静态语⾔代码⾮常接近 传⼊的参数是什么类型、返回的结果是什么类型
# ⼀⽬了然 如果不给 reader 函数添加注释，那么对于调⽤⽅⼩王来说 reader 就是⼀个不透明的盒⼦，只知道要传递
# 参数，返回结果，这样很容易传递类型不正确的值，从⽽造成运⾏时的类型异常。如果给 reader 传递的
# threshold 不是 int 类型就会得到 TypeError 的运⾏时错误。

def reader(name: str, threshold: int = 100) -> FileStorage:
    """
    将消息推送到指定服务器的指定队列中
    :param message：消息体
    :param host: 服务器地址
    :param name: 队列名称
    :return: 推送消息
    """
    file_storage = FileStorage()
    if len(name) > threshold:
        return file_storage
    pass

# funtion_one
def reader1(name: str, path: str, storage: FileStorage, header_line: int = 1, classify:
            str = "csv", threshold: int = 100) -> FileStorage:
    pass

# funtion_two
def reader2(name: str, path: str, storage: FileStorage,
            header_line: int=1, classify: str="csv",
            threshold: int = 100) -> FileStorage:
    pass
# cousumer = (age
#             + height
#             + weight
#             + threshold)

"""test"""

# 正确的规范
import requests
try:
    resp = requests.get("", timeout=10)

except Exception as e:

    print(e)
else:
    print(resp.status_code)

# 控制流语句 正确示范
import math
#  function 1
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None
#  function 2
def foo1(x):
    if x >= 0:
        return math.sqrt(x)
    return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

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

