# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 18:32
# @Author  : Mqz
# @FileName: ysq.py
# http://yc.wswj.net/ahsxx/LOL/public/public.html 安徽省雨水情监视
import random
import execjs
import requests
import json

headers = {
    "Referer": "http://yc.wswj.net/ahsxx/LOL/public/water.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
}
data = {
    # "name": "GetSwInfo",
    # "time": "202001171000",
    # "fresh": 0,
    # "waterEncode": "true",
    "name": "2.1ZUdTdEl3Zm4qbw==",
    "time": "2.1MDIwMjUwODA5MTAw",
    "fresh": "2.1KjA=",
    "waterEncode": "2.1cnRldQ==",
    "random": "0.26708501362794057"
}

with open("ysq.js", "r") as f:
    ctx = execjs.compile(f.read())

for k, v in data.items():
    data[k] = ctx.call("waterEncode", v)

data["random"] = random.random()
# print(data)

# url = "http://yc.wswj.net/ahsxx/service/PublicBusinessHandler.ashx"
# url = "http://61.191.22.196:5566/ahsxx/service/PublicBusinessHandler.ashx"
# res = requests.post(url, data=data, headers=headers).text
# # print(res)
# print(type(res))
# data_json = json.loads(res)
# print(data_json)
# data_json = res.json()["data"]
# data = ctx.call("resultDecode", data_json)
# data = json.loads(data)
# print(data[:2])  # 数据共有2000多个，这里只展示两个

import requests

url = "http://61.191.22.196:5566/ahsxx/service/PublicBusinessHandler.ashx"

payload = "name=2.1ZUdTdEl3Zm4qbw%3D%3D&time=2.1MDIwMjUwODA5MTAw&fresh=2.1KjA%3D&waterEncode=2.1cnRldQ%3D%3D&random=0.26708501362794057"
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'http://yc.wswj.net',
  'Referer': 'http://yc.wswj.net/ahsxx/LOL/public/water.html',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  # 'Content-Type': 'text/plain'
}

response = requests.post(url, headers=headers, data = payload).text

# print(response.text.encode('utf8'))
print(response)
json_data = json.loads(response)['data']
# json_data = response.json()['data']
print(type(json_data))

# print(json_data)
data = ctx.call("resultDecode", json_data)
print(data)
# data = json.loads(data)
# print(data[:2])  # 数据共有2000多个，这里只展示两个
