# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 19:30
# @Author  : Mqz
# @FileName: pingduoduo3.py
# import requests
#
# url = "http://mobile.yangkeduo.com/proxy/api/search?pdduid=9529332749915&item_ver=lzqq&source=index&search_met=manual&track_data=refer_page_id,10169_1586777352545_msp8lr1v5u&list_id=kFILIk9nUE&sort=_sales&filter=&q=%E9%9D%A2%E8%86%9C%E5%A5%B3&page=1&size=50&anti_content=0aoAfxvUHycYY9dV_ApSZPVtlaEPBTV6Gv_mpxjabJ2z_vRYsft_aHy3mSkjbQEN75HiPAUzWgPrPxr2VtJtt2cjuoIM7licqZ3IwE9r9uSo8d9uc4xkCQJsSfhS9YARzqdunBXEnyESuNE2a2rD3xuxNEzpBkRS1It78ALkAD6C-H8pXJp6Okes-wKOi_H44thJBdOtZj1dMBoUwfiJ3S51OtVj5QdgvBfIut2lHf103ONHyn-uwsonbEV78zxhPSqzD1SH3sp7MFvoEGgpe-H-ACdWXEGGjuqLM6VFutFF24IJNAaOY6ZYgzEjPL5-sZMfI1G_fexvjpqznbvDoUujupLaaMEoFbkbUTd39ccRJT2A92sy9eD5NOCixOJ9zQi8n9O-N5dwO_jddlRiMh2PwCbE2OBpER897Cfd3ggPdAB639CX9M-ql63p0W0U9di086SVi9A79TOjkoykNEj74jkrZN99_HcpLfyG9pIEUy7uZunzN-xv03nskwIiVOFm51aIpjFFiA4pLVR6suuD01kk_cLaJW5UJRLZSCpIIqMTeGOtElSxsGAuEZ-kxDvGT8KwGFCXyDgBoqHobOxub16y8f2I3uJqBwiOKP0q3pbzVrlwZu02yO7bAWG_fWMpD1cDOXWfg3f7ga7gUrqXWDrmgE-w85oDMdjQ4tlDRWNV9X0s5QORbJfQPsbRe2ZCb1-JvZdPCxATvER6m_6RAOGcrihpKAIe7NYWf3QA8Q7RTYYAOAF"
#
# payload = {}
# headers = {
#   'Connection': 'keep-alive',
#   'Pragma': 'no-cache',
#   'Cache-Control': 'no-cache',
#   'Accept': 'application/json, text/plain, */*',
#   'DNT': '1',
#   'AccessToken': 'HCIHJ7WYM6O5H7NC4ZEHFXC2VCWYPKXQKSXLUN7QBAKAKFWL6NLQ1125b87',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
#   'Referer': 'http://mobile.yangkeduo.com/search_result.html?search_key=%E9%9D%A2%E8%86%9C%E5%A5%B3&source=index&options=1&search_met_track=manual&refer_page_el_sn=99884&bui_search_id=1586777350931&refer_page_name=login&refer_page_id=10169_1586777352545_msp8lr1v5u&refer_page_sn=10169',
#   'Accept-Encoding': 'gzip, deflate',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Cookie': '_nano_fp=Xpdjnq9jX5TanpPxnC_39pz0DCEMD754YsQVh0nR; api_uid=CiHBjV6BeYOwxwBEKRpTAg==; ua=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F78.0.3904.108%20Safari%2F537.36; webp=1; PDDAccessToken=HCIHJ7WYM6O5H7NC4ZEHFXC2VCWYPKXQKSXLUN7QBAKAKFWL6NLQ1125b87; pdd_user_id=9529332749915; pdd_user_uin=GN3ACI2XKXVKLVL6DVC4V657WM_GEXDA; JSESSIONID=FE8F7A01035B001F127BF3B4C297EFB0',
#   'Cookie': 'JSESSIONID=40A03C053745C7610C44EBDFE76B0F1F'
# }
# s = requests.session()
# response = s.get(url, headers=headers, data = payload)
#
# print(response.text.encode('utf8'))
# SoSPIUxjCcis2g9Vvd0OIA
#
# import requests
#
# url = "http://mobile.yangkeduo.com/proxy/api/search?pdduid=9529332749915&is_back=1&item_ver=lzqq&source=index&search_met=manual&track_data=refer_page_id,10169_1586777749902_3gruqy52j7&list_id=4hA5HE3ziR&sort=_sales&filter=&q=%E9%9D%A2%E8%86%9C%E5%A5%B3&page=1&size=50&anti_content=0aoAfxvUONcYq9daFY7n46i_naaCe4s_GvfPLBplPO2gAIkZSK_DzPs25AwULZnsiuQgJAOAodcA99AUUA9ufhgGHg8aiWpLRHUMinA0o0J4qx4iVx4gSPK3PX6wOmMYuNANiL9DQULyDK3evFbBdUFq9YhvKFPjOtXxNa12tR5ntasYxKOK5K7Dj3UpBo4ErPXn5kBO56a0urqjXZEdBnP5dnMYfwO6EO9sS-JBf_vF-7w2BwoJr3s0M7nJxqPAusxnk5sdOwVavmZs4KHZS9a88uhxo7Qwk0tF_ac1qPf44EA4oMyhEQccPaVl8wzuDhAdQhHJ0DmavL29xdDhDz33e94m2i1O9RCqqLSMEQMdPKM5-mLVQZl3qGHXKANhgM87uiytuZ2kuT6No2J97lsQlaCxCwykP_KF8447uHz_uweFbB64DCGy8Bh3XSFLrSlhsV8o3R2035sN8Fbte7Zs5dajK76kv-PyjVYR2su8N6w4_flj0YPteUfnlWav5IuTrl1dctqZBe_za3-f5gfwDcq3zGiWhikW_hZIna0MYpuuXl8ZBnZYY6q1qvDVg3P33Xphc_yL9fmUJ2NcBFjp3hU7dsqhy5MsovAitmHvlHS6JRN3c5Ik0EiiR4OYZnx8nBORMWkVh7_RGiW2VL01M8P1XYmaNLcFv0osQGjxdZAv0QFGkqKFJvNWMZdG7Xr79726aeA8vP"
#
# payload = {}
# headers = {
#   'Connection': 'keep-alive',
#   'Pragma': 'no-cache',
#   'Cache-Control': 'no-cache',
#   'Accept': 'application/json, text/plain, */*',
#   'AccessToken': 'TH5ZPXJ4JPO6SZO4SOCNDPSCBBMFLT6YDLIXBUC5626GJD3ZX5JA1125b87',
#   'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
#   'VerifyAuthToken': 'r8_eQVljaBispoOUtN5Wog',
#   'Referer': 'http://mobile.yangkeduo.com/search_result.html?search_key=%E9%9D%A2%E8%86%9C%E5%A5%B3&source=index&options=1&search_met_track=manual&refer_page_el_sn=99884&refer_page_name=login&refer_page_id=10169_1586777749902_3gruqy52j7&refer_page_sn=10169&list_id=4hA5HE3ziR&flip=20%3B4%3B0%3B0%3B7068210d-f552-4c5c-b927-4aad8573cb83&page_id=10015_1586777779200_pb394g6nd5&is_back=1',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Cookie': 'api_uid=CiSpKl6T/HYT2wBOkfm0Ag==; _nano_fp=XpdJn5m8nqmxn0T8X9_lqbmDD8pOZCKDjRvptC1P; ua=Mozilla%2F5.0%20(iPhone%3B%20CPU%20iPhone%20OS%2013_2_3%20like%20Mac%20OS%20X)%20AppleWebKit%2F605.1.15%20(KHTML%2C%20like%20Gecko)%20Version%2F13.0.3%20Mobile%2F15E148%20Safari%2F604.1; webp=1; PDDAccessToken=TH5ZPXJ4JPO6SZO4SOCNDPSCBBMFLT6YDLIXBUC5626GJD3ZX5JA1125b87; pdd_user_id=9529332749915; pdd_user_uin=GN3ACI2XKXVKLVL6DVC4V657WM_GEXDA; JSESSIONID=320A2282F6F4DA9591E5D548D6AEB6F8',
#   'Cookie': 'JSESSIONID=77AAEF03B88A474B9E205C1DC0EC31DD'
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# print(response.text.encode('utf8'))
# res = response.text.encode('utf8')
# ress = bytes.decode(res)
# print(ress)
import requests

