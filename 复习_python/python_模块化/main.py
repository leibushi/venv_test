# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 19:02
# @Author  : Mqz
# @FileName: main.py

# main.py

from utils import get_sum
from class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))

# ########## 输出 ##########
#
# 3
# edcba
# abcde