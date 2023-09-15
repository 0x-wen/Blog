# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:51
# @Author  :  Jw
# @File    : applet_my_info_page.py
import time

from tools.base_page import BasePage
from locators.applet_my_info_locator import MyInfoLocator as my_info


class MyInfoPage(BasePage):
    """小程序我的页面元素"""

    @property
    def favorite(self):
        """收藏夹元素"""
        return self.get_webview_element(locator=my_info.favorite)

    @property
    def no_favorite(self):
        """还没收藏商品"""
        return self.get_webview_element(locator=my_info.no_favorite)

    @property
    def favorite_delete_image(self):
        """收藏夹删除图标"""
        return self.get_webview_element(locator=my_info.favorite_delete_image, is_more=True)

    @property
    def one_commodity(self):
        """第一个商品"""
        return self.get_webview_element(locator=my_info.one_commodity, is_more=True)

    @property
    def favorite_button(self):
        """收藏按钮"""
        return self.get_webview_element(locator=my_info.favorite_button)

    @property
    def return_index(self):
        """商品详情页 返回首页按钮"""
        return self.get_webview_element(locator=my_info.return_index)

    @property
    def my_address(self):
        """我的地址元素"""
        return self.get_webview_element(locator=my_info.my_address)

    @property
    def add_address(self):
        """新增收货地址元素"""
        return self.get_webview_element(locator=my_info.add_address)

    @property
    def consignee_input_box(self):
        """收货人项目输入框"""
        return self.get_webview_element(locator=my_info.consignee_input_box)

    @property
    def detailed_address(self):
        """详细地址输入框"""
        return self.get_webview_element(locator=my_info.detailed_address)

    @property
    def phone_number(self):
        """手机号码输入框"""
        return self.get_webview_element(locator=my_info.phone_number)

    @property
    def mailbox(self):
        """常用邮箱输入框"""
        return self.get_webview_element(locator=my_info.mailbox)

    @property
    def area(self):
        """请选择地区元素"""
        return self.get_webview_element(locator=my_info.area)

    @property
    def country(self):
        """请选择国籍"""
        return self.get_webview_element(locator=my_info.country)

    @property
    def province(self):
        """请选择省份"""
        return self.get_webview_element(locator=my_info.province)

    @property
    def city(self):
        """请选择城市"""
        return self.get_webview_element(locator=my_info.city, is_more=True)

    @property
    def district(self):
        """请选择区"""
        return self.get_webview_element(locator=my_info.district)

    def confirm_button(self):
        """选择地区浮层/确认按钮"""
        return self.get_webview_element(locator=my_info.confirm_button)

    @property
    def confirm_but(self):
        """新增收货地址页/底部确认按钮"""
        return self.get_webview_element(locator=my_info.confirm_but)

    @property
    def country_select(self):
        """地区浮层中 请选择 元素"""
        return self.get_webview_element(locator=my_info.country_select, is_more=True)

    @property
    def edit_icon(self):
        """修改图标 元素定位"""
        return self.get_webview_element(locator=my_info.edit_icon, is_more=True)
