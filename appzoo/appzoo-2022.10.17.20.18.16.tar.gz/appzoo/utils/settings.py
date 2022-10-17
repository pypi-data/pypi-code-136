#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : settings.py
# @Time         : 2022/9/23 下午3:54
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://blog.csdn.net/weixin_45389126/article/details/115307525

import logging
from appzoo.utils.handlers import FastApiHandler


def uvicorn_logger_init():
    LOGGER_NAMES = ("uvicorn.asgi", "uvicorn.access", "uvicorn", "uvicorn.error")

    # change handler for default uvicorn logger
    logging.getLogger().handlers = [FastApiHandler()]

    for logger_name in LOGGER_NAMES:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [FastApiHandler()]
