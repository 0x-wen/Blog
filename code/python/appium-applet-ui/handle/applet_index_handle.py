# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 11:39
# @Author  :  Jw
# @File    : applet_index_handle.py
import time

from element_pages.applet_index_page import AppletIndexPage


class AppletIndexHandle(AppletIndexPage):
    """小程序主页 操作处理"""

    def applet_index_face_click(self):
        """点击小程序主页 面部护肤元素"""
        self.do_log.info("点击小程序主页元素, 点击面部护肤")
        self.applet_index_face[0].click()

    def face_one_img_click(self, index: int):
        """点击小程序主页 面部护肤元素
        index: 选择元素坐标
        """
        self.do_log.info("点击面部护肤/第{}个商品信息".format(index))
        if index == 0:
            self.face_one_img[index].click()
        elif index == 1:
            # 具体页面的元素定位方式有点奇怪，需要+1才能定位到下一个图标点击
            self.face_one_img[index + 1].click()
        else:
            # 具体页面的元素定位方式有点奇怪，需要+2才能定位到下一个图标点击
            self.face_one_img[index + 2].click()

    def applet_menu(self):
        """点击小程序菜单导航"""
        self.home()
        self.sort()
        self.brand()
        self.shopping_card()
        self.my_info()

    def search_good_click(self):
        """点击搜索商品"""
        self.search_good.click()

    def key_word_click(self):
        """点击输入关键字"""
        self.key_word.click()

        # select_js = """
        # function getElementByXpath(path) {
        #   return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        # }
        # ele = getElementByXpath(arguments[0]);
        # ele.readOnly = false;
        # ele.value = arguments[1];
        # """
        # self.driver.execute_script(select_js, '//wx-input[@confirm-type="search"]', '22')

    def select_hot_search(self):
        """点击热门搜索下的关键字 默认点击第一个"""
        self.get_hot_search_value.click()

    def select_info_ele_click(self):
        """点击搜索信息项 第一个"""
        self.select_info_element.click()

    def commodity_img_click(self):
        """搜索列表页/商品图标信息 默认点击第一个"""
        time.sleep(self.time_sleep)
        self.do_log.info("搜索列表页/商品图标信息 默认点击第一个")
        commodity_elements = self.commodity_s_img
        commodity_elements[0].click()

    def add_shopping_cart_click(self):
        """点击底部加入购物车按钮"""
        self.add_shopping_cart.click()

    def into_shopping_cart_click(self):
        """点击进入购物车图标"""
        self.into_shopping_cart.click()

    @property
    def get_commodity_special_num(self):
        """获取商品特价元素-金额"""
        special = self.get_commodity_special_element[1].text
        return special

    @property
    def get_product_title(self):
        """获取商品标题名称"""
        product_title = self.product_title.text
        return product_title

    @property
    def product_title_and_price(self):
        """获取到商品详情页面的 商品名称和特价"""
        special = self.get_commodity_special_num
        title = self.get_product_title
        return special, title

    def update_commodity_num_click(self):
        """点击 更改商品数量元素"""
        self.update_commodity_num.click()

    def add_num_click(self, index: int):
        """点击 增加商品元素"""
        for _ in range(index):
            self.add_num.click()

    def sub_num_click(self, index: int):
        """点击 减少商品元素"""
        for _ in range(index):
            self.sub_num.click()

    def select_skus_click(self, index: int):
        """选择商品规格(sku)元素"""
        more_skus_element = self.select_skus
        return more_skus_element[index].click()

    def sku_attribute_text(self):
        """获取商品sku属性文本信息"""
        sku_text_all = self.sku_attribute.text
        sku_text = sku_text_all.split("，")
        return sku_text[0]

    def update_commodity_shop_car_click(self):
        """点击 浮层中加入购物车 元素"""
        self.update_commodity_shop_car.click()

    def to_pay_click(self):
        """确认订单页/去支付"""
        one_element = self.to_pay
        one_element.click()

    def obligation_click(self):
        """我的订单/点击待付款导航"""
        self.obligation.click()

    def obligation_data_click(self):
        """待付款导航下/ 点击取消订单元素"""
        return self.obligation_data.click()

    def complete_click(self):
        """我的订单/全部导航"""
        self.complete.click()
