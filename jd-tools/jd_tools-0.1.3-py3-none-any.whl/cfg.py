# -*- coding: utf8 -*-
""" 读取程序启动所需的配置，从配置文件 startup.ini 中读取配置。

用法：
cfg = Cfg("test.ini")     # 实例化 启动配置文件 读取对象
print(cfg.sections())

===============================================================================
Author:     WXG
Date:       2019-07-17

DATE        AUTHOR  DESCRIPTION
----------  ------  -----------------------------------------------------------------
2022-07-08  WXG     cfg 新增获取字符串类型的函数 str_val , 版本改为 2.3
2022-07-12  WXG     cfg 新增获取配置文件 段名称列表函数 sections , 版本改为 2.5
2022-07-23  WXG     redis 配置 移动到段[redis]中 , 版本改为 2.7
"""
from .parser_config import JdIniReader, NO_SECTION_OR_KEY

__all__ = ['Cfg', 'STARTUP_SECTION_TASKS', 'STARTUP_SECTION_DB']
__version__ = '2.9.3'


STARTUP_SECTION_RUN = 'run'
STARTUP_SECTION_REDIS = 'redis'             # redis 配置
STARTUP_SECTION_DB = 'db'                   # 主数据库
STARTUP_SECTION_FACE = 'face_recognize'     # 人脸识别
STARTUP_SECTION_CARD = 'card_recognize'     # 读卡器
STARTUP_SECTION_GZH = 'gzh'                 # 微信公众号相关配置
STARTUP_SECTION_TASKS = 'tasks'             # 定时任务 配置段


class FaceRecognize(object):
    """人脸识别参数"""
    def __init__(self, host, port, output):
        self._host = host
        self._port = port
        self._output = output

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def output(self):
        return self._output


