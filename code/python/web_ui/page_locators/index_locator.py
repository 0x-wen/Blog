# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 14:47
# @Author  : JW
# @FileName: index_locator.py
"""
from selenium.webdriver.common.by import By


class IndexLocator:
    """主页元素定位"""
    # 右上角账户名称定位
    username = (By.XPATH, '//div[@role="button"]')
    # 导航栏/会员后台定位
    vip_background = (By.XPATH, '//span[contains(text(),"会员后台")]')

    # 导航栏/商家管理定位
    shop_management = (By.XPATH, '//span[contains(text(),"商家管理")]')
    # 商家管理/已认证商家定位
    pass_shop = (By.XPATH, '//span[contains(text(),"已认证商家")]')
    # 商家管理/已认证商家/添加店铺
    add_shop = (By.XPATH, '//span[contains(text(),"添加店铺")]')
    # 添加店铺、店铺名称
    shop_name = (By.XPATH, '//*[@for="shopName"]//following-sibling::div//input')
    # 添加店铺、店铺经营地址
    shop_area = (By.XPATH, '//*[@class="select_area"]/span')
    # 添加店铺、店铺经营地址，选择城市
    choose_city = (By.XPATH, '//ul[@class="el-cascader-menu"]/li[contains(text(),"北京")]')
    # 添加店铺、店铺经营地址，选择区域
    choose_area = (By.XPATH, '//ul[@class="el-cascader-menu"]/li[contains(text(),"东城")]')
    # 添加店铺、详细地址
    shop_detailed_address = (By.XPATH, '//div[contains(@class,"el-textarea")]/textarea')
    # 添加店铺、店铺经营范围
    shop_business_scope = (By.XPATH, '//*[@class="management_scope_box"]/span')
    # 添加店铺、店铺经营范围，选择分类
    shop_business_scope_1 = (By.XPATH, '//*[@class="el-cascader-menu"]/li[contains(text(),"餐饮")]')
    # 添加店铺、店铺经营范围，选择分类
    shop_business_scope_2 = (By.XPATH, '//*[@class="el-cascader-menu"]/li[contains(text(),"火锅")]')
    # 添加店铺、店铺经营范围，选择分类
    shop_business_scope_3 = (By.XPATH, '//*[@class="el-cascader-menu"]/li[contains(text(),"牛肉火锅")]')
    # 添加店铺、靠近信息
    near = (By.XPATH, '//*[contains(text(),"靠近")]//following-sibling::div//input')
    # 添加店铺、获取精准坐标
    precise_coordinates = (By.XPATH, '//span[contains(text(),"获取精准坐标")]')
    # 页面在这里需要拖动窗口
    # 添加店铺、所属商圈
    business_circle = (
    By.XPATH, '//*[contains(text(),"所属商圈")]//following-sibling::div//span[contains(@class,"el-cascader--mini")]')
    # 添加店铺、附近地标
    near_landmark = (
    By.XPATH, '//*[contains(text(),"附近地标")]//following-sibling::div//span[contains(@class,"el-cascader--mini")]')
    # 添加店铺、统一社会信用代码
    social_credit_code = (By.XPATH, '//*[contains(text(),"工商注册信息")]/preceding-sibling::div//input')
    # 上传插图
    # upload = (By.XPATH, '//*[@class="el-upload__input"]')
    upload = (By.XPATH, '//*[@class="el-upload__input"]/preceding-sibling::button')

    # 添加店铺、保存，下一步
    save = (By.XPATH, '//*[contains(text(), "保存")]')
    # 上传店铺LOGO
    logo = (By.XPATH, '//*[contains(text(),"LOGO")]/parent::button/following-sibling::input')
    # 图片裁剪保存按钮
    btn = (By.XPATH, '//*[@class="save__btn"]/button')
    # 添加店铺详情图
    # details_picture = (By.XPATH, '//*[contains(text(),"+")]/parent::button/following-sibling::input')
    details_picture = (By.XPATH, '//*[contains(text(),"+")]/parent::button')
    btn_2 = (By.XPATH, '//img[contains(@class,"cropper-hidden")]/following-sibling::div//button')
    btn_3 = (By.XPATH, '//div[contains(@class,"el-dialog__wrapper")]//img[contains(@class,"cropper-hidden")]/following-sibling::div//button')
    # 人均消费
    consumption = (By.XPATH, '//label[@for="perCapita"]//following-sibling::div//input')
    # 经营电话
    telephone = (By.XPATH, '//label[@for="telephone"]//following-sibling::div//input')
    # 营业时间
    business_hours = (By.XPATH, '//input[@value="1" and @type="checkbox"]/preceding-sibling::span')
    business_hours_2 = (By.XPATH, '//input[@value="1" and @type="radio"]/preceding-sibling::span')
    # 推荐理由
    recommended_reasons = (By.XPATH, '//textarea[@class="el-textarea__inner"]')
    # 详细介绍
    detailed_introduction = (By.XPATH, '//div[contains(@class,"um-editor")]')
    # 保存
    save_all = (By.XPATH, '//div[@class="btn_box"]/button')
    # 添加成功之后验证元素
    add_shop_pass = (By.XPATH, '//span[contains(text(),"返回已认证商家")]')
 

