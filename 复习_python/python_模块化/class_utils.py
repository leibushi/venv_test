# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 19:02
# @Author  : Mqz
# @FileName: class_utils.py

# class_utils.py

class Encoder(object):
    def encode(self, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))