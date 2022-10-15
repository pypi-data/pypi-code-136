#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-09-02
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : state.py
# @Software: orm
# @Function:

# 默认状态字典
default_state_dict = {
    'draft': {
        'draft': '草稿',
        'submitted': '已提交',
        'deleted': '已删除',
    },
    'submitted': {
        'submitted': '已提交',
        'deleted': '已删除',
    },
    'deleted': {
        'deleted': '已删除',
    },
}


class BaseState(object):
    """ 简易状态机 """

    def __init__(self, state_dict: dict = None):
        self._state_dict = state_dict or default_state_dict.copy()

    @property
    def state_dict(self) -> dict:
        return self._state_dict

    @state_dict.setter
    def state_dict(self, value: dict) -> None:
        self._state_dict = value

    def action(self, source: str, target: str):
        """ 行动，进行状态流转 """

        _source = self._state_dict.get(source)
        if not _source:
            return None
        _target = _source.get('target')
        if not _target:
            return None
        return _target
