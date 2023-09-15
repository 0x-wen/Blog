# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 11:27
# @Author  :  Jw
# @File    : applet_index_page.py
import time

from tools.base_page import BasePage
from locators.applet_index_locator import AppletIndexLocator as index


class AppletIndexPage(BasePage):
    """小程序首页元素"""

    @property
    def applet_index_face(self):
        """小程序首页/面部护肤元素"""
        return self.get_webview_element(locator=index.one_image, is_more=True)

    @property
    def face_one_img(self):
        """面部护肤/第一个商品信息 元素"""
        return self.get_webview_element(locator=index.one_good, is_more=True)

    def home(self):
        """菜单导航-首页"""
        self.driver.tap([self.click_bottom_menu(1)], 500)
        self.do_log.info('进入小程序菜单导航-首页')
        time.sleep(self.time_sleep)

    def sort(self):
        """菜单导航-分类"""
        self.driver.tap([self.click_bottom_menu(2)], 500)
        self.do_log.info('进入小程序菜单导航-分类')
        time.sleep(self.time_sleep)

    def brand(self):
        """菜单导航-品牌"""
        self.driver.tap([self.click_bottom_menu(3)], 500)
        self.do_log.info('进入小程序菜单导航-品牌')
        time.sleep(self.time_sleep)

    def shopping_card(self):
        """菜单导航-购物车"""
        self.driver.tap([self.click_bottom_menu(4)], 500)
        self.do_log.info('进入小程序菜单导航-购物车')
        time.sleep(self.time_sleep)

    def my_info(self):
        """菜单导航-我的"""
        self.driver.tap([self.click_bottom_menu(5)], 500)
        self.do_log.info('进入小程序菜单导航-我的')
        time.sleep(self.time_sleep)

    @property
    def search_good(self):
        """搜索商品元素"""
        return self.get_webview_element(locator=index.search_good)

    @property
    def key_word(self):
        """输入关键字搜索框"""
        return self.get_webview_element(locator=index.key_word)

    @property
    def get_hot_search_value(self):
        """获取热门搜索下的关键字元素"""
        return self.get_webview_element(locator=index.hot_search_value)

    @property
    def select_info_element(self):
        """获取搜索信息第一个元素"""
        return self.get_webview_element(locator=index.select_info)

    @property
    def commodity_s_img(self):
        """搜索列表页/商品图标信息"""
        return self.get_webview_element(locator=index.commodity_s_img, is_more=True)

    @property
    def add_shopping_cart(self):
        """添加购物车底部button元素"""
        return self.get_webview_element(locator=index.add_shopping_cart)

    @property
    def into_shopping_cart(self):
        """进入购物车图标元素"""
        return self.get_webview_element(locator=index.into_shopping_cart)

    @property
    def get_commodity_special_element(self):
        """获取商品特价元素"""
        return self.get_webview_element(locator=index.special_elements, is_more=True)

    @property
    def product_title(self):
        """商品标题信息"""
        return self.get_webview_element(locator=index.product_title)

    @property
    def update_commodity_num(self):
        """更改商品数量元素"""
        return self.get_webview_element(locator=index.update_commodity_num)

    @property
    def add_num(self):
        """增加商品数量"""
        return self.get_webview_element(locator=index.add_num)

    @property
    def sub_num(self):
        """减少商品数量"""
        return self.get_webview_element(locator=index.sub_num)

    @property
    def select_skus(self):
        """选择商品sku元素"""
        return self.get_webview_element(locator=index.select_skus, is_more=True)

    @property
    def sku_attribute(self):
        """获取 商品详情页/浮层 商品sku属性文本元素"""
        return self.get_webview_element(locator=index.sku_attribute)

    @property
    def update_commodity_shop_car(self):
        """浮层中添加购物车元素"""
        return self.get_webview_element(locator=index.update_commodity_shop_car)

    @property
    def to_pay(self):
        """去支付元素"""
        return self.get_webview_element(locator=index.to_pay)

    @property
    def obligation(self):
        """我的订单/待付款导航"""
        return self.get_webview_element(locator=index.obligation)

    @property
    def obligation_data(self):
        """
        待付款导航/取消订单元素
        备注：订单待付款页面中 取消订单会出现6个元素，第二个元素才是想要到元素信息 所以下标取值为1
        """
        all_element = self.get_webview_element(locator=index.obligation_data, is_more=True)
        return all_element[1]

    @property
    def complete(self):
        """
        我的订单/全部导航元素
        """
        all_element = self.get_webview_element(locator=index.complete)
        return all_element

    @property
    def status_null(self):
        """待付款下 相关订单状态为空"""
        ele = self.get_webview_element(locator=index.status_null)
        return ele
