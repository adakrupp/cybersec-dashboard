from django.shortcuts import render
from django.views.generic import ListView
from .models import Tool, ToolCategory


class ToolListView(ListView):
    """List view for security tools"""
    model = Tool
    template_name = 'tools/list.html'
    context_object_name = 'tools'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        open_source = self.request.GET.get('open_source')

        if category:
            queryset = queryset.filter(category__slug=category)
        if open_source == 'true':
            queryset = queryset.filter(is_open_source=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ToolCategory.objects.all()
        context['page_title'] = 'Security Tools'
        return context
