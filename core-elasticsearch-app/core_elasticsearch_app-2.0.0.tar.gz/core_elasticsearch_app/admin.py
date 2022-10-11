""" Url router for the administration site
"""
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import re_path

from core_main_app.admin import core_admin_site
from core_elasticsearch_app.components.elasticsearch_template.models import (
    ElasticsearchTemplate,
)
from core_elasticsearch_app.views.admin import views as admin_views, ajax as admin_ajax


admin_urls = [
    re_path(
        r"^elasticsearch/templates",
        staff_member_required(admin_views.TemplatesView.as_view()),
        name="core_elasticsearch_app_templates",
    ),
    re_path(
        r"^elasticsearch/template/add",
        staff_member_required(admin_ajax.AddElasticsearchTemplateView.as_view()),
        name="core_elasticsearch_app_templates_add",
    ),
    re_path(
        r"^elasticsearch/template/(?P<pk>[\w-]+)/delete/$",
        staff_member_required(admin_ajax.DeleteElasticsearchTemplateView.as_view()),
        name="core_elasticsearch_app_templates_delete",
    ),
    re_path(
        r"^elasticsearch/template/(?P<pk>[\w-]+)/edit/$",
        staff_member_required(admin_ajax.EditElasticsearchTemplateView.as_view()),
        name="core_elasticsearch_app_templates_edit",
    ),
    re_path(
        r"^elasticsearch/template/(?P<pk>[\w-]+)/check/$",
        admin_ajax.check_data_from_template,
        name="core_elasticsearch_app_templates_check",
    ),
    re_path(
        r"^elasticsearch/template/(?P<pk>[\w-]+)/index/$",
        admin_ajax.index_data_from_template,
        name="core_elasticsearch_app_templates_index",
    ),
]

admin.site.register(ElasticsearchTemplate)
urls = core_admin_site.get_urls()
core_admin_site.get_urls = lambda: admin_urls + urls
