# encoding: utf-8
"""
@project: djangoModel->record_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 设备记录服务
@created_time: 2022/8/8 17:22
"""

# ===========  日志服务基类 start =============
from django.core.paginator import Paginator
from django.db.models import Sum, F
from django.db.models.functions import TruncHour

from xj_equipment.models import EquipmentRecord
from xj_equipment.utils.model_handle import format_params_handle


class EquipmentRecordService:
    @staticmethod
    def add_record(form_data):
        try:
            record = EquipmentRecord.objects.create(**form_data)
            res = {'id': record.id, 'equip_id': record.equip_id}
            return None, res
        except Exception as e:
            return None, str(e)

    @staticmethod
    def edit_record(form_data):
        try:
            id = form_data.pop('id')
            res = EquipmentRecord.objects.filter(id=id)
            res.update(**form_data)
            return None, None
        except Exception as e:
            return 5578, str(e)

    @staticmethod
    def record_list(form_data):
        page = form_data.pop('page', 1)
        size = form_data.pop('size', 20)
        form_data = format_params_handle(
            param_dict=form_data,
            filter_filed_list=["id", "equip", "flag", "unit", "value", "status", "summary", "created_time", "updated_time", "attribute_id", "hour", "equip_code"],
            alias_dict={"summary": "summary__contains", "equip_code": "equip__equip_code"}
        )
        list_set = EquipmentRecord.objects.annotate(attribute_name=F("attribute__name")) \
            .annotate(equip_name=F("equip__name")) \
            .annotate(address=F("equip__address")) \
            .annotate(region_code=F("equip__region_code")) \
            .annotate(equip_code=F("equip__equip_code"))

        list_set = list_set.filter(**form_data).values()

        count = list_set.count()
        page_set = Paginator(list_set, size).get_page(page)
        return {'count': count, "page": page, "size": size, "list": list(page_set.object_list)}, None

    @staticmethod
    def record_statistics(params):
        """
        场馆人流量统计
        原sql
        EquipmentRecord.objects.extra(select={"created_hour": 'date_format(created_time,"%%H")', }).filter(**params).values("created_hour").annotate(sum_value=Sum("value"))
        新sql
        EquipmentRecord.objects.filter(**params).annotate(created_hour=TruncHour("created_time")).values('created_hour').annotate(sum_value=Sum("value"))
        """
        try:
            params['attribute_id'] = 1
            input_sets = list(EquipmentRecord.objects.filter(**params).annotate(created_hour=TruncHour("created_time")).values('created_hour').annotate(sum_value=Sum("value")))
            params['attribute_id'] = 2
            output_sets = list(EquipmentRecord.objects.filter(**params).annotate(created_hour=TruncHour("created_time")).values('created_hour').annotate(sum_value=Sum("value")))
            # 格式化数据
            format_in = input_sets
            format_out = output_sets
            for index, item in enumerate(input_sets):
                format_in[index]['sum_value'] = int(item['sum_value'])
                format_in[index]['created_hour'] = int(item['created_hour'].strftime("%H"))
            for index, item in enumerate(format_out):
                format_out[index]['sum_value'] = int(item['sum_value'])
                format_out[index]['created_hour'] = int(item['created_hour'].strftime("%H"))

            res_set = {"in_visitors_flowrate": format_in, "out_visitors_flowrate": format_out}
            print("res_set", res_set)
            return res_set, None
        except Exception as e:
            return None, str(e)
