#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午1:27
# @name: adminx
# @author：jh

from xadmin.layout import Fieldset, Main, Row, Side
from xadmin.plugins.auth import UserAdmin
from .models import Author, Tag, Categoty, Blog, MyBlog, Horselight
from django.utils.translation import ugettext as _
import xadmin

class AuthorAdmin(UserAdmin):
    list_display = ["email", 'username', 'is_staff', 'is_active', 'date_joined']
    readonly_fields = ('date_joined','last_login', 'email', 'is_active', 'is_staff')

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Fieldset(
                    None,
                    "email", 'username', 'is_staff', 'is_active'
                ),
                Fieldset(
                    None,
                    'first_name','groups','last_name',
                    'user_permissions',
                    **{"style": "display:None"}
                )
            )
        return super(UserAdmin, self).get_form_layout()

class CategotyAdmin(object):
    list_display = ["cts", "pre_cts"]


class BlogAdmin(object):
    readonly_fields = ["read", "like"]
    list_display = ('title', 'author', 'cts', 'origin', 'tags', 'read', 'like', 'url')
    style_fields = {"content": "ueditor"}
#     list_display = ["title", "author", "desc", "cts", "tags", "cover", "content", "is_fine", "is_top"]
    # readonly_fields = ('read', 'like')


class HorseLightAdmin(object):
    list_display = ["target", "name"]

xadmin.site.register(Tag)
xadmin.site.register(Categoty, CategotyAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(MyBlog, BlogAdmin)
xadmin.site.register(Author, AuthorAdmin)
xadmin.site.register(Horselight, HorseLightAdmin)
