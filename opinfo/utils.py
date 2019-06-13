#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午6:56
# @name: utils
# @author：jh

import markdown


def get_content_view(content):
    result = markdown.markdown(content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return result