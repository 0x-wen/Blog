# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 14:57
# @Author  :  Jw
# @File    : test_sort.py
import inspect
import time
import unittest

from tools.base_driver import android_driver
from business.applet_business import IndexBusiness, ShopCarBusiness, SortBusiness, MyInfoBusiness
from business.go_to_applet import GoToApplet
from tools.operate_log import OperateLog


class ParameterTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameterTestCase, self).__init__(methodName)
        global parames
        parames = parame


class TestSort(ParameterTestCase):
    time_sleep = 0.5
    log = OperateLog().get_logger()

    def setUp(self) -> None:
        self.driver = android_driver(parames)
        self.driver.implicitly_wait(20)
        self.sort_business = SortBusiness(driver=self.driver)
        self.shop_car_business = ShopCarBusiness(driver=self.driver)
        self.go_applet = GoToApplet(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_01_go_to_applet(self):
        """测试进入小程序"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("执行 进入小程序 用例")
        self.go_applet.go_to_applet()
        self.go_applet.switch_to_context()

        face_elements = self.sort_business.applet_index_face
        try:
            self.assertTrue(face_elements[1].is_enabled(), msg="未找到验证元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_02_add_only_commodity(self):
        """测试添加商品"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.shop_car_business.clear_shop_car()

        self.log.info("执行 添加单一商品 用例")
        self.sort_business.add_only_commodity(product=1, select_sku=0)
        self.log.info("获取结算按钮的元素，获取到元素则用例通过")
        count_button_element = self.sort_business.count_button()

        try:
            self.assertTrue(count_button_element.is_displayed(), msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_09_add_spu_commodity(self):
        """测试 添加spu商品，对比商品sku属性文本"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.shop_car_business.clear_shop_car()

        self.log.info("执行 测试添加spu商品，对比商品sku属性文本 用例")
        self.log.info("获取商品详情页sku属性文本信息，购物车sku属性文本信息，对比一致则用例通过")
        detail_sku_text, product_sku_text = self.sort_business.add_spu_commodity(product=2, select_sku=0)

        try:
            self.assertEqual(detail_sku_text, product_sku_text, msg="商品详情页sku属性文本信息 != 购物车sku属性文本信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e
