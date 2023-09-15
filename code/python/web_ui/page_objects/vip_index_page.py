# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 16:50
# @Author  : JW
# @FileName: vip_index_page.py
"""
from page_locators.vip_index_locator import VipIndexLocator as locator
from common.handle_base_page import HandleBasePage
import time

from common.handle_upload_file import upload_file
from common.handle_path import PHOTO


class VipIndexPage(HandleBasePage):

    @property
    def vip_background_check(self):
        """跳转会员后台验证"""
        self.wait_visibility_element(locator=locator.vip_background_check)
        return self.driver.find_element(*locator.vip_background_check)

    def add_vip_card_click(self):
        """点击添加会员卡"""
        self.wait_visibility_element(locator=locator.add_vip_card)
        return self.driver.find_element(*locator.add_vip_card).click()

    @property
    def get_members_activity_management(self):
        """获取导航栏/会员活动管理"""
        self.wait_visibility_element(locator=locator.members_activity_management, model="等待会员活动管理")
        return self.driver.find_element(*locator.members_activity_management)

    def scan_code_members_click(self):
        """点击会员活动管理/扫码领会员"""
        self.wait_click_element(locator=locator.scan_code_members)
        return self.driver.find_element(*locator.scan_code_members).click()

    def add_activity(self):
        """扫码领会员/添加活动"""
        # 添加活动
        self.wait_click_element(locator=locator.add_activity)
        self.driver.find_element(*locator.add_activity).click()
        # 输入活动名称
        self.wait_visibility_element(locator=locator.activity_name)
        self.driver.find_element(*locator.activity_name).send_keys("扫码领取会员卡（限时）")
        # 活动开始时间
        self.wait_visibility_element(locator=locator.start_time)
        self.driver.find_element(*locator.start_time).send_keys("2019-08-30 00:00:00")
        # js_pha = "arguments[0].value='2019-08-30 00:00:00'"
        # self.driver.execute_script(js_pha, a)
        time.sleep(0.5)
        # 活动结束时间
        self.wait_visibility_element(locator=locator.end_time)
        self.driver.find_element(*locator.end_time).send_keys("2019-08-31 00:00:00")
        time.sleep(1)
        self.wait_visibility_element(locator=locator.pack_up)
        self.driver.find_element(*locator.pack_up).click()
        # 背景图
        self.wait_visibility_element(locator=locator.background)
        time.sleep(1)
        self.driver.find_element(*locator.background).click()
        time.sleep(1)
        upload_file(PHOTO)
        self.driver.find_element(*locator.background_ok).click()
        # 活动规则
        self.wait_visibility_element(locator=locator.activity_rules)
        self.driver.find_element(*locator.activity_rules).send_keys("2019-08-31 00:00:00")
        time.sleep(0.5)
        # 奖品设置
        self.wait_visibility_element(locator=locator.prize_set)
        self.driver.find_element(*locator.prize_set).click()
        # 选择会员卡
        self.wait_click_element(locator=locator.choose_members_card)
        self.driver.find_element(*locator.choose_members_card).click()
        # 选择会员卡、确定
        self.wait_visibility_element(locator=locator.ok_button)
        self.driver.find_element(*locator.ok_button).click()
        # 投放数量
        self.wait_visibility_element(locator=locator.number)
        self.driver.find_element(*locator.number).send_keys("3")
        # 保存按钮
        self.wait_visibility_element(locator=locator.save)
        time.sleep(1)
        self.driver.find_element(*locator.save).click()
        time.sleep(0.5)

    @property
    def add_activity_check(self):
        """验证添加 扫码领会员活动成功"""
        self.wait_visibility_element(locator=locator.add_activity_succeed, model="添加扫码领会员活动_成功验证")
        return self.driver.find_element(*locator.add_activity_succeed)
