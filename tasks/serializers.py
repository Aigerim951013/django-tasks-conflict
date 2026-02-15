from rest_framework import serializers
from .models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=5)

    class Meta:
        model = Task
        fields = ["title", "is_done"]
