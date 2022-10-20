# encoding: utf-8
"""
@project: djangoModel->equopment_log
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 日志API
@created_time: 2022/8/5 11:13
"""
import datetime

from rest_framework.views import APIView

from ..services.equipment_statistic_service import EquipmentStatisticService
from ..utils.model_handle import parse_data, util_response


class EquipmentRecordStatistic(APIView):

    def hour_statistics(self):
        """小时统计"""
        form_data = parse_data(self)
        date = form_data.pop('date', None)
        if date is None:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            today = date
        form_data['created_time__gte'] = today + " 09:00:00"
        form_data['created_time__lte'] = today + " 22:00:00"
        data, err_txt = EquipmentStatisticService.record_hour_statistics(form_data)
        if not err_txt:
            return util_response(data=data)
        return util_response(err=55796, msg=err_txt)

    def record_count_statistics(self):
        data, err_text = EquipmentStatisticService.record_count_statistics()
        return util_response(data=data)
