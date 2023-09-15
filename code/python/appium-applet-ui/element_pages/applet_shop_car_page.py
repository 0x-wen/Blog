# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:51
# @Author  :  Jw
# @File    : applet_shop_car_page.py
import time

from tools.base_page import BasePage
from locators.applet_shop_car_locator import ShopCarLocator as shop


class ShopCarPage(BasePage):
    """购物车页面元素"""

    def null_shop_car(self):
        """购物车空时查找元素"""
        return self.get_webview_element(locator=shop.null_shop_car)

    def delete(self):
        """购物车 删除商品图标"""
        return self.get_webview_element(locator=shop.delete, is_more=True)

    def confirm(self):
        """移动到购物车坐标 删除商品"""
        x, y = self.click_confirm_button()
        time.sleep(self.time_sleep)
        self.driver.tap([(x, y)], 50)
        self.do_log.info('点击弹窗 确认按钮')
        # self.driver.switch_to.alert.accept()

    @property
    def get_price_element(self):
        """购物车 获取价格元素"""
        return self.get_webview_element(locator=shop.price, is_more=True)

    @property
    def get_product_name(self):
        """购物车 商品名称元素"""
        return self.get_webview_element(locator=shop.product_name, is_more=True)

    @property
    def product_num(self):
        """购物车 商品数量元素"""
        return self.get_webview_element(locator=shop.product_num)

    @property
    def product_sku_text(self):
        """购物车 商品sku属性元素"""
        return self.get_webview_element(locator=shop.product_sku_text)
