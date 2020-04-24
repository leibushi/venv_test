# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/2.txt 15:03
# @Author  : Mqz
# @FileName: proxy_use.py
# socks5代理的使用
import requests
proxy = '127.0.0.1.txt:9742'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy,
}
try:
    url = 'http://httpbin.org/get'
    res = requests.get(url,proxies=proxies)
    print(res.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)



# 方法二全局方法
import requests
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1.txt', 9742)
socket.socket = socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)