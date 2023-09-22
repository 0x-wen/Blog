# -*- coding: utf-8 -*-
"""
@author: jw
@contact: 752911233@qq.com
@time: 2020/5/14 19:53
@file: handle_mysql.py
"""
import time

import pymysql
import random
import string


class HandleMysql:
    mysql_oms_database_info = {"host": "xxxx", "user": "root", "password": "xxxxx",
                               "db": "xxxx", "port": 12, "charset": "utf8"}

    def __init__(self):
        self.conn = pymysql.connect(host=self.mysql_oms_database_info["host"],
                                    user=self.mysql_oms_database_info["user"],
                                    password=self.mysql_oms_database_info["password"],
                                    db=self.mysql_oms_database_info["db"],
                                    port=self.mysql_oms_database_info["port"],
                                    charset=self.mysql_oms_database_info["charset"],
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def __call__(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)
        self.conn.commit()

        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()

        return result

    def execute_sql(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    mysql_obj = HandleMysql()
    # select_sql = 'SELECT * FROM `cs3_fu`.sales_flat_order WHERE `increment_id`=%s'
    # a = mysql_obj(sql=select_sql, args=["F16208966997685"], is_more=True)
    start_time = time.time()
    select_1000_sql = mysql_obj(sql="select * from `cs3_fu`.sales_flat_order limit 597;", is_more=True)

    # print(select_1000_sql, type(select_1000_sql))
    print(f"查询数据耗时：{time.time() - start_time}")
    mysql_obj.close()
