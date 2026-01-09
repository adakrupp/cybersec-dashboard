from django.urls import path
from . import views

app_name = 'cve'

urlpatterns = [
    path('', views.CVESearchView.as_view(), name='search'),
]
