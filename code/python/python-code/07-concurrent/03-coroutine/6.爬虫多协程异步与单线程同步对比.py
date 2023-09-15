# -*- coding: utf-8 -*-

import sys
import gevent
import requests
import time
from gevent import monkey
monkey.patch_all()


# sys.setrecursionlimit(2000)


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time

    return wrapper


# 协程函数发送10个网页的爬虫任务
def get_url(url):
    res = requests.get(url)
    print(url, res.status_code, len(res.content))


url_lst = [
    "http://www.baidu.com",
    "http://www.cntour.cn",
    "http://fanyi.youdao.com"
]


@count_time
def async_func():
    """定义一个异步任务方法"""
    g_lst = []
    for url in url_lst*10:
        g = gevent.spawn(get_url, url)
        g_lst.append(g)
    gevent.joinall(g_lst)


@count_time
def sync_func():
    """定义同步执行任务方法"""
    for url in url_lst*10:
        get_url(url)


if __name__ == '__main__':
    print(async_func())
    print(sync_func())
