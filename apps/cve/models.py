from django.db import models
from django.utils import timezone


class CVE(models.Model):
    """Common Vulnerabilities and Exposures"""
    SEVERITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    cve_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    published_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    cvss_score = models.FloatField(null=True, blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, null=True, blank=True)
    affected_products = models.JSONField(default=list, blank=True)
    references = models.JSONField(default=list, blank=True)
    cached_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['cve_id']),
            models.Index(fields=['-published_date']),
        ]

    def __str__(self):
        return self.cve_id


class CVESearch(models.Model):
    """Track popular CVE searches"""
    query = models.CharField(max_length=200)
    search_count = models.IntegerField(default=1)
    last_searched = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-search_count']

    def __str__(self):
        return f"{self.query} ({self.search_count} searches)"
