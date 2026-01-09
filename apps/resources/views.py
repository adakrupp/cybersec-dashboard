from django.shortcuts import render
from django.views.generic import ListView
from .models import Resource, Category, Certification


class ResourceListView(ListView):
    """List view for learning resources"""
    model = Resource
    template_name = 'resources/list.html'
    context_object_name = 'resources'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        difficulty = self.request.GET.get('difficulty')
        is_free = self.request.GET.get('is_free')

        if category:
            queryset = queryset.filter(category__slug=category)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        if is_free == 'true':
            queryset = queryset.filter(is_free=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['certifications'] = Certification.objects.all()
        context['page_title'] = 'Learning Resources'
        return context
