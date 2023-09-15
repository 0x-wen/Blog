# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:51
# @Author  :  Jw
# @File    : applet_brand_page.py
import time

from tools.base_page import BasePage
from locators.applet_brand_locator import BrandLocator as brand


class BrandPage(BasePage):
    """小程序品牌页面元素"""

    @property
    def brand_search_box(self):
        """小程序品牌/搜索框元素"""
        return self.get_webview_element(locator=brand.brand_search_box)
