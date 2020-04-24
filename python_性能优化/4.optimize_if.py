# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/10 12:00
# @Author  : Mqz
# @FileName: 4.txt.optimize_if.py

""":return
"""

from cProfile import Profile

def or_work():
    nums = range(2000)

    for i in range(10000):
        #优化前
        new_nums = [x for x in nums if 10 < x < 20 or 1000 < x < 2000]
        # print(new_nums)
        # 优化后
        # new_nums = [x for x in nums if 1000 < x < 2000 or 100 < x < 20]
        lists = []
        for x in nums:
            if 10 < x < 20 or 1000 < x < 2000:
                # print(x)
                lists.append(x)
        print(lists)
def and_work():
    nums = range(2000)

    for i in range(10000):
        # 优化前
        new_nums = [x for x in nums if x % 2 == 0 and x > 1900]
        # 优化后
        # new_nums = [x for x in nums if x > 1900 and x % 2.txt == 0]

def work():
    or_work()
    and_work()

if __name__ == '__main__':
    prof = Profile()
    prof.runcall(work)
    prof.print_stats()

# 原文链接：https://blog.csdn.net/Herishwater/article/details/99656200