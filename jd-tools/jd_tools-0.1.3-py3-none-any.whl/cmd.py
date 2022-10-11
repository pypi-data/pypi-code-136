# -*- coding: utf8 -*-
import datetime
from .tools import singleton

__version__ = '1.3'
__all__ = ['log', 'cmd', 'JdCmd']


@singleton
class JdCmd(object):
    def __init__(self):
        self._cmd_file = ''  # 输出文件
        self._log_file = ''  # 输出文件
        self._std_out = True    # 输出到屏幕

    @property
    def cmd_file(self):
        return self._cmd_file

    @property
    def log_file(self):
        return self._log_file

    @cmd_file.setter
    def cmd_file(self, new_file):
        self._cmd_file = new_file

    @log_file.setter
    def log_file(self, new_file):
        self._log_file = new_file

    @property
    def output(self):
        return self._std_out

    @output.setter
    def output(self, val):
        self._std_out = val


def log(*args, **kwargs):
    """
    写日志文件，并在 屏幕输出日志
    :param args:        普通参数
    :param kwargs:      key value, 字典
    :return:
    """
    today = datetime.datetime.today()
    date_str = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
    ms = '%03d' % (today.microsecond // 1000)
    formatted = f'[{date_str},{ms}]'
    jd_cmd = JdCmd()
    if jd_cmd.output:  # 通过配置文件 控制 是否 输出到屏幕
        print(formatted, *args, **kwargs)
    if jd_cmd.log_file:
        with open(jd_cmd.log_file, 'a', encoding='utf-8') as f:
            print(formatted, *args, file=f, **kwargs)


def cmd(*args, **kwargs):
    """
    写日志文件，并在 屏幕输出日志
    :param args:        普通参数
    :param kwargs:      key value, 字典
    :return:
    """
    today = datetime.datetime.today()
    date_str = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
    ms = '%03d' % (today.microsecond // 1000)
    formatted = f'[{date_str},{ms}]'
    jd_cmd = JdCmd()
    print(formatted, *args, **kwargs)
    if jd_cmd.cmd_file:
        with open(jd_cmd.cmd_file, 'a', encoding='utf-8') as f:
            print(formatted, *args, file=f, **kwargs)
