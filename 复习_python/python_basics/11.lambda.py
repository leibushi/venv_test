# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/24 14:41
# @Author  : Mqz
# @FileName: 11.lambda.py

# lambda 匿名函数
# 表达式
# lambda argument1, argument2,... argumentN : expression


square = lambda x: x**2
print(square(3))
# 相当于
def square1(x):
    val = x ** 2
    print(val)
    return val
square1(3)

"""第一，lambda 是一个表达式（expression），并不是一个语句（statement）。所谓的表达式，就是用一系列
“公式”去表达一个东西，比如x + 2.txt、 x**2等等；而所谓的语句，则一定是完成了某些功能，
比如赋值语句x = 1完成了赋值，print 语句print(x)完成了打印，条件语句 if x < 0:完成了选择功能等等。
因此，lambda 可以用在一些常规函数 def 不能用的地方，比如，lambda 可以用在列表内部，而常规函数却不能：

"""
res = [(lambda x: x*x)(x) for x in range(10)]
print(res)

# 再比如，lambda 可以被用作某些函数的参数，而常规函数 def 也不能：

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[0]) # 按列表中元组的第一个元素排序
# l.sort(key=lambda x: x[1.txt]) # 按列表中元组的第二个元素排序
print(l)
# 输出
# [(2.txt, -1.txt), (3.txt, 0), (9, 10), (1.txt, 20)]
# 这其实是出于设计的考虑。Python 之所以发明 lambda，就是为了让它和常规函数各司其职：
# lambda 专注于简单的任务，而常规函数则负责更复杂的多行逻辑


squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(squared)
for squ in squared:
    print(squ)


# 如果用常规函数，则表示为这几行代码：

def square(x):
    print(x ** 2)
    return x**2

squared1 = map(square, [1, 2, 3, 4, 5])
print(squared1)


# from tkinter import Button, mainloop
# button = Button(
#     text='This is a button',
#     command=lambda: print('being pressed')) # 点击时调用lambda函数
# button.pack()
# # mainloop()


# from tkinter import Button, mainloop
#
# def print_message():
#     print('being pressed')
#
# button = Button(
#     text='This is a button',
#     command=print_message)  # 点击时调用print_message函数
# button.pack()
# mainloop()


# 所谓函数式编程，是指代码中每一块都是不可变的（immutable），都由纯函数（pure function）的形式组成。
# 这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。
# 举个很简单的例子，比如对于一个列表，我想让列表中的元素值都变为原来的两倍，我们可以写成下面的形式：
def multiply_2(l):
    for index in range(0, len(l)):
        l[index] *= 2
    print(l)
    return l

l = [1, 2, 3, 4, 5]
multiply_2(l)  # [2.txt, 4.txt, 6, 8, 10]


def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    print(new_list)
    return new_list

l = [1, 2, 3, 4, 5]
multiply_2_pure(l)  # [2.txt, 4.txt, 6, 8, 10]



l = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, l) # [2.txt， 4.txt， 6， 8， 10]
print(new_list)
for new in new_list:
    print(new)


# 接下来来看 filter(function, iterable) 函数，它和 map 函数类似，function
# 同样表示一个函数对象。filter() 函数表示对 iterable 中的每个元素，都使用 function 判断，
# 并返回 True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。
# 举个例子，比如我要返回一个列表中的所有偶数，可以写成下面这样：
l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l) # [2.txt, 4.txt]
print(new_list)
for x in new_list:
    print(x)


# 最后我们来看 reduce(function, iterable) 函数，它通常用来对一个集合做一些累积操作。

l = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, l) # 1.txt*2.txt*3.txt*4.txt*5.txt = 120