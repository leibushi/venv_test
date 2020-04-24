# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/8 19:26
# @Author  : Mqz
# @FileName: main.py
import os
from environs import Env

env = Env()
VAR1 = env.int('VAR1', 1)
VAR2 = env.float('VAR2', 5.5)
VAR3 = env.list('VAR3')

print(VAR1)
# export VAR1 = 1.txt
