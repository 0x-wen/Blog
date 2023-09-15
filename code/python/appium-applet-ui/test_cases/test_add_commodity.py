# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 17:23
# @Author  :  Jw
# @File    : test_add_commodity.py
import inspect
import time
import unittest

from tools.base_driver import android_driver
from business.sort_list_add_commodity_shop_car import SortListAddCommodityShopCarBusiness, SearchGoodBusiness, \
    FavoriteBusiness
from business.go_to_applet import GoToApplet
from tools.operate_log import OperateLog


class AddCommodity(unittest.TestCase):
    time_sleep = 0.5
    log = OperateLog().get_logger()

    def setUp(self) -> None:
        self.driver = android_driver()
        self.driver.implicitly_wait(20)
        self.add_commodity_business = SortListAddCommodityShopCarBusiness(driver=self.driver)
        self.search_good = SearchGoodBusiness(driver=self.driver)
        self.favorite_business = FavoriteBusiness(driver=self.driver)
        self.applet_business = GoToApplet(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_01_go_to_applet(self):
        """测试进入小程序"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("执行 进入小程序 用例")
        self.applet_business.go_to_applet()
        self.applet_business.switch_to_context()

        face_elements = self.add_commodity_business.applet_index_face
        try:
            self.assertTrue(face_elements[1].is_enabled(), msg="未找到验证元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_02_add_only_commodity(self):
        """测试添加商品"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.applet_business.go_to_applet()

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

    def test_03_search_good_keyword(self):
        """测试热门搜索添加商品"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.applet_business.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.add_commodity_business.clear_shop_car()

        self.log.info("执行 测试热门搜索添加商品")
        special, price = self.search_good.search_good_keyword()
        time.sleep(self.time_sleep)
        self.log.info("获取结算按钮的元素，获取到元素则用例通过")
        count_button_element = self.add_commodity_business.count_button()

        try:
            self.assertTrue(count_button_element.is_displayed(), msg="未找到执行元素信息，用例失败")
            self.assertEqual(special, price, msg="价格对比失败，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_04_add_commodity_favorite(self):
        """测试添加商品至收藏夹"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.applet_business.go_to_applet()

        self.log.info("收藏商品之前，清空收藏夹")
        self.favorite_business.favorite_clear()

        self.log.info("清空收藏夹之后，后退页面")
        self.driver.keyevent(4)

        self.log.info("执行 测试添加商品至收藏夹")
        self.favorite_business.add_commodity_favorite()
        time.sleep(self.time_sleep)
        self.log.info("获取收藏页面 存在商品 有删除按钮则验证通过")
        delete_image_element = self.favorite_business.favorite_delete_image[0]

        try:
            self.assertTrue(delete_image_element.is_displayed(), msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_05_add_more_commodity_assert_price(self):
        """测试添加多个商品对比商品名称和价格"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.applet_business.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.add_commodity_business.clear_shop_car()
        bool_value = self.search_good.add_more_commodity_assert_price(num=2)

        try:
            self.assertEqual(bool_value, True, msg="商品详情页名称和价格 与 购物车页面名称和价格不一致，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_06_brand_search(self):
        """测试 搜索品牌添加商品信息"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.applet_business.go_to_applet()

        self.search_good.brand_search()
        time.sleep(self.time_sleep)
        self.log.info("获取结算按钮的元素，获取到元素则用例通过")
        count_button_element = self.add_commodity_business.count_button()

        try:
            self.assertTrue(count_button_element.is_displayed(), msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_07_update_commodity_num_business(self):
        """测试 商品详情页更改商品数量"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.applet_business.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.add_commodity_business.clear_shop_car()

        self.search_good.update_commodity_num_business()

        product_num = self.search_good.get_product_num

        try:
            self.assertEqual("2", product_num, msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_08_update_num_shopping_car(self):
        """测试 购物车页更改商品数量"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.applet_business.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.add_commodity_business.clear_shop_car()

        self.search_good.update_num_shopping_car()

        product_num = self.search_good.get_product_num

        try:
            self.assertEqual("2", product_num, msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_09_add_spu_commodity(self):
        """测试 添加spu商品，对比商品sku属性文本"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.applet_business.go_to_applet()

        self.log.info("添加商品之前，清空购物车")
        self.add_commodity_business.clear_shop_car()

        self.log.info("执行 测试添加spu商品，对比商品sku属性文本 用例")
        self.log.info("获取商品详情页sku属性文本信息，购物车sku属性文本信息，对比一致则用例通过")
        detail_sku_text, product_sku_text = self.add_commodity_business.add_spu_commodity(product=1, select_sku=0)

        try:
            self.assertEqual(detail_sku_text, product_sku_text, msg="商品详情页sku属性文本信息 != 购物车sku属性文本信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_10_delete_collect(self):
        """测试 删除收藏商品"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.applet_business.go_to_applet()

        self.log.info("执行 测试 删除收藏商品 用例")
        delete_bool = self.favorite_business.delete_collect()

        try:
            self.assertEqual(delete_bool, True, msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e


if __name__ == '__main__':
    unittest.main()
