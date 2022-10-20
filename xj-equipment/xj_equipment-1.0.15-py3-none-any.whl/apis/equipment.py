# encoding: utf-8
"""
@project: djangoModel->equipment
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 设备相关接口
@created_time: 2022/8/5 11:01
"""

# =============设备===================
from rest_framework.views import APIView

from ..models import Equipment
from ..services.equipment_service import EquipmentService
from ..utils.model_handle import parse_data, util_response, request_params_wrapper, format_params_handle


class CreatedEquipment(APIView):
    # 添加设备
    @request_params_wrapper
    def post(self, *args, request_params=None, **kwargs):
        request_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=[
                "equip_code", "region_code", "longitude", "latitude", "address", "admin_id", "group", "equip_type", "name",
                "mac", "status", "detail_json", "description", "setup_time", "updated_time", "warning_toplimit", "url", "account", "password"
            ]
        )
        data, err = EquipmentService.add_equipment(request_params)
        if not err:
            return util_response()
        return util_response(err=5778, msg=err)


class DelEquipment(APIView):
    # 删除设备
    @request_params_wrapper
    def post(self, *args, request_params=None, **kwargs):
        pk = request_params.get("id") or kwargs.get("pk")
        print("pk:", pk)
        res = Equipment.objects.filter(id=pk)
        if not res:
            return util_response(err=7557, msg="数据已不存在")
        res.delete()
        return util_response()


class EquipmentList(APIView):
    # 设备列表
    def get(self, request):
        from_data = parse_data(request)
        data, err = EquipmentService.equipment_list(params=from_data)
        if not err:
            return util_response(data=data)
        return util_response(err=5779, msg=err)


class EquipmentUpdate(APIView):
    # 设备更新
    @request_params_wrapper
    def post(self, *args, request_params=None, **kwargs):
        pk = request_params.pop("id") or kwargs.get("pk", None)
        if not pk:
            return util_response(err=5577, msg='参数错误')
        request_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=[
                "equip_code", "region_code", "longitude", "latitude", "address", "admin_id", "group", "equip_type", "name",
                "mac", "status", "detail_json", "description", "setup_time", "updated_time", "warning_toplimit", "url", "account", "password"
            ]
        )
        data, err = EquipmentService.edit_equipment(request_params, pk)
        if not err:
            return util_response()
        return util_response(err=5778, msg=err)
