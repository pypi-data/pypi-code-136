# 应用名称
from django.urls import re_path
from .apis import send_short_message

app_name = 'message'

urlpatterns = [

    re_path(r'^send_message/?$', send_short_message.SendShortMessag.as_view(), ),

]
