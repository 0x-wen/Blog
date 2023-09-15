# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/5/14 19:53
@file: handle_mysql.py
"""
import pymysql
import random
import string

from scripts.handle_config import do_config


class HandleMysql:

    def __init__(self):
        self.conn = pymysql.connect(host=do_config("MYSQL_QA002", "host"),
                                    user=do_config("MYSQL_QA002", "user"),
                                    password=do_config("MYSQL_QA002", "password"),
                                    db=do_config("MYSQL_QA002", "db"),
                                    port=do_config("MYSQL_QA002", "port"),
                                    charset=do_config("MYSQL_QA002", "charset"),
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
    select_sql = 'SELECT * FROM retail_shop.shop WHERE `name`=%s'
    a = mysql_obj(sql=select_sql, args=["xxx"], is_more=True)
    print(a, type(a))
    mysql_obj.close()
