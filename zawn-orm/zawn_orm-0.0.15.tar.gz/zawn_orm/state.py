#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-09-02
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : state.py
# @Software: orm
# @Function:


class BaseState():
    STATE_SUBMIT: str = 'submitted'  # 已提交状态
    STATE_DELETE: str = 'deleted'  # 已删除状态

    instance = None
    state_dict = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
            cls.state_dict = cls.get_state_dict()
        return cls.instance

    @classmethod
    def get_state_dict(cls, **kwargs):
        """ 获取状态字典 """
        return {
            'submit': [  # 提交
                {'from': '_', 'to': 'submitted'},
            ],
            'delete': [  # 删除
                {'from': 'submitted', 'to': 'deleted'},
            ],
        }
