# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 10:31
# @Author  : Mqz
# @FileName: test.py
# def abs(x):
#     if x >= 0:
#         print(x)
#     else:
#         print(-x)
#
# # abs(10)
# abs(-9)

# test = {'score': 0.008533447049558163, 'key': '其他洗护'}, {'score': 0.0007539567886851728, 'key': '其他护肤'}, {'score': 0.00017597497208043933, 'key': '润肤油'}]
# test.sort()
# print(test[-1])

# for tes in test:
#     print(tes)

# for i in test:
#     print(i)
#     for j in i.values():
#         print('test', j)
#         print(i[j])
#         # print({j:j:i[j]}.items())
#
# list = {j:i[j] for i in test for j in i.values()}
# print(list)

# x = [{'a': 3}, {'b': 1}, {'c': 5}]
# x = [{'score': 0.008533447049558163, 'key': '其他洗护'}, {'score': 0.0007539567886851728, 'key': '其他护肤'}, {'score': 0.00017597497208043933, 'key': '润肤油'}]
# lists = {}
# for i in x:
#     print('', i)
#     for j in i.keys():
#     # for j in i.values():
#         print('j', j)
#         print('test', {j:i[j]}.items())

# list = {j:i[j] for i in x for j in i.keys()}.items()
# print(list)

# list_a = sorted(list, reverse=True, key=lambda a:a[1])
# print(list_a)
#
# list_b = [{i[0]:i[1]} for i in list_a]
# print(list_b)

# x = [{'a': 3}, {'b': 1}, {'c': 5}]
#
# list = {j:i[j] for i in x for j in i.keys()}.items()
# print(list)
#
# list_a = sorted(list,reverse=True, key=lambda a:a[1])
# print(list_a)
#
# list_b = [{i[0]:i[1]} for i in list_a]
# print(list_b)

# x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# x = [{'score': 0.008533447049558163, 'key': '其他洗护'}, {'score': 0.0007539567886851728, 'key': '其他护肤'}, {'score': 0.00017597497208043933, 'key': '润肤油'}]

# sorted_x = sorted(x, key=lambda x : x['score'])
# print(sorted_x) #[{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
# sorted_x = sorted(x, key=lambda x : x['score'], reverse=True)
x = [{'score': 0.0007539567886851728, 'key': '其他护肤'}, {'score': 0.008533447049558163, 'key': '其他洗护'}, {'score': 0.00017597497208043933, 'key': '润肤油'}]
# sorted_x = sorted(x, key=lambda x : x['score'])
sorted_xx = sorted(x, key=lambda x: x['score'])
print(sorted_xx[-1])  #[{'age': 39, 'name': 'Homer'}, {'age': 10, 'name': 'Bart'}]
tup = []
for i in x:
    print(i['score'])
    tup.append(i['score'])
print(sorted(tup))

    # print(sorted(i['score']))
# print(sorted_x[0])  #[{'age': 39, 'name': 'Homer'}, {'age': 10, 'name': 'Bart'}]
import hashlib
import time
import base64
from typing import List, Any
import requests

INDEX_URL = 'https://dynamic6.scrape.cuiqingcai.com/api/movie?limit={limit}&offset={offset}&token={token}'
LIMIT = 10
OFFSET = 0

def get_token(args: List[Any]):
    timestamp = str(int(time.time()))
    args.append(timestamp)
    sign = hashlib.sha1(','.join(args).encode('utf-8')).hexdigest()
    return base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')

args = ['/api/movie']
token = get_token(args=args)
index_url = INDEX_URL.format(limit=LIMIT, offset=OFFSET, token=token)
response = requests.get(index_url)
print('response', response.json())

# get_token()