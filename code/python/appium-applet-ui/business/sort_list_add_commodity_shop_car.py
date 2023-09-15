# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 16:01
# @Author  :  Jw
# @File    : sort_list_add_commodity_shop_car.py
import time

from handle.applet_index_handle import AppletIndexHandle
from handle.applet_sort_handle import AppletSortHandle
from handle.applet_shop_car_handle import ShopCarHandle
from handle.applet_my_info_handle import MyInfoHandle
from handle.applet_brand_handle import BrandHandle

from test_datas.keyword import Search


class SortListAddCommodityShopCarBusiness(AppletIndexHandle, AppletSortHandle, ShopCarHandle):
    """分类列表添加商品至购物车业务"""

    def add_only_commodity(self, product: int = 0, select_sku: int = 0):
        """
        添加单一商品/和多规格商品 业务操作
        product: 点击下标为int商品 的加入购物车图标(商品搜索列表页，单品直接进入购物车，spu则将进入商品详情页)
        select_sku：选择sku的下标(商品详情页，浮层弹窗sku下标值)
        1.点击菜单导航-分类
        2.选择商品（魅力彩妆/眼部彩妆）
        3.点击第一个商品加入购物车
        4.点击进入购物车
        5.判断是否为spu商品，为spu商品时增加选择sku步骤
        """
        self.do_log.info("进入WEB webview")
        self.switch_to_context()
        self.do_log.info("点击菜单导航-分类")
        self.sort()
        self.do_log.info("点击魅力彩妆")
        self.make_up_click()
        self.do_log.info("点击眼部彩妆")
        self.eyes_make_up_click()
        self.do_log.info("点击下标为0的购物车图标，加入购物车")
        self.add_shop_car_image_click(index=product)

        self.do_log.info("如获取到 商品详情页/加入购物车 元素，则是spu商品 进入了详情页需在选择sku商品")
        one_ele = self.add_shopping_cart
        if one_ele:
            self.do_log.info("点击商品详情底部加入购物车")
            self.add_shopping_cart_click()
            self.do_log.info("选择下标为0的规格商品")
            self.select_skus_click(index=select_sku)
            self.do_log.info("点击浮层中加入购物车")
            self.update_commodity_shop_car_click()

        self.do_log.info("点击购物车图标")
        self.shop_car_click()
        # self.do_log.info("进入结算页，查找去结算按钮")
        # self.count_button_click()
        # time.sleep(3)

    def add_spu_commodity(self, product=1, select_sku=0):
        """:return detail_sku_text：商品详情页sku属性文本，product_sku_text：购物车sku属性文本
        添加多规格商品 业务操作
        product: 点击下标为int商品 的加入购物车图标(商品搜索列表页，单品直接进入购物车，spu则将进入商品详情页)
        select_sku：选择sku的下标(商品详情页，浮层弹窗sku下标值)
        1.点击菜单导航-分类
        2.选择商品（魅力彩妆/眼部彩妆）
        3.点击 product(下标) 商品加入购物车
        4.点击进入购物车,为spu商品时，进入商品详情页
        5.spu商品时增加选择sku步骤，继续下商品规则属性
        6.进入购物车对比 添加商品的规则属性
        """
        self.do_log.info("进入WEB webview")
        self.switch_to_context()
        self.do_log.info("点击菜单导航-分类")
        self.sort()
        self.do_log.info("点击魅力彩妆")
        self.make_up_click()
        self.do_log.info("点击眼部彩妆")
        self.eyes_make_up_click()
        self.do_log.info("点击下标为{}的购物车图标，加入购物车".format(product))
        self.add_shop_car_image_click(index=product)

        self.do_log.info("如获取到 商品详情页/加入购物车 元素，则是spu商品 进入了详情页需在选择sku商品")
        one_ele = self.add_shopping_cart
        if one_ele:
            self.do_log.info("点击商品详情底部加入购物车")
            self.add_shopping_cart_click()
            self.do_log.info("选择下标为{}的规格商品".format(select_sku))
            self.select_skus_click(index=select_sku)

            detail_sku_text = self.sku_attribute_text()
            self.do_log.info("获取商品详情页sku文本信息：{}".format(detail_sku_text))

            self.do_log.info("点击浮层中加入购物车")
            self.update_commodity_shop_car_click()
            self.do_log.info("点击购物车图标")
            self.shop_car_click()

            product_sku_text = self.get_product_sku_text()
            self.do_log.info("获取购物车页面商品sku文本信息：{}".format(product_sku_text))
            return detail_sku_text, product_sku_text
        else:
            self.do_log.error("直接加入购物车，则不是spu商品，请输入下标为spu的商品，此条用例才有实际意思")
            return None

    def clear_shop_car(self):
        """
        清空购物车 业务操作
        1.点击菜单导航-购物车
        2.判断当前页面是否有商品存在
        3.无商品：获取元素 (购物车空)
        4.有商品：获取元素（删除商品）
        """
        self.do_log.info("进入webview")
        self.switch_to_context()
        self.do_log.info("点击菜单导航-购物车")
        self.shopping_card()
        self.do_log.info("获取元素 购物车空空如也~")
        if self.get_null_shop_car_element:
            self.do_log.info("获取到购物车为空的元素信息，此时购物车为空")
        else:
            self.do_log.info("未获取到购物车为空的元素信息，此时还有商品，需要清空")
            time.sleep(self.time_sleep)
            self.delete_click()


