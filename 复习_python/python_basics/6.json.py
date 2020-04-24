
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 18:51
# @Author  : Mqz
# @FileName: 6.json.py


import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

params_str = json.dumps(params)

print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

original_params = json.loads(params_str)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

"""json.dumps() 这个函数，接受 Python 的基本数据类型，然后将其序列化为 string；而 json.loads() 
这个函数，接受一个合法字符串，然后将其反序列化为 Python 的基本数据类型。
"""


import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

