from django.contrib import admin
from .models import CVE, CVESearch


@admin.register(CVE)
class CVEAdmin(admin.ModelAdmin):
    list_display = ['cve_id', 'severity', 'cvss_score', 'published_date', 'cached_at']
    list_filter = ['severity', 'published_date']
    search_fields = ['cve_id', 'description']
    date_hierarchy = 'published_date'


@admin.register(CVESearch)
class CVESearchAdmin(admin.ModelAdmin):
    list_display = ['query', 'search_count', 'last_searched']
    search_fields = ['query']
    ordering = ['-search_count']
