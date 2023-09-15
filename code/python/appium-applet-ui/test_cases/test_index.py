# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 11:20
# @Author  :  Jw
# @File    : test_index.py
import inspect
import time
import unittest

from tools.base_driver import android_driver
from business.applet_business import IndexBusiness, ShopCarBusiness, SortBusiness
from business.go_to_applet import GoToApplet
from tools.operate_log import OperateLog


class ParameterTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameterTestCase, self).__init__(methodName)
        global parames
        parames = parame


class TestIndex(ParameterTestCase):
    time_sleep = 0.5
    log = OperateLog().get_logger()

    def setUp(self) -> None:
        self.driver = android_driver(parames)
        self.driver.implicitly_wait(20)
        self.index_business = IndexBusiness(driver=self.driver)
        self.shop_car_business = ShopCarBusiness(driver=self.driver)
        self.sort_business = SortBusiness(driver=self.driver)
        self.go_applet = GoToApplet(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_03_search_good_keyword(self):
        """测试热门搜索添加商品"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.shop_car_business.clear_shop_car()

        self.log.info("执行 测试热门搜索添加商品")
        special, price = self.index_business.search_good_keyword()
        time.sleep(self.time_sleep)
        self.log.info("获取结算按钮的元素，获取到元素则用例通过")
        count_button_element = self.sort_business.count_button()

        try:
            self.assertTrue(count_button_element.is_displayed(), msg="未找到执行元素信息，用例失败")
            self.assertEqual(special, price, msg="价格对比失败，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_05_add_more_commodity_assert_price(self):
        """测试添加多个商品对比商品名称和价格"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.shop_car_business.clear_shop_car()
        bool_value = self.index_business.add_more_commodity_assert_price(num=2)

        try:
            self.assertEqual(bool_value, True, msg="商品详情页名称和价格 与 购物车页面名称和价格不一致，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_07_update_commodity_num_business(self):
        """测试 商品详情页更改商品数量"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.go_applet.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.shop_car_business.clear_shop_car()

        self.index_business.update_commodity_num_business()

        product_num = self.shop_car_business.get_product_num

        try:
            self.assertEqual("2", product_num, msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_08_update_num_shopping_car(self):
        """测试 购物车页更改商品数量"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.go_applet.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.shop_car_business.clear_shop_car()

        self.index_business.update_num_shopping_car()

        product_num = self.shop_car_business.get_product_num

        try:
            self.assertEqual("2", product_num, msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_12_submit_order(self):
        """测试 提交订单"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("执行 测试 提交订单")
        status_null = self.index_business.submit_order()

        try:
            self.assertEqual(status_null, True, msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e
