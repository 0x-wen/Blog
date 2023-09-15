# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 14:50
# @Author  : JW
# @FileName: index_page.py
"""
from common.handle_path import PHOTO, LOGO
from page_locators.index_locator import IndexLocator as locator
from common.handle_base_page import HandleBasePage
from common.handle_upload_file import upload_file

import time


class IndexPage(HandleBasePage):

    def user_name_check(self):
        """验证登录后账户信息"""
        self.wait_visibility_element(locator=locator.username, timeout=30, model="后台主页")
        return self.driver.find_element(*locator.username).text

    def jump_vip_background(self):
        """跳转导航栏/会员后台"""
        self.wait_click_element(locator=locator.vip_background)
        return self.driver.find_element(*locator.vip_background).click()

    @property
    def get_shop_management(self):
        """导航栏/获取商家管理"""
        self.wait_click_element(locator=locator.shop_management, model="导航栏/获取商家管理")
        return self.driver.find_element(*locator.shop_management)

    @property
    def get_pass_shop(self):
        """商家管理/已认证商家"""
        self.wait_visibility_element(locator=locator.pass_shop, model="商家管理/已认证商家")
        return self.driver.find_element(*locator.pass_shop)

    def add_shop(self):
        """商家管理/已认证商家/添加店铺"""
        self.wait_visibility_element(locator=locator.add_shop, model="已认证商家/添加店铺")
        self.driver.find_element(*locator.add_shop).click()

    def add_shop_input_information(self, shop_name, shop_detailed_address, social_credit_code, near=None):
        """添加店铺/店铺名称,经营地址等"""
        self.wait_visibility_element(locator=locator.shop_name, model="添加店铺")
        time.sleep(0.5)
        self.driver.find_element(*locator.shop_name).send_keys(shop_name)
        # 点击店铺经营地址
        self.wait_click_element(locator=locator.shop_area)
        self.driver.find_element(*locator.shop_area).click()
        # 选择城市
        self.wait_visibility_element(locator=locator.choose_city)
        self.driver.find_element(*locator.choose_city).click()
        # 选择区域
        self.wait_visibility_element(locator=locator.choose_area)
        self.driver.find_element(*locator.choose_area).click()
        # 输入详细地址
        self.wait_visibility_element(locator=locator.shop_detailed_address)
        self.driver.find_element(*locator.shop_detailed_address).send_keys(shop_detailed_address)

        """添加店铺/店铺经营范围,社会统一信用代码,营业执照等"""
        # 点击店铺经营范围
        self.wait_click_element(locator=locator.shop_business_scope)
        self.driver.find_element(*locator.shop_business_scope).click()
        # 选择分类1
        self.wait_visibility_element(locator=locator.shop_business_scope_1)
        self.driver.find_element(*locator.shop_business_scope_1).click()
        # 选择分类2
        self.wait_visibility_element(locator=locator.shop_business_scope_2)
        self.driver.find_element(*locator.shop_business_scope_2).click()
        # 选择分类3
        self.wait_visibility_element(locator=locator.shop_business_scope_3)
        self.driver.find_element(*locator.shop_business_scope_3).click()
        # 靠近信息
        self.wait_visibility_element(locator=locator.near)
        self.driver.find_element(*locator.near).send_keys(near)
        # 获取精准坐标
        self.wait_click_element(locator=locator.precise_coordinates)
        self.driver.find_element(*locator.precise_coordinates).click()
        # 统一社会信用代码
        self.wait_visibility_element(locator=locator.social_credit_code)
        self.driver.find_element(*locator.social_credit_code).location_once_scrolled_into_view
        self.driver.find_element(*locator.social_credit_code).send_keys(social_credit_code)
        time.sleep(1)
        # 公司营业执照
        self.wait_presence_element(locator=locator.upload)
        # self.driver.find_element(*locator.upload).send_keys(PHOTO)
        self.driver.find_element(*locator.upload).click()
        time.sleep(3)
        upload_file(PHOTO)

        # 保存，下一步
        time.sleep(2)
        self.wait_click_element(locator=locator.save)
        self.driver.find_element(*locator.save).location_once_scrolled_into_view
        self.driver.find_element(*locator.save).click()
        pass

    def add_shop_input_information_2(self):
        """填写门店信息"""
        # 上传店铺logo
        self.wait_presence_element(locator=locator.logo, model="添加店铺")
        self.driver.find_element(*locator.logo).send_keys(LOGO)
        self.wait_visibility_element(locator=locator.btn)
        self.driver.find_element(*locator.btn).click()
        time.sleep(1)

        # 店铺详情图
        self.wait_presence_element(locator=locator.details_picture)
        # self.driver.find_element(*locator.details_picture).send_keys(PHOTO)
        self.driver.find_element(*locator.details_picture).click()
        time.sleep(3)
        upload_file(file_path=PHOTO)
        time.sleep(2)
        # 图片裁剪保存按钮
        self.wait_visibility_element(locator=locator.btn_3)
        self.driver.find_element(*locator.btn_3).click()

        # 人均消费
        self.wait_visibility_element(locator=locator.consumption)
        self.driver.find_element(*locator.consumption).send_keys("198")

        # 营业电话
        self.wait_visibility_element(locator=locator.telephone)
        self.driver.find_element(*locator.telephone).send_keys("15019248989")
        # 营业时间
        self.wait_visibility_element(locator=locator.business_hours)
        time.sleep(0.5)
        self.driver.find_element(*locator.business_hours).click()
        time.sleep(0.5)
        self.driver.find_element(*locator.business_hours_2).click()
        # 推荐理由
        self.wait_visibility_element(locator=locator.recommended_reasons)
        self.driver.find_element(*locator.recommended_reasons).location_once_scrolled_into_view
        self.driver.find_element(*locator.recommended_reasons).send_keys("好吃哈哈哈")
        # 详细介绍
        self.wait_visibility_element(locator=locator.detailed_introduction)
        self.driver.find_element(*locator.detailed_introduction).location_once_scrolled_into_view
        self.driver.find_element(*locator.detailed_introduction).send_keys("非常不错")
        # 保存所有信息
        self.wait_click_element(locator=locator.save_all)
        self.driver.find_element(*locator.save_all).location_once_scrolled_into_view
        self.driver.find_element(*locator.save_all).click()
        time.sleep(2)

    @property
    def add_shop_check(self):
        """验证添加店铺成功之后页面跳转元素"""
        try:
            self.wait_visibility_element(locator=locator.add_shop_pass, timeout=30, model="添加店铺成功")
            return self.driver.find_element(*locator.add_shop_pass)
        except Exception as e:
            self.do_log.error("登录后验证元素出错{}".format(e))
