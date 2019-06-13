# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.


class Info(View):
    def get(self, request, *args, **kwargs):
        # data = {
        #     "title": "首页_杨青个人博客 - 一个站在web前端设计之路的女技术员个人博客网站",
        #     "keywords": "个人博客,杨青个人博客,个人博客模板,杨青",
        #     "description": "杨青个人博客，是一个站在web前端设计之路的女程序员个人网站，提供个人博客模板免费资源下载的个人原创网站。"
        # }
        return render(request, 'index.html')


class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class ListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'list.html')


class LifeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'life.html')


class TimeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'time.html')


class GbookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gbook.html')


class InfoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'info.html')