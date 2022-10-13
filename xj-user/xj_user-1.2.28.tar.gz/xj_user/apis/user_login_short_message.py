import json

from django.http import HttpResponse
from rest_framework import response
from rest_framework.views import APIView
from django.core.cache import cache

from ..services.user_service import UserService
# from ..services.user_login_register import LoginRegister
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
        # 2. 获取redis中保存的code
        # print('缓存中是否包含:', cache.has_key(phone))
        # print('取值:', cache.get(phone))
        cache_code = cache.get(phone)
        # 3. 判断
        account, error = UserService.check_account(phone)
        # print("账户：", account)
        if code == cache_code:
            pass
            # err, data = LoginRegister.login_register(phone)
            # if err == 0:
            #     return util_response(data=data)
            # else:
            #     return util_response(msg=err, err=6004)
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
