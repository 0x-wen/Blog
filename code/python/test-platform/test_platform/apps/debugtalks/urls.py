# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 23:53
# @Author  : Jw
# @File    : urls.py
from django.urls import re_path, path
from rest_framework import routers

from . import views

urlpatterns = [
    re_path(r'^debugtalks/$', views.DebugTalksAPIView.as_view()),
    path('debugtalks/<int:pk>/', views.DebugTalksDetailAPIView.as_view()),
]
