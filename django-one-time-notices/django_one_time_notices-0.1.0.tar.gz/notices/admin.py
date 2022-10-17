from django.contrib.admin import ModelAdmin, register

from .models import Notice


@register(Notice)
class NoticeAdmin(ModelAdmin):
    ...
