from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LargeDataset
from .serializers import LargeDatasetSerializer

class LargeDatasetViewSet(viewsets.ModelViewSet):
    queryset = LargeDataset.objects.all()
    serializer_class = LargeDatasetSerializer
    permission_classes = [IsAuthenticated]  # Csak hitelesített felhasználók férhetnek hozzá
