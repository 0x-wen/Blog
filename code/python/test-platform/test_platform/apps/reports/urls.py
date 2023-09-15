# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 23:53
# @Author  : Jw
# @File    : urls.py
from django.urls import re_path, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'reports', viewset=views.ReportsViewSet)

urlpatterns = [
]
urlpatterns += router.urls
