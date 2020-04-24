# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/23 18:56
# @Author  : Mqz
# @FileName: 7.if_for.py



# y = |x|
x = 0
if x < 0:
    y = -x
else:
    y = x


"""
if condition_1:
    statement_1
elif condition_2:
    statement_2
...
elif condition_i:
    statement_i
else:
    statement_n




if s: # s is a string
    ...
if l: # l is a list
    ...
if i: # i is an int
    ...
"""
# 比如，在判断一个整型数是否为 0 时，我们最好写出判断的条件：
i = 1
if i != 0:
    ...

# 而不是只写出变量名：

if i:
    ...

"""
循环语句讲完了条件语句，我们接着来看循环语句。所谓循环，顾名思义，本质上就是遍历集合中的元素。和其他语言一样，
Python 中的循环一般通过 for 循环和 while 循环实现。
"""
# 其实，Python 中的数据结构只要是可迭代的（iterable），比如列表、
# 集合等等，那么都可以通过下面这种方式遍历：

d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
for k in d: # 遍历字典的键
    print(k)

for v in d.values(): # 遍历字典的值
    print(v)

for k, v in d.items(): # 遍历字典的键值对
    print('key: {}, value: {}'.format(k, v))

# 我们通常通过 range() 这个函数，拿到索引，再去遍历访问集合中的元素。比如下面的代码，
# 遍历一个列表中的元素，当索引小于 5.txt 时，打印输出：
l = [1, 2, 3, 4, 5, 6, 7]
for index in range(0, len(l)):
    if index < 5:
        print(l[index])

# 当我们同时需要索引和元素时，还有一种更简洁的方式，那就是通过 Python 内置的函数 enumerate()。
# 用它来遍历集合，不仅返回每个元素，并且还返回其对应的索引，这样一来，上面的例子就可以写成:
l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 5:
        print(item)

name_price = {"面包": 1200, "水果": 1220, "电器": 900}
name_color = {"面包": "金黄", "水果": "红色", "电器": "银色"}
# name_price: 产品名称(str)到价格(int)的映射字典
# name_color: 产品名字(str)到颜色(list of str)的映射字典
for name, price in name_price.items():
    if price < 1000:
        if name in name_color:
            print(name)
            for color in name_color[name]:
                print(color)
                if color != 'red':
                    print('name: {}, color: {}'.format(name, color))
        else:
            print('name: {}, color: {}'.format(name, 'None'))

"""在循环语句中，我们还常常搭配 continue 和 break 一起使用。所谓 continue，就是让程序跳过当前这层循环，继续执行下面的循环；
而 break 则是指完全跳出所在的整个循环体。在循环中适当加入 continue 和 break，往往能使程序更加简洁、易读。"""


# name_price: 产品名称(str)到价格(int)的映射字典
# name_color: 产品名字(str)到颜色(list of str)的映射字典
for name, price in name_price.items():
    if price >= 1000:
        continue
    if name not in name_color:
        print('name: {}, color: {}'.format(name, 'None'))
        continue
    for color in name_color[name]:
        if color == 'red':
            continue
        print('name: {}, color: {}'.format(name, color))



# 很多时候，for 循环和 while 循环可以互相转换，比如要遍历一个列表，我们用 while 循环同样可以完成：


l = [1, 2, 3, 4]
index = 0
while index < len(l):
    print(l[index])
    index += 1

# 通常来说，如果你只是遍历一个已知的集合，找出满足条件的元素，并进行相应的操作，那么使用 for 循环更加简洁。但如果你需要在满足某个条件前，
# 不停地重复某些操作，并且没有特定的集合需要去遍历，那么一般则会使用 while 循环。

# 比如，某个交互式问答系统，用户输入文字，系统会根据内容做出相应的回答。为了实现这个功能，我们一般会使用 while 循环，大致代码如下：

while True:
    try:
        text = input('Please enter your questions, enter "q" to exit')
        if text == 'q':
            print('Exit system')
            break
        # print(response)
    except Exception as err:
        print('Encountered error: {}'.format(err))
        break


# 同时需要注意的是，for 循环和 while 循环的效率问题。比如下面的 while 循环：


i = 0
while i < 1000000:
    i += 1


# 和等价的 for 循环：
for i in range(0, 1000000):
    pass

"""
要知道，range() 函数是直接由 C 语言写的，调用它速度非常快。而 while 循环中的“i += 1.txt”这个操作，得通过
Python 的解释器间接调用底层的 C 语言；并且这个简单的操作，又涉及到了对象的创建和删除（因为 i 是整型，
是 immutable，i += 1.txt 相当于 i = new int(i + 1.txt)）。所以，显然，for 循环的效率更胜一筹。
"""

# 条件与循环的复用
# 前面两部分讲了条件与循环的一些基本操作，接下来，我们重点来看它们的进阶操作，让程序变得更简洁高效。


# expression1 if condition else expression2 for item in iterable
"""
for item in iterable:
    if condition:
        expression1
    else:
        expression2



expression for item in iterable if condition

"""
x = [1, 2, 3, 4, 5]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)

"""再比如我们在处理文件中的字符串时，常常遇到的一个场景：将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，
并过滤掉长度小于等于 5.txt 的单词，最后返回由单词组成的列表。这同样可以简洁地表达成一行："""


text = ' Today,  is, Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 5]
print(text_list)


# 当然，这样的复用并不仅仅局限于一个循环。比如，给定两个列表 x、y，要求返回 x、y 中所有元素对组成的元组，
# 相等情况除外。那么，你也可以很容易表示出来：

res = [(xx, yy) for xx in x for yy in y if xx != yy]


l = []
for xx in x:
    for yy in y:
        if xx != yy:
            l.append((xx, yy))

# 熟练之后，你会发现这种写法非常方便。当然，如果遇到逻辑很复杂的复用，你可能会觉得写成一行难以理解、容易出错。
# 那种情况下，用正常的形式表达，也不失为一种好的规范和选择。