class SearchGoodBusiness(AppletIndexHandle, ShopCarHandle, BrandHandle, AppletSortHandle):
    """搜索商品业务"""

    def search_good_keyword(self):
        """
        根据搜索将商品加入购物车
        1.根据搜索关键字搜索商品 Search.search_keyword
        2.点击分类列表页商品
        3.点击 商品详情页 加入购物车
        4.判断购物车有商品信息
        :return 返回商品详情页 特价 和购物车页面 商品价格
        """
        # self.switch_to_context()
        # self.home()
        # self.search_good_click()
        # self.key_word_click()
        # time.sleep(self.time_sleep)
        # self.input_text_value(value=Search.search_keyword)
        # self.do_log.info("点击 搜索商品列表中 第一个图标，进入商品详情页")
        # self.select_info_ele_click()
        # # self.select_hot_search()
        # time.sleep(2)
        # self.commodity_img_click()
        self.go_to_commodity_details()
        self.add_shopping_cart_click()
        special = float(self.get_commodity_special_num)
        self.into_shopping_cart_click()
        price = self.get_price_num
        return special, price

    def go_to_commodity_details(self):
        """封装从首页搜索信息进入商品详情页流程"""
        self.switch_to_context()
        self.home()
        self.search_good_click()
        self.key_word_click()
        time.sleep(self.time_sleep)
        self.input_text_value(value=Search.search_keyword)
        self.do_log.info("点击 搜索商品列表中 第一个图标，进入商品详情页")
        self.select_info_ele_click()
        time.sleep(2)
        self.commodity_img_click()

    def brand_search(self):
        """:return
        品牌下搜索商品 加入购物车
        1.点击首页-品牌
        2.点击搜索框
        3.输入关键字
        4.选择商品 添加至购物车
        """
        self.switch_to_context()
        self.brand()
        time.sleep(self.time_sleep)
        self.brand_search_box_click()
        time.sleep(1)
        self.input_text_value(value=Search.brand_search)
        time.sleep(self.time_sleep)
        self.select_info_ele_click()
        time.sleep(self.time_sleep)
        self.do_log.info("点击下标为0的购物车图标，加入购物车")
        self.add_shop_car_image_click(index=0)
        self.do_log.info("点击购物车图标")
        self.shop_car_click()

    def add_more_commodity_assert_price(self, num: int):
        """
        添加多个商品对比价格
        1.进入首页
        2.点击 面部护肤/选择商品进入详情页
        3.获取商品详情页 名称和价格 并加入购物车
        4.进入购物车页面 获取商品名称和价格
        5.对比 相对应商品的价格和商品一致
        """
        self.switch_to_context()
        self.home()
        self.applet_index_face_click()
        time.sleep(self.time_sleep)
        all_title_and_price = []
        for i in range(num):
            self.do_log.info("选择下标为{}的商品进入 商品详情页".format(i))
            self.face_one_img_click(index=i)
            title_and_price = self.product_title_and_price
            self.do_log.info("获取商品详情页 商品名称:{},和价格:{}".format(title_and_price[1], title_and_price[0]))
            self.do_log.info("将商品详情页中的商品名称和价格加入 all_title_and_price")
            all_title_and_price.append(title_and_price)
            self.do_log.info("将商品加入购物车中")
            self.add_shopping_cart_click()
            self.do_log.info("后退页面")
            self.driver.keyevent(4)
        self.do_log.info("添加完商品之后 退至首页")
        self.driver.keyevent(4)
        time.sleep(self.time_sleep)
        self.do_log.info("点击菜单导航-购物车")
        self.shopping_card()
        all_name_add_price = self.price_and_name_group

        new_name_add_price = self.handle_name_price(all_name_add_price)

        for j in all_title_and_price:
            if j not in new_name_add_price:
                return False
            else:
                continue

        return True

    def update_commodity_num_business(self):
        """
        详情页更改商品数量业务
        1.清空购物车商品
        2.从首页搜索商品进入商品详情页
        3.更改商品数量 +2 -1 （初始值为1）
        4.进入购物车对比商品数量
        """
        self.do_log.info("点击 搜索商品列表中 第一个图标，进入商品详情页")
        self.go_to_commodity_details()
        self.update_commodity_num_click()
        self.add_num_click(index=2)
        self.sub_num_click(index=1)
        time.sleep(self.time_sleep)
        self.update_commodity_shop_car_click()
        self.do_log.info("点击 进入购物车图标 进入购物车页面")
        self.into_shopping_cart_click()

    def update_num_shopping_car(self):
        """
        购物车页面更改商品数量业务
        1.清空购物车商品
        2.从首页搜索商品进入商品详情页
        3.添加商品至购物车
        4.判断是否为spu商品,是则选择sku商品加入购物车
        5.在购物车页面 增加商品数量
        """
        self.do_log.info("点击 搜索商品列表中 第一个图标，进入商品详情页")
        self.go_to_commodity_details()

        time.sleep(self.time_sleep)

        self.do_log.info("点击商品详情底部加入购物车")
        self.add_shopping_cart_click()

        try:
            self.do_log.info("点击加入购物车之后，查看是否为spu商品，如果是则再次选择sku，不是则为None")
            select_sku = self.select_skus_click(index=0)
        except TypeError as e:
            self.do_log.error("None 类型不能click, 具体错误为{}".format(e))
            select_sku = None

        if select_sku:
            self.do_log.info("是spu商品的情况：需要选择下标为0的规格商品")
            self.select_skus_click(index=0)
            self.do_log.info("点击浮层中加入购物车")
            self.update_commodity_shop_car_click()

        self.do_log.info("点击 进入购物车图标 进入购物车页面")
        self.into_shopping_cart_click()
        self.add_num_click(index=1)


