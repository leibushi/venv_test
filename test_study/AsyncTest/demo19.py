# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 14:46
# @Author  : Mqz
# @FileName: demo19.py
import aiohttp
import asyncio


async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())