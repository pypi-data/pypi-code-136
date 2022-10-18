#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random, string
from test_script import *
from lcyframe.libs import cprint, utils


def get_permission_groups(*args, **kwargs):
    """
    角色详情:

    参数:
    - group_id # 必填,int,角色id
    """
    headers = {}
    files = {}
    params = {
        "group_id": 27,
        "content_type": 0
    }
    return send(methed="get", url="/permission/groups", params=params, headers=headers, files=files)


def post_permission_groups(*args, **kwargs):
    """
    新增角色:

    参数:
    - name # 必填,str,权限名称
    - content_type # 必填,int,0系统端角色，1业务的角色
    - describes # 选填,str,角色说明
    """
    headers = {}
    files = {}
    params = {
        "name": "权限名称",
        "content_type": 1,
        "describes": "角色说明",
    }
    return send(methed="post", url="/permission/groups", params=params, headers=headers, files=files)


def put_permission_groups(*args, **kwargs):
    """
    修改角色:

    参数:
    - group_id # 必填,int,id
    - name # 选填,str,权限名称
    - state # 选填,int,1启用，0禁用
    - describes # 选填,str,角色说明
    """
    headers = {}
    files = {}
    params = {
        "group_id": 32,
        # "name": "权限名称1",
        # "state": 0,
        "describes": "角s色说ss明",
        "content_type": 1,
    }
    return send(methed="put", url="/permission/groups", params=params, headers=headers, files=files)


def delete_permission_groups(*args, **kwargs):
    """
    删除角色:

    参数:
    - group_id # 必填,int,id
    """
    headers = {}
    files = {}
    params = {
        "group_id": "(必填)id",
    }
    return send(methed="delete", url="/permission/groups", params=params, headers=headers, files=files)


def get_permission_groups_list(*args, **kwargs):
    """
    角色列表:

    参数:
    - page # 选填,int,翻页码
    - count # 选填,int,每页显示条数
    - state # 选填,int,状态
    - content_type # 必填,int,0系统端角色，1业务的角色
    - company_id # 必填,int,指定商户，默认所有角色。
    """
    headers = {}
    files = {}
    params = {
        "page": 1,
        "count": 10,
        "state": 1,
        # "content_type": 1,
    }
    return send(methed="get", url="/permission/groups/list", params=params, headers=headers, files=files)


def get_permission_groups_members(*args, **kwargs):
    """
    该角色的用户
    参数:
    - group_id # int
    """
    headers = {}
    files = {}
    params = {
        # "company_id": 1,
        "group_id": 45
    }
    return send(methed="get", url="/permission/groups/members", params=params, headers=headers, files=files)


def post_permission_groups_members(*args, **kwargs):
    """
    该角色的用户
    参数:
    - group_id # int
    """
    headers = {}
    files = {}
    params = {
        "group_id": 45,
        "company_id": 14,
        "user_id": "53,55"
    }
    return send(methed="post", url="/permission/groups/members", params=params, headers=headers, files=files)


def post_permission_groups_check(*args, **kwargs):
    """
    编辑角色权限:权限勾选或取消,修改成功后，建议刷新本地权限缓存

    参数:
    - group_id # 必填,int,角色id
    - key # 必填,str,接口标识符
    - method # 必填,str,接口方法
    - value # 必填,int,1勾选，0取消
    """
    headers = {}
    files = {}
    params = {
        "group_id": "(必填)角色id",
        "key": "(必填)接口标识符",
        "method": "(必填)接口方法",
        "value": "(必填)1勾选，0取消",
    }
    return send(methed="post", url="/permission/groups/check", params=params, headers=headers, files=files)


def post_permission_groups_checks(*args, **kwargs):
    """
    批量编辑角色权限:权限勾选或取消,修改成功后，建议刷新本地权限缓存

    参数:
    - group_id # 必填,int,角色id
    - key # 必填,str,接口标识符
    - method # 必填,str,接口方法
    - value # 必填,int,1勾选，0取消
    """
    headers = {}
    files = {}
    params = {
        "group_id": 27,
        "permissions": utils.to_json({
            "demo1-api: get": 1,
            "demo2-api: get": 1,
            "demo3-api: get": 1,
            "demo4-api: get": 1,
        })
    }
    return send(methed="post", url="/permission/groups/checks", params=params, headers=headers, files=files)


def get_permission_groups_company(*args, **kwargs):
    """
    商户的所有角色:查看某商户的所有角色，不分页

    参数:
    - company_id # 必填,int,商户id
    """
    headers = {}
    files = {}
    params = {
        # "company_id": 10,
        "content_type": 1,
    }
    return send(methed="get", url="/permission/groups/company", params=params, headers=headers, files=files)


def post_permission_groups_company(*args, **kwargs):
    """
    分配角色:把角色分配给商户

    参数:
    - group_id # 必填,str,角色id， 多个角色用英文逗号隔开
    - company_id # 必填,int,商户id
    """
    headers = {}
    files = {}
    params = {
        "group_id": 34,
        "company_id": 10,
    }
    return send(methed="post", url="/permission/groups/company", params=params, headers=headers, files=files)


