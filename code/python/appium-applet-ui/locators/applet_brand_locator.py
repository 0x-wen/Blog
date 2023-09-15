# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:46
# @Author  :  Jw
# @File    : applet_brand_locator.py
from selenium.webdriver.common.by import By


class BrandLocator:
    """菜单导航-品牌 页面元素定位信息"""

    # 品牌搜索框
    brand_search_box = (By.XPATH, '//span[text()="请输入关键词"]/following-sibling::span')

    # 搜索页面、 输入值
    input_value = (By.XPATH, '//span[contains(text(),"请输入关键词")]')

    # 收藏夹/删除商品图标
    favorite_delete_image = (By.XPATH, '//wx-label[contains(@class,"shop-del")]//div')

    # 收藏夹页面 第一个商品(无法点击)
    one_commodity = (By.XPATH, '//wx-view[contains(@class, "image-wrapper")]//div')

    # 商品详情页 收藏按钮
    favorite_button = (By.XPATH, '//span[text()="收藏"]/parent::wx-text/preceding-sibling::wx-image/div')

    # 首页按钮
    return_index = (By.XPATH, '//wx-view[text()="首页"]/preceding-sibling::wx-image/div')