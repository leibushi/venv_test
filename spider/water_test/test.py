# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 19:21
# @Author  : Mqz
# @FileName: test.py
import random, execjs
import pprint

data = {
    "name": "2.1ZUdTdEl3Zm4qbw==",
    "time": "2.1MDIwMjUwNzA5MTAw",
    "fresh": 0,
    "waterEncode": "true"
}

with open('js.js', "r", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


for k, v in data.items():
    data[k] = ctx.call("waterEncode", v)
    

data['random'] = random.random()
pprint.pprint(data)
# print(data['random'] = random.random())

result = ctx.call(data)
print(result)