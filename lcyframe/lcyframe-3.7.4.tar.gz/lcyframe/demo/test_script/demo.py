#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random, string
from test_script import *
from lcyframe.libs import cprint, utils


def post_demo(*args, **kwargs):
    """
    添加:测试post
    """
    headers = {}
    files = {}
    # 上传文件，参数放在body内，以multipart/form-data方式提交;excel=self.params["excel"]
    # files["excel"] = open("../请指定文件路径")
    
    params = {
        "str": "",     # string,选填,描述
        "str": "",     # string,选填,手机号
        "int": 0,     # integer,必填,整形
        "float": 0,     # float,必填,浮点型
        "json": "",     # json,必填,json格式
        "form-data": "",     # json,选填,位置：body_json，参数放在body内，以multipart/form-data方式，json格式。json类型的参数，设为非必须时，需提供默认值
        "form-data2": "",     # string,选填,位置：body_json，参数放在body内，以multipart/form-data方式，json格式。json类型的参数，设为非必须时，需提供默认值
        "www-form": "",     # string,选填,位置：body_form，参数放在body表单内，以multipart/x-www-form-urlencoded方式提交。手机号正则限定
        }
    return send(methed="post", url="/demo", params=params, headers=headers, files=files)

def get_demo(*args, **kwargs):
    """
    查看:测试get
    """
    headers = {"token": 1}
    files = {}
    params = {
        "_id": "",     # str,选填,id
        "a": 1,     # integer,必填,角色id
        "b": "",     # string,选填,供应商id
        "d": 1,     # int,选填,城市全拼列表
        }
    return send(methed="get", url="/demo", params=params, headers=headers, files=files)


def get_demo_list(*args, **kwargs):
    """
    列表:
    """
    headers = {}
    files = {}
    params = {
        "page": 0,     # integer,选填,翻页码
        "count": 0,     # integer,选填,每页显示条数
        "search": "",     # str,选填,搜索关键字
        "search": "",     # str,选填,搜索关键字
        "state": 0,     # int,选填,申请状态
        "time_range": "",     # str,选填,申请时间范围，逗号隔开。2020-12-12 12:12:12,2022-12-12 12:12:12
        }
    return send(methed="get", url="/demo/list", params=params, headers=headers, files=files)


def batch_groups():
    """
    测试簇
    一键测试
    """
    post_demo()       # 添加
    get_demo()       # 查看
    get_demo_list()       # 列表
    

if __name__ == "__main__":
    # 添加
    # post_demo()
    # 查看
    get_demo()
    # 列表
    # get_demo_list()
    