from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
import markdown
from datetime import  datetime

from .models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment


class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()

        context = {
            'articles': articles,
        }
        return render(request, 'index.html', context)


class ArticleDetailView(View):
    ''' 文章详情处理View '''
    def get(self, request, id):
        article = get_object_or_404(Article, pk=id)   # 返回404表示文章不存在
        if article and article != 404:

            article.increase_views()
            # 把 Markdown 文本转为 HTML 文本再传递给模板
            article.content = markdown.markdown(article.content, extensions=[
                                                'markdown.extensions.extra',     #
                                                'markdown.extensions.codehilite',  # 语法高亮
                                                'markdown.extensions.toc',  # 自动生成目录
                                                ])
            form = CommentForm()
            comment_list = Comment.objects.filter(article=article)

            context = {
                'article': article,
                'form': form,
                'comment_list': comment_list,
            }
            return render(request, 'detail.html', context)


class ArchivesView(View):
    ''' 归档处理view '''
    def get(self, request, year, month):
        articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
        context = {
            'articles': articles,
        }
        return render(request, 'index.html', context)


class CategoryView(View):
    ''' 分类VIew'''

    def get(self, request, id):
        category = get_object_or_404(Category, pk=id)
        articles = category.get_articles()
        context = {
            'articles': articles,
        }
        return render(request, 'index.html', context)





