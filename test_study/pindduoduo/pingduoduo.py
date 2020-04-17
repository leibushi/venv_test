# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 13:49
# @Author  : Mqz
# @FileName: pingduoduo.py
# import requests
# url = 'http://app.yangkeduo.com/proxy/api/search?pdduid=0&item_ver=lzqq&source=index&search_met=manual&track_data=refer_page_id,10015_1586756738328_q81s7v7uyn&list_id=Gf2RPS1iUY&sort=_sales&filter=&q=%E9%9D%A2%E8%86%9C%E5%A5%B3&page=1&size=50&anti_content=0aoAfxvUHOcYY9dVZApvVv4EHY4Sw64d_1tLWsJW9set9jVvdQdtgFGxHEkliQErhC_7r5Fsv5o90oEDr9IHBB2STzs6_xlq5MRiAD73lZYzC09Gi92InETL42J9NICJBhpGLoRRAggWPuar4jH1hxsSI9rFLmH7merdzAxMxvtxvMVVjL2xyKdmFCFJOzusQlOPoyHx7JONpwKEg-zPuFNkd4F6Kvl_kWX3HGMpKTcitkpbvzdKkz0l8Ahgy3bvm6rjgFEz5Qwt7594quM_ibxJekKENczKARGtdcJrNuRN1WwoHB1Z1-G1zzEy04fwppG7v-Jn0iENpDuVahL7q99N3gPjo2iDSQzB5x2g7NXDPyZ5BYp1qIBtMLijb21wGW9gTxNnIC6oslE4BwSc-LDlOgy9jciwYqubjETEgKyM71gCglJrFOKU8kH_duoHj1zQCkWEXdR5Ifuf9wp1txZD5TlHb_RwQ8asD1OYAddEAf1GUgZZ5UkXWiMn0NBhpo7R288VFBFB41vHEoK3CLQe3l8fLWHBWW5L2Vur3fHN1bCP1HxTkQXZow7X2yC8dfpsI9ZkCaYBEXpc4jLr8aaUufUjrT-KWlGAuRu7TrMiw_GtNrA5jr-ereHuQliSAh18jUssHBqRLCom90qBS26UndQiNgY6oK5KKqWqGpy3zdmfBKh3pCR9nZFy3d'
# res = requests.get(url)
# print(res.text)
# print(res.status_code)

import requests

url = "https://mobile.yangkeduo.com/proxy/api/api/jinbao/h5_weak_auth/goods/query_goods_list_by_opt_id_c_v2?pdduid=0"

payload = "{\"pid\":\"2_126411416\",\"cpsSign\":\"CM_200115_2_126411416_532df979b6f32d755e91de2efc378f02\",\"optId\":-1,\"pageNum\":2,\"pageSize\":10,\"hasCoupon\":null,\"rangeItems\":null,\"listId\":\"1586772889844_c736413c67b8f84d729c314dae2cd98d\",\"recListId\":\"mobile-avengers-cms-mall_-1_rejn0zlmyxflhy26\"}"
headers = {
  'authority': 'mobile.yangkeduo.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accept': 'application/json, text/plain, */*',
  'origin': 'https://mobile.yangkeduo.com',
  'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
  'dnt': '1',
  'content-type': 'application/json;charset=UTF-8',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'referer': 'https://mobile.yangkeduo.com/duo_cms_mall.html?keyword=%E9%9D%A2%E8%86%9C%E5%A5%B3&ddjb_from=pc&pid=2_126411416&cpsSign=CM_200115_2_126411416_532df979b6f32d755e91de2efc378f02&duoduo_type=2&',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': '_nano_fp=Xpdjnq9jX5TanpPxnC_39pz0DCEMD754YsQVh0nR; api_uid=CiHBjV6BeYOwxwBEKRpTAg==; mobile-avengers-cms-mall=rejn0zlmyxflhy26; ua=Mozilla%2F5.0%20(Linux%3B%20Android%205.0%3B%20SM-G900P%20Build%2FLRX21T)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F78.0.3904.108%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=FD8642FF95294ADAE0A6EE07EB2885F1',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

res = response.text.encode('utf8')
print(response.status_code)
ress = bytes.decode(res)
print(ress)
import requests

url = "https://mobile.yangkeduo.com/proxy/api/search_suggest?query=%E9%9D%A2%E8%86%9C%E5%A5%B3&plat=H5&source=10015&search_source=&pdduid=0"

payload = {}
headers = {
  'authority': 'mobile.yangkeduo.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accesstoken': '',
  'dnt': '1',
  'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'accept': '*/*',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'referer': 'https://mobile.yangkeduo.com/duo_cms_mall.html?keyword=%E9%9D%A2%E8%86%9C%E5%A5%B3&ddjb_from=pc&pid=2_126411416&cpsSign=CM_200115_2_126411416_532df979b6f32d755e91de2efc378f02&duoduo_type=2&',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': '_nano_fp=Xpdjnq9jX5TanpPxnC_39pz0DCEMD754YsQVh0nR; api_uid=CiHBjV6BeYOwxwBEKRpTAg==; mobile-avengers-cms-mall=rejn0zlmyxflhy26; ua=Mozilla%2F5.0%20(Linux%3B%20Android%205.0%3B%20SM-G900P%20Build%2FLRX21T)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F78.0.3904.108%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=7E2FA64900D079FBC7B8B096433BB0CE',
  'Cookie': 'JSESSIONID=5FF9EAF3F2803E450FB362B13B514D84'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
res = response.text.encode('utf8')
ress = bytes.decode(res)
print(ress)


