from apiview.view import APIView
from django.views.decorators.http import require_http_methods

from xj_enroll.service.subitem_service import SubitemService
from xj_thread.services.thread_list_service import ThreadListService
from xj_user.utils.user_wrapper import user_authentication_wrapper
from ..join_list import JoinList
from ..service.enroll_services import EnrollServices
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data, request_params_wrapper


class SubitemApis(APIView):

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

    @require_http_methods(['POST'])
    def add(self, *args, **kwargs, ):
        params = parse_data(self)
        data, err = SubitemService.add(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
