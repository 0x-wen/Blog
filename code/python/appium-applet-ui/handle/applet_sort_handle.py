# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:53
# @Author  :  Jw
# @File    : applet_sort_handle.py
from element_pages.applet_sort_page import AppletSortPage


class AppletSortHandle(AppletSortPage):
    """分类页 操作处理"""

    def make_up_click(self):
        """点击魅力彩妆"""
        self.make_up().click()

    def eyes_make_up_click(self):
        """点击眼部彩妆"""
        self.eyes_make_up().click()

    def add_shop_car_image_click(self, index: int):
        """选择一个商品进购物车"""
        more_shop_car_ele = self.add_shop_car_image()
        more_shop_car_ele[index].click()

    def shop_car_click(self):
        """点击购物车图标"""
        self.shop_car().click()

    def count_button_click(self):
        """点击去结算按钮"""
        self.count_button().click()
