import time
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LargeDataset
from .serializers import LargeDatasetSerializer

from rest_framework.decorators import action


class LargeDatasetViewSet(viewsets.ModelViewSet):
    queryset = LargeDataset.objects.all()
    serializer_class = LargeDatasetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        limit = self.request.query_params.get("limit", 10)
        offset = self.request.query_params.get("offset", 0)

        try:
            limit = int(limit)
            offset = int(offset)
            if limit > 5000:
                limit = 5000
            if offset < 0:
                offset = 0
        except ValueError:
            limit = 100
            offset = 0

        return LargeDataset.objects.all()[offset:offset + limit]  

class LongRunningView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_time = time.time()
        
        # 6 perc várakozás
        time.sleep(360)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return Response({"message": "Process completed", "elapsed_time": elapsed_time})


class LongRunningViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({"detail": "Use 'process' action."})

    @action(detail=False, methods=["get"])
    def process(self, request):
        start_time = time.time()
        
        # 3 perc várakozás
        time.sleep(180)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return Response({"message": "Process completed", "elapsed_time": elapsed_time})
    

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import time

class LongRunningViewSet2(GenericViewSet):  # 🔹 ViewSet helyett GenericViewSet
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def process(self, request):
        start_time = time.time()
        
        # 3 perc várakozás
        time.sleep(180)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return Response({"message": "Process completed", "elapsed_time": elapsed_time})
