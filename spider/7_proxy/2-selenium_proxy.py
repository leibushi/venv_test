# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 15:12
# @Author  : Mqz
# @FileName: 2-selenium_proxy.py
from selenium import webdriver
import time
proxy = '58.218.200.228:5505'
url = 'http://www.baidu.com'
# chrome = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
# browser = webdriver.Chrome(chrome_options=chrome_options)  # 会有警告提示
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
time.sleep(10)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
req_url = "https://www.instagram.com/accounts/login/"
chrome_options=Options()
#设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
# 开始请求
browser.get(req_url)
#打印页面源代码
print(browser.page_source)
#关闭浏览器
browser.close()
#关闭chreomedriver进程

# https://blog.csdn.net/weixin_43870646/article/details/99310613