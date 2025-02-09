from rest_framework import serializers
from .models import LargeDataset

class LargeDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LargeDataset
        fields = "__all__"
