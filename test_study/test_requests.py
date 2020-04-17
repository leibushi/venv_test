# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 18:03
# @Author  : Mqz
# @FileName: test_requests.py
import time
import requests
#
# url_login = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
#
# session = requests.Session()
# session.get(url_login)
#
# token = session.cookies['csrftoken']
# session.post(url_login, data={'csrfmiddlewaretoken': token, 'username': 'guliang21', 'password': '123qwe'})
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
# url_pw = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/'
# try:
#     # timeout=(5, 10) 5连接时间， 超时时间
#     html = session.get(url_pw, timeout=(5, 10)).text
#     print('success')
# except requests.exceptions.RequestException as e:
#     print(e)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 超时重试
#
# 一般超时我们不会立即返回，而会设置一个三次重连的机制。
def gethtml(url):
  i = 0
  while i < 3:
    try:
      html = requests.get(url, timeout=5).text
      return html
    except requests.exceptions.RequestException:
      i += 1


import time
import requests
from requests.adapters import HTTPAdapter
def test():
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    # max_retries
    # 为最大重试次数，重试3次，加上最初的一次请求，一共是4次，所以上述代码运行耗时是20秒而不是15秒
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    try:
        r = s.get('http://www.google.com.hk', timeout=5)
        return r.text
    except requests.exceptions.RequestException as e:
        print(e)
    # 连接超时服务器在指定时间内没有应答
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    # 连接、读取超时
    # 若分别指定连接和读取的超时时间，服务器在指定时间没有应答，抛出 requests.exceptions.ConnectTimeout
    # - timeout=([连接超时时间], [读取超时时间])
    # - 连接：客户端连接服务器并并发送http请求服务器
    # - 读取：客户端等待服务器发送第一个字节之前的时间
    except requests.exceptions.ReadTimeout as e:
        print(e)
    # 3. 未知的服务器
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.ProxyError as e:
        print(e)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))


test()

# 方法二（推荐）：

import ssl
import urllib2

ssl._create_default_https_context = ssl._create_unverified_context
req = urllib2.Request('https://inv-veri.chinatax.gov.cn/')
data = urllib2.urlopen(req).read()
print(data)
# 或者通过捕获警告到日志的方式忽略警告：


import logging
import requests
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)