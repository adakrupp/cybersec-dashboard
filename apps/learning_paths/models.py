from django.db import models


class LearningPath(models.Model):
    """A learning path/roadmap container"""
    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    estimated_hours = models.IntegerField(help_text="Estimated completion time in hours")
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class SkillNode(models.Model):
    """Individual skill/topic in the learning tree"""
    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]

    learning_path = models.ForeignKey(LearningPath, on_delete=models.CASCADE, related_name='nodes')
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    estimated_hours = models.IntegerField(help_text="Hours to complete this skill")
    order = models.IntegerField(default=0, help_text="Display order in tree")

    # Curated learning resources specific to this skill
    learning_resources = models.JSONField(
        default=list,
        blank=True,
        help_text="List of curated learning resources: [{'title': '...', 'url': '...', 'type': 'video|article|course|tutorial|book|documentation', 'description': '...'}]"
    )

    # Prerequisites (self-referential ManyToMany)
    prerequisites = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='unlocks',
        blank=True,
        help_text="Skills that must be completed before this one"
    )

    # Links to existing database resources
    resources = models.ManyToManyField(
        'resources.Resource',
        related_name='skill_nodes',
        blank=True,
        help_text="Learning resources for this skill"
    )

    tools = models.ManyToManyField(
        'tools.Tool',
        related_name='skill_nodes',
        blank=True,
        help_text="Tools to practice this skill"
    )

    certifications = models.ManyToManyField(
        'resources.Certification',
        related_name='skill_nodes',
        blank=True,
        help_text="Certifications that test this skill"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ['learning_path', 'slug']

    def __str__(self):
        return f"{self.learning_path.name} - {self.title}"