def delete_permission_groups_company(*args, **kwargs):
    """
    移除角色:将角色从商户下移除，属于该角色的用户将失去该角色的所有权限

    参数:
    - group_id # 必填,int,角色id
    - company_id # 必填,int,商户id
    """
    headers = {}
    files = {}
    params = {
        "group_id": "34",
        "company_id": 10,
    }
    return send(methed="delete", url="/permission/groups/company", params=params, headers=headers, files=files)


def get_permission(*args, **kwargs):
    """
    权限详情:

    参数:
    - permission_id # 必填,int,id
    """
    headers = {}
    files = {}
    params = {
        "permission_id": 277,
    }
    return send(methed="get", url="/permission", params=params, headers=headers, files=files)


def post_permission(*args, **kwargs):
    """
    新增:

    参数:
    - content_type # 必填,int,0系统端角色，1业务的角色
    - key # 必填,str,接口标识符
    - name # 必填,str,名称
    - permission_class # 必填,int,类别，tag标签，api接口权限
    - method # 选填,str,接口方法， 当permission_class=api时必须提供
    - parent_id # 选填,str,父级id
    - describes # 选填,str,角色说明
    - state # 选填,int,角色说明
    - hook_func # 选填,str,钩子方法
    """
    headers = {}
    files = {}
    params = {
        "content_type": 1,
        "key": "dfddd",
        "name": "(必填)名称",
        "permission_class": "api",
        "method": "get",
        # "parent_id": "(选填)父级id",
        "describes": "(选填)角色说明",
        "state": 1,
        "hook_func": "(选填)钩子方法",
    }
    return send(methed="post", url="/permission", params=params, headers=headers, files=files)


def put_permission(*args, **kwargs):
    """
    修改:修改权限名称，描述，状态，钩子

    参数:
    - content_type # 必填,int,0系统端角色，1业务的角色
    - key # 选填,str,接口标识符
    - name # 选填,str,名称
    - permission_class # 选填,int,类别，tag标签，api接口权限
    - method # 选填,str,接口方法， 当permission_class=api时必须提供
    - parent_id # 选填,str,父级id
    - describes # 选填,str,角色说明
    - state # 选填,int,角色说明
    - hook_func # 选填,str,钩子方法
    """
    headers = {}
    files = {}
    params = {
        "permission_id": 276,
        "content_type": 1,
        "name": "(选填)名称22",
        # "permission_class": "tag",
        "method": "post",
        "parent_id": 255,
        "describes": "(选填)角色说明",
        "state": 1,
        "hook_func": "(选填)钩子方法",
    }
    return send(methed="put", url="/permission", params=params, headers=headers, files=files)


def delete_permission(*args, **kwargs):
    """
    删除:

    参数:
    - permission_id # 必填,int,id
    """
    headers = {}
    files = {}
    params = {
        "permission_id": 275,
        "content_type": 1
    }
    return send(methed="delete", url="/permission", params=params, headers=headers, files=files)


def get_permission_list(*args, **kwargs):
    """
    权限条目清单:

    参数:
    - state # 选填,int,状态
    - content_type # 必填,int,0系统端权限条目，1业务端权限条目
    """
    headers = {}
    files = {}
    params = {
        "state": 1,
        "content_type": 0,
    }
    return send(methed="get", url="/permission/list", params=params, headers=headers, files=files)


def get_permission_enable(*args, **kwargs):
    """
    是否启用权限系统:
    """
    headers = {}
    files = {}
    params = {
        "content_type": 1
    }
    return send(methed="get", url="/permission/enable", params=params, headers=headers, files=files)


def post_permission_enable(*args, **kwargs):
    """
    启用停用:停用权限系统后，所有访问都不做拦截

    参数:
    - state # 必填,int,状态， 1启用，0停用
    """
    headers = {}
    files = {}
    params = {
        "state": 0,
        "content_type": 0,
    }
    return send(methed="post", url="/permission/enable", params=params, headers=headers, files=files)


def post_permission_loads(*args, **kwargs):
    """
    载入

    参数:
    """
    headers = {}
    files = {}
    params = {

    }
    return send(methed="post", url="/permission/loads", params=params, headers=headers, files=files)


if __name__ == "__main__":
    # 角色详情
    # get_permission_groups()
    # 新增角色
    # post_permission_groups()
    # 修改角色
    # put_permission_groups()
    # # 删除角色
    # delete_permission_groups()
    # 角色列表
    get_permission_groups_list()
    # 属于该角色的用户
    get_permission_groups_members()
    # 改角色分配用户
    # post_permission_groups_members()
    # # 编辑角色权限(单个)
    # post_permission_groups_check()
    # # 编辑角色权限（批量）
    # post_permission_groups_checks()
    # # 商户的所有角色
    get_permission_groups_company()
    # 分配角色
    # post_permission_groups_company()
    # # 移除角色
    # delete_permission_groups_company()
    # # 权限详情
    # get_permission()
    # # 新增
    # post_permission()
    # 修改
    # put_permission()
    # # 删除
    # delete_permission()
    # # 权限条目清单
    # get_permission_list()
    # # 是否启用权限系统
    # get_permission_enable()
    # # 启用停用
    # post_permission_enable()
    # 自动载入
    # post_permission_loads()