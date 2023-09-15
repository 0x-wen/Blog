# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 11:47
# @Author  :  Jw
# @File    : wx_index_page.py
from tools.base_page import BasePage
from locators.wx_index_locator import WXIndexLocator as locator


class WXIndexPage(BasePage):
    """微信主页页面元素"""

    def swipe_down_wx_index(self):
        """下滑微信主页"""
        self.swipe_screen(direction='down')
        self.do_log.info('下滑微信主页，准备进入小程序')

    @property
    def applet_name_element(self):
        """获取小程序名称的元素信息"""
        return self.get_app_element(locator=locator.applet_name, model='微信主页/获取小程序名称')
