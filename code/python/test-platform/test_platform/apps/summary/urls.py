# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 23:53
# @Author  : Jw
# @File    : urls.py
from django.urls import path, re_path
from rest_framework import routers

from . import views

urlpatterns = [
    path('summary/', views.SummaryView.as_view()),
]
