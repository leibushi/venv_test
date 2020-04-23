# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 17:52
# @Author  : Mqz
# @FileName: 4.python_input_print.py

name = input('your name:')
gender = input('you are a boy?(y/n)')

#### 输入 ####
# your name:Jack
# you aer a boy?

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dict = {
    # 'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}

print('authorizing...')
# **的意思是解包把'prefix': 'Mr... 变成prefix=Mr.., 'name': name变成name=name
print(welcome_str.format(**welcome_dict))



a = input()
# 1
b = input()
# 2

print('a + b = {}'.format(a + b))
########## 输出 ##############
# a + b = 12
print('type of a is {}, type of b is {}'.format(type(a), type(b)))
########## 输出 ##############
# type of a is <class 'str'>, type of b is <class 'str'>
print('a + b = {}'.format(int(a) + int(b)))
########## 输出 ##############
# a + b = 3

"""
Python 对 int 类型没有最大限制（相比之下， C++ 的 int 最大为 2147483647，超过这个数字会产生溢出）
，但是对 float 类型依然有精度限制。这些特点，除了在一些算法竞赛中要注意，在生产环境中也要时刻提防，
避免因为对边界条件判断不清而造成 bug 甚至 0day（危重安全漏洞）。我们回望一下币圈。2018 年 4 月 23 
日中午 11 点 30 分左右，BEC 代币智能合约被黑客攻击。黑客利用数据溢出的漏洞，攻击与美图合作的公司美链
 BEC 的智能合约，成功地向两个地址转出了天量级别的 BEC 代币，导致市场上的海量 BEC 被抛售，该数字货币的价值也几近归零，
 给 BEC 市场交易带来了毁灭性的打击。由此可见，虽然输入输出和类型处理事情简单，但我们一定要慎之又慎。
 毕竟相当比例的安全漏洞，都来自随意的 I/O 处理。

"""