# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 18:45
# @Author  : Mqz
# @FileName: decorator.py
# 装饰器
"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
"""

def log(func):
    # wrapper 装饰器
    def wrapped(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapped

@log
def now():
    print("2015-3-25")

f = now
f()

# 函数有一个__name__属性，可以拿到函数的名字
# res = now.__name__
ress = f.__name__  # wrapped 方法now名变成了wrapped了
# print(res)
print(ress)
"""
现在我们要增加now（）函数的功能，比如，在函数调用前后自动打印日志，但有不希望该now()函数定义
，在运行期间动态增加功能的方式，我们称之为装饰器（Decorator)
观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，
把decorator置于函数的定义处：
调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
"""
def log1(text):
    def decorator(func):
        def wrapped(*args, **kw):
            print("%s %s ():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapped
    return decorator

# 这个3层嵌套的decorator用法如下：
@log1("execute")
def now1():
    print("2020-6-30")


now1()
"""
execute now1 ():
2020-6-30

"和两层嵌套的decorator相比，3层嵌套的效果是这样的：

>>> now = log('execute')(now)"

我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

>>> now.__name__
'wrapper'
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
"""

import functools
# 偏函数
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log3
def now3():
    print("2020-6-28")

now3()
# 打印函数名
print(now3.__name__)


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log4("execute")
def now4():
    print("2020-1688")

now4()
print(now4.__name__)