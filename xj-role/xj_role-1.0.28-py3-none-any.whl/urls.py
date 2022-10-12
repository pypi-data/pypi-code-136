# _*_coding:utf-8_*_

from django.urls import re_path

from .apis.group_api import GroupAPIView
from .apis.permission_api import PermissionValueAPIView, PermissionAPIView
from .apis.role_api import RoleAPIView

app_name = 'xj_role'

# 应用路由
urlpatterns = [

    # 角色相关接口
    re_path(r'^list/?$', RoleAPIView.list),  # 角色分页列表
    re_path(r'^tree/?$', RoleAPIView.tree),  # 角色树
    re_path(r'^role/?(?P<id>\d+)?$', RoleAPIView.as_view()),  # 角色 增加（post）/删除(delete)/修改(edit)

    # 权限API
    re_path(r'^permission_list/?', PermissionAPIView.list, ),  # 根据分组ID,获取绑定用户ID，测试接口
    re_path(r'^permission/?(?P<permission_id>\d+)?$', PermissionAPIView.as_view()),  # 分组 角色树
    # 权限值相关接口
    re_path(r'^permission_value_list/?$', PermissionValueAPIView.list, ),  # 权限值列表
    re_path(r'^permission_value/?(?P<id>\d+)?$', PermissionValueAPIView.as_view(), ),  # 权限值增删改

    re_path(r'^has_permission_value/?$', PermissionValueAPIView.permission, ),  # 用户权限判断

    # 分组相关的接口
    re_path(r'^get_user_from_list/(?P<user_group_id>\d+)?$', GroupAPIView.get_user_from_list, ),  # 根据分组ID,获取绑定用户ID，测试接口
    re_path(r'^group/?(?P<user_group_id>\d+)?$', GroupAPIView.as_view()),  # 分组 增加（post）/删除(delete)/修改(edit)
    re_path(r'^user_group_list/?$', GroupAPIView.user_group_list),  # 用户分组列表
    re_path(r'^user_group_tree/?$', GroupAPIView.user_group_tree),  # 用户分组树，原为role_group_tree，命名难以理解，改为role_user_group_tree
    re_path(r'^group_tree_role/?$', GroupAPIView.group_tree_role),  # 分组 角色树
    re_path(r'^group_tree_user/?$', GroupAPIView.group_tree_user),  # 分组 用户树
    re_path(r'^user_group_users/?$', GroupAPIView.user_group_users),  # 分组 用户列表
    re_path(r'^group_user_detail/?$', GroupAPIView.group_user_detail),  # 分组 用户详情
    re_path(r'^group_user_add/?$', GroupAPIView.group_user_add),  # 分组 用户添加
    re_path(r'^group_user_edit/?$', GroupAPIView.group_user_edit),  # 分组 用户修改
    re_path(r'^group_user_delete/?$', GroupAPIView.group_user_delete),  # 分组 用户删除
    # re_path(r'^bind_user_role/?$', GroupAPIView.bind_user_role),  # 用户角色那绑定
    re_path(r'^bind_user_group/?$', GroupAPIView.bind_user_group),  # 用户分组绑定

]
