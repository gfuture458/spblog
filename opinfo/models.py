from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

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
        verbose_name="帐号邮箱",
        unique=True
    )
    desc = models.TextField(max_length=200, blank=True, null=True, verbose_name="自我简介")
    alipay = models.ImageField(null=True, blank=True, upload_to="ds/alipay/", verbose_name="支付宝二维码")
    wechat = models.ImageField(null=True, blank=True, upload_to="ds/wechat/", verbose_name="微信二维码")

    class Meta:
        verbose_name_plural = verbose_name = "帐号"
        db_table = "blog_user"


class Author(UserAccount):
    class Meta:
        verbose_name_plural = verbose_name = "我的帐号"
        proxy = True

