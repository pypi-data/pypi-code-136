"""
Created on 2022-04-11
@description:刘飞
@description:发布子模块逻辑分发
"""
from rest_framework.views import APIView

from xj_location.services.location_service import LocationService
from xj_role.services.permission_service import PermissionService
from xj_user.services.user_detail_info_service import DetailInfoService
# from xj_user.services.user_service import UserService
from xj_user.utils.user_wrapper import user_authentication_wrapper
from ..services.thread_list_service import ThreadListService
from ..services.thread_statistic_service import StatisticsService
# from ..utils.custom_authentication_wrapper import authentication_wrapper
from ..utils.custom_response import util_response
from ..utils.j_dict import JDict
from ..utils.join_list import JoinList
from ..utils.model_handle import parse_data


class ThreadListAPIView(APIView):
    """
    get: 信息表列表
    post: 信息表新增
    """

    # @authentication_wrapper

    # 我们更希望通过装饰器来做权限验证，这样可以更好的精简API层的代码量 2022.10.3 by Sieyoo
    @user_authentication_wrapper  # 如果有token则返回user_info，无则返回空
    def get(self, request, category_value=None, user_info=None, *args, **kwargs):
        params = parse_data(request)
        # print("> ThreadListAPIView category_value:", category_value, user_info, params)
        category_value = request.GET.get('category_value', category_value)
        # print("> ThreadListAPIView category_value 2:", category_value)
        if category_value:
            params.setdefault("category_value", category_value)
        size = request.GET.get('size', 20)
        if int(size) > 100:
            return util_response(msg='每一页不可以超过100条', err=1000)

        # 弃用，我们更希望通过装饰器来做权限验证，这样可以更好的精简API层的代码量 2022.10.3 by Sieyoo
        # 获取权限,权限验证
        # token = request.META.get('HTTP_AUTHORIZATION', None)
        # print("> ThreadListAPIView token:", token)
        # if token and str(token).strip().upper() != "BEARER":
        #     token_serv, error_text = UserService.check_token(token)
        #     if error_text:
        #         return util_response(err=6000, msg=error_text)
        #     token_serv, error_text = UserService.check_token(token)

        auth_dict = {}
        user_id = user_info.get("user_id", None) if user_info else None
        if user_id:
            auth_dict, error_text = PermissionService.get_user_group_permission(user_id=user_id, module="thread")
            if error_text:
                return util_response(err=1002, msg=error_text)

        auth_dict = JDict(auth_dict)  # 与当前用户有关的权限值
        ban_user_list = []  # 允许读的用户列表
        allow_user_list = []  # 禁止读的用户列表
        if auth_dict.GROUP_PARENT and auth_dict.GROUP_PARENT.ban_view.upper() == "Y":
            ban_user_list.extend(auth_dict.GROUP_PARENT.user_list)
        else:
            allow_user_list.extend(auth_dict.GROUP_PARENT.user_list if auth_dict.GROUP_PARENT else [])

        if auth_dict.GROUP_CHILDREN and auth_dict.GROUP_CHILDREN.ban_view.upper() == "Y":
            ban_user_list.extend(auth_dict.GROUP_CHILDREN.user_list)
        else:
            allow_user_list.extend(auth_dict.GROUP_CHILDREN.user_list if auth_dict.GROUP_CHILDREN else [])

        if auth_dict.GROUP_INSIDE and auth_dict.GROUP_INSIDE.ban_view.upper() == "Y":
            ban_user_list.extend(auth_dict.GROUP_INSIDE.user_list)
        else:
            allow_user_list.extend(auth_dict.GROUP_INSIDE.user_list if auth_dict.GROUP_INSIDE else [])

        if not auth_dict.GROUP_ADMINISTRATOR and not auth_dict.GROUP_MANAGER:
            if auth_dict.GROUP_OUTSIDE and auth_dict.GROUP_OUTSIDE.ban_view.upper() == "Y":
                params['user_id__in'] = allow_user_list
            else:
                params["user_id__not_in"] = ban_user_list
        else:
            params["is_admin"] = True

        # print("> ThreadListAPIView auth_dict:", auth_dict)
        # print("> ThreadListAPIView params:", params)

        # 获取列表数据
        data, error_text = ThreadListService.list(params)
        if error_text:
            return util_response(err=1003, msg=error_text)

        # ID列表拆分
        thread_id_list = list(set([item['id'] for item in data['list'] if item['id']]))
        user_id_list = list(set([item['user_id'] for item in data['list'] if item['user_id']]))
        # 用户数据和统计数据
        statistic_list = StatisticsService.statistic_list(id_list=thread_id_list)
        user_info_list = DetailInfoService.get_list_detail(params=None, user_id_list=user_id_list)
        location_list, err = LocationService.location_list(params={"thread_id_list": thread_id_list},
                                                           need_pagination=False)
        # 用户数据(full_name, avatar), 统计数据(statistic),
        data['list'] = JoinList(l_list=data['list'], r_list=statistic_list, l_key="id", r_key='thread_id').join()
        data['list'] = JoinList(l_list=data['list'], r_list=user_info_list, l_key="user_id", r_key='user_id').join()
        if not err:
            data['list'] = JoinList(l_list=data['list'], r_list=location_list, l_key="id", r_key='thread_id').join()
        return util_response(data=data, is_need_parse_json=True)
