"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Aug-2021

https://web.stepwisemath.ai/stepwise/api/v1/configuration
https://web.stepwisemath.ai/stepwise/dashboard
https://web.stepwisemath.ai/stepwise/dashboard?language=es-419
"""
# Django
from django.conf.urls import url

# this repo
from stepwise_plugin.dashboard.views import student_dashboard
from stepwise_plugin.locale.views import marketing_redirector
from stepwise_plugin.api.urls import urlpatterns as api_urlpatterns

app_name = "stepwise_plugin"

urlpatterns = [
    url(r"^dashboard/?$", student_dashboard, name="stepwise_dashboard"),
    url(r"^marketing-redirector/?$", marketing_redirector, name="stepwise_marketing_redirector"),
] + api_urlpatterns
