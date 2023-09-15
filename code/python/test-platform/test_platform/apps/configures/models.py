from django.db import models

from utils.base_models import BaseModel


class Configures(BaseModel):
    name = models.CharField(verbose_name='配置名称', help_text='配置名称', max_length=100, unique=True)
    interface = models.ForeignKey(to='interfaces.Interfaces', on_delete=models.CASCADE, related_name='configures',
                                  help_text='所属接口')
    author = models.CharField(verbose_name='编写人员', help_text='编写人员', max_length=50)

    request = models.TextField(verbose_name='请求信息', help_text='请求信息')

    class Meta:
        db_table = 'tb_configures'  # 指明数据库表名
        verbose_name = '配置表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
