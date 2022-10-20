# encoding: utf-8
"""
@project: djangoModel->equopment_log
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 日志API
@created_time: 2022/8/5 11:13
"""

from rest_framework.views import APIView

from xj_equipment.customValidator import RecordValidator
from ..models import Equipment
from ..services.equipment_record_service import EquipmentRecordService
from ..utils.model_handle import parse_data, util_response, parse_model, request_params_wrapper


class AddEquipmentRecord(APIView):
    # 添加设备记录
    def post(self, request):
        form_data = parse_data(request)

        # 补全equip_id
        equip_code = form_data.pop("equip_code", None)
        if not form_data.get("equip_id", None):
            if equip_code is None:
                return util_response(err=2548, msg="未找到该设备")
            equip_obj = parse_model(Equipment.objects.filter(equip_code=equip_code))
            if not equip_obj:
                return util_response(err=2548, msg="未找到该设备")
            form_data['equip_id'] = equip_obj[0]['id']

        # 数据有效新判断
        validator = RecordValidator(form_data)
        is_pass, msg = validator.validate()
        if not is_pass:
            return util_response(err=54548, msg=msg)

        # 插入数据
        data, err_txt = EquipmentRecordService.add_record(form_data)
        if not err_txt:
            return util_response()
        return util_response(err=55796, msg=err_txt)


class EditEquipmentRecord(APIView):
    # 设备状态更新
    def post(self, request):
        form_data = parse_data(request)
        data, err_txt = EquipmentRecordService.edit_record(form_data)
        if not err_txt:
            return util_response()
        return util_response(err=55796, msg=err_txt)


class EquipmentRecordList(APIView):
    # 记录列表
    @request_params_wrapper
    def get(self, *args, request_params, **kwargs):
        print("request_params:", request_params)
        data, err_txt = EquipmentRecordService.record_list(request_params)
        if not err_txt:
            return util_response(data=data)
        return util_response(err=55796, msg=err_txt)
