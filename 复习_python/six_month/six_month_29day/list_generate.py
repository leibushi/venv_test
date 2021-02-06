# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 11:55
# @Author  : Mqz
# @FileName: list_generate.py

res = list(range(1, 11))
print(res)
# 方法一 太繁琐
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 方法二 简单很多
res2 = [x * x for x in range(1, 11)]
print(res2)

# for循环还可以加上if判断
res3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(res3)

# 可以使用两层循环，可以生成全排列
res4 = [m + n for m in "ABC" for n in "XYZ"]
# 可以生成平行的
res5 = [m + n for m, n in zip("ABC", "XYZ")]
print(res4)
print(res5)

import os
res6 = [d for d in os.listdir(".")]  # os.listdir可以列出文件和目录
print(res6)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
res7 = [k + "=" + v for k, v in d.items()]
print(res7)

L = ['Hello', 'World', 'IBM', 'Apple']

res8 = [s.lower() for s in L]
print(res8)

# 输出偶数
res9 = [x for x in range(1, 11) if x % 2 == 0]
print(res9)

ress = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(ress)
x = "abc"
y = 123
ress1 = isinstance(x, str)
print(ress1)

L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(g)  # 生成器
print(next(g))
for xx in g:
    print(xx)



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

fib(2)


for n in fib(3):
    print(n)


g = fib(5)
while True:
    try:
        x = next(g)
        print("g", x)
    except StopIteration as e:
        print("Generator return value", e.value)
        break