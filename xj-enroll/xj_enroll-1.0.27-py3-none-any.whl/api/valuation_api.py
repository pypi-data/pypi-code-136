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
    def valuate_test(self, *args, request_params, **kwargs):
        expression_string = request_params.get("expression", "5+if(((IF(1=5,5,0)+((3)))>=(1+3+4)),'号外号外',IF(2 >= 60, '及格', '不及格')) + SUM(1,2,5,7,8)", )
        variables_dict = request_params.get("variables", {"a": 1, "b": 2, "c": 5}, )
        data, err = ValuationService.valuate(
            expression_string,
            variables_dict
        )
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
