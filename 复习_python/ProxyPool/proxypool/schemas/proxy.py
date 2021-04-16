# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 16:36
# @Author  : Mqz
# @FileName: proxy.py
from attr import attrs, attr

@attrs
class Proxy(object):
    """
    proxy schema
    """
    host = attr(type=str, default=None)
    port = attr(type=int, default=None)

    def __str__(self):
        """
        to string, for print
        :return:
        """
        return f'{self.host}:{self.port}'

    def string(self):
        """
        to string
        :return: <host>:<port>
        """
        return self.__str__()

if __name__ == '__main__':
    proxy = Proxy(host='8.8.8.8', port=8888)
    print('proxy', proxy)
    print('proxy', proxy.string())
# class Book(object):
#
#     def __init__(self, isbn, name, author):
#         self.isbn = isbn
#         self.name = name
#         self.author = author
#
#     def __repr__(self):
#         return f"Book({self.isbn}, {self.name}, {self.author})"
#
# @attr.s(auto_attribs=True)
# class Books(object):
#     isbn: str
#     name: str
#     author: str
#     published_year: int
#     edition: int


