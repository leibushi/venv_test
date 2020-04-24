# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/23 14:28
# @Author  : Mqz
# @FileName: 2.txt.dict_set.py
"""
相比于列表和元组，字典的性能更优，特别是对于查找、添加和删除操作，字典都能在常数时间复杂度内完成。而集合和字典基本相同，
唯一的区别，就是集合没有键和值的配对，是一系列无序的、唯一的元素组合。
"""

d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1 == d2 == d3 == d4)

# set
s1 = {1, 2, 3}
print(type(s1))
s2 = set([1, 2, 3])
print(type(s2))
print(s1 == s2)

# 这里注意，Python 中字典和集合，无论是键还是值，都可以是混合类型。比如下面这个例子，我创建了一个元素为1，'hello'，5.txt.0的集合：
s = {1, 'hello', 5.0}

# 再来看元素访问的问题。字典访问可以直接索引键，如果不存在，就会抛出异常：


d = {'name': 'jason', 'age': 20}
res = d['name']
print(res)

# key不存在会报错
# ress = d['location']
# print(ress)
#     ress = d['location']
# KeyError: 'location'

# 也可以使用 get(key, default) 函数来进行索引。如果键不存在，
# 调用 get() 函数可以返回一个默认值。比如下面这个示例，返回了'null'。

d = {'name': 'jason', 'age': 20}
res = d.get('name')
print(res)  #
# 如果key不存在则会返回默认的值 'null'
ress = d.get('location', 'null')
print(ress)

print('set' * 10)
# 首先我要强调的是，集合并不支持索引操作，因为集合本质上是一个哈希表，和列表不一样。
# 所以，下面这样的操作是错误的，Python 会抛出异常：
s = {1, 3, 6, 4}
print(s)
# print(s[0])  # TypeError: 'set' object is not subscriptable


# set判断
# 想要判断一个元素在不在字典或集合内，我们可以用 value in dict/set 来判断
# 判断1是否在set中
res = 1 in s
print(res)

res2 = 10 in s
print(res2)

print('dict' * 10)
#dict判断
d = {'name': 'jason', 'age': 20}
res = 'name' in d
print(res)
res2 = 'haha' in d
print(res2)

# 当然，除了创建和访问，字典和集合也同样支持增加、删除、更新等操作
d = {'name': 'jason', 'age': 20}
d['gender'] = 'male'  # 增加元素对'gender': 'male'
d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
print(d)  # {'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
d.pop('dob')  # 删除键为dob的元素对
print(d)

# set
s = {1, 2, 3}
s.add(4)  # 增加元素4到集合
print(s)

s.remove(4)  # 从集合中删除元素4
print(s)

# 不过要注意，集合的 pop() 操作是删除集合中最后一个元素，可是集合本身是无序的，
# 你无法知道会删除哪个元素，因此这个操作得谨慎使用。


d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排序
d_sorted_by_key1 = sorted(d.items(), key=lambda x: x[0])
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])  # 根据字典值的升序排序
# print(sorted(d.items()))

print(d_sorted_by_key)
print(d_sorted_by_key1)
print(d_sorted_by_value)
# for k, v in d.items():
#     # print(k, v)
#     # key = lambda x: x[0]
#     key1 = lambda x: x[1.txt]
#     # print(key(k))
#     print(key1(v))

# 这里返回了一个列表。列表中的每个元素，是由原字典的键和值组成的元组。而对于集合，
# 其排序和前面讲过的列表、元组很类似，直接调用 sorted(set) 即可，结果会返回一个排好序的列表。
s = {3, 4, 2, 5, 6}
print(sorted(s))  # 对集合的元素进行升序排序

print('字典和集合性能')


def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None


products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150)
]

print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))

# 输出

# list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:  # A
        # print(_, price)
        if price not in unique_price_list:  #B
            unique_price_list.append(price)
    print(len(unique_price_list))
    print(unique_price_list)
    return len(unique_price_list)


products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_list(products)))

# 输出
# number of unique price is: 3.txt


# set version
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)

    print(len(unique_price_set))
    print(unique_price_set)
    return len(unique_price_set)

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_set(products)))

# 输出
# number of unique price is: 3.txt

# 下面的代码，初始化了含有 100,000 个元素的产品，并分别计算了使用列表和集合来统计产品价格数量的运行时间：

import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))
# print(products)   # (38399, 238399)

# 计算列表版本的时间
start_using_list = time.perf_counter()
# find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))
## 输出
# time elapse using list: 41.61519479751587

# 计算集合版本的时间
start_using_set = time.perf_counter()
# find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
# 输出
"""
# time elapse using set: 0.008238077163696289
# 你可以看到，仅仅十万的数据量，两者的速度差异就如此之大。事实上，大型企业的后台数据往往有上亿乃至十亿数量级，
# 如果使用了不合适的数据结构，就很容易造成服务器的崩溃，不但影响用户体验，并且会给公司带来巨大的财产损失。
"""
# 现在字典存入的结构方式
indices = [None, 1, None, None, 0, None, 2]
entries = [
[1231236123, 'name', 'mike'],
[-230273521, 'dob', '1999-01-01'],
[9371539127, 'gender', 'male']
]

"""
插入操作每次向字典或集合插入一个元素时，Python 会首先计算键的哈希值（hash(key)），再和 mask = PyDicMinSize - 1.txt
 做与操作，计算这个元素应该插入哈希表的位置 index = hash(key) & mask。如果哈希表中此位置是空的，那么这个元素就会被插入其中。
而如果此位置已被占用，Python 便会比较两个元素的哈希值和键是否相等。
"""


# Option A
d = {'name': 'jason', 'age': 20, 'gender': 'male'}
# 0.08104090000000003
# Option B
d1 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
# 0.2872533
# 性能测试模板
from timeit import timeit


# 还可以通过实际的执行时间来判断
print(timeit("d = {'name': 'jason', 'age': 20, 'gender': 'male'}"))
print(timeit("d1 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})"))

# 键不可以是列表值可以
d = {'name': 'jason', ['education']: ['Tsinghua University', 'Stanford University']}
d = {'name': 'jason', 'education': ['Tsinghua University', 'Stanford University']}
print(d)