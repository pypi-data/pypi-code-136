from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('miaApplicazione/', include('miaApplicazione.urls')),
    path('admin/', admin.site.urls),
]
