# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:54
# @Author  : Mqz
# @FileName: blibli_spider.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bilibili_spider.py
# @Author: 未衬

# pip install requests

# 向服务器发送请求的，等服务器响应之后拿到数据
import requests

'''
1. 上哔哩哔哩网站，去找视频资源
    http://vc.bilibili.com/p/eden/rank#/?tab=%E5%85%A8%E9%83%A8
2. 找到资源之后需要做下载
'''

# 请求资源 json xml
# 字典
dict_data = {'name': '未衬'}


def get_json(url):
    # 伪装成浏览器向服务器发送请求 做反爬的 禁止爬虫程序访问自身网站 会禁止你的ip
    # 服务器认定你是一个爬虫程序，拒绝你访问
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    # api 有关键字参数
    params = {
        'page_size': 10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }

    try:
        html = requests.get(url, params=params, headers=headers)
        return html.json()
    except BaseException:
        print('请求失败...')


# 下载函数
def downloader(url, path):
    # 初始化下载视频的大小
    size = 0

    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    # 下载一个视频
    response = requests.get(url, headers=headers, stream=True)

    # 构造下载器
    # 每次下载的数据大小
    chunk_size = 1024

    # 视频总大小
    content_size = int(response.headers['content-length'])
    print(content_size)

    # 文件处理 状态码
    if response.status_code == 200:
        # 响应头的大小单位为字节 MB
        print('[文件大小]：%0.2f MB' % (content_size / chunk_size / 1024))

        # 文件处理
        with open(path, 'wb') as file:
            # 迭代响应数据
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)


if __name__ == "__main__":
    for i in range(10):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url)
        infos = html['data']['items']
        for info in infos:
            # 小视频的标题
            title = info['item']['description']

            # 小视频的资源链接
            video_url = info['item']['video_playurl']

            # 下载操作
            # 为了防止这个视频地址失效产生报错，所以我们需要构建一个异常

            try:
                path = '%s.mp4' % title
                downloader(video_url, path)
                print(title, '下载成功...')
            except Exception:
                print(title, '下载失败...')