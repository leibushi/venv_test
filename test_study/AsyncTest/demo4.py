# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/3.txt 14:29
# @Author  : Mqz
# @FileName: demo4.py
import asyncio


async def execute(x):
    print('Number:', x)
    return x


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

task = asyncio.ensure_future(coroutine)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')