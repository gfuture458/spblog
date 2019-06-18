#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午1:27
# @name: adminx
# @author：jh

from xadmin.layout import Fieldset, Main, Row, Side
from xadmin.plugins.auth import UserAdmin, get_user_model
from .models import Author, Tag, Categoty, Blog, MyBlog, Horselight, Link
from django.utils.translation import ugettext as _
import xadmin
from xadmin import views

User = get_user_model()


class Base(object):
    site_title = '博客后台管理系统'
    site_footer = '郭家宏的博客'


class TagAdmin(Base):
    pass


class AuthorAdmin(Base, UserAdmin):
    list_display = [ 'username', "email", 'is_staff', 'is_active', 'date_joined']
    readonly_fields = ('date_joined', 'last_login', 'email', 'is_active', 'is_staff')
    style_fields = {"desc": "ueditor"}
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Fieldset(
                    None,
                    "email", 'username', 'is_staff', 'is_active'
                ),
                Fieldset(
                    None,
                    'first_name', 'groups', 'last_name',
                    'user_permissions',
                    **{"style": "display:None"}
                )
            )
        return super(UserAdmin, self).get_form_layout()


class OtherUser(AuthorAdmin):

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Fieldset(
                    None,
                    'username', "email", 'is_staff', 'is_active'
                ),
                Fieldset(
                    None,
                    'first_name', 'groups', 'last_name',
                    **{"style": "display:None"}
                )
            )
        return super(AuthorAdmin, self).get_form_layout()


class CategotyAdmin(Base):
    list_display = ["cts", "pre_cts"]


class BlogAdmin(Base):
    exclude = ["id", "author"]
    readonly_fields = ["read", "like"]
    list_display = ('title', 'author', 'cts', 'tags', 'if_origin', 'read', 'like', 'url')
    style_fields = {"content": "ueditor"}

    #     list_display = ["title", "author", "desc", "cts", "tags", "cover", "content", "is_fine", "is_top"]
    # readonly_fields = ('read', 'like')

    def save_models(self):
        if (not hasattr(self, 'author')) or (self.new_obj.author):
            self.new_obj.author = self.request.user
        self.new_obj.save()


class HorseLightAdmin(Base):
    list_display = ["target", "name"]


class LinkAdmin(Base):
    pass


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Categoty, CategotyAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(MyBlog, BlogAdmin)
xadmin.site.register(Author, AuthorAdmin)
xadmin.site.unregister(User)
xadmin.site.register(User, OtherUser)
xadmin.site.register(Horselight, HorseLightAdmin)
xadmin.site.register(Link, LinkAdmin)

xadmin.site.register(views.CommAdminView, Base)
