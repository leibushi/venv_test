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


def callback(task):
    print('Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)