# -*- coding: utf-8 -*-
import re
import urllib.parse
import time
import requests
import hmac
import json
import base64
import hashlib


class DingTalkException(IOError):
    def __init__(self, *args):
        super().__init__(*args)


class DingTalkApp:
    def __init__(self, dingtalk_token, webhook_secret=None):
        _signs = self._secure_sign(webhook_secret)
        self.msg_type = ['text', 'markdown']
        _token = dingtalk_token
        self.robot_url = "https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}".format(
            _token, _signs[0], _signs[1]
        )

    @staticmethod
    def _secure_sign(secret):
        """
        加签,只有机器人选择加签安全验证方式时使用
        :param secret: secret for DingDing robot!
        :return: tuple(timestamp, sign)
        """
        timestamp = str(round(time.time() * 1000))
        _secret = secret
        secret_enc = _secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, _secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

    def send(self, title=None, content=None, msg_type='text', at_users=None) -> tuple:
        """
        发送消息
        :param title:
        :param content:
        :param msg_type:
        :param at_users:
        :return: tuple(Bool,str)
        """
        if title is None:
            title = ""
        if content is None:
            content = ""
        if msg_type == 'text':
            contents = {'msgtype': msg_type,msg_type: {'title': title, 'content': content}}
        elif msg_type == 'markdown':
            contents = {'msgtype': msg_type, msg_type: {'title': title, 'text': content}}
        else:
            raise DingTalkException("不支持的消息类型：{}, 当前仅支持：{}".format(msg_type, ','.join(x for x in self.msg_type)))

        contents['at'] = self._load_at_list(at_users)
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(self.robot_url, headers=headers, data=json.dumps(contents))
        if resp.status_code == 200:
            if resp.json().get('errcode') != 0:
                raise DingTalkException(resp.json().get('errmsg'))
            else:
                return True, "DingDing notify send succeed! "
        return False, "DingDing notify send failed! "

    @staticmethod
    def _load_at_list(users=None):
        if users is None:
            return []
        at_users = {}
        if users == 'all' or users == 'All':
            at_users['isAtAll'] = 'true'
        else:
            for user in users.split(','):
                if re.findall(r"1[3-9]\d{9}", user):
                    if 'atMobiles' not in at_users.keys():
                        at_users['atMobiles'] = [user]
                    else:
                        at_users['atMobiles'].append(user)
                else:
                    if 'atUserIds' not in at_users.keys():
                        at_users['atUserIds'] = [user]
                    else:
                        at_users['atUserIds'].append(user)
        return at_users


class DingTalkApi(object):
    def __init__(self, config):
        self.config = config
        self.NAME = config['NAME']
        self.APP_LIST_CONFIG = config['APP_LIST']
        self.apps = {}
        self.init_apps()

    def init_apps(self):
        for k, v in self.APP_LIST_CONFIG.items():
            app = DingTalkApp(v['token'], v['secret'])
            self.apps[k] = app

    def __getattr__(self, item):
        return self.apps.get(item)
