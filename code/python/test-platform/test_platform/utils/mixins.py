# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 20:39
# @Author  : Jw
# @File    : mixins.py


from rest_framework.decorators import action


class NamesMixin:

    @action(methods=['get'], detail=False, url_path='names', url_name='names')  # 自动注册 自定义的路由信息
    def names(self, request, *args, **kwargs):
        """获取ID和名称"""
        return super().list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        return self.get_queryset() if self.action == 'names' else super().filter_queryset(queryset)

    def paginate_queryset(self, queryset):
        return None if self.action == 'names' else super().paginate_queryset(queryset)
