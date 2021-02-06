# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 14:54
# @Author  : Mqz
# @FileName: cookies_update.py
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

current_session = requests.session()

browser = webdriver.Chrome()
browser.get("http://www.dianping.com/shop/129879472/photos/tag-%E5%8F%91%E5%9E%8B%E7%A7%80")
time.sleep(3)

cookie = browser.get_cookies()  # 获取浏览器cookies
c = requests.cookies.RequestsCookieJar()
for i in cookie:  # 添加cookie到CookieJar
    c.set(i["name"], i["value"])
current_session.cookies.update(c)  # 更新session里的cookie

res = current_session.get("http://www.dianping.com/shop/129879472/photos/tag-%E5%8F%91%E5%9E%8B%E7%A7%80",
                          headers=headers)

print(res.text)
# 初始化css字典
#
# driver = webdriver.Chrome("/home/nianxiongdi/Downloads/chromedriver")
# driver.get('http://www.dianping.com/shop/129879472/photos/tag-%E5%8F%91%E5%9E%8B%E7%A7%80')
"""
try:
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    # 下一行代码是为了以开发者模式打开chrome
    chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://s.taobao.com/search?q=iPad")
    button = browser.find_element_by_class_name('login-switch')
    button.click()
    button = browser.find_element_by_class_name('weibo-login')
    button.click()
    user_name = browser.find_element_by_name('username')
    user_name.clear()
    user_name.send_keys('*****') #输入微博名 需要事先绑定淘宝
    time.sleep(1)
    user_keys = browser.find_element_by_name('password')
    user_keys.clear()
    user_keys.send_keys('*****') #输入微博密码
    time.sleep(1)
    button = browser.find_element_by_class_name('W_btn_g')
    button.click()
    time.sleep(1)
    cookies = browser.get_cookies()
    ses=requests.Session() # 维持登录状态
    c = requests.cookies.RequestsCookieJar()
    for item in cookies:
        c.set(item["name"],item["value"])
        ses.cookies.update(c)
        ses=requests.Session()
        time.sleep(1)
    print('登录成功')
except:
    print("登录失败")
"""