# encoding: utf-8
"""
@project: djangoModel->valuation_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/10/13 11:22
"""
from rest_framework.views import APIView

from ..service.valuation_service import ValuationService
from ..utils.custom_response import util_response
from ..utils.model_handle import request_params_wrapper


class ValuationAPIView(APIView):
    # 获取计价
    @request_params_wrapper
    def list(self, *args, request_params, **kwargs):
        print("request_params:", request_params)
        data, err = ValuationService.valuate()
        if err:
            return util_response(err=1000, msg=err)
        return util_response()
