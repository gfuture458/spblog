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
    path('me/', views.AboutMe.as_view()),
    path('list/', views.ListView.as_view()),
    path('life/', views.LifeView.as_view()),
    path('time/', views.TimeView.as_view()),
    path('gbook/', views.GbookView.as_view()),
    path('info/<bid>', views.InfoView.as_view())
]
