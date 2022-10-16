"""External API urls."""

from django.urls import include, path

from kalabash.core.extensions import exts_pool

app_name = "api"

urlpatterns = [
    path('', include("kalabash.core.api.v2.urls")),
    path('', include("kalabash.admin.api.v2.urls")),
    path('', include("kalabash.parameters.api.v2.urls")),
    path('', include("kalabash.limits.api.v1.urls")),
    path('', include("kalabash.relaydomains.api.v1.urls")),
    path('', include("kalabash.dnstools.api.v2.urls")),
    path('', include("kalabash.maillog.api.v2.urls")),
    path('', include("kalabash.transport.api.v2.urls")),
]

urlpatterns += exts_pool.get_urls(category="api")
