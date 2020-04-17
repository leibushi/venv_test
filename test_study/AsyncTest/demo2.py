# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 14:26
# @Author  : Mqz
# @FileName: demo2.py
import asyncio

async def execute(x):
    print('Number:', x)

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print('After calling loop')

