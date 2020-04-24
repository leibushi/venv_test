# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/3.txt 14:44
# @Author  : Mqz
# @FileName: demo16.py
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html: {html[:100]}...')
        print(f'status: {status}')


if __name__ == '__main__':
    asyncio.run(main())