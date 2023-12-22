from django.urls import include, path
from .views import DoctorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", DoctorViewSet, basename='doctor_operations')

urlpatterns = [
    path("", include(router.urls)),
]