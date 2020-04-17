# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 16:41
# @Author  : Mqz
# @FileName: test.py
import requests

url = 'https://dynamic1.scrape.cuiqingcai.com/'
html = requests.get(url).text
print(html)