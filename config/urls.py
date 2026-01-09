"""URL Configuration for cybersec-dashboard"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('news/', include('apps.news.urls')),
    path('resources/', include('apps.resources.urls')),
    path('tools/', include('apps.tools.urls')),
    path('cve/', include('apps.cve.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin site
admin.site.site_header = "CyberSec Dashboard Admin"
admin.site.site_title = "CyberSec Dashboard"
admin.site.index_title = "Dashboard Administration"
