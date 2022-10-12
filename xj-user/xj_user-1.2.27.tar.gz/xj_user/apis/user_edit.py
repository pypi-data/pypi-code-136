# _*_coding:utf-8_*_

import os, logging, time, json, copy
import re
import jwt
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password
from main.settings import BASE_DIR
from pathlib import Path
from rest_framework import response
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.db.models import Q

from xj_role.services.user_group_service import UserGroupService
from xj_role.services.role_service import RoleService
from ..models import *
from ..services.user_service import UserService
from ..utils.model_handle import parse_data, model_delete
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict

module_root = str(Path(__file__).resolve().parent)
# 配置之对象
main_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_user"))
module_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_user"))

jwt_secret_key = main_config_dict.jwt_secret_key or module_config_dict.jwt_secret_key or ""

logger = logging.getLogger(__name__)


class UserInfoSerializer(serializers.ModelSerializer):
    # 方法一：使用SerializerMethodField，并写出get_platform, 让其返回你要显示的对象就行了
    # p.s.SerializerMethodField在model字段显示中很有用。
    # platform = serializers.SerializerMethodField()

    # # 方法二：增加一个序列化的字段platform_name用来专门显示品牌的name。当前前端的表格columns里对应的’platform’列要改成’platform_name’
    user_id = serializers.ReadOnlyField(source='id')

    # platform_id = serializers.ReadOnlyField(source='platform.platform_id')
    # platform_name = serializers.ReadOnlyField(source='platform.platform_name')

    class Meta:
        model = BaseInfo
        fields = [
            'user_id',
            # 'platform',
            # 'platform_uid',
            # 'platform__platform_name',
            # 'platform_id',
            # 'platform_name',
            'user_name',
            'full_name',
            'phone',
            'email',
            'wechat_openid',
            'user_info',
        ]
        # exclude = ['platform_uid']

    # 这里是调用了platform这个字段拼成了get_platform
    def get_platform(self, obj):
        return obj.platform.platform_name
        # return {
        #     'id': obj.platform.platform_id,
        #     'name': obj.platform.platform_name,
        # }


