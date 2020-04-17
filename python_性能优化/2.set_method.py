# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 11:46
# @Author  : Mqz
# @FileName: 2.set_method.py
"""
集合的交集，并集，
"""
from cProfile import Profile
# 交集 包含list1 和list2中共同元素的新集合
def get_intersection():
    list_a = list(range(1000))
    list_b = list(range(1000))

    for i in range(1000):
        intersection = []
        for a in list_a:
            if a in list_b:
                    intersection.append(a)
        intersection = list(set(list_a) & set(list_b))

# 合并 list1 和list2的所有数据集合
def get_union():
    list_a = list(range(1000))
    list_b = list(range(1000))

    for i in range(1000):
        union = []
        union.extend(list_a)
        for b in list_b:
            if b not in list_a:
                union.append(b)
        print(union)
        # union = list(set(list_a) | set(list_b))

# 在list1中出现在不在list2中出现的元素集合
def get_difference():
    list_a = list(range(1000))
    list_b = list(range(1000))

    for i in range(1000):
        difference = []
        for a in list_a:
            if a not in list_b:
                difference.append(a)
        # difference = list(set(list_a) - set(list_b))

def list_operation():
    get_intersection()
    get_union()
    get_difference()

if __name__ == "__main__":
    prof = Profile()
    prof.runcall(list_operation)
    prof.print_stats()

# 原文链接：https://blog.csdn.net/Herishwater/article/details/99656200