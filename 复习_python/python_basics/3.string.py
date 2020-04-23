# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 17:11
# @Author  : Mqz
# @FileName: 3.string.py

# 字符串
# 什么是字符串呢？字符串是由独立字符组成的一个序列，通常包含在单引号（''）双引号（""）或者三引号之中
# （''' '''或""" """，两者一样），比如下面几种写法。
s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)

s = 'a\nb\tc'
print(s)
# 但是会计入长度\n, \t 每一个会计入一个长度
print(len(s))
"""
这段代码中的'\n'，表示一个字符——换行符；'\t'也表示一个字符——横向制表符。
所以，最后打印出来的输出，就是字符 a，换行，字符 b，然后制表符，最后打印字符 c。
不过要注意，虽然最后打印的输出横跨了两行，但是整个字符串 s 仍然只有 5 个元素。

在转义字符的应用中，最常见的就是换行符'\n'的使用。比如文件读取，如果我们一行行地读取，
那么每一行字符串的末尾，都会包含换行符'\n'。而最后做数据处理时，我们往往会丢掉每一行的换行符。
"""

name = 'jason'
res = name[0]
res1 = name[1:3]
print(res)
"""
和其他数据结构，如列表、元组一样，字符串的索引同样从 0 开始，index=0 表示第一个元素（字符），
[index:index+2]则表示第 index 个元素到 index+1 个元素组成的子字符串。
"""
print(res1)
print('*' * 10)
for char in name:
    print(char)

s = 'hello'
# s[0] = 'H'  # TypeError: 'str' object does not support item assignment

s = 'H' + s[1:]
s = s.replace('h', 'H')
print(s)
"""
第一种方法，是直接用大写的'H'，通过加号'+'操作符，与原字符串切片操作的子字符串拼接而成新的字符串。第二种方法，是直接扫描原字符串
，把小写的'h'替换成大写的'H'，得到新的字符串。
"""

str1 = None
str2 = None
# str1 += str2  # 表示str1 = str1 + str2
s = ''
for n in range(0, 100000):
    s += str(n)
    # print(s)


l = []
for n in range(0, 100):
    l.append(str(n))
print("*"*10)
print(l)  # ['0', '1', '2', '3', '4', '5']
l1 = ' '.join(l)
print(l1)  # 0 1 2 3 4 5 6 7 8 9 10 11 12 13

# string.split()

def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding
    data
    """

path = 'hive://ads/training_table'
res = path.split('//')
res1 = path.split('//')[1]
print(res)
print(res1)
namespace = path.split('//')[1].split('/')[0]  # 返回'ads'
table = path.split('//')[1].split('/')[1]  # 返回 'training_table'
data = query_data(namespace, table)
print(table)
print(data)

"""
string.strip(str)，表示去掉首尾的 str 字符串；
string.lstrip(str)，表示只去掉开头的 str 字符串；
string.rstrip(str)，表示只去掉尾部的 str 字符串。
string.find(sub, start, end)，表示从 start 到 end 查找字符串中子字符串 sub 的位置等等
"""

strss = 'hello world'
res = strss.split('h')
res1 = strss.strip('h')  # ello world
res1 = strss.strip('d')  # hello worl
res2 = strss.lstrip('h')  # ello world
print(res)
print(res1)
print(res2)

"""
Python 中字符串使用单引号、双引号或三引号表示，三者意义相同，并没有什么区别。其中，
三引号的字符串通常用在多行字符串的场景。
"""
