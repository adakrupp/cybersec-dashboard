from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import CVE, CVESearch
from .nvd_api import search_cve, fetch_recent_cves


class CVESearchView(TemplateView):
    """Search view for CVEs"""
    template_name = 'cve/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')

        if query:
            # Search using NVD API (checks cache first)
            cves = search_cve(query)
            context['cves'] = cves
            context['query'] = query

            # Track search
            search, created = CVESearch.objects.get_or_create(query=query)
            if not created:
                search.search_count += 1
                search.save()
        else:
            # Show recent CVEs from cache, or fetch if empty
            recent_cves = CVE.objects.all()[:20]
            if not recent_cves.exists():
                # Fetch recent CVEs from API on first load
                recent_cves = fetch_recent_cves(days=30)
            context['cves'] = recent_cves

        context['popular_searches'] = CVESearch.objects.all()[:5]
        context['page_title'] = 'CVE Tracker'
        return context
