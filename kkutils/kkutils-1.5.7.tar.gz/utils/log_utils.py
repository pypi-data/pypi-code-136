#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: zhangkai
Email: zhangkai@cmcm.com
Last modified: 2018-01-05 11:27:36
'''

import logging
from functools import lru_cache

from coloredlogs import BasicFormatter, ColoredFormatter


class WatchedFileHandler(logging.handlers.WatchedFileHandler):
    '''重写handler，使指定级别的日志只写入指定的文件中'''

    def emit(self, record):
        if record.levelno == self.level:
            super(WatchedFileHandler, self).emit(record)


class CustomAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        return f"[{self.extra}] {msg}", kwargs


FIELD_STYLES = dict(
    asctime=dict(color='cyan'),
    hostname=dict(color='magenta'),
    levelname=dict(color='black', bold=True),
    filename=dict(color='magenta'),
    name=dict(color='blue'),
    threadName=dict(color='green')
)

LEVEL_STYLES = dict(
    debug=dict(color='blue'),
    info=dict(color='green'),
    warning=dict(color='yellow'),
    error=dict(color='red'),
    critical=dict(color='red')
)


@lru_cache()
def Logger(filename=None, name=None, level='INFO', stream=True, prefix=None):
    logger = logging.getLogger(name)
    if logger.handlers and logger.handlers[0].name == 'Logger':
        return logger

    logger.setLevel(level.upper())
    logger.propagate = False
    logger.handlers = []
    logfmt = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'

    if stream:
        handler = logging.StreamHandler()
        handler.setFormatter(ColoredFormatter(logfmt, level_styles=LEVEL_STYLES, field_styles=FIELD_STYLES))
        handler.name = 'Logger'
        logger.addHandler(handler)

    if filename:
        handler = logging.handlers.WatchedFileHandler(filename=filename, mode='a', encoding='utf-8')
        handler.setFormatter(BasicFormatter(logfmt))
        handler.name = 'Logger'
        logger.addHandler(handler)

    if prefix:
        logger = CustomAdapter(logger, prefix)

    return logger