url = "http://mobile.yangkeduo.com/proxy/api/search?pdduid=9529332749915&is_back=1&item_ver=lzqq&source=index&search_met=manual&track_data=refer_page_id,10169_1586777749902_3gruqy52j7&list_id=4hA5HE3ziR&sort=_sales&filter=&q=%E9%9D%A2%E8%86%9C%E5%A5%B3&page=2&size=50&anti_content=0aoAfxvUUNhYq9EaFy8kgQ9CwH6UPag1UYkZe8gkTxtdnuzpfw1gxHocgwlJ5eAM0Rn6NIcgx9VaPg56b4Q9A-joJLCCNR758LhPN-QlaY9JBNo6y3B7D0DLP4NLqN2sNkIuSc4qCbXbMRZcZbABgkk2yPfWmlqw_tZfOW0Q0d1omHoNUOwnkIzJqKvIj3UwBorDmoYnOPBK5ejnuWwjs9Ddjy9O_lIvivnBTKQeKsENRtZFMFzAkw8Xbjtj1NG6ZeAxIlB1yJKb1GY4LJThF2iF7-XckbNzrbJt5xvGjwjzbzwwq2a-giS3RpDeplBpuNkFXyxTrjGR-jJODj4AYKzN7Dd5CmdC6OTavY9W8v2eozATZ-AcXw-fc3LOUHamm8MniDOjpEKjPvaY9v897CBdJdmDB6t2GvSCtUpmEfOYawwoG9N0aaXo2jJ00OezxbbzRDCAI-nJ_hJ9zhaDeKW_1zJT7zXNcvKMBWZfw1AhUW7QpSbTrpxjoHVfwl2K5qm_cm6ks9d_MododpzVSlKpMw4YWLUA0eNA85nhVeVUViC03tHjHm8Ztv58dGp1bCnTHWguOgeMRn_OCkjpH9V8spLbY7Yf1lK-x8puEeML5MqypfPwxl8lQUrMPoc8MYK3ZgbDA--RMWkVlvmRLiW2VL4SMM91XUHxNq-_ZVJ06Mqk45QZSFxeHDaKb-bl5KfbZUAG0qhGy898CU&flip=20%3B0%3B0%3B0%3Ba4903450-2b50-4360-8a1a-66f930d699a2"

