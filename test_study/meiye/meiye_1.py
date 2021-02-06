# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/2.txt 9:48
# @Author  : Mqz
# @FileName: meiye_1.py
import requests

url = "https://ai.meiyeyanjiu.com/data/material/del-filter"
# url = "https://ai.meiyeyanjiu.com/data/nmpa/get-nmpa-cosmetics"

# payload = "{\"category\": "null"}"
payload = {"category": "null"}
# payload = {"brandType":1,"pageNo":2,"pageSize":12,"category": "null","cosmeticsType": "null","originPlace": "null","province": "null","brandCountry":"null","beginDateStr":"2014-01-01","endDateStr":"2020-05-19","keywordList":[],"dayInterval":"m3"}
headers = {
  # 'Connection': 'keep-alive',
  # 'Pragma': 'no-cache',
  # 'Cache-Control': 'no-cache',
  # 'Accept': 'application/json, text/plain, */*',
  # 'Sec-Fetch-Dest': 'empty',
  'tk': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ6aGFveWwiLCJzdWIiOiIzNjgiLCJ1c2VyTmFtZSI6Inp5bF9kZXZfbXF6Iiwibmlja05hbWUiOiLmooXlhajmtLIiLCJjb3JwSWQiOjEwMTk1fQ.pms8x230Ti8zKkaaH8SR4IuT_6Nu0wvqPTfM9RbQuE8',
  'User-Agent': 'Mozilla/5.txt.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
  # 'Content-Type': 'application/json;charset=UTF-8',
  # 'Origin': 'https://ai.meiyeyanjiu.com',
  # 'Sec-Fetch-Site': 'same-origin',
  # 'Sec-Fetch-Mode': 'cors',
  # 'Accept-Language': 'zh-CN,zh;q=0.9',
  # 'Cookie': 'mac=8c25b75d63ec735326186de115914a3d; key=ee77d4a19d232b668a6c5e9c2997e5c6; token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ6aGFveWwiLCJzdWIiOiIzNjgiLCJ1c2VyTmFtZSI6Inp5bF9kZXZfbXF6Iiwibmlja05hbWUiOiLmooXlhajmtLIiLCJjb3JwSWQiOjEwMDAwfQ.d2utbVHZHTFjWMQ5mTxPHOAKaPh2mJGhtARfTOcMrvA',
  'Cookie': 'mac=8c25b75d63ec735326186de115914a3d; token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ6aGFveWwiLCJzdWIiOiIzNjgiLCJ1c2VyTmFtZSI6Inp5bF9kZXZfbXF6Iiwibmlja05hbWUiOiLmooXlhajmtLIiLCJjb3JwSWQiOjEwMTk1fQ.pms8x230Ti8zKkaaH8SR4IuT_6Nu0wvqPTfM9RbQuE8'

  # 'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