# 获取用户信息
class UserEdit(generics.UpdateAPIView):  # 或继承(APIView)
    permission_classes = (AllowAny,)  # 允许所有用户 (IsAuthenticated,IsStaffOrBureau)
    serializer_class = UserInfoSerializer
    params = None

    def post(self, request, *args, **kwargs):
        # self.params = request.query_params.copy()  # 返回QueryDict类型
        self.params = request.data.copy()  # 返回QueryDict类型
        # print("> params:", self.params)
        # print("> params: user_info:", self.params.get('user_info', ''))
        # print("> params: user_info:", type(self.params.get('user_info', '')))

        try:
            token = self.request.META.get('HTTP_AUTHORIZATION', '')
            if re.match(r'Bearer (.*)', token):
                token = re.match(r'Bearer (.*)', token).group(1)
            # print("> token:", token)

            if not token:
                raise MyApiError('缺少Token', 3001)

            # 判断token是否失效
            t_auth = Auth.objects.filter(token=token).order_by('-update_time').first()
            # print("> t_auth:", t_auth)
            if not t_auth:
                raise MyApiError('token失效', 3002)

            # 如果有用户ID则找到该ID，没有则修改自己的ID
            # print("> self.params['user_id']:", self.params)
            if 'user_id' in self.params:
                user_id = self.params.get('user_id', '')
            else:
                user_id = t_auth.user_id
            # print("> user_id:", user_id)

            t_user = BaseInfo.objects.get(id=user_id)
            # print("> t_user:", t_user)

            # 检查必填项
            # if not self.params.get('platform_uid', ''):
            #     self.params['platform_uid'] = t_user.platform_uid
            if not self.params.get('user_name', ''):
                self.params['user_name'] = t_user.user_name

            serializer = UserInfoSerializer(instance=t_user, data=self.params, )
            if not serializer.is_valid():
                raise MyApiError(serializer.errors, 3003)
            serializer.save()

            res = {
                'err': 0,
                'msg': '修改成功',
            }

        except SyntaxError:
            # print("> SyntaxError:")
            res = {
                'err': 4001,
                'msg': '语法错误'
            }
        except LookupError:
            res = {
                'err': 4002,
                'msg': '无效数据查询'
            }
        # 这里 error是一个类的对象，要用error.属性名来返回
        except Exception as error:
            res = {
                'err': error.err if hasattr(error, 'err') else 4000,  # 发生系统异常时报4000
                'msg': error.msg if hasattr(error, 'msg') else error.args,  # 发生系统异常时捕获error.args
            }
            if not hasattr(error, 'err'):
                res['file'] = error.__traceback__.tb_frame.f_globals["__file__"],  # 发生异常所在的文件
                res['line'] = error.__traceback__.tb_lineno,  # 发生异常所在的行数
        except:
            res = {
                'err': 4999,
                'msg': '未知错误'
            }

        # return super(UserLogin, self).patch(request, *args, **kwargs)
        return response.Response(res)

    def put(self, request, *args, **kwargs):
        self.params = parse_data(request)
        # 权限验证
        token = request.META.get('HTTP_AUTHORIZATION', '')
        token_serv, error_text = UserService.check_token(token)
        if error_text:
            raise MyApiError(error_text, 6010)
            # 判断token是否失效
        if re.match(r'Bearer(.*)$', token, re.IGNORECASE):
            token = re.match(r'Bearer(.*)$', token, re.IGNORECASE).group(1).strip()
        t_auth = Auth.objects.filter(token=token).order_by('-update_time').first()
        # print("> t_auth:", t_auth)
        if not t_auth:
            raise MyApiError('token失效', 3002)

        # 如果有用户ID则找到该ID，没有则修改自己的ID
        # print("> self.params['user_id']:", self.params)
        if 'user_id' in self.params:
            user_id = self.params.get('user_id', '')
        else:
            user_id = t_auth.user_id
        # print("> user_id:", user_id)
        # 添加逻辑
        try:
            account = str(self.params.get('account', ''))
            # password = str(self.params.get('password', ''))
            phone = str(self.params.get('phone', ''))
            full_name = str(self.params.get('full_name', ''))
            nickname = str(self.params.get('nickname', ''))

            # 用户角色部门绑定
            user_role_list = self.params.get('user_role_list', None)
            user_group_list = self.params.get('user_group_list', None)

            # 边界检查
            if not account:
                raise MyApiError("account必填", 2001)

            # if not password:
            #     raise MyApiError("password必填", 2003)

            if not full_name:
                raise MyApiError("full_name必填", 2008)

            # 账号类型判断
            if re.match(r'(^1[356789]\d{9}$)|(^\+?[78]\d{10}$)', account):
                account_type = 'phone'
            elif re.match(r'^\w+[\w\.\-\_]*@\w+[\.\w]*\.\w{2,}$', account):
                account_type = 'email'
            elif re.match(r'^[A-z\u4E00-\u9FA5]+\w*$', account):
                account_type = 'username'
            else:
                raise MyApiError("账号必须是用户名、手机或者邮箱，用户名不能是数字开头", 2009)

            # 检查账号是否存在
            user_list = None
            if account_type == 'phone':
                user_list = BaseInfo.objects.filter(Q(phone=account), ~Q(id=user_id))
            elif account_type == 'email':
                user_list = BaseInfo.objects.filter(Q(email=account), ~Q(id=user_id))
            elif account_type == 'username':
                user_list = BaseInfo.objects.filter(Q(user_name=account), ~Q(id=user_id))
            if user_list.count() and account_type == 'phone':
                raise MyApiError("手机已被注册: " + account)
            elif user_list.count() and account_type == 'email':
                raise MyApiError("邮箱已被注册: " + account)
            elif user_list.count() and account_type == 'username':
                raise MyApiError("用户名已被注册: " + account)

            # # 检查平台是否存在
            # platform_id = None
            # platform_set = Platform.objects.filter(platform_name__iexact=platform)
            # if not platform_set.count() == 0:
            #     platform_id = platform_set.first().platform_id

            base_info = {
                'user_name': account if account_type == 'username' else '',
                'full_name': full_name,
                "nickname": nickname,
                'phone': account if account_type == 'phone' else phone,
                'email': account if account_type == 'email' else '',
            }
            current_user = BaseInfo.objects.filter(id=user_id).update(**base_info)
            # token = jwt.encode({'account': account}, jwt_secret_key)
            # auth = {
            #     'user_id': user_id,
            #     'password': make_password(password, None, 'pbkdf2_sha1'),
            #     'plaintext': password,
            #     'token': token,
            # }
            # Auth.objects.create(**auth)
            # 用户绑定权限和部门
            if user_group_list:
                UserGroupService.bind_user_group(user_id, user_group_list)

            if user_role_list:
                RoleService.bind_user_role(user_id, user_role_list)

            res = {
                'err': 0,
                'msg': '修改成功',
                'data': {"user_id": user_id},
            }

        except SyntaxError:
            res = {
                'err': 4001,
                'msg': '语法错误'
            }
        except LookupError:
            res = {
                'err': 4002,
                'msg': '无效数据查询'
            }
        except Exception as valueError:
            res = {
                'err': valueError.err if hasattr(valueError, 'err') else 4000,
                'msg': valueError.msg if hasattr(valueError, 'msg') else valueError.args,
            }
        except:
            res = {
                'err': 4999,
                'msg': '未知错误'
            }

        return response.Response(data=res, status=None, template_name=None, headers={"Authorization": token},
                                 content_type=None)

    def delete(self, request, *args, **kwargs):
        return model_delete(request, BaseInfo)


class MyApiError(Exception):
    def __init__(self, message, err_code=4010):
        self.msg = message
        self.err = err_code

    def __str__(self):
        # repr()将对象转化为供解释器读取的形式。可省略
        return repr(self.msg)
