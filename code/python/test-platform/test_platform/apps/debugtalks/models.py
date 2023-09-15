from django.db import models

from utils.base_models import BaseModel


class DebugTalks(BaseModel):
    name = models.CharField(verbose_name='debugtalk文件名称', help_text='debugtalk文件名称', max_length=100,
                            default='debugtalk.py')
    debugtalk = models.TextField(null=True, default='#debugtalk.py', help_text='debugtalk.py文件')
    project = models.OneToOneField('projects.Projects', on_delete=models.CASCADE, related_name='debugtalks',
                                   help_text='所属项目')

    class Meta:
        db_table = 'tb_debugtalks'  # 指明数据库表名
        verbose_name = 'debugtalk.py文件'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
