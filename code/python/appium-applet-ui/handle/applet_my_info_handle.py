# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:54
# @Author  :  Jw
# @File    : applet_my_info_handle.py
import time

from appium.webdriver.common.touch_action import TouchAction

from element_pages.applet_my_info_page import MyInfoPage
from element_pages.applet_shop_car_page import ShopCarPage


class MyInfoHandle(MyInfoPage, ShopCarPage):
    """小程序我的页面 操作处理"""

    def favorite_click(self):
        """点击收藏夹"""
        self.favorite.click()

    def delete_favorite(self):
        """删除收藏夹商品"""
        self.do_log.info("获取收藏夹删除商品图标")
        more_elements = self.favorite_delete_image
        len_more_elements = len(more_elements)
        self.do_log.info("收藏夹存在的商品信息：%d 个" % len_more_elements)
        while len_more_elements > 0:
            self.do_log.info("删除收藏夹内第一个商品")
            time.sleep(self.time_sleep)
            more_elements[0].click()
            self.do_log.info("# 点击弹窗 确定删除")
            self.confirm()
            self.do_log.info("# 重新获取收藏夹中需要删除商品的个数")
            more_elements = self.favorite_delete_image
            if more_elements:
                len_more_elements -= 1
                self.do_log.info("# 收藏夹中还剩下%d 个商品" % len_more_elements)
            else:
                self.do_log.info("# 已清空收藏夹内所有商品")
                len_more_elements = 0
        return True if len_more_elements == 0 else False

    def one_commodity_click(self):
        """点击第一个商品"""
        time.sleep(self.time_sleep)
        a = self.one_commodity
        a[0].click()
        pass

    def favorite_button_click(self):
        """点击收藏按钮"""
        self.favorite_button.click()

    def return_index_click(self):
        """点击返回首页按钮"""
        self.return_index.click()

    def my_address_click(self):
        """点击我的地址"""
        self.my_address.click()

    def add_address_click(self):
        """点击新增收货地址"""
        self.add_address.click()

    def consignee_input_box_click(self):
        """点击收货人姓名输入框"""
        self.consignee_input_box.click()

    def detailed_address_click(self):
        """点击详细地址输入框"""
        self.detailed_address.click()

    def phone_number_click(self):
        """点击手机号码输入框"""
        self.phone_number.click()

    def mailbox_click(self):
        """点击常用邮箱输入框"""
        self.mailbox.click()

    def area_click(self):
        """点击所在地区元素"""
        self.area.click()

    def country_click(self):
        """点击选择国籍"""
        self.country.click()

    def province_click(self):
        """点击选择省份"""
        self.province.click()
        # province_element = self.province
        # result = province_element.location_once_scrolled_into_view
        #
        # select_elements = self.country_select
        # select_elements[1].click()
        # select_result = select_elements[1].location_once_scrolled_into_view
        #
        # end_x_y = {"x": int(select_result['x']), "y": int(select_result['y']) + 20}
        # self.driver.swipe(start_x=int(select_result['x']), start_y=int(select_result['y']),
        #                   end_x=end_x_y['x'],
        #                   end_y=end_x_y['y'], duration=100)
        #
        # # touch_action = TouchAction(driver=self.driver)
        # # touch_action.press(select_elements[1]).move_to(x=result['x'], y=result['y']).perform()
        # self.province.click()
        # time.sleep(self.time_sleep)
        #
        # # self.driver.tap([(result['x'], result['y'])], 50)
        pass

    def city_click(self):
        """点击选择城市"""
        self.city[1].click()
        # city_element = self.city
        # result = city_element.location_once_scrolled_into_view
        # time.sleep(self.time_sleep)
        # # self.driver.tap([(result['x'], result['y'])], 50)
        # city_element.click()

    def district_click(self):
        """点击选择区"""
        district_element = self.district
        district_element.click()
        # result = district_element.location_once_scrolled_into_view
        # time.sleep(self.time_sleep)
        # # self.driver.tap([(result['x'], result['y'])], 50)
        # district_element.click()

    def confirm_button_click(self):
        """点击 选择地区/确认按钮"""
        self.confirm_button().click()

    def confirm_but_click(self):
        """点击 新增收货地址页/底部确认按钮"""
        self.confirm_but.click()

    def bool_edit_icon(self):
        """判断修改按钮是否存在,存在返回TRUE,否则返回FALSE"""
        bool_result = self.edit_icon
        return True if bool_result else False