payload = {}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Accept': 'application/json, text/plain, */*',
  'AccessToken': 'TH5ZPXJ4JPO6SZO4SOCNDPSCBBMFLT6YDLIXBUC5626GJD3ZX5JA1125b87',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'VerifyAuthToken': 'r8_eQVljaBispoOUtN5Wog',
  'Referer': 'http://mobile.yangkeduo.com/search_result.html?search_key=%E9%9D%A2%E8%86%9C%E5%A5%B3&source=index&options=1&search_met_track=manual&refer_page_el_sn=99884&refer_page_name=login&refer_page_id=10169_1586777749902_3gruqy52j7&refer_page_sn=10169&list_id=4hA5HE3ziR&flip=20%3B0%3B0%3B0%3Ba4903450-2b50-4360-8a1a-66f930d699a2&page_id=10015_1586777779200_pb394g6nd5&is_back=1&sort_type=_sales&price_index=-1&filter=',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'api_uid=CiSpKl6T/HYT2wBOkfm0Ag==; _nano_fp=XpdJn5m8nqmxn0T8X9_lqbmDD8pOZCKDjRvptC1P; ua=Mozilla%2F5.0%20(iPhone%3B%20CPU%20iPhone%20OS%2013_2_3%20like%20Mac%20OS%20X)%20AppleWebKit%2F605.1.15%20(KHTML%2C%20like%20Gecko)%20Version%2F13.0.3%20Mobile%2F15E148%20Safari%2F604.1; webp=1; PDDAccessToken=TH5ZPXJ4JPO6SZO4SOCNDPSCBBMFLT6YDLIXBUC5626GJD3ZX5JA1125b87; pdd_user_id=9529332749915; pdd_user_uin=GN3ACI2XKXVKLVL6DVC4V657WM_GEXDA; JSESSIONID=2CC328F2B4829510ED3D085669540A81',
  'Cookie': 'JSESSIONID=5252C19ACC9660493E1A85EDCF9B498C'
}
r = requests.session()
# response = r.get("GET", url, headers=headers, data = payload)
response = r.get(url, headers=headers, data = payload)

print(response.text.encode('utf8'))

