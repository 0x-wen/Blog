# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 22:58
# @Author  : Jw
# @File    : base_models.py
from django.db import models


# 接口模型类
class BaseModel(models.Model):
    id = models.BigAutoField(verbose_name='主键ID', help_text='主键ID', primary_key=True)

    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', help_text='修改时间', auto_now=True)

    class Meta:
        # 指定当前类为抽象模型类，数据迁移不会生成一张表
        abstract = True
