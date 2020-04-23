# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 14:55
# @Author  : Mqz
# @FileName: lambda.py


# 这段代码中，lambda num: num% 2是lambda函数。num是参数，num%2是表达式，
# 用来计算后返回结果。该表达式获取输入参数除以2的模数并返回。将5作为参数传入，
# 通过除以2进行计算，得到余数1.
res = lambda num: num % 2
print(res(5))

# 和以下代码相同
def res(num):
    print(num % 2)
    return num % 2

# res(5)

product = lambda x, y : x * y
print(product(3, 4))


def testfunc(num):
    # print(lambda x: x * num)
    return lambda x: x * num

result1 = testfunc(10)
result2 = testfunc(100)
print(result1(9))
print(result2(9))

# Lambda函数可以和Python的内置函数一起使用，例如map（）,filter（）等。
#
# filter() 函数
#
# Python中的filter( )函数接受一个列表参数和一个lambda函数参数。它的语法如下：

# 这里的object必须是一个返回布尔值的lambda函数。对迭代器中的每一项都会调用该函数来计算其结果是True或False。请注意，本函数只能接受一个迭代器作为输入。
#
# lambda函数，和需要被处理的列表，被一同传递给filter( )函数。filter（）函数将返回一个新的列表，新的列表中只包含旧列表中被lambda函数处理后
# 返回值为True的那些元素。请参考下面给出的例子：
# filter(object, iterable)

numbers_list = [2, 4, 5, 6, 7, 18, 22, 44]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
filtered_list2 = list(filter(lambda num: (num < 7), numbers_list))
print(filtered_list)
print(filtered_list2)

# 在上面的例子中，我们先创建了一个包含一系列整数的列表number_list,接着我们创建了一个lambda函数来检查大于7的整数。此lambda函数作为
# 参数传递给filter（）函数，过滤后的结果保存在一个名为filtered_list的新列表中。

# map() 函数
# map( )函数是另一个以一个函数对象和一个列表作为参数的内置函数。map函数的语法如下：
# map(object, iterable_1, iterable_2)

# 传入map（）函数的迭代器可以是字典，列表等。map（）函数主要是根据lambda函数定义的逻辑来将输入迭代器中的每一项映射到输出迭代器中的相关项。
# 请参考以下的例子
numbers_list = [2, 4, 5, 6, 7, 18, 22, 44, 22, 42]
# 返回 [False, False, False, False, False, True, True, True, True, True]
mapped = list(map(lambda num : num > 10, numbers_list))
# [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
mapped1 = list(map(lambda num : num % 2, numbers_list))
print(mapped)
print(mapped1)
# 在上面的脚本中，我们先定义了一个由随机数组成的列表numbers_list,接着我们调用map（）函数，并传递一个lambda函数作为参数。
# 此lambda函数计算每个数除以2之后的余数。映射的结果保存在一个名为mapped_list的列表中。最后，我们打印出列表的内容。