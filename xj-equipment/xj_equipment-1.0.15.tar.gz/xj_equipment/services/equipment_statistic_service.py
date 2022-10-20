# encoding: utf-8
"""
@project: djangoModel->equipment_statistic_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 统计服务
@created_time: 2022/8/23 14:20
"""
import calendar
from datetime import timedelta

from django.db.models import Sum
from django.db.models.functions import TruncHour, datetime

from xj_equipment.models import EquipmentRecord


class EquipmentStatisticService:
    @staticmethod
    def record_hour_statistics(params):
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
            return res_set, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def record_count_statistics(params=None):
        """统计 昨日 今日 本月 全部的金客量"""

        now = datetime.datetime.now()
        # 昨天
        yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
        yesterday_num = EquipmentRecord.objects.filter(created_time__gte=yesterday + " 09:00:00", created_time__lte=yesterday + " 22:00:00", attribute_id=1).aggregate(Sum('value'))
        print(yesterday_num)
        if yesterday_num['value__sum'] is None:
            yesterday_num['value__sum'] = 0
        else:
            yesterday_num['value__sum'] = int(yesterday_num['value__sum'])

        # 当日
        today = now.strftime("%Y-%m-%d")
        today_num = EquipmentRecord.objects.filter(created_time__gte=today + " 09:00:00", created_time__lte=today + " 22:00:00", attribute_id=1).aggregate(Sum("value"))
        if today_num['value__sum'] is None:
            today_num['value__sum'] = 0
        else:
            today_num['value__sum'] = int(today_num['value__sum'])

        # 当月
        this_month_start = datetime.datetime(now.year, now.month, 1).strftime("%Y-%m-%d 00:00:00")
        this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]).strftime("%Y-%m-%d 23:59:59")
        this_month_num = EquipmentRecord.objects.filter(created_time__gte=this_month_start, created_time__lte=this_month_end, attribute_id=1).aggregate(Sum("value"))
        if this_month_num['value__sum'] is None:
            this_month_num['value__sum'] = 0
        else:
            this_month_num['value__sum'] = int(this_month_num['value__sum'])

        # 全部uhi总
        all_num = EquipmentRecord.objects.filter(attribute_id=1).aggregate(Sum("value"))
        if all_num['value__sum'] is None:
            all_num['value__sum'] = 0
        else:
            all_num['value__sum'] = int(all_num['value__sum'])

        # 全部uhi总
        res = {"yesterday_num": yesterday_num, "today_num": today_num, "this_month_num": this_month_num, "all_num": all_num}
        return res, None
