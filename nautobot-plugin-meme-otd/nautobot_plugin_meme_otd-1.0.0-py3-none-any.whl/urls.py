"""Urls for plugin."""
from django.urls import path

from .views import MemeOfTheDayView

urlpatterns = [path("", MemeOfTheDayView.as_view(), name="meme-otd")]
