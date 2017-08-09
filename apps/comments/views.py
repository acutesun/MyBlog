from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect,reverse
from django.views import View
from blog.models import Article
from .forms import CommentForm
from django.http import  HttpResponseRedirect


class CommentView(View):
    ''' 评价视图 '''
    def post(self, request, id):
        article = get_object_or_404(Article, pk=id)

        form = CommentForm(request.POST)
        if form.is_valid():
            # commit = False的作用是仅仅利用表单的数据生成
            # Comment模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            # 将评论文章关联
            comment.article = article
            comment.save()
            return HttpResponseRedirect(article.get_absolute_url())



