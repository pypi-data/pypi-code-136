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


class ValuationAPIView(APIView):
    # 获取计价
    def list(self):
        data, err = ValuationService.valuate()
        if err:
            return util_response(err=1000, msg=err)
        return util_response()
