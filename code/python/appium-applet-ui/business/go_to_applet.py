# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 17:46
# @Author  :  Jw
# @File    : go_to_applet.py
import time

from handle.wx_index_handle import WXIndexHandle


class GoToApplet(WXIndexHandle):
    """进入小程序"""

    def go_to_applet(self):
        """下滑微信，点击小程序名称"""
        self.click_applet_name()
        time.sleep(1)
