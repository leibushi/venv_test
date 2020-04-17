# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 9:41
# @Author  : Mqz
# @FileName: guazi_spider.py
import requests

url = "https://www.guazi.com/gz?act=ajaxGetBrand"

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Sec-Fetch-Dest': 'empty',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Referer': 'https://www.guazi.com/gz/',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'antipas=93123893080v6f610q462a; uuid=54c3b4e0-c160-470c-920f-37c07f0f7486; cityDomain=gz; clueSourceCode=%2A%2300; user_city_id=16; ganji_uuid=6243838107057838223727; sessionid=46c533be-4de5-49d8-d2ff-e48c34c59888; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2254c3b4e0-c160-470c-920f-37c07f0f7486%22%2C%22ca_city%22%3A%22gz%22%2C%22sessionid%22%3A%2246c533be-4de5-49d8-d2ff-e48c34c59888%22%7D; close_finance_popup=2020-04-10; preTime=%7B%22last%22%3A1586482490%2C%22this%22%3A1586482437%2C%22pre%22%3A1586482437%7D',
  'Cookie': 'clueSourceCode=%2A%2300; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2254c3b4e0-c160-470c-920f-37c07f0f7486%22%2C%22ca_city%22%3A%22gz%22%2C%22sessionid%22%3A%2246c533be-4de5-49d8-d2ff-e48c34c59888%22%7D'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

