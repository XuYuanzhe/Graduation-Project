from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    created_time = models.DateTimeField()
    # 文章上一次修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 文章分类
    category = models.ForeignKey(Category)
    # 文章标签
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
