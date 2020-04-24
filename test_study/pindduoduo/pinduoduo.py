# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/13 19:20
# @Author  : Mqz
# @FileName: pinduoduo.py

import requests

# url = "https://youhui.pinduoduo.com/network/api/goods/common/list"
url = "https://youhui.pinduoduo.com/search/landing?keyword=面膜女"

# payload = {"keyword":"面膜女","sortType":6,"withCoupon":0,"pageNumber":1.txt,"pageSize":60,"crawlerInfo":"0anAfxn5rNIyg9maDie108YJO-00lG9GI_pjda-U1-PIljZctJv8GtNFdUxjoxD7bOnj2iMRVYAhWpWrsLS8WRB69TN4CRACrNLVim9CQXG76wPJ97kOCCAgpx94rmLsbqh4XL3pPmN_ilRLlmRL2L-kGzrqn1j8Kab8IL1HHL_jKeKvRzZ_vvJB3lDfQnx7kkjh6j8XhOOykwhxdTwud6BQKFgfffgMelfPBn28Ml9EbwMG5abLHGw6Da4yIqYBEigrP7Yix_slVjf_PEVbYxKUXgqFX7P97ZnZVoMzUUz4ZjJ76fFCMTbgFo6PEh5dQHrV1uSMp5L8C33OxlYzLHoiognkUYb1oJjqLdMtXl0wWiUj-LoFqUAXmIAJX7FTCe0QtLI84aXQGzOf8VPcm_03mWbLQXfqc8tJ9r-zvv0WfJyvzBrXttXmHd4l-PwR1k7cIsReM44NKh2ueyitUdw7EHZGOuWu3z3UpA1cbG2ITjx1LzT8lupli8D7WhWLurkaMOc"}
headers = {
  'authority': 'youhui.pinduoduo.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accept': 'application/json, text/plain, */*',
  'origin': 'https://youhui.pinduoduo.com',
  'user-agent': 'Mozilla/5.txt.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
  'dnt': '1.txt',
  'content-type': 'application/json; charset=UTF-8',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'referer': 'https://youhui.pinduoduo.com/search/landing?keyword=%E9%9D%A2%E8%86%9C%E5%A5%B3',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': '_nano_fp=XpdJn5m8X5mbnqPxn9_6_9uU64gi4hUq56323KiK; api_uid=rBQQsF6UO4ITbji+XBOIAg==',
  'Content-Type': 'text/plain'
}

# response = requests.request("POST", url, headers=headers, data=payload)
response = requests.request("GET", url, headers=headers,)

# print(response.text.encode('utf8'))
print(response.status_code)
print(response.text)
