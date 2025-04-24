import time
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import viewsets
from .models import LargeDataset, Post, Report, Task, Notice, SecureData
from .serializers import (LargeDatasetSerializer,
                          PostSerializer,
                          ReportSerializer,
                          TaskSerializer,
                          NoticeSerializer,
                          SecureDataSerializer)

from rest_framework.permissions import DjangoModelPermissions

from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import (IsPostAuthor,
                          IsInEditorsGroup,
                          IsAdminOrChangeOnly,
                          IsOwnerOrAdmin,
                          IsWorkingHours,
                          HasTrustedHeader,
                          HasValidAPIKeyFromDB)
import time

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

class LongRunningViewSet2(GenericViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def process(self, request):
        start_time = time.time()
        
        # 3 perc várakozás
        time.sleep(180)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return Response({"message": "Process completed", "elapsed_time": elapsed_time})


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsPostAuthor]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        serializer = self.get_serializer(
            instance, 
            data=request.data, 
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.datetime.now())

class PostViewSet2(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsInEditorsGroup]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet3(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrChangeOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated, IsWorkingHours, HasTrustedHeader]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SecureDataViewSet(viewsets.ModelViewSet):
    queryset = SecureData.objects.all()
    serializer_class = SecureDataSerializer
    permission_classes = [HasValidAPIKeyFromDB]