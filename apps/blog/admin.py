from django.contrib import admin
from .models import Tag, Category, Article


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'modify_time']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)