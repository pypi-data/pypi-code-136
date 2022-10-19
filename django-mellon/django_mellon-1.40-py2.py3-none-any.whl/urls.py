import django
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='mellon_login'),
    path('login/debug/', views.debug_login, name='mellon_debug_login'),
    path('logout/', views.logout, name='mellon_logout'),
    path('metadata/', views.metadata, name='mellon_metadata'),
]
