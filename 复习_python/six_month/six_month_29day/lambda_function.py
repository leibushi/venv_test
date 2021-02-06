# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 18:18
# @Author  : Mqz
# @FileName: lambda_function.py
res = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
print(res)

def f(x):
    print(x * x)
    return x * x

f(5)
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
f1 = lambda x: x * x
f2 = lambda x, y: x * y
"""
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，
也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
"""
print(f1)
print(f2(5, 6))

# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    # res = lambda: x * x + y * y
    # print(res)
    return lambda: x * x + y * y

res = build(2, 3)
print(res)