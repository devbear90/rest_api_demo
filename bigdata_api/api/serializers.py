from rest_framework import serializers
from .models import LargeDataset, Post

class LargeDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LargeDataset
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']
