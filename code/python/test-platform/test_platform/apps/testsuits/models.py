from django.db import models

from utils.base_models import BaseModel


class TestSuits(BaseModel):
    name = models.CharField(verbose_name='套件名称', help_text='套件名称', max_length=100, unique=True)
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, related_name='testsuits',
                                help_text='所属项目')

    include = models.TextField('包含接口', null=False, help_text='包含接口')

    class Meta:
        db_table = 'tb_testsuits'  # 指明数据库表名
        verbose_name = '测试套件表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
