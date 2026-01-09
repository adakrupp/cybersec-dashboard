from django.db import models


class Category(models.Model):
    """Resource categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Certification(models.Model):
    """Cybersecurity certifications"""
    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
        ('EXPERT', 'Expert'),
    ]

    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    cost_range = models.CharField(max_length=100)
    description = models.TextField()
    official_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.provider})"


class Resource(models.Model):
    """Learning resources"""
    RESOURCE_TYPE_CHOICES = [
        ('COURSE', 'Course'),
        ('TUTORIAL', 'Tutorial'),
        ('DOCUMENTATION', 'Documentation'),
        ('VIDEO', 'Video'),
        ('BOOK', 'Book'),
        ('LAB', 'Practice Lab'),
    ]

    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]

    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resources')
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    url = models.URLField()
    description = models.TextField()
    provider = models.CharField(max_length=200)
    is_free = models.BooleanField(default=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    tags = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
