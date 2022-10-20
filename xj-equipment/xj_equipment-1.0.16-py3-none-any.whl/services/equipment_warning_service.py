# encoding: utf-8
"""
@project: djangoModel->record_warning_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 预警模块
@created_time: 2022/8/8 18:12
"""
from django.core.paginator import Paginator
from django.db.models import F

from xj_equipment.models import EquipmentWarn, Equipment
from xj_equipment.utils.model_handle import format_params_handle


class EquipmentWarningService:
    @staticmethod
    def add(params):
        # 恩据设备编码去找设备ID，根据实际情况，设备编码前端更容易得到，所以允许使用设备编码绑定设备ID
        equip_obj = Equipment.objects.filter(equip_code=params.pop("equip_code", 0))
        if equip_obj:
            equip_id = equip_obj.values("id").first().get("id")
            params.setdefault("equip_id", equip_id)

        insert_params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id", "equip_id", "equip_record_id", "summary", "work_level", "warn_type", "is_manual_report", "created_time", "report_time", "extend_json", ]
        )

        try:
            instance = EquipmentWarn.objects.create(**insert_params)
        except Exception as e:
            return None, "参数错误：" + str(e)

        return instance.to_json(), None

    @staticmethod
    def edit(params, pk):
        if not pk:
            return None, "参数错误"

        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id", "equip_id", "equip_record_id", "summary", "work_level", "warn_type", "is_manual_report", "created_time", "report_time", "extend_json", ]
        )

        try:
            instance = EquipmentWarn.objects.filter(id=pk)
            if not instance:
                return None, "数据不存在"
            instance.update(**params)
        except Exception as e:
            return None, "参数错误：" + str(e)

        return {"id": pk}, None

    @staticmethod
    def list(params):
        page = params.pop('page', 1)
        size = params.pop('size', 20)
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "id", "equip_id", "equip_record_id", "summary", "work_level", "warn_type",
                "is_manual_report", "equip_code", "region_code"
            ],
            alias_dict={
                "summary": "summary__contains",
                "work_level": "work_level__contains",
                "equip_code": "equip__equip_code",
                "region_code": "equip__equip_code"
            }
        )
        list_obj = EquipmentWarn.objects
        list_obj = list_obj.annotate(equip_code=F("equip__equip_code")) \
            .annotate(equip_name=F("equip__name")) \
            .annotate(region_code=F("equip__region_code")) \
            .annotate(address=F("equip__address")) \
            .annotate(warning_toplimit=F("equip__warning_toplimit"))

        list_obj = list_obj.filter(**params).values()
        limit_set = Paginator(list_obj, size)
        page_set = limit_set.get_page(page)
        count = list_obj.count()
        res = {'count': count, "page": page, "size": size, "list": list(page_set.object_list)}
        return res, None

    @staticmethod
    def delete(pk):
        warning_obj = EquipmentWarn.objects.filter(id=pk)
        if not warning_obj:
            return None, None
        warning_obj.delete()
        return None, None
