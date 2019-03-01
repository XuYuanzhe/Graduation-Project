import markdown

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags


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
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 自增计数文章阅读量 可绑定用户防止同一用户频繁访问
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 重写save方法自动生成文章摘要
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extension_configs=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time', 'title']
