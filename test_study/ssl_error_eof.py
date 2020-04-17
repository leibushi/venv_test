# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 10:03
# @Author  : Mqz
# @FileName: ssl_error_eof.py
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context


# This is the 2.11 Requests cipher string, containing 3DES.
CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
    'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
    '!eNULL:!MD5'
)


class DESAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests.
    """
    # 初始化、进程管理池
    def init_poolmanager(self, *args, **kwargs):
        # 创建url上下文 密码、运算
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)
    # 管理代理
    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)

s = requests.Session()
s.mount('https://some-3des-only-host.com', DESAdapter())
r = s.get('https://some-3des-only-host.com/some-path')
print(r.text)
# # ————————————————
# 原文链接：https://blog.csdn.net/haiyanggeng/article/details/81229546