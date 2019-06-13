#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午2:07
# @name: views
# @author：jh

from django.shortcuts import redirect

def reset_password(request, uid):
    uri = 'xadmin/'
    if request.user.is_authenticated:
        uri = '/xadmin/account/password/'
    return redirect(uri)