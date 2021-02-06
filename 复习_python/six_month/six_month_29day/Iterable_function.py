# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:19
# @Author  : Mqz
# @FileName: Iterable_function.py

from collections.abc import Iterable
# 可迭代对象
res = isinstance([], Iterable)
print(res)

res1 = isinstance({}, Iterable)
print(res1)

res2 = isinstance("abc", Iterable)
print(res2)

res3 = isinstance((x for x in range(10)), Iterable)
print("range", res3)

res4 = isinstance(100, Iterable)
print(res4)
# iterator 迭代器
from collections.abc import Iterator

ress1 = isinstance((x for x in range(10)), Iterator)
print(ress1)
ress2 = isinstance([], Iterator)
print(ress2)

ress3 = isinstance({}, Iterator)
print(ress3)

ress4 = isinstance("abc", Iterator)
print(ress4)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
ress5 = isinstance(iter([]), Iterator)
print(ress5)

ress6 = isinstance(iter([]), Iterator)
print(ress6)

for x in [1, 2, 3, 4, 5]:
    pass

# 等价于
it = iter([1, 2, 3, 4, 5])
# 循环：
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration as e:
        # 遇到StopIteration就退出循环
        break