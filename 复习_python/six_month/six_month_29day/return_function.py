# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 17:36
# @Author  : Mqz
# @FileName: return_function.py

def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
        # ax = ax + n
    print(ax)
    return ax

# calc_sum(2, 4, 5, 8)
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    # print(sum)
    return sum


f = lazy_sum(1, 3, 5, 18)
f1 = lazy_sum(1, 3, 5, 18)
print(f())  # 27 调用f()才是真正求和的结果
print(f1())  # 27 调用f()才是真正求和的结果
print(f == f1)  # False

# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
def count():
    fs = []
    for i in range(1, 4):
        def f3():
            return i * i
        fs.append(f3)

    return fs
f4, f5, f6 = count()


print(f4())
print(f5())
print(f6())
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

"""
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
"""

def count1():
    def ff(j):
        def g():
            return j * j
        return g

    fs = []
    for i in range(1, 4):
        fs.append(ff(i))
    print(fs)
    return fs

# 缺点是代码较长，可利用lambda函数缩短代码。
ff1, ff2, ff3 = count1()
print(ff1())
print(ff2())
print(ff3())

