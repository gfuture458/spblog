#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-12 下午1:37
# @name: urls
# @author：jh

from django.urls import path
from opinfo import views

from xadmin.plugins import xversion

urlpatterns = [
    path('', views.Info.as_view()),
]
