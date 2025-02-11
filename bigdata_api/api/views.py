import time
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LargeDataset
from .serializers import LargeDatasetSerializer

class LargeDatasetViewSet(viewsets.ModelViewSet):
    queryset = LargeDataset.objects.all()
    serializer_class = LargeDatasetSerializer
    permission_classes = [IsAuthenticated]

class LongRunningView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_time = time.time()
        
        # 6 perc várakozás
        time.sleep(360)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return Response({"message": "Process completed", "elapsed_time": elapsed_time})
