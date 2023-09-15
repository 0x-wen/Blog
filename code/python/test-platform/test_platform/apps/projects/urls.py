# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 23:53
# @Author  : Jw
# @File    : urls.py
from django.urls import path, re_path
from rest_framework import routers

from . import views

# 1.创建路由对象
router = routers.SimpleRouter()
# router = routers.DefaultRouter()
# 2.注册路由
# 使用视图集中的路由机制，只会为特定的action生成路由
# 自定义的action不会自动生成路由条目，需要手动添加 或 导入action 在自定义action上添加装饰器
router.register(r'projects', viewset=views.ProjectsViewSet)

urlpatterns = [
    # re_path(r'^projects/$', views.ProjectsViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'patch': 'partial_update',
    #     'delete': 'destroy',
    # })),
    # path('one/', views.OneActionInterface.as_view({
    #     'post': 'create'
    # })),
    # path('two/<int:pk>/', views.TwoActionInterface.as_view()),
]

# 3.添加路由
urlpatterns += router.urls
