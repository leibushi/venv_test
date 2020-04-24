# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/2.txt 15:38
# @Author  : Mqz
# @FileName: img_spider.py
import requests
from lxml import etree
import os
from retrying import retry
import time
import random
import threading
from queue import Queue


class AiXjj():
    def __init__(self):
        self.USER_AGENTS = [
            # Opera
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
            "Opera/8.0 (Windows NT 5.txt.1.txt; U; en)",
            "Mozilla/5.txt.0 (Windows NT 5.txt.1.txt; U; en; rv:1.txt.8.1.txt) Gecko/20061208 Firefox/2.txt.0.0 Opera 9.50",
            "Mozilla/4.txt.0 (compatible; MSIE 6.0; Windows NT 5.txt.1.txt; en) Opera 9.50",
            # Firefox
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
            "Mozilla/5.txt.0 (X11; U; Linux x86_64; zh-CN; rv:1.txt.9.2.txt.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.txt.6.10",
            # Safari
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/534.57.2.txt (KHTML, like Gecko) Version/5.txt.1.txt.7 Safari/534.57.2.txt",
            # chrome
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Mozilla/5.txt.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.txt.0 (Windows; U; Windows NT 6.1.txt; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
            # 360
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64; Trident/7.0; rv:11.0) like Gecko",
            # 淘宝浏览器
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.txt.0 Safari/536.11",
            # 猎豹浏览器
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.1.txt (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1.txt LBBROWSER",
            "Mozilla/5.txt.0 (compatible; MSIE 9.0; Windows NT 6.1.txt; WOW64; Trident/5.txt.0; SLCC2; .NET CLR 2.txt.0.50727; .NET CLR 3.txt.5.txt.30729; .NET CLR 3.txt.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.txt.0 (compatible; MSIE 6.0; Windows NT 5.txt.1.txt; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            # QQ浏览器
            "Mozilla/5.txt.0 (compatible; MSIE 9.0; Windows NT 6.1.txt; WOW64; Trident/5.txt.0; SLCC2; .NET CLR 2.txt.0.50727; .NET CLR 3.txt.5.txt.30729; .NET CLR 3.txt.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.txt.0 (compatible; MSIE 6.0; Windows NT 5.txt.1.txt; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            # sogou浏览器
            "Mozilla/5.txt.0 (Windows NT 5.txt.1.txt) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.txt.X MetaSr 1.txt.0",
            "Mozilla/4.txt.0 (compatible; MSIE 7.0; Windows NT 5.txt.1.txt; Trident/4.txt.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.txt.X MetaSr 1.txt.0)",
            # maxthon浏览器
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.txt.4.txt.3.txt.4000 Chrome/30.0.1599.101 Safari/537.36",
            # UC浏览器
            "Mozilla/5.txt.0 (Windows NT 6.1.txt; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.txt.0.3214.0 Safari/537.36",
        ]
        self.base_url = 'https://www.xxxx.com'

    # 实现一个方法，获取随机User-agent的请求头
    def get_request_headers(self):
        headers = {
            'User-Agent': random.choice(self.USER_AGENTS)
        }
        return headers

    # 根据url发起请求
    def get_page_from_url(self, url):
        """根据请求的url，发起请求"""
        try:
            headers = self.get_request_headers()
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
            else:
                pass
        except Exception as e:
            print('请求超时', e)
            return False

    # 根据页面获取列表页的url
    def get_all_page_urls(self):
        """获取所有列表页的url"""
        maxpage = 2
        page_urls = [self.base_url + '/page/{}'.format(page) for page in range(1, maxpage)]
        return page_urls

    # 根据列表页url获取列表页的选集url
    def get_xuanji_url(self, page_url):

        page = self.get_page_from_url(page_url)
        if page == False:
            pass
        else:
            html = etree.HTML(page.text)
            codes = html.xpath('/html/body/div[2.txt]/div[1.txt]/ul/li/a/@href')
            urls = [self.base_url + code for code in codes]
            return urls

    # 根据选集url获取选集的照片url
    def get_pic_url(self, xuanji_url):

        response = self.get_page_from_url(xuanji_url)
        if response == False:
            pass
        else:
            html = etree.HTML(response.text)
            url = html.xpath('//*[@id="content"]/a/img/@src')[0]
            title = html.xpath('/html/body/div[2.txt]/div[1.txt]/h2/text()')[0]
            pic_url = 'https:' + url
            self.save_pic(title, pic_url)
            self.get_next_page_url(html)

    # 根据选集url判断是否有下一页
    def get_next_page_url(self, html):
        if html.xpath('//*[@id="page"]/a[last()]/text()')[0] == '下一页':
            code = html.xpath('//*[@id="page"]/a[last()]/@href')[0]
            self.get_pic_url(self.base_url + code)

    # 根据选集照片的url和选集titlt创建文件夹和保存文件
    def save_pic(self, title, pic_url):

        base_dir = 'D:\download1' + '\{}'.format(title)
        # 如果目录不存在，则新建
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        # 获取图片
        response = self.get_page_from_url(pic_url)
        if response == False:
            pass
        else:
            # 写入图片
            with open(base_dir + '\\' + pic_url.split('/')[-1] + '.jpg', 'wb') as fp:
                fp.write(response.content)
            print(title, pic_url, '保存成功')

    @retry
    def run(self):
        all_page_urls = self.get_all_page_urls()
        for page_url in all_page_urls:
            urls = self.get_xuanji_url(page_url)
            for url in urls:
                self.get_pic_url(url)

if __name__ == '__main__':
    axjj = AiXjj()
    axjj.run()


# 原文链接：https://blog.csdn.net/weixin_43870646/article/details/105176726