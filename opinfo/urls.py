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
    # path('me/', views.AboutMe.as_view()), # 关于我
    path('language', views.LanguageView.as_view()), # 编程语言
    path('study', views.StudyView.as_view()), # 学习笔记
    path('life', views.LifeView.as_view()), # 日常生活
    path('time', views.TimeView.as_view()), # 时间轴
    path('gbook', views.GbookView.as_view()), # 留言板
    path('info/<bid>', views.InfoView.as_view()), # 文章详情
    path('sub_info/<cid>', views.SubInfoView.as_view()), # 二级文章列表详情

    path('get_tag/<tid>', views.GetTagView.as_view()),# 获取标签博客

    path('get_tag_name/<name>', views.GetTagNameView.as_view()), # 获取标签博客

    path('add_link/', views.LinkView.as_view()), # 添加

    path('web_exist/', views.web_name_exist)
]
