# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:51
# @Author  :  Jw
# @File    : applet_sort_page.py
from tools.base_page import BasePage
from locators.applet_sort_locator import AppletSortLocator as sort


class AppletSortPage(BasePage):
    """小程序分类页面元素"""

    def make_up(self):
        """1级分类-魅力彩妆"""
        return self.get_webview_element(locator=sort.make_up)

    def eyes_make_up(self):
        """魅力彩妆/眼部彩妆"""
        return self.get_webview_element(locator=sort.eyes_make_up, is_more=False)

    def add_shop_car_image(self):
        """眼部彩妆/商品信息 加入购物车图标"""
        return self.get_webview_element(locator=sort.add_shop_car_image, is_more=True)

    def add_succeed(self):
        """添加成功提示 提示弹窗时间太短了 需要切换窗口遍历查找元素，存在找不到此元素的情况"""
        return self.get_webview_element(locator=sort.add_succeed)

    def shop_car(self):
        """购物车图标"""
        return self.get_webview_element(locator=sort.shop_car)

    def count_button(self):
        """去结算按钮"""
        return self.get_webview_element(locator=sort.count_button)
