# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 11:46
# @Author  : Mqz
# @FileName: __init__.py.py
import pkgutil
from .base import BaseCrawler
import inspect


classes = []
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    for name, value in inspect.getmembers(module):
        globals()[name] = value
        if inspect.isclass(value) and issubclass(value, BaseCrawler) and value is not BaseCrawler \
            and not getattr(value, 'ignore', False):
            classes.append(value)

__all__ = __ALL__ = classes
