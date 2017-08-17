from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.db.models import Q

from .models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment

from pure_pagination import Paginator, PageNotAnInteger


class IndexView(View):
    def get(self, request):
        all_article = Article.objects.all()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_article, 3, request=request)
        articles = p.page(page)

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
            md = markdown.Markdown(extensions=[
                                                'markdown.extensions.extra',     #
                                                'markdown.extensions.codehilite',  # 语法高亮
                                                TocExtension(slugify=slugify),  # 自动生成目录
                                                ])
            article.content = md.convert(article.content)
            article.toc = md.toc
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
        # 使用mysql时无法查询， 需要MySQL：安装pytz，并使用mysql_tzinfo_to_sql加载时区表，看queryapi中的datetimes
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
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


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键字'
        return render(request, 'index.html', {'error_msg': error_msg})
    articles = Article.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
    context = {
        'error_msg': error_msg,
        'articles': articles,
    }
    return render(request, 'index.html', context)






