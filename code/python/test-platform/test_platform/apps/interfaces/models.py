from django.db import models

from utils.base_models import BaseModel


# 接口模型类
class Interfaces(BaseModel):
    name = models.CharField(verbose_name='接口名称', help_text='接口名称', max_length=200, unique=True)
    developer = models.CharField(verbose_name='接口开发人员', help_text='接口开发人员', max_length=50,
                                 null=True, blank=True, unique=False)
    tester = models.CharField(verbose_name='测试人员', help_text='测试人员', max_length=50, null=True, blank=True)

    project = models.ForeignKey(to='projects.Projects', on_delete=models.CASCADE, related_name='interfaces',
                                help_text='所属项目')

    desc = models.TextField(verbose_name='接口描述', help_text='接口描述', null=True, blank=True, default='')

    class Meta:
        db_table = 'tb_interfaces'  # 指明数据库表名
        verbose_name = '接口表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
