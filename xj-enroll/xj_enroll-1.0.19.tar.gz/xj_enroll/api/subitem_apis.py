from apiview.view import APIView
from django.views.decorators.http import require_http_methods

from xj_enroll.service.subitem_service import SubitemService
from xj_user.utils.user_wrapper import user_authentication_wrapper
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data, request_params_wrapper


class SubitemApis(APIView):

    @require_http_methods(['GET'])
    @request_params_wrapper
    @user_authentication_wrapper
    def list(self, request_params=None, user_info=None, *args, **kwargs, ):
        data, err = SubitemService.list(params=request_params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    @require_http_methods(['POST'])
    def add(self, *args, **kwargs, ):
        params = parse_data(self)
        data, err = SubitemService.add(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
