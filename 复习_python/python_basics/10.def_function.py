# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 10:43
# @Author  : Mqz
# @FileName: 10.def_function.py
"""其中：def 是函数的声明；my_func 是函数的名称；括号里面的 message 则是函数的参数；
而 print 那行则是函数的主体部分，可以执行相应的语句；在函数最后，
你可以返回调用结果（return 或 yield），也可以不返回。总结一下，大概是下面的这种形式：
"""
def find_largest_element(l):
    # 判断l，list是否是一个实例
    if not isinstance(l, list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is: {}'.format(largest_element))


# find_largest_element([8, 1, -3, 2, 0])

# 需要注意，主程序调用函数时，必须保证这个函数此前已经定义过，不然就会报错，比如
"""
my_func('hello world')


def my_func(message):
    print('Got a message: {}'.format(message))

但是，如果我们在函数内部调用其他函数，函数间哪个声明在前、哪个在后就无所谓，因为 def 是可执行语句，
函数在调用之前都不存在，我们只需保证调用时，所需的函数都已经声明定义：

"""


def my_func(message):
    my_sub_func(message)  # 调用my_sub_func()在其声明之前不影响程序执行


def my_sub_func(message):
    print('Got a message: {}'.format(message))


my_func('hello world')

# 另外，Python 函数的参数可以设定默认值，比如下面这样的写法：
def func(param = 0):
    print(param)
# 参数可以传也可以不传
func(10)

# 这样，在调用函数 func() 时，如果参数 param 没有传入，则参数默认为 0；而如果传入了参数 param，
# 其就会覆盖默认值。

"""Python 和其他语言相比的一大特点是，Python 是 dynamically typed 的，可以接受任何数据类型（整型，浮点，字符串等等）
。对函数参数来说，这一点同样适用。比如还是刚刚的 my_sum 函数，我们也可以把列表作为参数来传递，表示将两个列表相连接："""
# my_sub_func([1, 2])
func([1, 3])

"""我们可以看到，Python 不用考虑输入的数据类型，而是将其交给具体的代码去判断执行，同样的一个函数
（比如这边的相加函数 my_sum()），可以同时应用在整型、列表、字符串等等的操作中。
在编程语言中，我们把这种行为称为多态。这也是 Python 和其他语言，比如 Java、C 等很大的一个不同点。当然，Python 这种方便的特性
，在实际使用中也会带来诸多问题。因此，必要时请你在开头加上数据的类型检查。Python 函数的另一大特性，是 Python 支持函数的嵌套。
所谓的函数嵌套，就是指函数里面又有函数，比如
"""


def f1():
    print('hello')
    def f2():
        print('world')

    f2()
f1()
"""这里函数 f1() 的内部，又定义了函数 f2()。在调用函数 f1() 时，会先打印字符串'hello'，
然后 f1() 内部再调用 f2()，打印字符串'world'。你也许会问，为什么需要函数嵌套？这样做有什么好处呢？其实，
函数的嵌套，主要有下面两个方面的作用。第一，函数的嵌套能够保证内部函数的隐私。内部函数只能被外部函数所调用和访问，
不会暴露在全局作用域，因此，如果你的函数内部有一些隐私数据（比如数据库的用户、密码等），不想暴露在外，
那你就可以使用函数的的嵌套，将其封装在内部函数中，只通过外部函数来访问。比如："""

"""
def connect_DB():
    def get_DB_configuration():
        ...
        return host, username, password
    conn = connector.connect(get_DB_configuration())
    return conn

这里的函数 get_DB_configuration，便是内部函数，它无法在 connect_DB()
 函数以外被单独调用。也就是说，下面这样的外部直接调用是错误的："""

# get_DB_configuration()

# 输出 NameError: name 'get_DB_configuration' is not defined

# 第二，合理的使用函数嵌套，能够提高程序的运行效率。我们来看下面这个例子：


def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )
    ...

    def inner_factorial(input):
        # 内部阶乘
        if input <= 1:
            return 1
        print(input)
        print(inner_factorial(input-1))
        # print(input * inner_factorial(input-1))
        return input * inner_factorial(input-1)
    # print(inner_factorial(input))
    return inner_factorial(input)

print('*'*10)


def inner_factorial(input):
    # 内部阶乘
    if input <= 1:
        print('input小于等于{}'.format(input))
        return 1
    # print('input{}'.format(input))
    # 再次调用了inner_factorial函数
    res = input
    val = inner_factorial(res - 1)
    print('其他', val)
    return val
    # return inner_factorial(input-1)
    # print(input * inner_factorial(input-1))
    # return input * inner_factorial(input-1)
# print(factorial(5))
inner_factorial(5)

