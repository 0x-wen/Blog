# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:46
# @Author  :  Jw
# @File    : applet_shop_car_locator.py
from appium.webdriver.common.mobileby import MobileBy


class ShopCarLocator:
    """购物车页面 定位信息"""

    # 购物车空空如也~
    null_shop_car = (MobileBy.XPATH, '//span[contains(text(),"购物车空空")]')

    # 删除商品图标
    delete = (MobileBy.XPATH, '//wx-image[contains(@class,"icon-delete")]/div')
    
    # 获取价格元素 [一个商品时会获取到两个元素，2个时则4个，以此类推]
    price = (MobileBy.XPATH, '//wx-text[contains(@class,"price-unit")]/parent::span')

    # 获取商品title
    product_name = (MobileBy.XPATH, '//wx-view[contains(@class,"component-shopping-cart-card")]')

    # 获取商品数量
    product_num = (MobileBy.XPATH, '//wx-input[contains(@class,"number")]')

    # 获取商品sku文本信息 (色号：Very Black)
    product_sku_text = (MobileBy.XPATH, '//wx-text[contains(@class,"tag")]//span/following-sibling::span')

    # 获取删除弹窗 确认 按钮
    # confirm = ('aaa', 'new UiSelector().resourceId("com.tencent.mm:id/ffp")')
    # confirm = (MobileBy.XPATH, '//*[contains(text(),"确认")]')
