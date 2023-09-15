# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 17:23
# @Author  :  Jw
# @File    : test_add_commodity.py
import inspect
import multiprocessing
import os
import threading
import time
from datetime import datetime
import unittest

from libs import HTMLTestRunnerNew

from tools.base_driver import android_driver
from business.sort_list_add_commodity_shop_car import SortListAddCommodityShopCarBusiness, SearchGoodBusiness, \
    FavoriteBusiness
from business.go_to_applet import GoToApplet
from tools.operate_log import OperateLog
from tools.operate_yaml import OperateYaml
from tools.server import Server
from tools.constants import TEST_REPORTS_DIR, report_path


class ParameterTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameterTestCase, self).__init__(methodName)
        global parames
        parames = parame


class AddCommodity(ParameterTestCase):
    time_sleep = 0.5
    log = OperateLog().get_logger()

    @classmethod
    def setUpClass(cls) -> None:
        print('------parames-------', parames)
        cls.driver = android_driver(parames)
        cls.driver.implicitly_wait(20)
        cls.add_commodity_business = SortListAddCommodityShopCarBusiness(driver=cls.driver)
        cls.search_good = SearchGoodBusiness(driver=cls.driver)
        cls.favorite_business = FavoriteBusiness(driver=cls.driver)
        cls.applet_business = GoToApplet(driver=cls.driver)
        cls.log.info("进入小程序")
        cls.applet_business.go_to_applet()

    def setUp(self) -> None:
        pass

    # def tearDown(self):
    #     self.driver.quit()

    def test_01_go_to_applet(self):
        """测试进入小程序"""
        print("test case 01 里面的参数", parames)
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        # self.log.info("执行 进入小程序 用例")
        # self.applet_business.go_to_applet()
        self.applet_business.switch_to_context()

        face_elements = self.add_commodity_business.applet_index_face
        try:
            self.assertTrue(face_elements[1].is_enabled(), msg="未找到验证元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_02_add_only_commodity(self):
        """测试添加商品"""
        print("test case 02 里面的参数", parames)
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))

        self.log.info("添加商品之前，清空购物车")
        self.add_commodity_business.clear_shop_car()

        self.log.info("执行 添加单一商品 用例")
        self.add_commodity_business.add_only_commodity(product=1, select_sku=0)
        self.log.info("获取结算按钮的元素，获取到元素则用例通过")
        count_button_element = self.add_commodity_business.count_button()

        try:
            self.assertTrue(count_button_element.is_displayed(), msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e


def get_suite(i):
    print("get_suite里面的", i)
    print("开启子进程的编号", os.getpid())
    print("子进程的父级编号", os.getppid())
    suite = unittest.TestSuite()
    suite.addTest(AddCommodity("test_01_go_to_applet", parame=i))
    suite.addTest(AddCommodity("test_02_add_only_commodity", parame=i))

    report_file = report_path + '_' + datetime.strftime(datetime.now(), "%Y%m%d_") + str(i) + '.html'

    with open(report_file, 'wb+') as file:
        HTMLTestRunnerNew.HTMLTestRunner(stream=file).run(suite)


def appium_init():
    server = Server()
    server.main()


def get_count():
    read_yaml_line = OperateYaml()
    count = read_yaml_line.get_file_lines()
    return count


if __name__ == '__main__':
    appium_init()
    print("当前主进程的编号", os.getpid())
    threads = []
    for i in range(get_count()):
        print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)
