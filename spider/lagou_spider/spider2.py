# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/22 18:24
# @Author  : Mqz
# @FileName: spider2.py
# 复制代码
# coding:utf-8
import requests
import csv
import time
def data(page):
    s = requests.session()
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
    headers = {
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'User-Agent': "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            'Referer':'https://www.lagou.com/jobs/list_%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='
    }
    form_data = {
            'first': 'true',
            'pn': page,
            'kd': '爬虫工程师'
    }
    url_list = 'https://www.lagou.com/jobs/list_%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='
    s.get(url_list, headers=headers,timeout=3)
    cookie = s.cookies
    response = s.post(url, data=form_data, headers=headers,cookies=cookie,timeout=3)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    job_json = response.json()
    job_list = job_json['content']['positionResult']['result']
    csv_data = []
    for i in job_list:
        job_info = []
        job_info.append(i['positionName'])  # 职位
        job_info.append(i['companyShortName'])  # 公司
        job_info.append(i['salary'])    # 薪资
        job_info.append(i['education'])  # 学历
        job_info.append(i['district'])  # 位置
        job_info.append(i['workYear'])  # 工作经验要求
        job_info.append(i['positionAdvantage'])  # 福利待遇
        csv_data.append(job_info)
    print(csv_data)
    csvfile = open('软件职业.csv', 'a+',encoding='utf-8-sig',newline='')
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
    csvfile.close()
    return csv_data
if __name__ == '__main__':
    a = [('职位','公司','薪资','学历','位置','工作经验要求','福利待遇')]
    csvfile = open('软件职业.csv', 'a+',encoding='utf-8-sig',newline='')
    writer = csv.writer(csvfile)
    writer.writerows(a)
    csvfile.close()
    all_company = []
    for page_num in range(1, 100):
        result = data(page=page_num)
        all_company += result
        print('已抓取{}页, 总职位数:{}'.format(page_num, len(all_company)))
        time.sleep(15)  # 如果速度太快可能被网站识别出爬虫