# coding: utf-8
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views.generic import View
from . import models, utils
from DjangoUeditor.forms import UEditorField
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

    def get(self, request, bid,*args, **kwargs):
        query = self.model.objects.filter(pk=bid).first()
        query.content = query.content.replace('<img', '<img class="myimg"')
        sider = utils.get_fine_top_like()
        query.read += 1
        query.save(update_fields=("read",))
        next = self.model.objects.filter(created_at__gt=query.created_at, is_active=True).order_by('-created_at').first()
        prev = self.model.objects.filter(created_at__lt=query.created_at, is_active=True).order_by('-created_at').first()

        # 根据标签查找相关文章
        others = self.model.objects.exclude(pk=query.id).filter(tags__name__in=[x.name for x in query.tags.all()])[:10]
        context = {
            "blog": query,
            "sider": sider,
            "xq": True,
            "next": next,
            "prev": prev,
            "others": others
        }
        return render(request, 'info.html', context=context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("bid")
        not_like_ever = utils.deal_session(request, pk)
        if not_like_ever:
            blog = self.model.objects.filter(pk=pk).first()
            blog.like += 1
            blog.save(update_fields=("like", ))
            return JsonResponse(utils.true_return(msg="点赞成功"))
        return JsonResponse(utils.false_return(msg="您已点过赞"))
