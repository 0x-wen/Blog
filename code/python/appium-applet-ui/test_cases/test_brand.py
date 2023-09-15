# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 14:56
# @Author  :  Jw
# @File    : test_brand.py
import inspect
import time
import unittest

from tools.base_driver import android_driver
from business.applet_business import IndexBusiness, ShopCarBusiness, SortBusiness, MyInfoBusiness, BrandBusiness
from business.go_to_applet import GoToApplet
from tools.operate_log import OperateLog


class ParameterTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameterTestCase, self).__init__(methodName)
        global parames
        parames = parame


class TestBrand(ParameterTestCase):
    time_sleep = 0.5
    log = OperateLog().get_logger()

    def setUp(self) -> None:
        self.driver = android_driver(parames)
        self.driver.implicitly_wait(20)
        self.brand_business = BrandBusiness(driver=self.driver)
        self.sort_business = SortBusiness(driver=self.driver)
        self.go_applet = GoToApplet(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_06_brand_search(self):
        """测试 搜索品牌添加商品信息"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.go_applet.go_to_applet()

        self.brand_business.brand_search()
        time.sleep(self.time_sleep)
        self.log.info("获取结算按钮的元素，获取到元素则用例通过")
        count_button_element = self.sort_business.count_button()

        try:
            self.assertTrue(count_button_element.is_displayed(), msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e
