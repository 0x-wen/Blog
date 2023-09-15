# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 16:50
# @Author  : JW
# @FileName: vip_index_locator.py
"""
from selenium.webdriver.common.by import By


class VipIndexLocator:
    """vip后台主页、会员卡管理元素定位"""
    # 验证跳转会员后台成功
    vip_background_check = (By.XPATH, '//*[@class="no-redirect"]')

    # 添加会员卡按钮
    add_vip_card = (By.XPATH, '//span[contains(text(),"添加会员卡")]')

    # 导航栏/会员活动管理
    members_activity_management = (By.XPATH, '//*[contains(text(),"会员活动管理")]/parent::div')
    # 会员活动管理/扫码领会员
    scan_code_members = (By.XPATH, '//*[contains(text(),"扫码领会员")]/parent::li')
    # 扫码领会员/添加活动
    add_activity = (By.XPATH, '//*[contains(text(),"添加活动")]/parent::button')
    # 添加活动、活动名称
    activity_name = (By.XPATH, '//*[@for="actName"]/following-sibling::div//input')
    # 添加活动、活动时间
    start_time = (By.XPATH, '//*[@placeholder="开始时间"]')
    end_time = (By.XPATH, '//*[@placeholder="结束时间"]')
    # 时间填写完点击其他区域收起控件
    pack_up = (By.XPATH, '//span[@class="no-redirect"]/..')
    # 添加活动、背景图
    background = (By.XPATH, '//*[contains(text(),"上传图片")]/..')
    background_ok = (By.XPATH, '//div[@class="save__btn"]/button')
    # 添加活动、活动规则
    activity_rules = (By.XPATH, '//textarea[@class="el-textarea__inner"]')
    # 添加活动、奖品设置
    prize_set = (By.XPATH, '//*[contains(text(),"奖品设置")]/../..')
    # 添加活动、选择会员卡
    choose_members_card = (By.XPATH, '//*[@for="vipCardId"]//following-sibling::div//button')
    # 添加活动、选择会员卡、确定(默认选择第一张会员卡)
    ok_button = (By.XPATH, '//span[contains(text(),"确")]/..')
    # 添加活动、投放数量
    number = (By.XPATH, '//*[@for="stockTotal"]/following-sibling::div//input')
    # 添加活动、保存按钮
    save = (By.XPATH, '//div[@class="btns"]//span[contains(text(),"保存")]/..')
    # 验证添加活动成功定位
    add_activity_succeed = (By.XPATH, '//p[@class="el-message__content" and contains(text(),"活动")]')


