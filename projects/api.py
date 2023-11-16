"""This file is used to create the API endpoints for the projects app."""

from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Project model."""
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
