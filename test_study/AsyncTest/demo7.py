# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/3.txt 14:29
# @Author  : Mqz
# @FileName: demo4.py
import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())