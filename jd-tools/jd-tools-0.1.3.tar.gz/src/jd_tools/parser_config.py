# -*- coding: utf8 -*-
# =============================================================================
# 文件:  parser_config.py
# 日期:  2021/10/7 14:01
# ini 文件 解析类。
#
# 例如
# ; ini 文件示例， 本行为注释行
# [section_name]
# key = 1  ; 注释内容，英文分号后为注释内容， 整型数字 会转换为 int
# key2 = test   ; 非 整形数字，会返回字符串
#
# 行注释中存在 分号(;) 时， 会忽略注释内容。
# 用法：
#   cfg = JdIniReader(filename)
#   value = cfg.get('section_name', 'key')      # value == 1， 而不是 '1'
#   or
#   val_list = cfg.get('section_name')     # val_list 为 [('key', 1), ('key2', 'test')]
#
# ConfigParser 会将所有的 key 都转换为 小写
# =============================================================================
import os

from configparser import ConfigParser
from threading import Lock
from .tools import JdTools


__version__ = '1.3'


def lock(func):
    def wrapper(self, *args, **kwargs):  # self变量,可以调用对象的相关方法
        with Lock():
            return func(self, *args, **kwargs)

    return wrapper


NO_SECTION_OR_KEY = '<no_section_or_key>'


# 解决ConfigParser模块读取、写入文件时自动转换为小写字符的问题
# 第二种解决方案是自己写一个MyConfigParser，继承自ConfigParser，重写一下optionxform()方法：
class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, option_str):
        return option_str


class JdIniReader(object):
    """
    读写ini配置文件
    """

    def __init__(self, path):
        self.path = path

        if not os.path.exists(self.path):
            raise IOError('file {} not found!'.format(self.path))
        try:
            self.cf = MyConfigParser()
            self.cf.read(self.path, encoding='UTF-8')
        except Exception as e:
            raise IOError(e)

    def get(self, section, key):
        """读取配置文件数据"""

        if self.cf.has_section(section) and key in self.cf.options(section):
            val = self.cf.get(section, key)
            return JdIniReader.__trim_del_comment(val)
        else:
            return NO_SECTION_OR_KEY

    def sections(self):
        """返回可用的section的列表; 默认section不包括在列表中"""
        return self.cf.sections()

    def get_section(self, section):
        """读取配置文件中某个section下的所有key和value， 返回值 [(k:v),(k:v),...]"""
        lst = self.cf.items(section)
        ret = list()
        for i in lst:
            ret.append((i[0], JdIniReader.__trim_del_comment(i[1])))
        return ret

    @lock
    def set(self, section, key, value):
        """向配置文件写入数据"""
        self.cf.set(section, key, value)
        with open(self.path, 'w', encoding='utf-8') as f:
            self.cf.write(f)

    @staticmethod
    def __trim_del_comment(val):
        # 过滤空格， 删除 ; 或 # 号及后面的所有注释字符
        i = val.find(';')
        j = val.find('#')
        if i >= 0 and j >= 0:
            m = min(i, j)
        elif i >= 0:
            m = i
        elif j >= 0:
            m = j
        else:
            m = -1  # 分号和井号都没有
        if m >= 0:
            val = val[0: m]
        v2 = JdTools.trim(val)
        try:
            v2 = int(v2)    # 若可以转换为 int，则转换，否则原样返回
        except ValueError:
            pass
        return v2
