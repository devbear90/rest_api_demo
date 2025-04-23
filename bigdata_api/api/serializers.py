from rest_framework import serializers
from .models import LargeDataset, Post, Report, Task, Notice, APIKey, SecureData

class LargeDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LargeDataset
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'title', 'content', 'created_by']
        read_only_fields = ['created_by']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'created_at']
        read_only_fields = ['assigned_to', 'created_at']

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'message', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['id', 'name', 'key', 'is_active']

class SecureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureData
        fields = ['id', 'label', 'value']