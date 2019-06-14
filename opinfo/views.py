# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic import View
from . import models, utils
from django.core.paginator import Paginator, Page

# Create your views here.


class Info(View):
    model = models.Blog
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.order_by("-created_at")
        horse = models.Horselight.objects
        sider = utils.get_fine_top_like()
        context = {
            "blog": query_list,
            "top": {
                "left": horse.filter(name="A"),
                "right": horse.filter(name="B")
            },
            "sider": sider,
            "art": True
        }
        return render(request, 'index.html', context=context)


class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class ListView(View):
    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(cts__pre_cts="A")
        sider = utils.get_fine_top_like()
        context = {
            "blog": blogs,
            "sider": sider
        }
        return render(request, 'list.html', context)


class LifeView(View):
    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(cts__pre_cts="B")
        sider = utils.get_fine_top_like()
        comtext = {
            "sider": sider,
            "blog": blogs
        }
        return render(request, 'life.html', context=comtext)


class TimeView(View):
    model = models.Blog
    def get(self, request, *args, **kwargs):
        blogs = self.model.objects.all()
        return render(request, 'time.html', context={"blogs": blogs, "time": True})


class GbookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gbook.html')


class InfoView(View):
    model = models.Blog
    def get(self, request, *args, **kwargs):
        query = self.model.objects.filter(id=kwargs.get("bid")).first()
        sider = utils.get_fine_top_like()
        query.content = utils.get_content_view(query.content)
        query.read += 1
        query.save(update_fields=("read",))
        return render(request, 'info.html', context={"blog": query,'sider':sider, 'xq': True})

    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        return