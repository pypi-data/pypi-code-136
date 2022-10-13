# -*- coding: utf-8 -*-
# @Time    :2022/9/27 19:45
# @Author  :Sang Jiajun
# @Email   :jiajun_sang@outlook.com
# @File    :data_op.py
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import json


def read_file(path):
    """
    读取文件，返回行数据的list

    :param path: 文件路径
    :return: 返回读取到的文件内容
    """
    with open(path, "r", encoding="utf-8") as f:
        datas = f.read()
        datas = datas.split("\n")
        datas = [_.strip() for _ in datas if _ != "\n"]
        return datas


def write_file(data, path):
    """

    :param data:
    :param path:
    :return:
    """
    with open(path, "w", encoding="utf-8") as f:
        data = [_.strip()+"\n" for _ in data]
        f.writelines(data)


def read_json(path):
    with open(path, 'r',  encoding="utf-8") as f:
        data = json.loads(f.read())
        return data


def write_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
