# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/10 11:56
# @Author  : Mqz
# @FileName: 3.txt.optimize_for.py
"""
优化循环
对循环的优化所遵循的原则是尽量减少循环过程中的计算量，
循环之外能做的事不要放在循环内
"""
from cProfile import Profile

def loop_work():
    list_a = list(range(100))
    list_b = list(range(100))

    len_a = len(list_a)
    len_b = len(list_b)

    #循环优化前
    # for i in range(10000):
    #     for i in range(len(list_a)):
    #         for j in range(len(list_b)):
    #             x = list_a[i] + list_b[j]
    #循环优化后
    for i in range(10000):
        for i in range(len_a):
            x = list_a[i]
            for j in range(len_b):
                x += list_b[j]


if __name__ == '__main__':
    prof = Profile()
    prof.runcall(loop_work)
    prof.print_stats()

# 原文链接：https://blog.csdn.net/Herishwater/article/details/99656200