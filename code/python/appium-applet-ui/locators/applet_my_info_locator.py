# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:47
# @Author  :  Jw
# @File    : applet_my_info_locator.py
from selenium.webdriver.common.by import By


class MyInfoLocator:
    """菜单导航-我的 页面元素定位信息"""

    # 收藏夹
    # favorite = (By.XPATH, '//wx-view[text()="收藏夹"]')
    favorite = (By.XPATH, '//wx-view[text()="商品收藏"]')

    # 您还没收藏商品
    no_favorite = (By.XPATH, '//span[contains(text(),"还没收藏商品")]')

    # 收藏夹/删除商品图标
    favorite_delete_image = (By.XPATH, '//wx-label[contains(@class,"shop-del")]//div')

    # 收藏夹页面 第一个商品(无法点击)
    one_commodity = (By.XPATH, '//wx-view[contains(@class, "image-wrapper")]//div')

    # 商品详情页 收藏按钮
    favorite_button = (By.XPATH, '//span[text()="收藏"]/parent::wx-text/preceding-sibling::wx-image/div')

    # 首页按钮
    return_index = (By.XPATH, '//wx-view[text()="首页"]/preceding-sibling::wx-image/div')

    # 我的地址
    my_address = (By.XPATH, '//wx-view[contains(text(),"我的地址")]')

    # 新增收货地址
    add_address = (By.XPATH, '//wx-view[contains(text(),"新增收货地址")]')

    # 收货人输入框
    consignee_input_box = (By.XPATH, '//div[contains(text(),"姓名")]')

    # 详细地址输入框
    detailed_address = (By.XPATH, '//div[contains(text(),"请填写详细地址")]')

    # 手机号码输入框
    phone_number = (By.XPATH, '//div[contains(text(),"请输入正确的手机号码")]')

    # 常用邮箱输入框
    mailbox = (By.XPATH, '//div[contains(text(),"请输入正确的邮箱")]')

    # 所在地区
    area = (By.XPATH, '//wx-view[contains(text(),"请选择地区")]')

    # 所在地区选择 国籍-请选择
    country_select = (By.XPATH, '//div[@class="wrapper"]//span[text()="请选择"]/following-sibling::span')

    # 所在地区选择 国籍
    country = (By.XPATH, '//span[text()="中国大陆"]/following-sibling::span')

    # 所在地区选择 省份-请选择
    province_select = (By.XPATH, '//span[text()="请选择"]/following-sibling::span')

    # 所在地区选择 省份
    province = (By.XPATH, '//span[text()="北京市"]/following-sibling::span')

    # 所在地区选择 城市
    city = (By.XPATH, '//span[text()="北京市"]/following-sibling::span')

    # 所在地区选择 区
    district = (By.XPATH, '//span[text()="东城区"]/following-sibling::span')

    # 选择地区浮层/确定按钮
    confirm_button = (By.XPATH, '//wx-view[text()="确认" and contains(@class, "btn-confirm")]')

    # 新增收货地址页/底部确认按钮
    confirm_but = (By.XPATH, '//wx-view[text()="确认" and @class="bottom-btn"]')

    # 收货地址页面/修改图标,有修改图标即有地址
    edit_icon = (By.XPATH, '//wx-image[contains(@class, "edit-icon")]')
