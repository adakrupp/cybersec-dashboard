from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view - displays dashboard overview"""
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'
        return context


def health_check(request):
    """Health check endpoint for Docker"""
    from django.http import JsonResponse
    return JsonResponse({'status': 'healthy'})
