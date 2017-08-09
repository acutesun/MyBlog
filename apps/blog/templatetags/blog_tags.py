# 自定义模板标签
from ..models import Article, Category, Tag
from django import template
from django.db.models import Count


register = template.Library()


@register.simple_tag   # 注册为模板标签
def get_new_articles(num=5):
    '''
    最新文章模板标签
    获取最新文章
    :param num: 获取的文章数量, 默认5
    :return: 返回获取的所有文章
    '''
    articles = Article.objects.all().order_by('-create_time')
    return articles[:num]


@register.simple_tag
def archives():
    '''
    归档模板标签
    :return: 返回date 对象，精确到月份
    '''
    arch = Article.objects.dates('create_time', 'day', order='DESC')  # 降序排列
    return arch


@register.simple_tag
def get_categories():
    '''
    分类模板标签
    :return:
    '''
    return Category.objects.annotate(article_nums=Count('article'))


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('article'))