# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 13:43
# @Author  :  Jw
# @File    : main.py
import multiprocessing
import os
import time
import unittest
from datetime import datetime

from unittestreport import TestRunner

from test_cases.test_brand import TestBrand
from test_cases.test_index import TestIndex
from test_cases.test_my_info import TestMyInfo
from test_cases.test_sort import TestSort
from tools.constants import report_path, TEST_REPORTS_DIR
from tools.operate_yaml import OperateYaml
from tools.server import Server


def get_suite_one(pid):
    print("get_suite里面的第{}个进程".format(pid))
    print("开启子进程的编号", os.getpid())
    print("子进程的父级编号", os.getppid())
    suite = unittest.TestSuite()
    # suite.addTest(TestSort("test_09_add_spu_commodity", parame=pid))

    suite.addTests([TestMyInfo("test_04_add_commodity_favorite", pid),
                    TestMyInfo("test_10_delete_collect", pid),
                    TestBrand("test_06_brand_search", pid),
                    TestSort("test_01_go_to_applet", pid),
                    TestSort("test_02_add_only_commodity", pid),
                    TestSort("test_09_add_spu_commodity", pid),
                    TestIndex("test_03_search_good_keyword", pid),
                    TestIndex("test_05_add_more_commodity_assert_price", pid),
                    TestIndex("test_07_update_commodity_num_business", pid),
                    TestIndex("test_08_update_num_shopping_car", pid),
                    ])

    report(suite=suite, pid=pid)


def get_suite_two(pid):
    print("get_suite里面的第{}个进程".format(pid))
    print("开启子进程的编号", os.getpid())
    print("子进程的父级编号", os.getppid())

    suite = unittest.TestSuite()
    # for method in dir(TestMyInfo):
    #     if method.startswith("test"):
    #         suite.addTest(TestMyInfo(method, pid))

    # for method in dir(TestIndex):
    #     if method.startswith("test"):
    #         suite.addTest(TestIndex(method, pid))
    #
    # for method in dir(TestSort):
    #     if method.startswith("test"):
    #         suite.addTest(TestSort(method, pid))

    for method in dir(TestBrand):
        if method.startswith("test"):
            suite.addTest(TestBrand(method, pid))

    # suite.addTest(TestIndex("test_12_submit_order", pid))

    report(suite=suite, pid=pid)


def appium_init():
    server = Server()
    server.main()


def get_count():
    read_yaml_line = OperateYaml()
    count = read_yaml_line.get_file_lines()
    return count


def report(suite, pid):
    report_file = report_path + '_' + \
        datetime.strftime(datetime.now(), "%Y%m%d_") + str(pid) + '.html'
    runner = TestRunner(suite=suite, filename=report_file,
                        report_dir=TEST_REPORTS_DIR, templates=1)
    runner.rerun_run(count=3)

    # 发送测试报告至钉钉

    # 发送附件到邮箱


if __name__ == '__main__':
    appium_init()
    print("当前主进程的编号", os.getpid())
    threads = []
    for i in range(get_count()):
        if i == 0:  # 第一个子进程执行的内容
            t = multiprocessing.Process(target=get_suite_two, args=(i,))
        if i == 1:  # 第二个子进程执行的内容
            t = multiprocessing.Process(target=get_suite_two, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)
