import json
import os
import time

import rsa
import base64
import logging
from pathlib import Path

from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from celery.utils.serialization import b64encode
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from wechatpy import WeChatPay
from wechatpy.utils import to_binary, to_text
from main.settings import BASE_DIR
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict

module_root = str(Path(__file__).resolve().parent)
# 配置之对象
main_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_payment"))
module_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_payment"))
# 服务商商户的APPID
app_id = main_config_dict.wechat_service_app_id or module_config_dict.wechat_service_app_id or ""

app_secret = main_config_dict.wechat_service_app_secret or module_config_dict.wechat_service_app_secret or ""

mch_id = main_config_dict.wechat_service_mch_id or module_config_dict.wechat_service_mch_id or ""

merchant_key = main_config_dict.wechat_service_merchant_key or module_config_dict.wechat_service_merchant_key or ""

sub_appid = main_config_dict.wechat_merchant_app_id or module_config_dict.wechat_merchant_app_id or ""

sub_app_secret = main_config_dict.wechat_merchant_app_secret or module_config_dict.wechat_merchant_app_secret or ""

sub_mch_id = main_config_dict.wechat_merchant_mch_id or module_config_dict.wechat_merchant_mch_id or ""

apiv3_secret = main_config_dict.wechat_apiv3_secret or module_config_dict.wechat_apiv3_secret or ""
# 密钥地址
private_key_path = main_config_dict.wechat_merchant_private_key_file or module_config_dict.wechat_merchant_private_key_file or (
        str(BASE_DIR) + "/config/apiclient_key.pem")
# 读取文件获取密钥
private_key = open(private_key_path, encoding="utf-8").read() if os.path.exists(private_key_path) else ""

url = "https://api.mch.weixin.qq.com/v3/pay/partner/transactions/jsapi"

logger = logging.getLogger(__name__)


def my_ali_pay():
    wechat = WeChatPay(
        appid=app_id,
        sub_appid=sub_appid,
        api_key=merchant_key,
        mch_id=mch_id,
        sub_mch_id=sub_mch_id,
        mch_key=apiv3_secret,
    )
    return wechat

# def format_url(params, api_key=None):
#     data = [to_binary('{0}={1}'.format(k, params[k])) for k in sorted(params) if params[k]]
#     if api_key:
#         data.append(to_binary('key={0}'.format(api_key)))
#     return b"&".join(data)


# def sign_str(method, url, timestamp, nonce_str, body):
#     """
#     拼接sign字符串
#     """
#     # sign_list = [
#     #     method,
#     #     url,
#     #     timestamp,
#     #     nonce_str,
#     #     body
#     # ]
#     sign_list = [
#         body['appId'],
#         body['timeStamp'],
#         body['nonceStr'],
#         body['package'],
#     ]
#     # print(sign_list)
#     return '\n'.join(sign_list) + '\n'


# 生成sign
# def calculate_sign(body, method, url, timestamp, nonce_str):
# a = sign_str(method, url, timestamp, nonce_str, json.dumps(body))
# signer = pkcs1_15.new(RSA.importKey(open(r"apiclient_key.pem").read()))
# a = sign_str(method, url, timestamp, nonce_str, json.dumps(body))
# a = sign_str(method, url, timestamp, nonce_str, body)
# signs = rsa_sign(private_key, a)
# cipher = SHA256.new(private_key)
# cipher_text = base64.encodebytes(cipher.encrypt(a))
# signer = pkcs1_15.new(RSA.importKey(private_key))
# signature = signer.sign(SHA256.new(a.encode("utf-8")))
# sign = base64.b64encode(signature).decode("utf-8").replace("\n", "")
# sign = cipher_text
# return None


# def rsa_sign(private_key, sign_str):
#     message = sign_str.encode('UTF-8')
#     signature = private_key.sign(data=message, padding=PKCS1v15(), algorithm=SHA256())
#     sign = b64encode(signature).decode('UTF-8').replace('\n', '')
#     return sign
#
#
# def get_pay_sign_info(data, prepay_id):
#     content = '{}\n{}\n{}\n{}\n'.format(data['appId'], data['timeStamp'], data['nonceStr'], data['package'])
#     signer = pkcs1_15.new(RSA.importKey(private_key))
#     print(private_key)
#     digest = SHA256.new(content.encode('utf-8'))
#     sign_v = base64.b64encode(signer.sign(digest)).decode('utf-8')
#     return {
#         'appid': data['appId'],
#         'timestamp': data['timeStamp'],
#         'noncestr': data['nonceStr'],
#         # 'prepay_id': prepay_id,
#         # 'package': 'Sign=WXPay',
#         "package": data['package'],
#         'sign': sign_v,
#     }
