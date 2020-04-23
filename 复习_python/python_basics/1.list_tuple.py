# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 11:50
# @Author  : Mqz
# @FileName: 1.list_tuple.py


l = [1, 2, 'hello', 'world'] # 列表中同时含有int和string类型的元素
print(l)

tup = ('jason', 22)  # 元组中同时含有int和string类型的元素
print(tup)
# 列表是动态的，长度大小不固定，可以随意地增加、删减或者改变元素（mutable）。
# 而元组是静态的，长度大小固定，无法增加删减或者改变（immutable）。


l = [1, 2, 3, 4]
l[3] = 40  # 和很多语言类似，python中索引同样从0开始，l[3]表示访问列表的第四个元素
print(l)

tup = (1, 2, 3, 4)
# tup[3] = 40  #     tup[3] = 40
# TypeError: 'tuple' object does not support item assignment

print(tup[3])
# print(tup[3] = 40)


print('1'*10)
tup = (1, 2, 3, 4)
new_tup = tup + (5,)  # 创建新的元组new_tup，并依次填充原元组的值
# new_tup = tup + (5, 8)  # 创建新的元组new_tup，并依次填充原元组的值
print(new_tup)

l = [1, 2, 3, 4]
l.append(5)  # 添加元素5到原列表的末尾
print(l)


# 首先，和其他语言不同，Python 中的列表和元组都支持负数索引，-1 表示最后一个元素
# ，-2 表示倒数第二个元素，以此类推。

l = [1, 2, 3, 4]
print(l[-1])

tup = (1, 2, 3, 4)
print(tup[-1])

# 除了基本的初始化，索引外，列表和元组都支持切片操作：

l = [1, 2, 3, 4]
print(l[1:3])  # 返回列表中索引从1到2的子列表


tup = (1, 2, 3, 4)
print(tup[1:3])  # 返回元组中索引从1到2的子元组

print('2'*20)

# 列表和元组都可以随意嵌套：

l = [[1, 2, 3], [4, 5]]  # 列表的每一个元素也是一个列表

tup = ((1, 2, 3), (4, 5, 6))  # 元组的每一个元素也是一个元组

# ：
print('当然，两者也可以通过 list() 和 tuple() 函数相互转换')
print(list((1, 2, 3)))
print(tuple([1, 2, 3]))


print("count(item) 表示统计列表 / 元组中 item 出现的次数。index(item) 表示返回列表 / 元组中 item 第一次出现的索引。list.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。reversed() 和 sorted() 同样表示对列表 / 元组进行倒转和排序，reversed() 返回一个倒转后的迭代器"
      "（上文例子使用 list() 函数再将其转换为列表）；sorted() 返回排好序的新列表。")
l = [3, 2, 3, 7, 8, 1]
# 统计元素出现的次数 3 出现的次数
print(l.count(3))
# 下标值在列表中对应下标数
print(l.index(7))
l1 = [3, 2, 3, 7, 8, 1]
# list.reverse() 和 list.sort() 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。l1.reverse()
print(l1)
# 排序从小到大
l.sort()
print(l)
print('元祖' * 20)
tup = (3, 2, 3, 7, 8, 1)
print(tup.count(3))

print(tup.index(7))

res = list(reversed(tup))
print(res)
tup1 = (3, 2, 3, 7, 8, 1)

# sorted() 返回排好序的新列表。
sorted(tup1)
print(tup1)


print('列表和元组存储方式的差异')
# 前面说了，列表和元组最重要的区别就是，列表是动态的、可变的，
# 而元组是静态的、不可变的。这样的差异，势必会影响两者存储方式。
# 我们可以来看下面的例子：
l = [1, 2, 3]
print(l.__sizeof__())

tup = (1, 2, 3)
print(tup.__sizeof__())

# 你可以看到，对列表和元组，我们放置了相同的元素，但是元组的存储空间，
# 却比列表要少 16 字节。这是为什么呢？
# 事实上，由于列表是动态的，所以它需要存储指针，来指向对应的元素（上述例子中，对于 int 型，8 字节）。
# 另外，由于列表可变，所以需要额外存储已经分配的长度大小（8 字节），这样才可以实时追踪列表空间的使用情况，
# 当空间不足时，及时分配额外空间。

print('查看_空间'*10)

l = []
print(l.__sizeof__())  # 空列表的存储空间为40字节
# 40
l.append(1)
print(l.__sizeof__())
#  加入了元素1之后，列表为其分配了可以存储4个元素的空间 (72 - 40)/8 = 4
l.append(2)
print(l.__sizeof__())
#  由于之前分配了空间，所以加入元素2，列表空间不变
l.append(3)
print(l.__sizeof__())
# 72 # 同上
l.append('4')
print(l.__sizeof__())
# 72 // 同上
l.append(5)
l.__sizeof__()
# 104 // 加入元素5之后，列表的空间不足，所以又额外分配了可以存储4个元素的空间

# 上面的例子，大概描述了列表空间分配的过程。我们可以看到，为了减小每次增加 / 删减操作时空间分配的开销，
# Python 每次分配空间时都会额外多分配一些，这样的机制（over-allocating）保证了其操作的高效性：
# 增加 / 删除的时间复杂度均为 O(1)

print("列表和元祖的性能")
# 通过学习列表和元组存储方式的差异，我们可以得出结论：
# 元组要比列表更加轻量级一些，所以总体上来说，元组的性能速度要略优于列表。

"""
D:\Spider\venv_test>python -m timeit 'x=[1,2,3,4,5,6]'
50000000 loops, best of 5: 6.96 nsec per loop

D:\Spider\venv_test>python -m timeit 'x=(1,2,3,4,5,6)'
50000000 loops, best of 5: 6.94 nsec per loop

"""


print("索引操作")
"""
D:\Spider\venv_test>python -m timeit -s 'x=[1,2,3,4,5,6]' 'y=x[3]'
50000000 loops, best of 5: 6.98 nsec per loop

D:\Spider\venv_test>python -m timeit -s 'x=(1,2,3,4,5,6)' 'y=x[3]'
50000000 loops, best of 5: 6.92 nsec per loop

"""
