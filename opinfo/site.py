#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-12 下午3:49
# @name: site
# @author：jh

from . import models
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


def head_info(request):
    """站点head信息"""
    site = {
        "abname": "dancesmile | 郭家宏",
        "title": "郭家宏的博客",
        "keywords": "个人博客,郭家宏的博客,郭家宏个人博客,郭家宏",
        "description": "郭家宏个人博客，是一个站在web后端进阶之路的程序员个人网站，记录博主学习和成长，关注各种后端技术的学习和研究。",
        "abposition": "Web后端工程师",
        "abtext": "短暂的生命，走走停停。有趣的灵魂，疯言疯语。时间让一切过于梦幻，零星的记忆总会和当前交织起来，似曾相识却又无从回忆。"
                  "所以在此，记录生活和学习的点点滴滴。"
    }
    return site


User = get_user_model()


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user:
            if user.check_password(password):
                return user
        return None
