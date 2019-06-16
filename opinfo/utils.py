#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午6:56
# @name: utils
# @author：jh

# import markdown
from . import models

from django.utils import timezone

# def get_content_view(content):
#     result = markdown.markdown(content, extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         'markdown.extensions.toc'
#     ])
#     return result.replace("p><img", 'p align="center"><img').replace('"codehilite"', '"codehilite" style="max-width: 650px;height: auto"')


def get_fine_top_like():
    fine = models.Blog.objects.filter(is_fine=True).order_by('-created_at')[:3]
    top = models.Blog.objects.filter(is_top=True).order_by('-created_at')[:3]
    like = models.Blog.objects.order_by("-like")[:5]
    tags = models.Tag.objects.all()
    context = {
        "t_fine": fine[0] if fine else '',
        "is_fine": fine[1:] if fine else '',
        "is_top": top,
        "t_like": like[0] if like else '',
        "like": like[1:] if like else '',
        "tags": tags
    }
    return context


def true_return(data=[], msg="请求成功", code=200):
    return {"data": data,"msg": msg, "code": code}


def false_return(data=[], msg="请求失败", code=-1):
    return {"data": data,"msg": msg, "code": code}


def deal_session(request, pk):
    if not request.session.get(pk):
        request.session[pk] = True
        request.session.set_expiry(60*60*24*7)
        return True
    return False