# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 11:32
# @Author  : Mqz
# @FileName: usage.py
import requests

proxypool_url = "http://127.0.0.1:5555/random"
target_url = "https://antispider5.scrape.center/"

def get_random_proxy():
    """
    get random proxy from proxypool
    :return proxy
    :param
    """
    return requests.get(proxypool_url).text.strip()


def crawl(url, proxy):
    """
    use proxy to crawl page
    :param proxy: proxy,such as 8.8.8.8:8888
    :return: html
    """
    proxies = {'http': 'http://' + proxy}
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry points
    :return: none
    :param
    """
    proxy = get_random_proxy()
    print('get random proxy', proxy)
    html = crawl(target_url, proxy)
    print(html)

if __name__ == '__main__':
    main()