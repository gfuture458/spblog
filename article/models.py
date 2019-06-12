from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=10, verbose_name="文章名称")
    content = MDTextField(verbose_name="内容")

    class Meta:
        verbose_name_plural = verbose_name = "文章"

    def __str__(self):
        return self.name