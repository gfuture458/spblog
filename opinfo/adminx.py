#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 19-6-13 下午1:27
# @name: adminx
# @author：jh

from xadmin.layout import Fieldset, Main, Row, Side
from xadmin.plugins.auth import UserAdmin
from .models import Author
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

xadmin.site.register(Author, AuthorAdmin)