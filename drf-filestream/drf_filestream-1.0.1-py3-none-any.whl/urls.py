from django.urls import re_path

from .views import FileStreamView


urlpatterns = [
    re_path('(?P<filepath>.+)$', FileStreamView.as_view(), name='file-stream'),
]
