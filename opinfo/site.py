#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-12 下午3:49
# @name: site
# @author：jh

from . import models

def head_info(request):
    """站点head信息"""
    site = {
        "title": "郭家宏的博客",
        "keywords": "个人博客,郭家宏个人博客,郭家宏",
        "description": "杨青个人博客，是一个站在web前端设计之路的女程序员个人网站，提供个人博客模板免费资源下载的个人原创网站。"
    }
    return site
