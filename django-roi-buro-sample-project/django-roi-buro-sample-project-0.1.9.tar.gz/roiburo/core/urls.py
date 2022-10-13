"""Core URL Configuration"""

from django.urls import path

import roiburo.core.views as views

urlpatterns = [
    path(
        "system-states",
        views.CreateSystemStateView.as_view(),
        name="create-system-state",
    ),
    path(
        "system-state-details",
        views.SystemStateStatsView.as_view(),
        name="get-system-state-details",
    ),
]
