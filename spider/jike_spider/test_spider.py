# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/21 17:19
# @Author  : Mqz
# @FileName: test_spider.py
import requests

url = "http://127.0.0.1.txt:8888/"

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Upgrade-Insecure-Requests': '1.txt',
  'User-Agent': 'Mozilla/5.txt.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
  'Sec-Fetch-Dest': 'document',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1.txt',
  'Accept-Language': 'zh-CN,zh;q=0.9'
}

response = requests.request("GET", url, headers=headers, data = payload)
res = response.text.encode('utf8')
ress = bytes.decode(res)
"""
#bytes object
    byte = b"byte example"
    # str object
    str = "str example"
    # str to bytes 字符串转字节
    bytes(str, encoding="utf8")
    # bytes to str  字节转字符串
    str(bytes, encoding="utf-8")
    # an alternative method
    # str to bytes  字符串转为字节
    str.encode(str)
    # bytes to str  字节转为字符串
    bytes.decode(bytes)

"""
print(ress)
