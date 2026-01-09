from django.db import models
from django.utils import timezone


class NewsSource(models.Model):
    """Model for news sources (RSS feeds, Reddit, etc.)"""
    SOURCE_TYPE_CHOICES = [
        ('RSS', 'RSS Feed'),
        ('REDDIT', 'Reddit'),
    ]

    name = models.CharField(max_length=200)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPE_CHOICES)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    fetch_frequency = models.IntegerField(default=30, help_text="Fetch frequency in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.source_type})"


class NewsArticle(models.Model):
    """Model for aggregated news articles"""
    title = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE, related_name='articles')
    published_date = models.DateTimeField()
    summary = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    score = models.IntegerField(default=0, help_text="Reddit score/votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['-published_date']),
            models.Index(fields=['source', '-published_date']),
        ]

    def __str__(self):
        return self.title