class FavoriteBusiness(MyInfoHandle, AppletIndexHandle):
    """收藏夹/地址业务"""

    def favorite_clear(self):
        """
        清空收藏夹
        1.进入收藏夹 判断是否存在商品
        2.存在商品则进行删除
        """
        self.switch_to_context()
        self.my_info()
        self.favorite_click()
        self.do_log.info("获取元素 您还没收藏商品")
        if self.no_favorite:
            self.do_log.info("获取到收藏夹为空的元素信息，此时收藏夹为空")
            return True
        else:
            self.do_log.info("未获取到收藏夹为空的元素信息，此时收藏夹还有商品，需要清空")
            clear_bool = self.delete_favorite()
            return clear_bool

    def add_commodity_favorite(self, index=0):
        """:return
        将商品添加至收藏夹
        1.进入菜单导航-首页
        2.点击面部护肤
        3.点击商品进入商品详情页
        4.收藏至收藏夹
        5.回到首页-回到我的-点击收藏夹 验证删除图标存在
        """
        self.switch_to_context()
        self.home()
        self.applet_index_face_click()
        time.sleep(self.time_sleep)
        self.face_one_img_click(index=index)
        self.favorite_button_click()
        self.do_log.info("点击返回首页")
        self.return_index_click()
        time.sleep(self.time_sleep)
        self.my_info()
        self.favorite_click()

    def delete_collect(self):
        """
        删除收藏商品
        1.进入菜单导航-首页
        2.点击面部护肤
        3.点击商品进入商品详情页
        4.收藏至收藏夹
        5.回到首页-回到我的-点击收藏夹
        6.删除收藏夹内商品，全部删除返回True
        """
        self.add_commodity_favorite(index=2)
        self.do_log.info("获取元素 您还没收藏商品")
        if self.no_favorite:
            self.do_log.info("获取到收藏夹为空的元素信息，此时收藏夹为空")
            return True
        else:
            self.do_log.info("未获取到收藏夹为空的元素信息，此时收藏夹还有商品，需要清空")
            clear_bool = self.delete_favorite()
            return clear_bool

    def add_my_address(self):
        """:return
        添加我的地址
        1.进入菜单导航-我的
        2.点击我的地址
        3.
        """
        self.switch_to_context()
        time.sleep(self.time_sleep)
        self.my_info()
        self.my_address_click()
        self.add_address_click()
        # self.consignee_input_box_click()
        # self.input_text_value(value='zhangsan')
        # self.detailed_address_click()
        # self.input_text_value(value='shenzhenaaa')
        # self.phone_number_click()
        # self.input_text_value(value="15055555555")
        # self.mailbox_click()
        # self.input_text_value(value="55555555@qq.com")

        self.area_click()
        self.country_click()
        time.sleep(self.time_sleep)
        self.province_click()
        self.city_click()
        self.district_click()
        time.sleep(10)


if __name__ == '__main__':
    from tools.base_driver import android_driver
    from handle.wx_index_handle import WXIndexHandle

    driver = android_driver()
    wx_index = WXIndexHandle(driver=driver)
    # driver1 = SortListAddCommodityShopCarBusiness(driver=driver)
    # driver2 = SearchGoodBusiness(driver=driver)
    driver3 = FavoriteBusiness(driver=driver)

    wx_index.click_applet_name()
    # driver1.clear_shop_car()
    # driver1.add_only_commodity()
    # driver2.search_good_keyword()
    # driver3.add_commodity_favorite()
    # bool_value = driver2.add_more_commodity_assert_price(num=3)
    # print(bool_value)
    # driver2.update_num_shopping_car()
    # driver2.update_commodity_num_business()
    driver3.delete_collect()
    # driver3.add_my_address()
