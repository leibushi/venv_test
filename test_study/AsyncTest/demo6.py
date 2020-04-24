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


coroutine = request()
task = asyncio.ensure_future(coroutine)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('Task Result:', task.result())