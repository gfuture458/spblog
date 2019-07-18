# coding: utf-8
from django.shortcuts import render, redirect, render_to_response
from django.http.response import JsonResponse, Http404
from django.views.generic import View
from . import models, utils

# Create your views here.


class Info(View):
    model = models.Blog

    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.filter(is_active=True).order_by("-created_at")
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
        user = models.UserAccount.objects.filter(is_superuser=True).first()
        user.desc = user.desc.replace('<img', '<img class="myimg"')
        context = {
            "my": user
        }
        return render(request, 'about.html', context=context)


class LanguageView(View):
    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(is_active=True, cts__pre_cts="A")
        sider = utils.get_fine_top_like()
        context = {
            "blog": blogs,
            "sider": sider,
            "topic": "编程语言",
            "famous": ""
        }
        return render(request, 'list.html', context)


class StudyView(View):
    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(is_active=True, cts__pre_cts="B")
        sider = utils.get_fine_top_like()
        context = {
            "blog": blogs,
            "sider": sider,
            "topic": "学习笔记",
            "famous": "观众器者为良匠，观众病者为良医。——叶适"
        }
        return render(request, 'list.html', context)


class LifeView(View):
    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(is_active=True, cts__pre_cts="C")
        sider = utils.get_fine_top_like()
        comtext = {
            "sider": sider,
            "blog": blogs,
            "topic": "日常生活",
            "famous": "镜破不改光，兰死不改香。——孟郊"
        }
        return render(request, 'list.html', context=comtext)


# class InspirationView(View):
#     def get(self, request, *args, **kwargs):
#         blogs = models.Blog.objects.filter(is_active=True, cts__pre_cts="D")
#         sider = utils.get_fine_top_like()
#         comtext = {
#             "sider": sider,
#             "blog": blogs,
#             "topic": "灵光一现",
#             "famous": "情之所至，诗无不至；诗之所至，情以之至。——清·王夫之"
#         }
#         return render(request, 'list.html', context=comtext)


class TimeView(View):
    model = models.Blog

    def get(self, request, *args, **kwargs):
        blogs = self.model.objects.filter(is_active=True).order_by("-created_at")
        return render(request, 'time.html', context={"blogs": blogs, "time": True})


class GbookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gbook.html')


class InfoView(View):
    model = models.Blog

    def get(self, request, bid, *args, **kwargs):
        query = self.model.objects.filter(pk=bid)
        if query.count():
            query = query.first()
        else:
            raise Http404
            # return render_to_response('404.html', status=404)
        query.content = query.content.replace('<img', '<img class="myimg"')
        sider = utils.get_fine_top_like()
        query.read += 1
        query.save(update_fields=("read",))
        next = self.model.objects.filter(created_at__gt=query.created_at, is_active=True).order_by(
            '-created_at').first()
        prev = self.model.objects.filter(created_at__lt=query.created_at, is_active=True).order_by(
            '-created_at').first()

        # 根据标签查找相关文章
        others = self.model.objects.exclude(pk=query.id).filter(is_active=True, tags__name__in=[x.name for x in query.tags.all()])[:10]
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
            blog.save(update_fields=("like",))
            return JsonResponse(utils.true_return(msg="点赞成功"))
        return JsonResponse(utils.false_return(msg="您已点过赞"))


class SubInfoView(View):
    model = models.Blog

    def get(self, request, cid):
        blogs = self.model.objects.filter(cts=cid, is_active=True)
        topic = models.Categoty.objects.filter(pk=cid).first()
        sider = utils.get_fine_top_like()
        comtext = {
            "sider": sider,
            "blog": blogs,
            "topic": topic
        }
        return render(request, 'list.html', context=comtext)


class LinkView(View):
    model = models.Link

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        link = request.POST.get("link")
        email = request.POST.get("email")
        try:
            self.model.objects.create(
                name=name,
                link=link,
                email=email
            )
        except Exception as err:
            print(err)
            return JsonResponse(utils.false_return())
        return JsonResponse(utils.true_return())


class GetTagView(View):

    def get(self, request, tid):
        blogs = models.Blog.objects.filter(tags=tid)
        sider = utils.get_fine_top_like()
        tag_info = models.Tag.objects.filter(pk=tid).first()
        comtext = {
            "sider": sider,
            "blog": blogs,
            "target_tag": tag_info.name,
            "target_tag_id":tid,
            "famous": "情之所至，诗无不至；诗之所至，情以之至。——清·王夫之",
            "tag_info": True
        }
        return render(request, 'list.html', context=comtext)


class GetTagNameView(View):

    def get(self, request, name):
        blogs = models.Blog.objects.filter(tags__name=name)
        sider = utils.get_fine_top_like()
        tag_info = models.Tag.objects.filter(name=name).first()
        comtext = {
            "sider": sider,
            "blog": blogs,
            "target_tag": name,
            "target_tag_id": tag_info.id,
            "famous": "情之所至，诗无不至；诗之所至，情以之至。——清·王夫之",
            "tag_info": True
        }
        return render(request, 'list.html', context=comtext)


def web_name_exist(request):
    import re
    print(request.GET)
    tp = request.GET.get("type")
    value = request.GET.get("name")
    if tp == "web_name":
        count = models.Link.objects.filter(name=value).count()
        if count:
            return JsonResponse(utils.false_return(msg="网站名称已存在"))
        return JsonResponse(utils.true_return(msg="网站名称可用"))
    elif tp == "web_link":
        count = models.Link.objects.filter(link=value).count()
        if count:
            return JsonResponse(utils.false_return(msg="网站链接已存在"))
        if not re.match(r'(http|https)://.+\..+$', value):
            return JsonResponse(utils.false_return(msg="非法链接，可能缺少http://或者https://"))
        return JsonResponse(utils.true_return(msg='链接可用'))
    else:
        count = models.Link.objects.filter(email=value).count()
        if count:
            return JsonResponse(utils.false_return(msg="email已存在"))
        else:
            if not re.match('^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', value):
                return JsonResponse(utils.false_return(msg='邮箱不正确'))
            return JsonResponse(utils.true_return(msg='邮箱可用'))
