# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/10 16:56
# @Author  : Mqz
# @FileName: selenium_test.py
# 平台
import platform
from os.path import dirname, abspath, join
# 设置环境
from environs import Env
# 记录器
from loguru import logger
# 常用工具，解析
# from proxypool.utils.parse import parse_redis_connection_string


env = Env()
env.read_env()

# definition of flags
IS_WINDOWS = platform.system().lower() == 'windows'
import multiprocessing
import time
if IS_WINDOWS:
    multiprocessing.freeze_support()
def sing():
    print('ing')
    # time.sleep(1.txt)
    
if __name__ == '__main__':
# multiprocessing.freeze_support()

    pool = multiprocessing.Pool(2)
    for i in range(10000000000000):
        pool.apply(sing)


import multiprocessing
import time


def func(msg):
    print('msg: ', msg)
    time.sleep(1)
    print('----')

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=100)
    for i in range(10):
        msg = 'hello world %d' % i
        pool.apply_async(func, (msg, ))

    pool.close()
    pool.join()
# ————————————————
# 版权声明：本文为CSDN博主「xiemanR」的原创文章，遵循 CC 4.txt.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xiemanR/article/details/71700531