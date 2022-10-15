#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-08-25
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : exception.py
# @Software: orm
# @Function:


class EmptyModelException(Exception):
    """ 空模型异常类 """


class InvalidFieldException(Exception):
    """ 无效字段异常类 """


class ExisitFieldException(Exception):
    """ 存在字段异常类 """


class InvalidValueException(Exception):
    """ 无效值异常类 """


class InvalidOperationException(Exception):
    """ 无效操作异常类 """
