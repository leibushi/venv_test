# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:57
# @Author  : Mqz
# @FileName: def_tall_1.py
x =abs(-2)
print(x)

# 函数本身可以赋值给变量，即：变量可以执行函数
f = abs
print(f)
# 成功！说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x, y, f):
    print(f(x) + f(y))
    return f(x) + f(y)

add(-5, 6, f)
add(-5, 6, abs)

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
res = list(r)
print(res)

# 还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
ress = list(map(str, [1, 2, 3, 4, 5, 6, 7]))
print(ress)


from functools import reduce

def add(x, y):
    return x + y

ress = reduce(add, [1, 3, 5, 7, 9])
print(ress)

# 也可以使用内建函数sum()
# 把【1，2， 3， 4， 5】
def fn(x, y):
    print("x", x, "y", y)
    return x * 10 + y
ress2 = reduce(fn, [1, 3, 5, 7, 9])
# print(ress2)

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

from functools import reduce

def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
    print("index", s)
    return digits[s]

print(reduce(fn,map(char2num, "13579")))

digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))
print('str 13579',str2int("13579"))

#  还可以用lambda函数进一步简化成：
from functools import reduce
digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

def char2num(s):
    return digits[s]

def str2int1(s):
    res = reduce(lambda x, y: x * 10 + y, map(char2num, s))
    print(res)
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

str2int1("13579")

