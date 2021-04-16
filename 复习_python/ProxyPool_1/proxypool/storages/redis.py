# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 10:15
# @Author  : Mqz
# @FileName: redis.py
import redis
from proxypool.exceptions import PoolEmptyException
from proxypool.schemas.proxy import Proxy
from proxypool.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY, PROXY_SCORE_MAX,\
    PROXY_SCORE_MIN, PROXY_SCORE_INIF
from random import choice
from typing import List
from loguru import logger
from proxypool.utils.proxy import is_valid_proxy, convert_proxy_or_proxies

REDIS_CLIENT_VERSION = redis.__version__
IS_REDIS_VERSION_2 = REDIS_CLIENT_VERSION.startswith('2.')

class RedisClient(object):
    """
    redis connection client of proxypool
    """
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB, **kwargs):
        """
        init redis client
        :param host: redis host
        :param port: redis port
        :param password: redis password
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True, **kwargs)


    def add(self, proxy: Proxy, score=PROXY_SCORE_INIF) -> int:
        """
        add proxy and set it to init score
        :param proxy: proxy, ip:port, like 8.8.8.8:88
        :param score: int score
        :return result
        """
        if not is_valid_proxy(f'{proxy.host}:{proxy.port}'):
            logger.info(f'invalid proxy {proxy}, throw it')
            return
        
        if not self.exists(proxy):
            if IS_REDIS_VERSION_2:
                return self.db.zadd(REDIS_KEY, score, proxy.string())
            return self.db.zadd(REDIS_KEY, {proxy.string(): score})

    def random(self) -> Proxy:
        """
        get random proxy
        firstly try to get proxy with max score
        if not exists, try to get proxy by rank
        if not exists, raise error
        :return: proxy like 8.8.8.8:88
        """
        proxies = self.db.zrangebyscore(REDIS_KEY, PROXY_SCORE_MAX, PROXY_SCORE_MAX)
        if len(proxies):
            return convert_proxy_or_proxies(choice(proxies))
        
        proxies = self.db.zrevrange(REDIS_KEY, PROXY_SCORE_MIN, PROXY_SCORE_MAX)
        if len(proxies):
            return convert_proxy_or_proxies(choice(proxies))

        raise PoolEmptyException


    def decrease(self, proxy: Proxy) -> int:
        """
        decrease score of proxy, if mall than PROXY_SCORE_MIN, delete it
        :param proxy: proxy
        :return new score
        """
        if IS_REDIS_VERSION_2:
            self.db.zincrby(REDIS_KEY, proxy.string(), -1)
        else:
            self.db.zincrby(REDIS_KEY, -1, proxy.string())
        score = self.db.zscore(REDIS_KEY, proxy.string())
        logger.info(f'{proxy.string()} curent score {score}, remove')
        self.db.zrem(REDIS_KEY, proxy.string())

    def exsts(self, proxy: Proxy) -> bool:
        """
        if proxy exists
        :param proxy: proxy
        :return: if exissts, bool
        """
        return not self.db.zscore(REDIS_KEY, proxy.string()) is None

    def max(self, proxy: Proxy):
        """
        set proxy to max score
        :param proxy:
        :return: new score
        """
        logger.info(f'{proxy.string()} is valid, set to {PROXY_SCORE_MAX}')
        if IS_REDIS_VERSION_2:
            return self.db.zadd(REDIS_KEY,PROXY_SCORE_MAX, proxy.string())
        return self.db.zadd(REDIS_KEY, {proxy.string(): PROXY_SCORE_MAX})


    def count(self) -> int:
        """
        get count of proxies
        :return: count, int
        """
        return convert_proxy_or_proxies(self.db.zrangebyscore(REDIS_KEY, PROXY_SCORE_MIN, PROXY_SCORE_MAX))

    def batch(self, cursor, count) -> List[Proxy]:
        """
        get batch of proxies
        :param oursor: soan cursor
        :param count: soan count
        """
        cursor, proxies = self.db.zscan(REDIS_KEY, cursor, count=count)
        return cursor, convert_proxy_or_proxies([i[0] for i in proxies])

if __name__ == '__main__':
    conn = RedisClient()
    result = conn.random()
    print(result)