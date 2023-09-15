from django.db import models

from utils.base_models import BaseModel


class TestCases(BaseModel):
    name = models.CharField(verbose_name='用例名称', help_text='用例名称', max_length=100, unique=True)
    interface = models.ForeignKey(to='interfaces.Interfaces', on_delete=models.CASCADE, help_text='所属接口',
                                  related_name='testcases', )
    author = models.CharField(verbose_name='编写人员', help_text='编写人员', max_length=50)

    setup = models.TextField(verbose_name='用例前置', help_text='用例前置', null=True, blank=True)
    request = models.TextField(verbose_name='请求信息', help_text='请求信息')
    teardown = models.TextField(verbose_name='用例后置', help_text='用例后置', null=True, blank=True, default='')

    class Meta:
        db_table = 'tb_testcases'  # 指明数据库表名
        verbose_name = '用例表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
