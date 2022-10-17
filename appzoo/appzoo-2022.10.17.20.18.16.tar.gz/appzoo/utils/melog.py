#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : meloh
# @Time         : 2022/9/29 下午6:12
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 


from loguru import logger
# from mark import BASE_DIR
import logging

# logger.add(BASE_DIR/'run.log', serialize='json')


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Retrieve context where the logging call occurred, this happens to be in the 6th frame upward
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


# logging.getLogger("uvicorn").setLevel(10)
# logging.getLogger("uvicorn").handlers = []
# logging.getLogger("uvicorn").addHandler(InterceptHandler())

# logging.getLogger("uvicorn.error").setLevel(10)
# logging.getLogger("uvicorn.error").handlers = []
# logging.getLogger("uvicorn.error").addHandler(InterceptHandler())

# logging.getLogger("fawn.error").setLevel(10)
# logging.getLogger("fawn.error").handlers = []
# logging.getLogger("fawn.error").addHandler(InterceptHandler())

logger_name_list = [name for name in logging.root.manager.loggerDict]
# logger_name_list = [name for name in logging.root.manager.loggerDict if '.' not in name]

for logger_name in logger_name_list:
    logging.getLogger(logger_name).setLevel(10)
    logging.getLogger(logger_name).handlers = []
    if '.' not in logger_name:
        logging.getLogger(logger_name).addHandler(InterceptHandler())


print(logger_name_list)
print(logging.root.manager.loggerDict)
