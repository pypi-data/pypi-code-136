# -*- coding:utf-8 -*-
# utils/measure.py
# ---------------------------------------------------------
# 时间测量， 用于测试 函数功能耗时长短
#  2020-1-12
# 用法
#     time_measure = TimeMeasure('dance_check_in_report_get')
#     time_measure.measure('begin')
#
#     time_measure.measure('t1')
#     被测试函数
#     time_measure.measure('t2')
#     time_measure.show_time()      # 显示 t1 到 t2 的时间
#
#     time_measure.measure('end')
#     time_measure.show('end', 'begin')     # 显示 begin 到 end 的时间
# ---------------------------------------------------------
import time
import functools
from .logs import logger

__version__ = "1.2"
__author__ = ""
__all__ = [
    'TimeMeasure', 'timeit'
]

LOGGER = logger


class TimeMeasure(object):
    def __init__(self, module=''):
        self.module = module
        self.time_line = {}     # name: time
        self.out = True
        self.name_list = []

    def measure(self, name):
        tm = time.time()
        self.time_line[name] = tm
        self.name_list.append((name, tm))

    def show(self, pt1, pt2):
        if not self.out:
            return
        t1 = self.time_line.get(pt1)
        t2 = self.time_line.get(pt2)
        if t1 is None or t2 is None:
            return
        msg = '[%s] time elapse [%s - %s]: %s' % (self.module, pt1, pt2, abs(t1-t2))
        LOGGER.debug(msg)

    def show_time(self):
        if not self.out:
            return
        len_name = len(self.name_list)
        if len_name < 2:
            return
        n1, t1 = self.name_list[len_name - 1]
        n2, t2 = self.name_list[len_name - 2]
        msg = '[%s] time elapse [%s - %s]: %s' % (self.module, n1, n2, abs(t1 - t2))
        LOGGER.info(msg)


def timeit(desc=''):
    def timed(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = f(*args, **kwargs)
            t2 = time.time()
            LOGGER.debug(f'[{desc} {f.__name__}] time: {t2-t1}s')
            return result
        return wrapper
    return timed
