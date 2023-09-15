from django.db import models

from utils.base_models import BaseModel


class Reports(BaseModel):
    name = models.CharField(verbose_name='报告名称', help_text='报告名称', max_length=200, unique=True)
    result = models.BooleanField(verbose_name='执行结果', help_text='执行结果', default=1)
    count = models.IntegerField(verbose_name='用例总数', help_text='用例总数')
    success = models.IntegerField(verbose_name='成功总数', help_text='成功总数')
    html = models.TextField(verbose_name='报告源码', help_text='报告源码', null=True, blank=True, default='')
    summary = models.TextField('报告详情', help_text='报告详情', null=True, blank=True, default='')

    class Meta:
        db_table = 'tb_reports'  # 指明数据库表名
        verbose_name = '测试报告'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
