"""Models for the projects app."""


from django.db import models

# Create your models here.


class Project(models.Model):
    """Model for a project."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
