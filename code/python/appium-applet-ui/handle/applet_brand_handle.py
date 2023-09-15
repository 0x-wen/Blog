# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:54
# @Author  :  Jw
# @File    : applet_brand_handle.py
import time

from element_pages.applet_brand_page import BrandPage


class BrandHandle(BrandPage):
    """小程序品牌页 操作处理"""

    def brand_search_box_click(self):
        """点击 小程序品牌/搜索框元素"""
        self.do_log.info("点击 小程序品牌/搜索框元素")
        brand_search_ele = self.brand_search_box
        brand_search_ele.click()
