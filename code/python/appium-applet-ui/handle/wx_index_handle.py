# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 14:13
# @Author  :  Jw
# @File    : wx_index_handle.py
import time

from element_pages.wx_index_page import WXIndexPage


class WXIndexHandle(WXIndexPage):

    def click_applet_name(self):
        """下滑微信，点击小程序名称"""
        self.swipe_down_wx_index()
        time.sleep(1)
        n = 3
        while n > 0:
            element = self.applet_name_element
            if element:
                element.click()
                n = -1
            else:
                # 在下拉一次
                self.swipe_screen(direction="down", t=0.7)
                time.sleep(0.5)
                n -= 1
                self.do_log.info("尚未找到小程序元素，再次下拉微信主页")


if __name__ == '__main__':
    from tools.base_driver import android_driver

    driver1 = WXIndexHandle(driver=android_driver())
    driver1.click_applet_name()
