from django.contrib import admin
from .models import ToolCategory, Tool


@admin.register(ToolCategory)
class ToolCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_open_source', 'difficulty']
    list_filter = ['category', 'is_open_source', 'difficulty']
    search_fields = ['name', 'description', 'use_case']
