from django.db import models

from utils.base_models import BaseModel


class Envs(BaseModel):
    name = models.CharField(verbose_name='环境名称', help_text='环境名称', max_length=100, unique=True)
    base_url = models.URLField(verbose_name='', help_text='', max_length=200)
    desc = models.CharField(verbose_name='描述', max_length=200, help_text='描述')

    class Meta:
        db_table = 'tb_envs'  # 指明数据库表名
        verbose_name = '环境信息'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
