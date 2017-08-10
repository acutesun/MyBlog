from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    '''
        使用数据建立索引以及存放索引
    '''
    text = indexes.CharField(document=True, use_template=True)
    template_name = 'article_text.txt'

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
