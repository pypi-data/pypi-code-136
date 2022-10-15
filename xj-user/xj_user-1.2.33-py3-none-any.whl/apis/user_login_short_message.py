import json

from django.http import HttpResponse
from rest_framework import response
from rest_framework.views import APIView
from django.core.cache import cache

from ..services.user_service import UserService
from xj_user.services.wechat_service import WechatService
from ..services.user_sms_service import UserSmsService
from ..utils.custom_response import util_response

class ShortMessageLogin(APIView):
    # 短信验证码校验
    def post(self, request):
        # 1. 电话和手动输入的验证码
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        if code is None:
            res = {
                'err': 4002,
                'msg': '验证码不能为空',
            }
            return response.Response(data=res, status=None, template_name=None)
        cache_code = cache.get(phone)
        if code == cache_code:
            app = UserSmsService()
            err, data = app.phone_login(phone=phone)
            if err == 0:
                return util_response(data=data)
            else:
                return util_response(msg=err, err=6004)
        else:
            res = {
                'err': 4002,
                'msg': '验证码错误',
            }
            return response.Response(data=res, status=None, template_name=None)


class MyApiError(Exception):
    def __init__(self, message, err_code=4010):
        self.msg = message
        self.err = err_code

    def __str__(self):
        # repr()将对象转化为供解释器读取的形式。可省略
        return repr(self.msg)
