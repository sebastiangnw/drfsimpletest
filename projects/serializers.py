"""Projects serializers."""

from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project model."""

    class Meta:
        """Meta class to define the serializer's fields."""
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )
