from django.db import models


class ToolCategory(models.Model):
    """Categories for security tools"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tool Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Tool(models.Model):
    """Security tools directory"""
    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(ToolCategory, on_delete=models.CASCADE, related_name='tools')
    description = models.TextField()
    use_case = models.TextField(help_text="When and how to use this tool")
    url = models.URLField()
    github_url = models.URLField(blank=True)
    is_open_source = models.BooleanField(default=True)
    platforms = models.JSONField(default=list, help_text="List of supported platforms")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    tags = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
