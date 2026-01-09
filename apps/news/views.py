from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsArticle, NewsSource


class NewsListView(ListView):
    """List view for news articles"""
    model = NewsArticle
    template_name = 'news/list.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        source = self.request.GET.get('source')
        if source:
            queryset = queryset.filter(source_id=source)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sources'] = NewsSource.objects.filter(is_active=True)
        context['page_title'] = 'Latest News'
        return context
