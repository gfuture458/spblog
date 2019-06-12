from django.contrib import admin
import xadmin
# Register your models here.

from .models import *

xadmin.site.register(Article)
