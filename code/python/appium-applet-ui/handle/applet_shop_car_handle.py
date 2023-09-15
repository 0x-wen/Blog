# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 15:54
# @Author  :  Jw
# @File    : applet_shop_car_handle.py
import time

from element_pages.applet_shop_car_page import ShopCarPage


class ShopCarHandle(ShopCarPage):
    """购物车 操作处理"""

    @property
    def get_null_shop_car_element(self):
        """获取到购物车为空的元素信息"""
        return self.null_shop_car()

    @property
    def get_price_num(self):
        """获取购物车价格数值"""
        price_str = self.get_price_element[1].text
        price_list = list(price_str)[1:]
        var = float("".join(price_list))
        return var

    @property
    def price_and_name_group(self):
        """将购物车中 价格和名称 组合在一起"""
        name_elements = self.get_product_name
        name_len = len(name_elements)
        price_add_name = []
        for i in range(name_len):
            # 循环取值 购物车中的名称和价格
            one_name = name_elements[i].text
            one_price = self.get_price_element[(i * 2) + 1].text
            price_add_name.append([one_name, one_price])
            pass
        return price_add_name

    @staticmethod
    def handle_name_price(all_name_add_price: list):
        """处理一下从购物车获取到的名称和价格"""
        var = []
        for j in all_name_add_price:
            name_split = j[0].split("\n")
            name = name_split[0]
            price = "".join(list(j[1]))[1:]
            var.append((price, name))
        return var

    def delete_click(self):
        """点击删除商品图标"""
        self.do_log.info("获取购物车删除图标")
        time.sleep(self.time_sleep)
        try:
            more_elements = self.delete()
        except TypeError as e:
            self.do_log.info("没有获取到购物车内删除图标，具体错误为{}".format(e))
            time.sleep(self.time_sleep)
            more_elements = self.delete()

        len_more_elements = len(more_elements)
        self.do_log.info("购物车存在的商品信息：%d 个" % len_more_elements)
        while len_more_elements > 0:
            self.do_log.info("删除购物车内第一个商品")
            more_elements[0].click()
            self.do_log.info("# 点击弹窗 确定删除")
            self.confirm()
            self.do_log.info("# 重新获取窗口中删除商品的个数")

            time.sleep(self.time_sleep)

            more_elements = self.delete()
            time.sleep(self.time_sleep)
            if more_elements:
                len_more_elements -= 1
                self.do_log.info("# 购物车中还剩下%d 个商品" % len_more_elements)
            else:
                self.do_log.info("# 已清空购物车内所有商品")
                len_more_elements = 0

    @property
    def get_product_num(self):
        """获取购物车商品个数"""
        product_num_text = self.product_num.text
        return product_num_text

    def get_product_sku_text(self):
        """获取购物车 商品sku属性 文本"""
        product_sku_text_all = self.product_sku_text.text
        product_sku_text_list = product_sku_text_all.split("：")
        return product_sku_text_list[-1]
