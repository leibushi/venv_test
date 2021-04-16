# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 14:15
# @Author  : Mqz
# @FileName: definition_method.py
import re


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    # else:
    #     if not x.isdigit():
    #         print("int")
    #     else:
    #         print("float")

        # raise

    if x > 0:
        print(x)
        return x
    else:
        return -x

my_abs(2.0)

strs = "testsss111"
strs = "1233"
ints = 12323
# if strs.isdigit():
# 检查字符串是否由数字组成
print(strs.isdigit())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(f"{sum}")

calc([1,3,6])
calc((1,3,6))

def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(f"{sum}")

calc_1(1,3,6)

def person(name, age, **kw):
    print("name", name, "age:", age, "kw:", kw)
    # print("name", name, "age:", age, "kw:", **kw)

person("test", 18)
person("test", 18, test="test", tes2=33)

def person_1(name, **kwargs):
    print("name:", name, "kwargs:", kwargs)

person_1("mayun", host=123, cookie="cookies")
heaers = {"cookie": "cookiessssssss"}
person_1("liutao", **heaers)

def person_2(name, age, *, city, job):
    print(name, age, city, job)

person_2('yaya', 20, city=20, job="Engineer1")

def person_3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person_3("test", 30, job='Engineer', city="guangzhou")

url = 'https://mecmor.tmall.com'
if url.endswith('.com'):
    url += '/'
    print(url)
res = re.search('https://(\w.*?)/', url)
print(res)

