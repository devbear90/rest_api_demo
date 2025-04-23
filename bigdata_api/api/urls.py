from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LargeDatasetViewSet,
                    LongRunningView,
                    LongRunningViewSet,
                    LongRunningViewSet2,
                    PostViewSet,
                    PostViewSet2,
                    PostViewSet3,
                    ReportViewSet,
                    TaskViewSet,
                    NoticeViewSet,
                    SecureDataViewSet)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"datasets", LargeDatasetViewSet)
router.register(r"long-process-3min", LongRunningViewSet, basename="long-process-3min")
router.register(r"long-process-3min2", LongRunningViewSet2, basename="long-process-3min2")
router.register(r'posts', PostViewSet, basename='post')
router.register(r'posts_editor', PostViewSet2, basename='post2')
router.register(r'posts_custom_object', PostViewSet3, basename='post3')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'notices', NoticeViewSet, basename='notice')
router.register(r'secure-data', SecureDataViewSet, basename='securedata')

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token-auth/", obtain_auth_token, name="api_token_auth"),
    path("long-process/", LongRunningView.as_view(), name="long_process"),
]
