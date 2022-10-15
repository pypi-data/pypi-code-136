from apiview.view import APIView
from django.db import transaction
from django.views.decorators.http import require_http_methods

from xj_enroll.service.subitem_service import SubitemService
from xj_thread.services.thread_item_service import ThreadItemService
from xj_thread.services.thread_list_service import ThreadListService
from xj_user.utils.user_wrapper import user_authentication_wrapper, user_authentication_force_wrapper
from ..join_list import JoinList
from ..service.enroll_services import EnrollServices
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data, format_params_handle, request_params_wrapper


class EnrollAPI(APIView):

    @require_http_methods(['GET'])
    @request_params_wrapper
    @user_authentication_wrapper
    def list(self, request_params=None, user_info=None, *args, **kwargs, ):
        data, err = EnrollServices.enroll_list(params=request_params)
        if err:
            return util_response(err=1000, msg=err)
        # 合并thread模块数据
        id_list = [i['thread_id'] for i in data['list'] if i]
        thread_list, err = ThreadListService.search(id_list)
        data['list'] = JoinList(data['list'], thread_list, "thread_id", "id").join()
        # 数据返回
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    @require_http_methods(['GET'])
    @request_params_wrapper
    @user_authentication_force_wrapper
    def own_list(self, *args, request_params=None, user_info=None, **kwargs):
        is_finish = request_params.get("is_finish", 0)
        user_id = user_info.get("user_id")
        params = {"is_finish": is_finish, "user_id": user_id, "page": request_params.get("page", 1), "size": request_params.get("page", 20)}
        data, err = EnrollServices.enroll_user_list(params)
        if err:
            return util_response(err=1000, msg=err)
        # 合并thread模块数据
        id_list = [i['thread_id'] for i in data['list'] if i]
        thread_list, err = ThreadListService.search(id_list)
        data['list'] = JoinList(data['list'], thread_list, "thread_id", "id").join()
        # 数据返回
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    @require_http_methods(['GET'])
    def detail(self, *args, **kwargs, ):
        params = parse_data(self)
        enroll_id = kwargs.get("enroll_id") or params.pop("enroll_id") or None
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")
        data, err = EnrollServices.enroll_detail(enroll_id)
        if err:
            return util_response(err=1001, msg=err)
        # 数据拼接
        thread_list, err = ThreadListService.search([data.get("thread_id")])
        if err:
            return util_response(err=1002, msg=err)
        data = JoinList([data], thread_list, "thread_id", "id").join()
        data = data[0] if not len(data) > 1 else data
        # 响应数据
        if err:
            return util_response(err=1003, msg=err)
        return util_response(data=data)

    @require_http_methods(['POST'])
    @user_authentication_force_wrapper
    def add(self, *args, user_info, **kwargs, ):
        user_id = user_info.get("user_id")
        params = parse_data(self)
        # 表单数据验证
        # is_valid, error = EnrollValidator(params).validate()
        # if not is_valid:
        #     return util_response(err=1000, msg=error)

        # 参数校验
        subitem_params = params.get("subitem")
        if not subitem_params:
            return util_response(err=1000, msg="分项表参数不能为空")
        thread_params = format_params_handle(
            param_dict=params,
            remove_filed_list=[
                # 报名表字段
                "trading_relate", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number",
                "min_count_apiece", "max_count_apiece", "enroll_rule_group", "price", "count", "unit", "fee", "reduction", "subitems_amount",
                "amount", "paid_amount", "unpaid_amount", "commision", "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit",
                "need_vouch", "need_deposit", "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time",
                "finish_time", "spend_time", "create_time", "update_time", "snapshot", "remark",
                # 报名分项字段
                "subitem"
            ],
            alias_dict={"thread_category_id": "category_id", "thread_remark": "remark"}
        )
        if not thread_params:
            return util_response(err=1001, msg="请填写项目基本信息")

        main_params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "thread_id", "trading_relate", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number",
                "min_count_apiece", "max_count_apiece", "enroll_rule_group", "price", "count", "unit", "fee", "reduction", "subitems_amount",
                "amount", "paid_amount", "unpaid_amount", "commision", "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit",
                "need_vouch", "need_deposit", "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time",
                "finish_time", "spend_time", "create_time", "update_time", "snapshot", "remark"
            ]
        )
        sid = transaction.savepoint()

        # 信息表联调
        thread_params.setdefault("user_id", user_id)
        thread_id = thread_params.get("thread_id")
        if not thread_id:
            data, err = ThreadItemService.add(thread_params)
        else:
            data, err = ThreadItemService.edit(thread_params, thread_id)
        if err:
            transaction.savepoint_rollback(sid)
            return util_response(err=1002, msg="信息添加错误：" + err)

        thread_id = thread_id or data['id']
        main_params.setdefault("thread_id", thread_id or data['id'])
        # 报名主表添加
        main_params.setdefault("enroll_status_code", 0)
        main_params.setdefault("user_id", user_id)
        main_instance, err = EnrollServices.enroll_add(main_params)
        if err:
            transaction.savepoint_rollback(sid)
            return util_response(err=1003, msg=err)

        # 报名分项联动
        for item_params in params["subitem"]:
            item_params.setdefault("enroll_id", main_instance.get('id'))
            data, err = SubitemService.add(item_params)
            if err:
                transaction.savepoint_rollback(sid)
                return util_response(err=1004, msg=err)

        transaction.clean_savepoints()  # 清除保存点
        return util_response(data=main_instance)

    @require_http_methods(['PUT'])
    def edit(self, *args, **kwargs, ):
        params = parse_data(self)
        enroll_id = kwargs.get("enroll_id") or params.pop("enroll_id") or None
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")
        data, err = EnrollServices.enroll_edit(params, enroll_id)
        if err:
            return util_response(err=1000, msg=err)
        # TODO联动信息模块修改
        thread_id = params.pop("thread_id", None) or data.get("thread_id", None)
        if thread_id:
            thread_params = format_params_handle(
                param_dict=params,
                remove_filed_list=[
                    "thread_id", "trading_relate", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number",
                    "min_count_apiece", "max_count_apiece", "enroll_rule_group", "price", "count", "unit", "fee", "reduction", "subitems_amount",
                    "amount", "paid_amount", "unpaid_amount", "commision", "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit",
                    "need_vouch", "need_deposit", "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time",
                    "finish_time", "spend_time", "create_time", "update_time", "snapshot", "remark"
                ]
            )
            if thread_params:
                data, err = ThreadItemService.edit(thread_params, thread_id)
                if err:
                    return util_response(err=1001, msg=err)

        return util_response(data=data)

    @require_http_methods(['DELETE'])
    def delete(self, *args, **kwargs, ):
        params = parse_data(self)
        enroll_id = kwargs.get("enroll_id") or params.pop("enroll_id") or None
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")
        data, err = EnrollServices.enroll_delete(enroll_id)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
