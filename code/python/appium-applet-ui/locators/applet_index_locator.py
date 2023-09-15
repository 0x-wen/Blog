# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 11:28
# @Author  :  Jw
# @File    : applet_index_locator.py
from selenium.webdriver.common.by import By


class CommodityDetailsLocator:
    """商品详情元素定位信息"""

    # 特价元素  获得两个元素(币种图标和钱数额)
    special_elements = (By.XPATH, '//wx-view[contains(@class,"sale-price")]/wx-text/span[2]')

    # 商品title
    product_title = (By.XPATH, '//wx-view[contains(@class,"product-title")]')

    # 更改商品数量
    update_commodity_num = (By.XPATH, '//wx-view[text()="已选"]/following-sibling::wx-view[contains(@class,"flex-1")]')

    # add + 商品
    add_num = (By.XPATH, '//wx-view[contains(@class,"max")]')

    # sub - 商品
    sub_num = (By.XPATH, '//wx-view[contains(@class,"min")]')

    # 选择规格(sku)元素
    select_skus = (By.XPATH, '//wx-view[contains(@class,"items-wrapper")]//div')

    # 记录选择sku商品的规则属性
    sku_attribute = (
        By.XPATH, '//span[contains(text(),"已选")]/../following-sibling::wx-text//span/following-sibling::span')

    # 浮层中 加入购物车
    update_commodity_shop_car = (By.XPATH, '//wx-safe-area-bottom//wx-view[contains(@class,"btn")]')

    # 加入购物车底部button
    add_shopping_cart = (By.XPATH, '//wx-view[contains(text(),"加入购物车") and contains(@class,"btn-wrapper")]')

    # 进入购物车图标
    into_shopping_cart = (By.XPATH, '//wx-view[text()="购物车"]')


class Order:
    # 确认订单页/去支付按钮
    to_pay = (By.XPATH, '//wx-view[text()="去支付"]')

    # 我的订单/待付款 导航定位
    obligation = (By.XPATH, '//span[text()="待付款"]/following-sibling::span')

    # 待付款导航/取消订单 数据定位
    obligation_data = (By.XPATH, '//wx-button[text()="取消订单"]')

    # 待付款导航/全部导航
    complete = (By.XPATH, '//span[text()="全部"]/following-sibling::span')

    # 待付款/相关状态为空
    status_null = (By.XPATH, '//span[text()="相关订单状态为空"]/following-sibling::span')


class CommodityList:
    """商品列表页"""

    # 搜索列表页/商品图标信息
    # commodity_s_img = (By.XPATH, '//wx-view[contains(@class, "image-wrapper")]//div')
    commodity_s_img = (By.XPATH, '//wx-product-card[@is="components/product-card"]//div')


class AppletIndexLocator(CommodityDetailsLocator, CommodityList, Order):
    """小程序主页元素定位信息"""

    # 面部护肤
    one_image = (By.XPATH, '//wx-advertisement[contains(@is, "components/home/advertisement")]//wx-image')

    # 面部护肤/第一个商品
    one_good = (By.XPATH, '//wx-product-card[contains(@is,"components/product-card")]//wx-image')

    # 搜索商品输入框
    search_good = (By.XPATH, '//span[text()="搜索商品"]/following-sibling::span')

    # 输入关键字
    key_word = (By.XPATH, '//wx-input[@confirm-type="search"]')

    # 关键字输入框 （输入的value有双向绑定 单独更改value无法实现输入值，已使用adb shell 实现输入字符[不含中文]）
    input_key_word = (By.XPATH, '//wx-input[@confirm-type="search"]')

    # 热门搜索的元素信息input_key_word
    hot_search = (By.XPATH, '//wx-view[text()="热门搜索"]')

    # 热门搜索下的关键字 元素信息
    hot_search_value = (By.XPATH, '//wx-view[text()="热门搜索"]/following::wx-view[contains(@class,"box-tags")]/wx-view')

    # 搜索后的选择信息 默认选择第一个
    select_info = (By.XPATH, '//wx-view[contains(@data-event-opts,"list,,0")]')
