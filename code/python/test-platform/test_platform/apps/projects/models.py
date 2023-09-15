from django.db import models

from utils.base_models import BaseModel


# 项目模型类
class Projects(BaseModel):
    name = models.CharField(verbose_name='项目名称', help_text='项目名称', max_length=100, unique=True)
    leader = models.CharField(verbose_name='项目负责人', help_text='项目负责人', max_length=50, null=True, blank=True)
    developer = models.CharField(verbose_name='开发人员', help_text='开发人员', max_length=50, null=True, blank=True)
    tester = models.CharField(verbose_name='测试人员', help_text='测试人员', max_length=50, null=True, blank=True)
    # is_build = models.BooleanField(verbose_name='是否构建', help_text='是否构建', default=False)
    publish_app = models.CharField('发布应用', max_length=100, help_text='发布应用')

    desc = models.TextField(verbose_name='项目描述', help_text='项目描述', null=True, blank=True, default='')

    class Meta:
        db_table = 'tb_projects'  # 指明数据库表名
        verbose_name = '项目表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
