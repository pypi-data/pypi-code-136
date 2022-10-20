# encoding: utf-8
"""
@project: djangoModel->service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 设备服务封装
@created_time: 2022/6/7 11:55
"""
from django.core.paginator import Paginator
from rest_framework import serializers

from xj_equipment.utils.model_handle import format_params_handle
from ..models import Equipment, EquipmentRecord


class EquipmentRecordSerializer(serializers.ModelSerializer):
    """展示类型序列化器"""

    class Meta:
        model = EquipmentRecord
        fields = [
            'sum_value',
            'hour'
        ]


# ============  设备服务类 start ==============
class EquipmentService():
    @staticmethod
    def add_equipment(params):
        # 添加设备
        try:
            Equipment.objects.create(**params)
        except Exception as e:
            return None, str(e)
        return None, None

    @staticmethod
    def edit_equipment(params, pk):
        # 添加设备
        pk = params.pop("id", None) or pk
        try:
            res = Equipment.objects.filter(id=pk)
            if not res:
                return None, "不存在ID位" + str(pk) + "该设备"
            res.update(**params)
        except Exception as e:
            return None, str(e)
        return None, None

    @staticmethod
    def equipment_list(params):
        page = params.pop('page', 1)
        size = params.pop('size', 20)

        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "id", "equip_code", "region_code", "longitude", "latitude", "address", "admin_id", "group_id", "equip_type", "name",
                "mac", "status", "detail_json", "description", "setup_time", "updated_time", "warning_toplimit", "url", "account", "password",
            ],
            alias_dict={'name': "name__contains", 'address': "address__contains", }
        )
        list_set = Equipment.objects.filter(**params).values()
        count = list_set.count()
        page_set = Paginator(list_set, size).get_page(page)
        return {'count': count, "page": page, "size": size, "list": list(page_set.object_list)}, None
