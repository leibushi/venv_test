# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 16:20
# @Author  : Mqz
# @FileName: daili66.py
from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = "https://www.66ip.cn/{page}.html"
MAX_PAGE = 5

class Daili66Crawler(BaseCrawler):
    """
    daili 66 crawler, http://www.66ip.con/1.html
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE)]

    def parse(self, html):
        """:param
        """
        doc = pq(html)
        trs = doc('.containerbox table tr:gt (0)').times()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:ntl-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = Daili66Crawler()
    for proxy in crawler.crawl():
        print(proxy)