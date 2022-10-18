from django.urls import path, re_path, include
from rest_framework import routers
from .views import ObjectClassViewSet, ObjectViewSet

router = routers.DefaultRouter()
router.register('objects', ObjectViewSet)
router.register('object_classes', ObjectClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
