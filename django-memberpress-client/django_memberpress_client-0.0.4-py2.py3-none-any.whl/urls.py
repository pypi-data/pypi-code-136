"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Oct-2022

memberpress REST API Client plugin for Django - url scaffolding
"""
from memberpress_client.api import urls as api_urls

app_name = "memberpress_client"
urlpatterns = [] + api_urls.urlpatterns
