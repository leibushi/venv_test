# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/3.txt 14:33
# @Author  : Mqz
# @FileName: demo8.py
import asyncio
import requests
import time

start = time.time()


async def request():
    url = 'https://static4.scrape.cuiqingcai.com/'
    print('Waiting for', url)
    response = requests.get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)