class Cfg(object):
    """程序启动后读取配置文件， 如配置文件/Section/key不存在，对应值返回 0 ****"""

    def __init__(self, path_filename):
        # 读取默认配置文件
        try:
            self.__startup_cfg = JdIniReader(path_filename)
        except IOError:
            self.__startup_cfg = None

        # 是否 腾讯 token 主控服务器    0 否， 1 是
        self.__is_token_server = self.__get_v(STARTUP_SECTION_RUN, 'is_token_server')
        # 是否创建微信公众号自定义菜单    0 否， 1 是
        self.__is_create_menu = self.__get_v(STARTUP_SECTION_RUN, 'create_wx_menu')
        self.__sandbox = self.__get_v(STARTUP_SECTION_RUN, 'sandbox')
        self.__wx_test = self.__get_v(STARTUP_SECTION_RUN, 'wx_test')
        self.__user = self.__get_v(STARTUP_SECTION_DB, 'user')
        self.__password = self.__get_v(STARTUP_SECTION_DB, 'pwd')
        self.__database = self.__get_v(STARTUP_SECTION_DB, 'database')
        v = self.__get_v(STARTUP_SECTION_DB, 'host')
        self.__host = 'localhost' if v == 0 else v
        self.__port = self.__get_v(STARTUP_SECTION_DB, 'port', 3306)
        self.__is_mysql = self.__get_v(STARTUP_SECTION_DB, 'use_mysql', 1)
        self.__start_face_server = self.__get_v(STARTUP_SECTION_RUN, 'start_face_server')
        v = self.__get_v(STARTUP_SECTION_FACE, 'host')
        face_host = 'localhost' if v == 0 else v
        self.face = FaceRecognize(face_host,
                                  self.__get_v(STARTUP_SECTION_FACE, 'port', 9999),
                                  self.__get_v(STARTUP_SECTION_FACE, 'output'))

        self.__start_card_server = self.__get_v(STARTUP_SECTION_RUN, 'start_card_server')
        v = self.__get_v(STARTUP_SECTION_CARD, 'host')
        card_host = 'localhost' if v == 0 else v
        self.card = FaceRecognize(card_host,
                                  self.__get_v(STARTUP_SECTION_CARD, 'port', 9998),
                                  self.__get_v(STARTUP_SECTION_CARD, 'output'))
        self.__http_port = self.__get_v(STARTUP_SECTION_RUN, 'http_port', 80)

    @property
    def is_token_server(self):
        return self.__is_token_server

    @property
    def is_create_menu(self):
        return self.__is_create_menu

    @property
    def sandbox(self):
        return self.__sandbox

    @property
    def wx_test(self):
        return self.__wx_test

    @property
    def start_face_server(self):        # 是否启用人脸识别服务器。 1 是； 0 否
        return self.__start_face_server

    @property
    def start_card_server(self):        # 是否启用读卡器服务器。 1 是； 0 否
        return self.__start_card_server

    @property
    def http_port(self):  # web 服务器端口号 默认 80
        return self.__http_port

    @property
    def ws_port(self):  # web socket 服务器端口号 默认 31298
        ws = self.__get_v(STARTUP_SECTION_RUN, 'ws_port', 31298)
        return ws

    @property
    def http_host(self):  # web 服务器 ip， 默认 127.0.0.1
        v_ = self.__get_v(STARTUP_SECTION_RUN, 'http_host')
        return '127.0.0.1' if v_ == 0 else v_

    @property
    def ws_async_mode(self):  # ws 异步模式， 默认 None
        v_ = self.__get_v(STARTUP_SECTION_RUN, 'ws_async_mode')
        return None if v_ == 0 else v_

    @property
    def send_error_email(self):  # 发送异常邮件。 默认 0 否
        v_ = self.__get_v(STARTUP_SECTION_RUN, 'send_error_email')
        return v_

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def database(self):
        return self.__database

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def is_mysql(self):
        return self.__is_mysql

    @property
    def redis_pwd(self) -> str:
        return self.__get_v_str(STARTUP_SECTION_REDIS, 'password')

    @property
    def redis_host(self) -> str:
        return self.__get_v_str(STARTUP_SECTION_REDIS, 'host', 'localhost')

    @property
    def redis_port(self) -> int:
        return self.__get_v(STARTUP_SECTION_REDIS, 'port', 6379)

    @property
    def cyt_web_server(self):  # 财艺通 线上服务器
        return self.__get_v(STARTUP_SECTION_RUN, 'cyt_web_server')

    @property
    def task_backup_db(self):       # 启动 备份 数据库 任务
        return self.__get_v(STARTUP_SECTION_TASKS, 'backup_db', 1)

    @property
    def task_wx_token(self):        # 获取 微信公众号 token 任务
        return self.__get_v(STARTUP_SECTION_TASKS, 'wx_token', 1)

    @property
    def gzh_openid(self):  # 微信公众号 openid
        v_ = self.__get_v(STARTUP_SECTION_GZH, 'openid')
        return '' if v_ == 0 else v_

    @property
    def gzh_company_id(self):  # 微信公众号 发送模板消息的 公司id for test ==============
        v_ = self.__get_v(STARTUP_SECTION_GZH, 'company_id')
        return '' if v_ == 0 else v_

    def __get_v(self, s, k, default=0):
        """获取 section=s, key=k的值。 若 s,k 不存在，返回 0. 存在 返回 配置值 v"""
        v = NO_SECTION_OR_KEY
        if self.__startup_cfg:
            v = self.__startup_cfg.get(s, k)

        return v if v != NO_SECTION_OR_KEY else default

    def __get_v_str(self, s, k, default=''):
        """获取 section=s, key=k的值。 若 s,k 不存在，返回 ''. 存在 返回 配置值 v"""
        v = NO_SECTION_OR_KEY
        if self.__startup_cfg:
            v = self.__startup_cfg.get(s, k)

        return str(v) if v != NO_SECTION_OR_KEY else default

    def face_key(self, key):    # 人脸识别 key value 获取
        return self.__get_v(STARTUP_SECTION_FACE, key)

    def face_heat_beat(self):   # 刷脸考勤  是否输出心跳包
        return self.face_key('heart_beat')

    @property
    def show_rsp(self):   # 请求相应
        return self.__get_v(STARTUP_SECTION_RUN, 'show_rsp')

    def show_template(self):   # 显示微信模板内容
        return self.__get_v(STARTUP_SECTION_RUN, 'show_template')

    def get_val(self, val, key=STARTUP_SECTION_RUN):  # 获取配置项，返回值是字符串 或者 数值（能转强转）
        return self.__get_v(key, val)

    def str_val(self, val, key=STARTUP_SECTION_RUN):  # 获取配置项，返回值为字符串
        return self.__get_v_str(key, val)

    def sections(self):   # 查询配置文件中的 段 名称列表
        if not self.__startup_cfg:
            return []
        return self.__startup_cfg.sections()
