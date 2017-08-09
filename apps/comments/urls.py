from django.conf.urls import url
from .views import CommentView

urlpatterns = [
    url(r'^commit/(?P<id>\d+)/$', CommentView.as_view(), name='commit'),
]