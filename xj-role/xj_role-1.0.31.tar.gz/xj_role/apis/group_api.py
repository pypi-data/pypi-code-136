# encoding: utf-8
"""
@project: djangoModel->group_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 分组api
@created_time: 2022/9/5 11:48
"""
from rest_framework.views import APIView

from xj_user.services.user_service import UserService
from ..services.user_group_service import UserGroupService
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data


class GroupAPIView(APIView):
    def get_user_from_list(self, *args, **kwargs):
        params = parse_data(self)
        group_id = params.get("user_group_id") or kwargs.get("user_group_id") or 0
        if not group_id:
            return util_response(err=1000, msg="user_group_id 必传")
        data, err = UserGroupService.get_user_from_group(group_id)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def user_group_tree(self, **kwargs):
        """用户分组树"""
        params = parse_data(self)
        token = self.META.get('HTTP_AUTHORIZATION', None)
        token_serv, error_text = UserService.check_token(token)
        if error_text:
            return util_response(err=1000, msg=error_text)
        # 这句看起来有问题，用户所在组ID是由接口传入的，不安全， 20221006 by sieyoo
        user_group_id = params.get("user_group_id") or kwargs.get("user_group_id") or 0
        user_id = token_serv['user_id']
        # user_group_set = GroupService.
        # print("> user_group_id:", user_group_id)
        data, err = UserGroupService.get_user_group_tree(user_group_id, is_family_tree=True)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    # 分组树 ==> 角色列表
    def group_tree_role(self):
        params = parse_data(self)
        data, err = UserGroupService.group_tree_role(params)
        return util_response(data=data)

    # 分组树 ==> 用户列表
    def group_tree_user(self):
        params = parse_data(self)
        data, err = UserGroupService.group_tree_user(params)
        return util_response(data=data)

    def user_group_users(self):
        group_id = self.GET.get("group_id", None)
        page = self.GET.get("page", 1)
        size = self.GET.get("size", 10)
        is_subtree = self.GET.get("is_subtree", False) == "1"
        data, err = UserGroupService.user_group_users(group_id, page, size, is_subtree)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def group_user_detail(self):
        token = self.META.get('HTTP_AUTHORIZATION', None)
        user_id = self.GET.get("user_id", None)
        if not user_id:
            token_serv, error_text = UserService.check_token(token)
            if error_text:
                return util_response(err=2000, msg=error_text)
            user_id = token_serv['user_id']

        data, err = UserGroupService.group_user_detail(user_id)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def group_user_add(self):
        data, err = UserGroupService.group_user_add(self.POST)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def group_user_edit(self):
        params = parse_data(self)
        data, err = UserGroupService.group_user_edit(params)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def group_user_delete(self):
        user_id = self.POST.get("user_id", None)
        data, err = UserGroupService.group_user_delete(user_id)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def user_group_list(self, **kwargs):
        # 用户组 列表接口
        params = parse_data(self)
        data, err = UserGroupService.get_user_group_list(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def put(self, request, **kwargs):
        # 用户组 修改接口
        params = parse_data(request)
        params.setdefault("id", kwargs.get("user_group_id", None))
        data, err = UserGroupService.edit_group(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def post(self, request, **kwargs):
        # 用户组 添加接口
        params = parse_data(request)
        data, err = UserGroupService.add_group(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def delete(self, request, **kwargs):
        # 用户组 删除接口
        id = parse_data(request).get("id", None) or kwargs.get("user_group_id")
        if not id:
            return util_response(err=1000, msg="id 必传")
        data, err = UserGroupService.del_group(id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    def bind_user_group(self, **kwargs):
        # 用户组 修改接口
        user_id = self.POST.get("user_id", None)
        group_list = self.POST.get("group_list", None)
        data, err = UserGroupService.bind_user_group(user_id, group_list)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
