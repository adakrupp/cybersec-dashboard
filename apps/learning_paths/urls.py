from django.urls import path
from . import views

app_name = 'learning_paths'

urlpatterns = [
    path('', views.LearningPathListView.as_view(), name='list'),
    path('<slug:slug>/', views.LearningPathDetailView.as_view(), name='detail'),
]
