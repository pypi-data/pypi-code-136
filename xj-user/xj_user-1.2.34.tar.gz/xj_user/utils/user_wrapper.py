"""
Created on 2022-05-20
@author:刘飞
@description:用户验证装饰器，为单个请求方式做验证
"""
from django.http import JsonResponse
from rest_framework import exceptions

from ..services.user_service import UserService


def user_authentication_wrapper(func):
    """
    用户认证装饰器，如果有Authorization则检查用户的有效性，如没有则认为用户以游客访问
    """

    def wrapper(instance, request=None, *args, **kwargs, ):
        """
        @param instance 实例是一个APIView的实例
        @param request APIView实例会传入请求包
        @param request APIView实例会传入请求包
        @param args 其它可变参数元组
        @param kwargs 其它可变关键字参数字典
        """
        print("> user_authentication_wrapper:", request, args, kwargs)

        if not request:
            return func(request, user_info=None, *args, **kwargs)
        # token = request.META.get('HTTP_AUTHORIZATION', None)
        token = request.headers.get('Authorization', None)
        print("> user_authentication_wrapper token:", token, type(token))

        # 如果没有传token则可视为以游客身份访问
        if not token or str(token) == 'null' or str(token).strip().upper() == "BEARER":
            return func(instance, request=request, user_info=None, *args, **kwargs)

        user_serv, error_text = UserService.check_token(token)
        # print("> user_authentication_wrapper user_serv, error_text:", user_serv, error_text)
        if error_text:
            raise exceptions.AuthenticationFailed(error_text)
            # raise exceptions.AuthenticationFailed(error_text)

        request.user = user_serv
        result = func(instance, request=request, user_info=user_serv, *args, **kwargs)
        return result

    return wrapper


def user_authentication_force_wrapper(func):
    """
    用户认证装饰器，如果有Authorization则检查用户的有效性，如没有则认为用户以游客访问
    """

    def wrapper(instance, *args, request=None, **kwargs, ):
        """
        @param instance 实例是一个APIView的实例
        @param request APIView实例会传入请求包
        @param request APIView实例会传入请求包
        @param args 其它可变参数元组
        @param kwargs 其它可变关键字参数字典
        """
        # print("> user_authentication_wrapper:", request, args, kwargs)
        if str(type(instance)) == "<class 'django.core.handlers.wsgi.WSGIRequest'>":
            request = instance
        if not request:
            return func(request, user_info=None, *args, **kwargs)
        # token = request.META.get('HTTP_AUTHORIZATION', None)
        token = request.headers.get('Authorization', None)
        # print("> user_authentication_wrapper token:", token, type(token))

        # 如果没有传token则可视为以游客身份访问
        if not token or str(token) == 'null' or str(token).strip().upper() == "BEARER":
            print("token:", token)
            return JsonResponse({'err': 6000, 'msg': '该用户未登录'})

        user_serv, error_text = UserService.check_token(token)
        # print("> user_authentication_wrapper user_serv, error_text:", user_serv, error_text)
        if error_text:
            return JsonResponse({'err': 6001, 'msg': error_text})
            # raise exceptions.AuthenticationFailed(error_text)
            # raise exceptions.AuthenticationFailed(error_text)

        request.user = user_serv
        result = func(request, user_info=user_serv, *args, **kwargs)
        return result

    return wrapper
