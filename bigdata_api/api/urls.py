from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LargeDatasetViewSet, LongRunningView, LongRunningViewSet, LongRunningViewSet2

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"datasets", LargeDatasetViewSet)
router.register(r"long-process-3min", LongRunningViewSet, basename="long-process-3min")
router.register(r"long-process-3min2", LongRunningViewSet, basename="long-process-3min2")


urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token-auth/", obtain_auth_token, name="api_token_auth"),
    path("long-process/", LongRunningView.as_view(), name="long_process"),
]
