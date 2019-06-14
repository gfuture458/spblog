# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from . import utils
# Create your views here.


class Info(View):
    model = models.Blog
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.all().order_by("-created_at")
        horse = models.Horselight.objects.all()
        context = {
            "blog": query_list,
            "top": {
                "left": horse.filter(name="A"),
                "right": horse.filter(name="B")
            },
            "art": True
        }
        return render(request, 'index.html', context=context)


class AboutMe(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class ListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'list.html')


class LifeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'life.html')


class TimeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'time.html')


class GbookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gbook.html')


class InfoView(View):
    model = models.Blog
    def get(self, request, *args, **kwargs):
        query = self.model.objects.filter(id=kwargs.get("bid")).first()
        query.content = utils.get_content_view(query.content)
        return render(request, 'info.html', context={"blog": query, 'xq': True})