from apiview.view import APIView
from django.views.decorators.http import require_http_methods

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
    def add(self, *args, **kwargs, ):
        params = parse_data(self)
        # 表单数据验证
        # is_valid, error = EnrollValidator(params).validate()
        # if not is_valid:
        #     return util_response(err=1000, msg=error)
        # 信息表联调
        thread_params = format_params_handle(
            param_dict=params,
            remove_filed_list=[
                "category", "classify", "trading_relate", "region_code", "occupy_room", "enroll_status_code",
                "min_number", "max_number", "min_count_apiece", "max_count_apiece", "enroll_calc_rule", "price", "count",
                "unit", "fee", "reduction", "subitems_amount", "amount", "paid_amount", "unpaid_amount", "commision", "deposit",
                "bid_mode", "ticket", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit", "has_vouch", "need_deposit",
                "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time", "finish_time",
                "spend_time", "create_time", "update_time", "snapshot", "remark",
            ],
            alias_dict={"thread_category_id": "category_id"}
        )
        if thread_params:
            thread_id = thread_params.get("thread_id")
            if not thread_id:
                data, err = ThreadItemService.add(thread_params)
            else:
                data, err = ThreadItemService.edit(thread_params, thread_id)
            if err:
                return util_response(err=1001, msg=err)
            params.setdefault("thread_id", thread_id or data['id'])

        # 主表信息字段
        main_params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "thread_id", "category", "classify", "trading_relate", "region_code", "occupy_room", "enroll_status_code",
                "min_number", "max_number", "min_count_apiece", "max_count_apiece", "enroll_calc_rule", "price", "count",
                "unit", "fee", "reduction", "subitems_amount", "amount", "paid_amount", "unpaid_amount", "commision", "deposit",
                "bid_mode", "ticket", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit", "has_vouch", "need_deposit",
                "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time", "finish_time",
                "spend_time", "create_time", "update_time", "snapshot", "remark",
            ]
        )
        main_params.setdefault("enroll_status_code", 0)
        # 添加数据
        data, err = EnrollServices.enroll_add(main_params)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    @require_http_methods(['PUT'])
    def edit(self, *args, **kwargs, ):
        params = parse_data(self)
        enroll_id = kwargs.get("enroll_id") or params.pop("enroll_id") or None
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")
        data, err = EnrollServices.enroll_edit(params, enroll_id)
        if err:
            return util_response(err=1000, msg=err)
        print(data)
        # TODO联动信息模块修改
        thread_id = params.pop("thread_id", None) or data.get("thread_id", None)
        print(thread_id)
        if thread_id:
            thread_params = format_params_handle(
                param_dict=params,
                remove_filed_list=[
                    "id", "category", "classify", "trading_relate", "region_code", "occupy_room", "enroll_status_code",
                    "min_number", "max_number", "min_count_apiece", "max_count_apiece", "enroll_calc_rule", "price", "count",
                    "unit", "fee", "reduction", "subitems_amount", "amount", "paid_amount", "unpaid_amount", "commision", "deposit",
                    "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit", "has_vouch", "need_deposit",
                    "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time", "finish_time",
                    "spend_time", "create_time", "update_time", "snapshot", "remark",
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
