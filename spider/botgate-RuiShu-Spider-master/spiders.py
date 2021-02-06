# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 17:13
# @Author  : Mqz
# @FileName: spiders.py
import requests

url = "http://www.jsnc.gov.cn/nccqjy/portal.do?method=province_cj_gg_list"

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'JSESSIONID=9E6BA39AD4538ADB862588BDEFD40EB8'
}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
res = response.text.encode('utf8')
ress = bytes.decode(res)
print(ress)

