from django.conf.urls import url
from .views import IndexView, ArticleDetailView, ArchivesView, CategoryView, AboutView
from .views import search

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<id>\d+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', ArchivesView.as_view(), name='archive'),
    url(r'^category/(?P<id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^search/$', search, name='search'),


]
