"""spblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, re_path
from . import settings
from django.views.static import serve
from django.conf.urls.static import static
import xadmin
from . import views
from xadmin.plugins import xversion
xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    path("xadmin/", xadmin.site.urls),
    path('xadmin/opinfo/author/<uid>/password/', views.reset_password),
    # url(r'mdeditor/', include('mdeditor.urls')),
    url(r'ueditor/', include("DjangoUeditor.urls")),
    path("", include('opinfo.urls')),
    re_path('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='uploads'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

