# encoding: utf-8
"""
@project: djangoModel->equipment_warning
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 设备告警
@created_time: 2022/8/5 11:15
"""
from rest_framework.views import APIView

from xj_equipment.services.equipment_warning_service import EquipmentWarningService
from ..utils.model_handle import util_response, request_params_wrapper


class EquipmentWarningReport(APIView):
    # 告警列表
    @request_params_wrapper
    def list(self, *args, request_params, **kwargs):
        data, err_txt = EquipmentWarningService.list(request_params)
        if not err_txt:
            return util_response(data=data)
        return util_response(err=55796, msg=err_txt)

    # 上报接口
    @request_params_wrapper
    def post(self, *args, request_params, **kwargs):
        data, err_txt = EquipmentWarningService.add(request_params)
        if not err_txt:
            return util_response(data=data)
        return util_response(err=1000, msg=err_txt)

    @request_params_wrapper
    def delete(self, *args, request_params, **kwargs):
        pk = request_params.get("id") or kwargs.get("pk")
        data, err_txt = EquipmentWarningService.delete(pk)
        if not err_txt:
            return util_response(data=data)
        return util_response(err=55796, msg=err_txt)

    # 上报接口
    @request_params_wrapper
    def put(self, *args, request_params, **kwargs):
        pk = request_params.get("pk") or kwargs.get("pk")
        data, err_txt = EquipmentWarningService.edit(request_params, pk)
        if not err_txt:
            return util_response(data=data)
        return util_response(err=1000, msg=err_txt)
