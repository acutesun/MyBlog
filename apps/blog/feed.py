from django.contrib.syndication.views import Feed
from .models import Article


class ArticleFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = 'Django 项目'
    # 跳转地址
    link = '/'
    # 显示在聚合阅读器上的描述
    description = 'djanog 项目展示'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.categorys, item.title)

    def item_description(self, item):
        return item.content

