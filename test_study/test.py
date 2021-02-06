# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/1.txt 14:42
# @Author  : Mqz
# @FileName: selenium_test.py
import random
import time
sleep_time = 5 + random.random()
print('开始休息:', sleep_time, '秒')
time.sleep(sleep_time)
import requests
import time
def monirequest(isget=1, url='', header='', data='', i=1):
    try:
       if isget == 1:
           response = requests.get(url, headers=header, timeout=5)
       else:
           response = requests.post(url, headers=header, data=data, timeout=1)
       response.encoding = response.apparent_encoding
       if response.status_code == 200:
           return response.text
    except requests.exceptions.Timeout:
       if i == 1:
           print('请求超时，第%s次重复请求' % i)
           time.sleep(5)
       if i == 2:
           print('请求超时，第%s次重复请求' % i)
           time.sleep(30)
       if i == 3:
           print('请求超时，第%s次重复请求' % i)
           time.sleep(300)
       if i == 4:
           print('请求超时，第%s次重复请求' % i)
           time.sleep(600)
       if i == 5:
           print('请求超时，第%s次重复请求' % i)
           time.sleep(1800)
       if i > 5:
           print('超时退出')
           return -1
       i += 1
       monirequest(isget, url, header, data, i)
    return -1

if __name__ == '__main__':
    result = monirequest(2, "http://www.baidu.com")
    print(result)

a = 624235
b = 622904
c = 405
print(a - b)