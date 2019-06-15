#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午6:56
# @name: utils
# @author：jh

import markdown
from . import models


def get_content_view(content):
    result = markdown.markdown(content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return result


def get_fine_top_like():
    fine = models.Blog.objects.filter(is_fine=True).order_by('-created_at')[:3]
    top = models.Blog.objects.filter(is_top=True).order_by('-created_at')[:3]
    like = models.Blog.objects.order_by("-like")[:5]
    tags = models.Tag.objects.all()
    print(fine)
    context = {
        "t_fine": fine[0] if fine else '',
        "is_fine": fine[1:] if fine else '',
        "is_top": top,
        "t_like": like[0] if like else '',
        "like": like[1:] if like else '',
        "tags": tags
    }
    return context
