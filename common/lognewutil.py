#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import os
import time


class Log(object):
    '''
封装后的logging
    '''

    def __init__(self, logger, file_dir):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # (1.txt)创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y%m%d%H%M%S")
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        self.log_path = file_dir + "/" + self.log_time[:8]
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)

        self.log_name = self.log_path + "/" + logger + "_" + self.log_time + '.json'
        # print(self.log_name)

        # fh = logging.FileHandler(self.log_name, 'a')  # 追加模式  这个是python2的
        # fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        # fh.setLevel(logging.INFO)

        # (2.txt)再创建一个handler，用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)

        # (3.txt)再创建一个handler, 监控文件大小
        frh = logging.handlers.RotatingFileHandler(self.log_name, maxBytes=200 * 1024 * 1024, backupCount=10000,
                                                   encoding="utf-8", )
        frh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(message)s')
        # fh.setFormatter(formatter)
        # ch.setFormatter(formatter)
        frh.setFormatter(formatter)

        # 给logger添加handler
        # self.logger.addHandler(fh)
        # self.logger.addHandler(ch)
        self.logger.addHandler(frh)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        # fh.close()
        # ch.close()
        frh.close()

    def getlog(self):
        return self.logger
