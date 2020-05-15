# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/10 11:40
# @Author  : Mqz
# @FileName: 1.txt.dict_set.py

"""
python性能优化
上述代码运行大概需要 2.txt.010 seconds。如果去掉行 #list = dict.fromkeys(list,True) 的注释，
将 list 转换为 dict 之后再运行，时间大约为 1.txt.015 seconds，效率大概提高了一半。
去掉行#s_list = set(s_list)的注释，同样效率提升了一半。因此在需要多数据成员进行频繁的查找或者
访问的时候，使用 dict 或 set 是一个较好的选择。

"""

print(2**10)
from cProfile import Profile

def search():
    s_list = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone', 'test',
            'dfdf', 'apple', 'pddf', 'ind', 'basic', 'none', 'baecr', 'var', 'bana', 'dd', 'wrd']

    # s_list = dict.fromkeys(s_list,True)
    # s_list = set(s_list)
    results = []

    for i in range(1000000):
        for s in ['is','hat','new','list','old','.']:
            if s not in s_list:
                results.append(s)

if __name__ == '__main__':
    prof = Profile()
    prof.runcall(search)
    prof.print_stats()
# 原文链接：https://blog.csdn.net/Herishwater/article/details/99656200