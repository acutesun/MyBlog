from django.db import models
from blog.models import Article


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='用户名')
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    url = models.URLField(blank=True, verbose_name='个人网站')
    text = models.TextField(verbose_name='评论内容')  # auto_now_add 的作用是，当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    article = models.ForeignKey(Article, related_name='comm_artc')

    def __str__(self):
        return self.name + ': ' +self.text[:20]


