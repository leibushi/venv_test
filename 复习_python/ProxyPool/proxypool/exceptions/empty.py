# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 15:12
# @Author  : Mqz
# @FileName: empty.py
class PoolEmptyException(Exception):
    def __str__(self):
        """
        proxypool is used out
        :return:
        """
        return repr('no proxy is proxypool')
