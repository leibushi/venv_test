# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 17:23
# @Author  : Mqz
# @FileName: def_tall_3.py

# 排序算法
res = sorted([36, 5, -12, 9, -21])
print(res)


res1 = sorted([36, 5, -12, 9, -21], key=abs)
print(res1)
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
#
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一
# 个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
res2 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(res2)
# print()
# 这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
res3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(res3)
# 按照降序排序 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
res4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(res4)

