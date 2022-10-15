# encoding: utf-8
"""
@project: djangoModel->role_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 角色API
@created_time: 2022/9/2 15:38
"""
from rest_framework.views import APIView
from xj_role.services.role_service import RoleService, RoleTreeService
from ..utils.model_handle import *


class RoleAPIView(APIView):
    def tree(self):
        params = parse_data(self)
        res, err = RoleTreeService.role_tree(params.get("role_id", 0))
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=res)

    def list(self):
        params = parse_data(self)
        data, err = RoleService.get_role_list(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def put(self, request, **kwargs):
        # 角色 修改接口
        params = parse_data(request)
        params.setdefault("id", kwargs.get("role_id", None))
        data, err = RoleService.edit_role(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def post(self, request, **kwargs):
        # 角色 添加接口
        params = parse_data(request)
        data, err = RoleService.add_role(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def delete(self, request, **kwargs):
        # 角色 删除接口
        id = parse_data(request).get("id", None) or kwargs.get("role_id")
        if not id:
            return util_response(err=1000, msg="id 必传")
        data, err = RoleService.del_role(id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)
