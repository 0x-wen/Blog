# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 13:56
# @Author  :  Jw
# @File    : applet_sort_locator.py
from selenium.webdriver.common.by import By


class SubCategories:
    """小程序二级分类页 元素定位信息"""
    # 眼部彩妆
    eyes_make_up = (By.XPATH, '//span[text()="眼部彩妆"]/following-sibling::span')

    # 眼部彩妆/商品信息 加入购物车图标
    add_shop_car_image = (By.XPATH, '//wx-image[contains(@class,"cart-icon")]/div')

    # 添加成功提示
    add_succeed = (By.XPATH, '//*[contains(@text, "加入购物车成功")]')

    # 购物车图标
    shop_car = (By.XPATH, '//wx-image[@src="/static/cart-icon.png"]/div')

    # 去结算按钮
    count_button = (By.XPATH, '//wx-view[contains(text(),"去结算")]')


class AppletSortLocator(SubCategories):
    """小程序一级分类页 元素定位信息"""

    # 一级分类-面部护肤
    face_maintain = (By.XPATH, '//span[text()="面部护肤"]/following-sibling::span')

    # 一级分类-魅力彩妆
    make_up = (By.XPATH, '//span[text()="魅力彩妆"]/following-sibling::span')
