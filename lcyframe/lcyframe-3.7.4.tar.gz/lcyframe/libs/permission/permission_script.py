import os
import json
import re
import sys
import datetime
import random
import django
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"settings.dev")
django.setup()

from django.conf import settings
from django.db import connection
from django.db.models import Q
from django.forms.models import model_to_dict
from permission.permission_struct import service_permissions, system_permissions, service_groups, system_groups
from permission.models import Permissions, Groups, CompanyGroups

keys = []
names = []

def check_field(permissions):
    """
    校验权限合法性
    :param item:
    :return:
    """
    for p in permissions:
        if p.get("children", []):
            check_field(p["children"])
        else:
            if not p["name"] or not p["key"] or not p["permission_class"]:
                raise Exception("关键字都必填")
            # if p["permission_class"] == "tag" and not p["children"]:
            #     raise Exception("标签下尚未设置权限")
            if p["permission_class"] == "api" and not p["method"]:
                raise Exception("API级别权限必须指定方法：get、post、put、delete")
            if p["permission_class"] == "logic" and not p["method"]:
                raise Exception("暂不支持逻辑权限")

            if p["permission_class"] == "api":
                unique_name = p["key"] + ":" + p["method"]
            else:
                unique_name = p["key"]
            if unique_name not in keys:
                keys.append(unique_name)
            else:
                raise Exception("存在重复的key：%s" % p["key"])

            if p["name"] not in keys:
                names.append(p["name"])
            else:
                raise Exception("存在重复的name：%s" % p["name"])
    return True

def import_permissions(content_type=1):
    """
    权限json导入db
    "content_type": 1 or 0              # 1 业务端使用，0系统管理端
    :return:
    """
    if Permissions.objects.filter(content_type=content_type).first():
        raise Exception("请勿重复导入")

    if content_type == 1:
        permissions = service_permissions
    else:
        permissions = system_permissions
    assert check_field(permissions)
    def loop_create_item(item, parent=None):
        parent = Permissions.objects.create(
            name=item["name"],
            key=item["key"],
            method=item.get("method", ""),
            # parent=item.get("parent", ""),    # 去父级的key+method
            parent_id=parent["id"] if parent else None,
            permission_class=item.get("permission_class", ""),
            hook_func=item.get("hook_func", ""),
            state=item.get("state", 1),
            desc=item.get("desc", ""),
            content_type=content_type
        )
        print("写入权限:%s" % item["name"])
        for children in item.get("children", []):
            loop_create_item(children, model_to_dict(parent))

    for p in permissions:
        loop_create_item(p)

    print("权限导入完成，总计:%s条" % len(keys))

def import_groups(content_type=1):
    """
    创建初始化角色
    :return:
    """
    if content_type == 1:
        groups = service_groups
    else:
        groups = system_groups
    for group in groups:
        g = Groups.objects.create(**group)
        print("角色写入：", model_to_dict(g))

def set_company_groups(company_id, content_type=1):
    """
    给商户分配角色
    :param company_id:
    :return:
    """
    groups = []
    for g in Groups.objects.filter(state=1, content_type=content_type):
        groups.append(model_to_dict(g))
    for i in random.sample(groups, len(groups)-1):
        i["company_id"] = company_id
        g = CompanyGroups.objects.create(**{"company_id": company_id, "group_id": i["id"]})
        print("给商户分配角色:", model_to_dict(g))

def set_groups_permission(content_type=1):
    """
    设置角色权限：随机
    :return:
    """
    permissions = Permissions.objects.filter(content_type=content_type, permission_class="api")
    for group in Groups.objects.all():
        random_permission = random.sample(list(permissions), int(len(permissions)/2))
        for p in random_permission:
            p = model_to_dict(p)
            group.permissions[p["key"] + ":" + p["method"]] = 1
            group.save()

if __name__ == '__main__':
    # import_permissions(1)
    # import_groups(1)
    # set_groups_permission(1)
    # print(set_company_groups(1))
    pass