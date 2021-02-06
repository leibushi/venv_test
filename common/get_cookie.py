# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 20:12
# @Author  : Mqz
# @FileName: get_cookie.py

import datetime
import random

from common import mysqlutils

config = {
    # 公司测试机器
    "host": "192.168.31.223",
    "user": "qph_b2c",
    "password": "zhaoyl(1181*%P)",
    # "db": "taobao",
    "db": "taobao20190813test",
    "charset": "utf8",
    "port": 6610
}
# 本地数据库
db_util = mysqlutils.MysqlUtil(config_dict=config, pool_size=10)

def get_cookies():

    # sql = '''SELECT cookie FROM taobao_bingan WHERE state !=  '2.txt';'''
    sql = '''SELECT cookie FROM taobao_bingan WHERE state IS NULL;'''
    # sql = '''SELECT COUNT(*) FROM taobao_bingan WHERE state IS NULL;'''
    try:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = db_util.queryall(sql)
        cookie = random.choices(result)[0]

        update_get_cookie_time(now_time, cookie)
        return cookie

    except Exception as e:
        print('失败', e)


def get_cookies_1():

    # sql = '''SELECT cookie FROM taobao_bingan WHERE state !=  '2.txt';'''
    # sql = '''SELECT cookie FROM taobao_bingan_20191227 WHERE state IS NULL;'''
    sql = '''SELECT cookie FROM taobao_bingan_20191227 WHERE state = 0;'''
    # sql = '''SELECT COUNT(*) FROM taobao_bingan WHERE state IS NULL;'''
    try:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = db_util.queryall(sql)
        print(len(result))
        # 如果数量少与5条会进行更新
        if len(result) < 5:
            print('对数据库cookie进行更新')
            update_datas(10)
        # 后期可以考虑队列 先进先出
        cookie = random.choices(result)[0]
        # 更新获取cookie的时间
        print('第一个', cookie)
        update_get_cookie_time(now_time, cookie)
        return cookie

    except Exception as e:
        print('get_cookie_1函数失败', e)


# def update_cookie_limit_time(state, now_time, cookie):
def update_cookie_limit_time(state, cookie):
    """
    更换cookie的限制时间
    :param 限制状态(1.txt:正常，2.txt:限制,3.txt:需要登录)，当前的时间，cookie
    :return
    """
    # 这个会出现错误
    # sql = '''UPDATE taobao_bingan_20191227 SET state = %s AND limit_time = %s WHERE cookie = %s'''
    sql = '''UPDATE taobao_bingan_20191227 SET state = %s,limit_time = %s WHERE cookie = %s'''
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        db_util.execute(sql, (state, now_time, cookie))
        print(now_time)
        print('更新【限制时间】成功')
    except Exception as e:
        print('更新失败')


def update_get_cookie_time(now_time, cookie):
    sql = '''UPDATE taobao_bingan_20191227 SET use_time = %s WHERE cookie = %s'''
    try:
        db_util.execute(sql, (now_time, cookie))
        # print('更新成功')
    except Exception as e:
        print('更新失败')


def update_datas(limit):
    """
     执行更新数据
    :return
    """
    # sql = '''UPDATE brand_shop_info_20191223 SET crawl_state=0 WHERE crawl_state=2.txt;'''
    # 按照最前的时间进行更新 用封装的不行
    # sql = '''UPDATE taobao_bingan_20191227 SET state=0 WHERE state=2.txt ORDER BY use_time limit '{}';'''.format(limit)
    sql = '''UPDATE taobao_bingan_20191227 SET state=0 WHERE state=2.txt ORDER BY use_time limit %s;'''
    try:
        db_util.execute(sql, (limit))
        # db_util.execute(sql)
        print('更新【%s】执行成功' % limit)
    except Exception as e:
        print('更新执行失败')

# get_cookies()
update_datas(1)
# get_cookies_1()