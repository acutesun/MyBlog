from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import reverse
from django.utils.html import strip_tags
import markdown
from django.utils import timezone


class Category(models.Model):
    ''' 文章分类 '''
    name = models.CharField(max_length=100, verbose_name='分类名')

    def __str__(self):
        return self.name

    def get_articles(self):
        ''' 返回这个分类下的所有文章 '''
        return self.article_set.all()

    def get_art_nums(self):
        ''' 返回分类下的文章的数量 '''
        return self.article_set.all().count()


class Tag(models.Model):
    ''' 文章标签 多对多 '''
    name = models.CharField(max_length=100, verbose_name='标签名')

    def __str__(self):
        return self.name


class Article(models.Model):
    ''' 博客文章 '''
    title = models.CharField(max_length=60, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateField(default=timezone.now, verbose_name='创建时间')
    modify_time = models.DateField(default=timezone.now, verbose_name='修改时间')
    excerpt = models.CharField(max_length=300, blank=True, verbose_name='文章摘要')

    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')
    categorys = models.ForeignKey(Category, verbose_name='文章分类')
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型
    author = models.ForeignKey(User, verbose_name='作者')
    click_nums = models.IntegerField(verbose_name='阅读数', default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})

    class Meta:
        ordering = ['-create_time', 'title']

    def increase_views(self):
        self.click_nums += 1
        self.save(update_fields=['click_nums'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.content))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Article, self).save(*args, **kwargs)


