from django.urls import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from appointment.views import AppointmentViewSet

router = DefaultRouter()
router.register(r'', AppointmentViewSet, basename='appointment_operations')

urlpatterns = [
    path("", include(router.urls))
]