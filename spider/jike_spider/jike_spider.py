# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/21 16:16
# @Author  : Mqz
# @FileName: jike_spider.py
import requests

url = "https://time.geekbang.org/serv/v1/article"

payload = "{\"id\":\"997\",\"include_neighbors\":true,\"is_freelyread\":true}"
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Accept': 'application/json, text/plain, */*',
  'Origin': 'https://time.geekbang.org',
  'User-Agent': 'Mozilla/5.txt.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
  'DNT': '1.txt',
  'Content-Type': 'application/json',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Referer': 'https://time.geekbang.org/column/article/997',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'gksskpitn=0e039c2f-240b-4b10-9cf5-c6a46df9b27f; LF_ID=1586914271477-2792071-1181915; _ga=GA1.2.txt.796986178.1586914272; GCID=93a2b1b-bed67fd-ede4af0-b70a182; GRID=93a2b1b-bed67fd-ede4af0-b70a182; GCESS=BAQEAC8NAAsCBAAJAQEKBAAAAAAFBAAAAAAMAQECBF5kll4HBHlksqUBBOjuHQADBF5kll4IAQMGBEmJF8c-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1586916957,1586917005,1586917031,1587122583; _gid=GA1.2.txt.1961570946.1587345799; _gat=1.txt; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1587455748|1587452902; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587455750',
  'Content-Type': 'text/plain',
  'Cookie': 'SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1587458183|1587452902'
}

response = requests.request("POST", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

res = response.text.encode('utf8')
ress = bytes.decode(res)

print(ress)
