# -*- coding: utf-8 -*-
# author: xu3352<xu3352@gmail.com>
# python3 环境
"""
Python Mysql 工具包
1.txt. 通过 db_config.json 加载数据库配置
2.txt. 常规的增删改查进行封装

注意事项:
1.txt. %s 为 mysql 占位符; 能用 %s 的地方就不要自己拼接 sql 了
2.txt. sql 里有一个占位符可使用 string 或 number; 有多个占位符可使用 tuple|list
3.txt. insertmany 的时候所有字段使用占位符 %s (预编译), 参数使用 tuple|list
4.txt. queryall 结果集只有一列的情况, 会自动转换为简单的列表 参考:simple_list()
5.txt. queryone 结果集只有一行一列的情况, 自动转为结果数据 参考:simple_value()
6. insertone 插入一条数据, 返回数据ID
"""
import json
import os
import traceback

import pymysql.cursors
import pymysqlpool

from common import loggerutils

logger = loggerutils.logger


class MysqlUtil:
    def __init__(self, config_dict=None, pool_size=2):
        self.__config = config_dict
        self.pool_size = pool_size if pool_size and pool_size > 0 else 2
        self.__pool = self.__connect()

    def connect_mysql(self):

        """ 创建链接 """
        try:
            return self.__pool.get_connection()

        except Exception as e:
            logger.error(traceback.format_exc())
        logger.error("cannot create mysql connect")

    def queryone(self, sql, param=None):
        """
        返回结果集的第一条数据
        :param sql: sql语句
        :param param: string|tuple|list
        :return: 字典列表 [{}]
        """
        con = self.connect_mysql()
        cur = con.cursor()

        row = None
        try:
            cur.execute(sql, param)
            row = cur.fetchone()
        except Exception as e:
            con.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))

        cur.close()
        con.close()
        return MysqlUtil._simple_value(row)

    def queryall(self, sql, param=None):
        """
        返回所有查询到的内容 (分页要在sql里写好)
        :param sql: sql语句
        :param param: tuple|list
        :return: 字典列表 [{},{},{}...] or [,,,]
        """
        con = self.connect_mysql()
        cur = con.cursor()

        rows = None
        try:
            cur.execute(sql, param)
            rows = cur.fetchall()
        except Exception as e:
            con.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))

        cur.close()
        con.close()
        return MysqlUtil._simple_list(rows)

    def insertmany(self, sql, arrays=None):
        """
        批量插入数据
        :param sql: sql语句
        :param arrays: list|tuple [(),(),()...]
        :return: 入库数量
        """
        con = self.connect_mysql()
        cur = con.cursor()

        cnt = 0
        try:
            cnt = cur.executemany(sql, arrays)
            con.commit()
        except Exception as e:
            con.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, arrays))

        cur.close()
        con.close()
        return cnt

    def insertone(self, sql, param=None):
        """
        插入一条数据
        :param sql: sql语句
        :param param: string|tuple
        :return: id
        """
        con = self.connect_mysql()
        cur = con.cursor()

        lastrowid = 0
        try:
            cur.execute(sql, param)
            # 一定要在 commit 前，否则会返回 0
            lastrowid = cur.lastrowid
            con.commit()
        except Exception as e:
            con.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))

        cur.close()
        con.close()
        return lastrowid

    def execute(self, sql, param=None):
        """
        执行sql语句:修改或删除
        :param sql: sql语句
        :param param: string|list
        :return: 影响数量
        """
        con = self.connect_mysql()
        cur = con.cursor()

        cnt = 0
        try:
            cnt = cur.execute(sql, param)
            con.commit()
        except Exception as e:
            con.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))

        cur.close()
        con.close()
        return cnt

    @staticmethod
    def _simple_list(rows):
        """
        结果集只有一列的情况, 直接使用数据返回
        :param rows: [{'id': 1.txt}, {'id': 2.txt}, {'id': 3.txt}]
        :return: [1.txt, 2.txt, 3.txt]
        """
        if not rows:
            return rows

        if len(rows[0].keys()) == 1:
            simple_list = []
            # print(rows[0].keys())
            key = list(rows[0].keys())[0]
            for row in rows:
                simple_list.append(row[key])
            return simple_list

        return rows

    @staticmethod
    def _simple_value(row):
        """
        结果集只有一行, 一列的情况, 直接返回数据
        :param row: {'count(*)': 3.txt}
        :return: 3.txt
        """
        if not row:
            return None

        if len(row.keys()) == 1:
            # print(row.keys())
            key = list(row.keys())[0]
            return row[key]

        return row

    def __connect(self):
        try:
            if self.__config:
                load_dict = self.__config
            else:
                config = MysqlUtil._find("db_config.json", os.path.abspath("."))
                if not config:
                    common_path = os.path.dirname(os.path.abspath(__file__))
                    config = MysqlUtil._find("db_config.json", common_path)
                with open(config, "r") as file:
                    load_dict = json.load(file)
            return pymysqlpool.ConnectionPool(size=self.pool_size, cursorclass=pymysql.cursors.DictCursor, **load_dict)

        except Exception as e:
            logger.error(traceback.format_exc())
        logger.error("cannot create mysql pool")

    @staticmethod
    def _find(name, path):
        """ 查找文件路径 """
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)


if __name__ == '__main__':
    print("hello everyone!!!")

    # print("删表:", execute('drop table test_users'))
    db_util = MysqlUtil()
    sql = '''
            CREATE TABLE `test_users` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `email` varchar(255) NOT NULL,
              `password` varchar(255) NOT NULL,
              PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='测试用的, 可以直接删除';
            '''
    print("建表:", db_util.execute(sql))

    # 批量插入
    sql_str = "insert into test_users(email, password) values (%s, %s)"
    arrays = [
        ("aaa@126.com", "111111"),
        ("bbb@126.com", "222222"),
        ("ccc@126.com", "333333"),
        ("ddd@126.com", "444444")
    ]
    print("插入数据:", db_util.insertmany(sql_str, arrays))

    # 查询
    print("只取一行:", db_util.queryone("select * from test_users limit %s,%s", (0, 1)))  # 尽量使用limit
    print("查询全表:", db_util.queryall("select * from test_users"))

    # 条件查询
    print("一列:", db_util.queryall("select email from test_users where id <= %s", 2))
    print("多列:",
          db_util.queryall("select * from test_users where email = %s and password = %s", ("bbb@126.com", "222222")))

    # 更新|删除
    print("更新:", db_util.execute("update test_users set email = %s where id = %s", ('new@126.com', 1)))
    print("删除:", db_util.execute("delete from test_users where id = %s", 4))

    # 查询
    print("再次查询全表:", db_util.queryall("select * from test_users"))
    print("数据总数:", db_util.queryone("select count(*) from test_users"))
