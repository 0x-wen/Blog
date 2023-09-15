# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 14:55
# @Author  :  Jw
# @File    : test_my_info.py
import inspect
import time
import unittest
from libs.ddt import ddt, data

from tools.base_driver import android_driver
from business.applet_business import IndexBusiness, ShopCarBusiness, SortBusiness, MyInfoBusiness
from business.go_to_applet import GoToApplet
from tools.operate_log import OperateLog
from test_datas.keyword import Address


class ParameterTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameterTestCase, self).__init__(methodName)
        global parames
        parames = parame


@ddt
class TestMyInfo(ParameterTestCase):
    time_sleep = 0.5
    log = OperateLog().get_logger()
    all_user_address_data = Address.user_address

    def setUp(self) -> None:
        self.driver = android_driver(0)
        self.driver.implicitly_wait(20)
        self.my_info_business = MyInfoBusiness(driver=self.driver)
        self.go_applet = GoToApplet(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_04_add_commodity_favorite(self):
        """测试添加商品至收藏夹"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("收藏商品之前，清空收藏夹")
        self.my_info_business.favorite_clear()

        self.log.info("清空收藏夹之后，后退页面")
        self.driver.keyevent(4)

        self.log.info("执行 测试添加商品至收藏夹")
        self.my_info_business.add_commodity_favorite()
        time.sleep(self.time_sleep)
        self.log.info("获取收藏页面 存在商品 有删除按钮则验证通过")
        delete_image_element = self.my_info_business.favorite_delete_image[0]

        try:
            self.assertTrue(delete_image_element.is_displayed(), msg="未找到执行元素信息，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    def test_10_delete_collect(self):
        """测试 删除收藏商品"""
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("执行 测试 删除收藏商品 用例")
        delete_bool = self.my_info_business.delete_collect()

        try:
            self.assertEqual(delete_bool, True, msg="收藏夹商品不为空，用例失败")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e

    @data(*all_user_address_data)
    def test_11_add_my_address(self, user_address):
        """测试 添加我的收货地址"""
        # user_address = Address.user_address[0]
        print('参数信息：{}'.format(user_address))
        self.log.info('当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))
        self.log.info("进入小程序")
        self.go_applet.go_to_applet()

        self.log.info("执行 添加我的收货地址")
        self.my_info_business.add_my_address(consignee=user_address["consignee"],
                                             detailed_address=user_address["detailed_address"],
                                             phone_number=user_address["phone_number"],
                                             mailbox=user_address["mailbox"])
        is_edit_icon = self.my_info_business.bool_edit_icon()

        try:
            self.assertEqual(is_edit_icon, True, msg="修改图标不存在，请查看用例")
        except Exception as e:
            self.log.error('异常信息为{}'.format(e))
            raise e


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    for method in dir(TestMyInfo):
        if method.startswith("test"):
            suite.addTest(TestMyInfo(method))
    unittest.TextTestRunner().run(suite)
