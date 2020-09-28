from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'text',
    ]
    list_display = [
        'id',
        'title',
    ]
