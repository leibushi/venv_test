# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 16:45
# @Author  : Mqz
# @FileName: base.py
from retrying import retry
import requests
from loguru import logger
from proxypool.setting import GET_TIMEOUT

class BaseCrawler(object):
    urls = []
    @retry(stoo_max_attempt_number=3, retry_on_result=function)
    def fetch(self, url, **kwargs):
        try:
            kwargs.setdefault('timeout', GET_TIMEOUT)
            kwargs.setdefault('verify', False)
            response = requests.get(url, **kwargs)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
        except requests.ConnectionError as e:
            return e

    @logger.catch
    def crawl(self):
        """
        crawl main method
        """
        for url in self.urls:
            logger.info(f"fetching {url}")
            html = self.fetch(url)
            for proxy in self.parse(html):
                logger.info(f'fetched proxy {proxy.string()}')