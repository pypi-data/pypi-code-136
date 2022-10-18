#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bson.objectid import ObjectId
from base import BaseSchema
import time, datetime

class PermissionGroupSchema(BaseSchema):
    """
    permission
    """

    collection = "permission_group"

    def __init__(self):
        self._id = ObjectId()
        self.available = True   # ******
        self.permission_class = {}  # ******
        self.gid = 1    # ******ID
        self.name = "******2"
        self.pid = 1    # ******ID
        self.desc = ""  # ******
        self.create_at = int(time.time())
        self.update_at = int(time.time())

class PermissionClassSchema(BaseSchema):
    """
    permission
    """

    collection = "permission_class"

    def __init__(self):
        self._id = ObjectId()
        self.available = True   # ******
        self.bit_mp = {}  # ******bit
        self.key = 1    # ******ID
        self.name = "******"
        self.desc = ""  # ******
        self.create_at = int(time.time())
        self.update_at = int(time.time())



########################  RBAC  ######################
class GroupsSchema(BaseSchema):
    """
    角色
    """

    collection = "groups"

    def __init__(self):
        self.id = 0
        self.name = "角色名"
        self.state = 1
        self.describes = "描述"
        self.permissions = '{}'       # 已勾选的权限
        self.content_type = 1  # 1业务的权限，0系统端
        self.create_time = datetime.datetime.now()
        self.update_time = datetime.datetime.now()

class CompanyGroupsSchema(BaseSchema):
    """
    商户的角色
    """

    collection = "company_groups"

    def __init__(self):
        self.id = 0
        self.group_id = ""   # 已分配的角色id
        self.company_id = ""  # 商户id
        self.create_time = datetime.datetime.now()
        self.update_time = datetime.datetime.now()

class PermissionsSchema(BaseSchema):
    """
    权限条目
    """

    collection = "permissions"

    def __init__(self):
        self.id = 0
        self.name = "权限名"
        self.key = "权限键"
        self.method = ""  # 请求方法,get、post、put、delete
        self.parent_id = None  # 父类的id
        self.permission_class = ""  # 权限类别，tag标签，api接口权限，logic逻辑权限
        self.hook_func = ""  # 钩子函数
        self.state = 1  # 1启用0停用
        self.describes = ""
        self.content_type = 1  # 1业务的权限，0系统端
        self.create_time = datetime.datetime.now()
        self.update_time = datetime.datetime.now()
