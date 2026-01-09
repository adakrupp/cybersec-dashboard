from django.contrib import admin
from .models import Category, Certification, Resource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'difficulty', 'cost_range']
    list_filter = ['difficulty', 'provider']
    search_fields = ['name', 'description']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'resource_type', 'is_free', 'difficulty', 'provider']
    list_filter = ['category', 'resource_type', 'is_free', 'difficulty']
    search_fields = ['title', 'description', 'provider']
