# encoding: utf-8
"""
@project: djangoModel->Auth
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 小程序SDK
@created_time: 2022/7/7 9:38
"""
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password
import jwt
from pathlib import Path
from main.settings import BASE_DIR
from ..models import BaseInfo, Auth
from ..utils.model_handle import parse_model
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict

module_root = str(Path(__file__).resolve().parent)
# 配置之对象
main_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_user"))
module_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_user"))

app_id = main_config_dict.app_id or module_config_dict.app_id or ""
app_secret = main_config_dict.secret or module_config_dict.secret or ""
jwt_secret_key = main_config_dict.jwt_secret_key or module_config_dict.jwt_secret_key or ""
expire_day = main_config_dict.expire_day or module_config_dict.expire_day or ""
expire_second = main_config_dict.expire_second or module_config_dict.expire_second or ""

class UserSmsService:

    def phone_login(self, phone):
        current_user = BaseInfo.objects.filter(phone=phone).filter()
        current_user = parse_model(current_user)

        if not current_user:
            base_info = {
                'user_name': '',
                'nickname': phone,
                'phone': phone,
                'email': '',
                'full_name': '请修改用户名',
            }
            BaseInfo.objects.create(**base_info)
            current_user = BaseInfo.objects.filter(phone=phone).filter()
            current_user = parse_model(current_user)
            current_user = current_user[0]
            # 生成登录token
            token = self.__set_token(current_user.get('id', None), phone)

            # 创建用户登录信息，绑定token
            auth = {
                'user_id': current_user.get('id', None),
                'password': make_password('123456', None, 'pbkdf2_sha1'),
                'plaintext': '123456',
                'token': token,
            }
            Auth.objects.update_or_create({'user_id': current_user.get('id', None)}, **auth)
            auth_set = Auth.objects.filter(user_id=current_user.get('id', None), password__isnull=False).order_by(
                '-update_time').first()
            return 0, {'token': auth_set.token, 'user_info': current_user}
        current_user = current_user[0]
        token = self.__set_token(current_user.get('id', None), phone)
        # 创建用户登录信息，绑定token
        auth = {
            'token': token,
        }
        Auth.objects.filter(user_id=current_user.get('id', None)).update(**auth)
        auth_set = Auth.objects.filter(user_id=current_user.get('id', None), password__isnull=False).order_by(
            '-update_time').first()
        return 0, {'token': auth_set.token, 'user_info': current_user}

    def __set_token(self, user_id, account):
        # 生成过期时间
        expire_timestamp = datetime.utcnow() + timedelta(
            days=7,
            seconds=0
        )
        # 返回token
        return jwt.encode(
            payload={'user_id': user_id, 'account': account, "exp": expire_timestamp},
            key=jwt_secret_key
        )
