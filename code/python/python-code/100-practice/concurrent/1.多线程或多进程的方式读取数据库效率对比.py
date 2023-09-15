# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 14:50
# @Author  :  Jw
# @File    : 1.多线程或多进程的方式读取数据库效率对比.py
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor

from handle_mysql import HandleMysql

handle_mysql_obj = HandleMysql()
__lock = threading.Lock()

mysql_data_list = []


def read_sql_1():
    """读取前面200条数据"""
    print("线程1...")
    with __lock:
        select_sql = handle_mysql_obj(sql="select * from `cs3_fu`.sales_flat_order limit 200;", is_more=True)
        mysql_data_list.append(select_sql)


def read_sql_2():
    """读取前面500条数据"""
    print("线程2...")
    with __lock:
        select_sql = handle_mysql_obj(sql="select * from `cs3_fu`.sales_flat_order limit 200,397;", is_more=True)
        mysql_data_list.append(select_sql)


def main():
    t1 = threading.Thread(target=read_sql_1)
    t2 = threading.Thread(target=read_sql_2)
    t1.start()
    t2.start()
    t1.join()  # 阻塞，主进程/主线程 会等待 子线程执行结束之后，在执行主线程代码
    t2.join()  # 阻塞，主进程/主线程 会等待 子线程执行结束之后，在执行主线程代码


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f"消耗时间为：{time.time() - start_time}")
    print(mysql_data_list)
