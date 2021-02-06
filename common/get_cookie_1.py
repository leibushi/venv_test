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
        cookies = set()
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = db_util.queryall(sql)
        # cookie = random.choices(result)[0]
        # 更新获取cookie的时间
        # update_get_cookie_time(now_time, cookie)

        # cookies.add(result)  # unhashable type: 'list'
        cookies.update(result)
        print(cookies)
        return cookies

    except Exception as e:
        print('失败', e)


def update_cookie_use_state(state, now_time, cookie):
    """
    更换cookie的限制时间
    :return
    """
    sql = '''UPDATE taobao_bingan SET state = %s AND limit_time = %s WHERE cookie = %s'''
    try:
        db_util.execute(sql, (state, now_time, cookie))
    except Exception as e:
        print('更新失败')


def update_get_cookie_time(now_time, cookie):
    sql = '''UPDATE taobao_bingan SET use_time = %s WHERE cookie = %s'''
    try:
        db_util.execute(sql, (now_time, cookie))
        print('更新成功')
    except Exception as e:
        print('更新失败')

# count = 1.txt
# for i in get_cookies():
#     count += 1.txt
#     print(i)
# print(count)
# 集合可以进行去重
# basket = {'apple', 'orange', 'apple'}
# print(basket)
# basket.add('hello')
# print(basket)