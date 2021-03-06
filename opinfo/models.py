from django.db import models
# from mdeditor.fields import MDTextField
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

# Create your models here.

cats = (
        ("A", "热点分享"),
        ("B", "学习笔记"),
        ("C", "日常生活"),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_active = models.BooleanField(default=True, verbose_name="是否可见")

    class Meta:
        abstract = True


class UserAccount(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=30,
        unique=True,
        help_text="1~30个字符",
        error_messages={
            "unique": _("用户名已存在"),
            "null": _("用户名不能为空")
        },
        blank=False
    )
    header = models.ImageField(null=True, blank=True, upload_to="header/", verbose_name="头像")
    email = models.EmailField(
        verbose_name="登陆邮箱",
        unique=True
    )
    # desc = models.TextField(max_length=200, blank=True, null=True, verbose_name="自我简介")
    desc = UEditorField(verbose_name="自我简介", blank=True,width="100%",
                           imagePath='my/img/', filePath='my/file/')
    alipay = models.ImageField(null=True, blank=True, upload_to="ds/alipay/", verbose_name="支付宝二维码")
    wechat = models.ImageField(null=True, blank=True, upload_to="ds/wechat/", verbose_name="微信二维码")

    class Meta:
        verbose_name_plural = verbose_name = "帐号"
        db_table = "jh_user"

    def __str__(self):
        return self.username


class Author(UserAccount):
    class Meta:
        verbose_name_plural = verbose_name = "我的帐号"
        proxy = True


class Categoty(BaseModel):
    pre_cts = models.CharField(max_length=1, choices=cats, verbose_name="前置分类")
    cts = models.CharField(max_length=10, verbose_name="分类", null=False, blank=False)

    class Meta:
        verbose_name_plural = verbose_name = "分类"
        db_table = "jh_categoty"

    def __str__(self):
        return self.cts


class Tag(BaseModel):
    name = models.CharField(max_length=10, verbose_name="标签名", unique=True,
                            null=False, blank=False, help_text="请输入20以内字符标签名")

    class Meta:
        verbose_name_plural = verbose_name = "标签"
        db_table = "jh_tag"

    def __str__(self):
        return self.name


class Blog(BaseModel):
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name="标题",help_text="请输入0-20个字符串的标题")
    author = models.ForeignKey(
        to=UserAccount,
        on_delete=models.CASCADE,
        limit_choices_to={
            "is_active":True,
            "is_staff":True
        },
        verbose_name="作者"
    )
    desc = models.TextField(max_length=100, null=True, verbose_name="文章简介")
    cts = models.ForeignKey(to=Categoty, related_name='ctsblogs', null=True, verbose_name="文章分类",
                            on_delete=models.SET_NULL, limit_choices_to={"is_active":True})
    origin = models.BooleanField(default=False, verbose_name="原创")
    tags = models.ManyToManyField(to=Tag, related_name="tblogs", verbose_name="标签",
                                  blank=True, limit_choices_to={"is_active": True})
    cover = models.ImageField(upload_to='blog/cover', verbose_name="封面", blank=True, null=True)
    # content = MDTextField()
    content = UEditorField(verbose_name="内容", blank=True,width="100%",
                           imagePath='blog/img/', filePath='blog/file/')
    source = models.URLField(null=True, blank=True, verbose_name="原文链接", )
    is_fine = models.BooleanField(default=False, verbose_name="推荐文章")
    is_top = models.BooleanField(default=False, verbose_name="特别推荐")
    read = models.PositiveIntegerField(default=0, verbose_name="阅读数")
    like = models.PositiveIntegerField(default=0, verbose_name="喜欢")

    class Meta:
        verbose_name_plural = verbose_name = "博客"
        db_table = "jh_blog"

    def __str__(self):
        return self.title

    def url(self):
        path = "/info/{}".format(self.id)
        return mark_safe('<a href="{}" target="_blank">{}</a>'.format(path, path))

    url.short_description = "链接"

    def if_origin(self):
        if not self.origin:
            url = self.source
            return mark_safe('<a href={} target="_blank">{}</a>'.format(url, "原文链接"))
        return True

    if_origin.short_description = "是否原创"


class MyBlog(Blog):
    class Meta:
        verbose_name_plural = verbose_name = "我的博客"
        proxy = True


class Horselight(BaseModel):
    tps = (
        ("A", "走马灯"),
        ("B", "小窗口")
    )
    name = models.CharField(max_length=10,choices=tps, verbose_name="类型")
    target = models.ManyToManyField(to=Blog, related_name="lblog", verbose_name="博文")
    # right = models.ManyToManyField(to=Blog, related_name="rblog", verbose_name="走马灯右侧博文")

    class Meta:
        verbose_name_plural = verbose_name = "轮播图"
        db_table = 'jh_horse'

    def __str__(self):
        return self.name


class Link(BaseModel):
    name = models.CharField(verbose_name="网站名称", max_length=15)
    link = models.CharField(verbose_name="网站地址", max_length=100,
                            null=False, blank=False, unique=True)
    email = models.EmailField(verbose_name="邮箱地址", unique=True)
    is_active = models.BooleanField(default=False, verbose_name="是否可见")

    class Meta:
        verbose_name_plural = verbose_name = "友情链接"
        db_table = "jh_link"

    def __str__(self):
        return self.name
