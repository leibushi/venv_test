# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 14:45
# @Author  : Mqz
# @FileName: demo17.py
import aiohttp
import asyncio


async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())