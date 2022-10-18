#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random, string
from test_script import *
from lcyframe.libs import cprint, utils


def get_admin_member(*args, **kwargs):
    """
    无说明:
    """
    headers = {"token": "111"}
    files = {}
    params = {
        "uid": 0,     # int,必填,uid
        }
    return send(methed="get", url="/admin/member", params=params, headers=headers, files=files)

def post_admin_member(*args, **kwargs):
    """
    无说明:
    """
    headers = {}
    files = {}
    params = {
        "user_name": "",     # str,必填,无描述
        "pass_word": "",     # str,必填,无说明，无说明
        "nick_name": "",     # str,必填,无描述
        "sex": 0,     # int,必填,1 无说明 0 无说明
        "mobile": "",     # str,必填,无说明
        "email": "",     # str,必填,无说明
        "gid": 0,     # int,必填,无说明 1 无说明 2 无说明
        }
    return send(methed="post", url="/admin/member", params=params, headers=headers, files=files)

def put_admin_member(*args, **kwargs):
    """
    无说明:
    """
    headers = {}
    files = {}
    params = {
        "uid": 0,     # int,必填,无描述
        "nick_name": "",     # str,选填,无描述
        "sex": 0,     # int,选填,1 无说明 0 无说明
        "mobile": "",     # str,选填,无说明
        "email": "",     # str,选填,无说明
        "gid": 0,     # int,选填,无说明 1 无说明 2 无说明
        }
    return send(methed="put", url="/admin/member", params=params, headers=headers, files=files)

def delete_admin_member(*args, **kwargs):
    """
    无说明:
    """
    headers = {}
    files = {}
    params = {
        "uid": 0,     # int,选填,uid
        }
    return send(methed="delete", url="/admin/member", params=params, headers=headers, files=files)


def post_admin_login(*args, **kwargs):
    """
    登录:
    """
    headers = {}
    files = {}
    params = {
        "user_name": "",     # str,必填,用户名
        "pass_word": "",     # str,必填,密码
        }
    return send(methed="post", url="/admin/login", params=params, headers=headers, files=files)


def post_admin_resetpwd(*args, **kwargs):
    """
    忘记密码:
    """
    headers = {}
    files = {}
    params = {
        "pass_word": "",     # str,必填,旧密码
        "新密码": "",     # str,必填,无说明
        }
    return send(methed="post", url="/admin/resetpwd", params=params, headers=headers, files=files)


def post_admin_find(*args, **kwargs):
    """
    无说明:无说明（无说明）
    """
    headers = {}
    files = {}
    params = {
        "page": "",     # str,必填,无说明
        }
    return send(methed="post", url="/admin/find", params=params, headers=headers, files=files)

def get_admin_find(*args, **kwargs):
    """
    无说明:无说明
    """
    headers = {}
    files = {}
    params = {
        }
    return send(methed="get", url="/admin/find", params=params, headers=headers, files=files)


def batch_groups():
    """
    测试簇
    一键测试
    """
    get_admin_member()       # 无说明
    post_admin_member()       # 无说明
    put_admin_member()       # 无说明
    delete_admin_member()       # 无说明
    post_admin_login()       # 登录
    post_admin_resetpwd()       # 忘记密码
    post_admin_find()       # 无说明
    get_admin_find()       # 无说明
    

if __name__ == "__main__":
    # 无说明
    get_admin_member()
    # 无说明
    # post_admin_member()
    # # 无说明
    # put_admin_member()
    # # 无说明
    # delete_admin_member()
    # # 登录
    # post_admin_login()
    # # 忘记密码
    # post_admin_resetpwd()
    # # 无说明
    # post_admin_find()
    # # 无说明
    # get_admin_find()
    