from django.contrib import admin
from .models import LearningPath, SkillNode


@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'estimated_hours', 'is_published', 'order']
    list_filter = ['difficulty', 'is_published']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


class SkillNodeInline(admin.TabularInline):
    model = SkillNode
    extra = 0
    fields = ['title', 'difficulty', 'estimated_hours', 'order']
    show_change_link = True


@admin.register(SkillNode)
class SkillNodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'learning_path', 'difficulty', 'estimated_hours', 'order']
    list_filter = ['learning_path', 'difficulty']
    search_fields = ['title', 'description']
    filter_horizontal = ['prerequisites', 'resources', 'tools', 'certifications']
    prepopulated_fields = {'slug': ('title',)}
