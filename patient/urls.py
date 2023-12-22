from django.urls import include, path
from rest_framework.routers import DefaultRouter

from patient.views import PatientViewSet


router = DefaultRouter()
router.register(r"", PatientViewSet, basename='patient_operations')

urlpatterns = [
    path("", include(router.urls))
]
