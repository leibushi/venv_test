# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 18:45
# @Author  : Mqz
# @FileName: definition_method.py
"""
定义方法
让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
"""
def my_abs(x):
    """
    只允许整数和浮点数类型的参数
    isinstance (a,(str,int,list))    # 是元组中的一个返回 True
    :return
    """
    if not isinstance(x, (int, float)):
    # if not isinstance(x, (int, float, str)):
        raise TypeError("bad operand type")
    if x > 0:
        print(x)
        return x
    else:
        return -x


my_abs(2.0)
a = 3
a1 = "3"
c = isinstance(a, int)
c1 = isinstance(a1, str)
print(c)
print(c1)


# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print("sum", sum)
    return sum
# 但是调用的时候，需要先组装出一个list或tuple：
calc([1, 2, 3])  # list
calc((1, 2, 3))  # tuple
print("*" * 10)
# 如果利用可变参数，调用函数的方式可以简化成这样：
def calc1(*numbers):
    print(numbers)  # (1, 2, 3)
    print(*numbers)  # 1 2 3
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)
    return sum
calc1(1, 2, 3)  # 参数改为可变参数可以1个或者多个
print("666")
calc([1, 2, 3])  # list
calc((1, 2, 3))  # tuple


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个
# 或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print("name", name, "age", age, "other", kw)


person("haha", 30)  # name haha age 30 other {}
person("mayun", 18, city="Bejing")  # name mayun age 18 other {'city': 'Bejing'}
# 方法一
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("mayun", 18, city=extra["city"], job=extra["job"])  # name mayun age 18 other {'city': 'Bejing'}

# 方法二
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("Jack", 28, **extra)
"""
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外
的extra。
"""

# 命名关键字参数
def person1(name, age, **kw):
    if "city" in kw:
        pass
    if "job" in kw:
        pass

    print('name:', name, 'age:', age, 'other:', kw)

person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineerq')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
# person3('Jack', 24, 'Beijing', 'Engineer')

def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person4('Jack', 24, job='Engineer1')



# 参数组合

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a, b, c=0, *, d, **kw):
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)



# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, "a", "b", ["hh"], ("test"))  # 字符串，列表，元祖的类型都是属于可变参数，x=77的形式都是关键字参数
# f1(1, 2, 3, "a", "b", x=99)
f1(1, 2, 3, d=88, x='99')
# # f1(1, 2, c=3)
# print("****" * 10)
# f2(1, 2, d=99, ext=None)
# args = (1, 2, 3, 4)
# kw = {"d": 99, "x": "#"}
# f1(*args, **kw)
# args = {1, 2, 3}
# kw = {"d": 88, "x": "#"}
# f2(*args, **kw)


