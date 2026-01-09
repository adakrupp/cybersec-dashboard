from django.contrib import admin
from .models import NewsSource, NewsArticle


@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'source_type', 'is_active', 'fetch_frequency', 'created_at']
    list_filter = ['source_type', 'is_active']
    search_fields = ['name', 'url']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'published_date', 'score', 'created_at']
    list_filter = ['source', 'published_date']
    search_fields = ['title', 'summary']
    date_hierarchy = 'published_date'
