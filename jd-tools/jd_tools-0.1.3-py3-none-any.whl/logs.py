# -*- coding: utf8 -*-
# 文件:  logs.py
# 日期:  2021/11/28 17:42
import logging
from logging.handlers import RotatingFileHandler


__version__ = '1.1.2'
__all__ = ["jd_config_logger", "JdRequestFormatter", "jd_set_logger_file_handler",
           "JD_LOG_FMT", "logger"
           ]


class JdRequestFormatter(logging.Formatter):  # 自定义格式化类
    def format(self, record):
        """每次生成日志时都会调用, 该方法主要用于设置自定义的日志信息
        :param record 日志信息"""
        try:
            from flask import request

            record.url = request.path  # 获取请求的 url url_rule
            record.ip = request.remote_addr  # 获取客户端的ip
        except (RuntimeError, ImportError):
            record.url = '.'
            record.ip = '.'

        return super().format(record)  # 执行父类的默认操作


LOG_FORMAT = ('%(levelname) -10s %(asctime)s  %(name) -50s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')

JD_LOG_FMT = '[%(asctime)s] %(ip)s -- %(url)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'


# flask 中的运行错误也会记录到flask.app的日志中
def jd_config_logger(log, filename=None, count=5, size=50):
    """配置 flask 日志"""
    # 创建flask.app日志器
    jd_logger = log
    # 设置全局级别
    jd_logger.setLevel('DEBUG')

    # 创建控制台处理器
    console_handler = logging.StreamHandler()

    # 给处理器设置输出格式
    file_formatter = JdRequestFormatter(JD_LOG_FMT)

    # fmt = '[%(asctime)s] %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    # console_formatter = logging.Formatter(fmt)
    console_handler.setFormatter(file_formatter)

    # 日志器添加处理器
    jd_logger.addHandler(console_handler)

    # 创建文件处理器
    if filename:
        jd_set_logger_file_handler(log, filename, count, size)


def jd_set_logger_file_handler(log, filename, count=5, size=50):
    # 创建文件处理器
    jd_logger = log
    file_handler = RotatingFileHandler(filename=filename, maxBytes=size * 1024 * 1024, backupCount=count,
                                       encoding='utf-8')

    # 给处理器设置输出格式
    file_formatter = JdRequestFormatter(JD_LOG_FMT)

    # 给处理器设置输出格式
    file_handler.setFormatter(file_formatter)
    # 单独设置文件处理器的日志级别
    file_handler.setLevel('DEBUG')

    # 日志器添加处理器
    jd_logger.addHandler(file_handler)


logger = logging.getLogger('app')
jd_config_logger(logger)
