# encoding: utf-8
"""
@project: djangoModel->urls
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 子路由文件
@created_time: 2022/6/7 13:53
"""
from django.urls import re_path

from .apis.equipment import CreatedEquipment, DelEquipment, EquipmentList, EquipmentUpdate  # 设备创建
from .apis.equipment_types import GetEquipmentTypes  # 设备相关信息相关列表
from .apis.equipment_use_map import EquipmentUseMap
from .apis.equipment_warning import EquipmentWarningReport  # 设备 应急预警（包括人工上报系统）
from .apis.equopment_record import AddEquipmentRecord, EditEquipmentRecord, EquipmentRecordList
from .apis.equopment_statistic import EquipmentRecordStatistic

urlpatterns = [
    # 设备管理
    re_path('^list/?$', EquipmentList.as_view()),  # 设备列表
    re_path('^create/?$', CreatedEquipment.as_view()),  # 创建/注册设备
    re_path('^del/?(?P<pk>\d+)?$', DelEquipment.as_view()),  # 删除
    re_path('^update/?(?P<pk>/)?$', EquipmentUpdate.as_view()),  # 设备列表

    # 用途映射
    re_path('^use_map/?$', EquipmentUseMap.as_view()),  # 获取用途映射 CURD

    # 获取设备相关信息
    re_path('^get_equipment_type/?$', GetEquipmentTypes.get_equipment_type),  # 设备类型
    re_path('^get_use_type/?$', GetEquipmentTypes.get_use_type),  # 获取使用类型
    re_path('^get_equipment_flag/?$', GetEquipmentTypes.get_equipment_flag_type),  # 获取计量类型
    re_path('^get_equipment_uint/?(?P<flag_id>\d+)?$', GetEquipmentTypes.get_equipment_uint_type),  # 获取计量单位

    # 设备记录管理
    re_path('^record_create/?$', AddEquipmentRecord.as_view()),
    re_path('^record_update/?$', EditEquipmentRecord.as_view()),
    re_path('^record_list/?$', EquipmentRecordList.as_view()),
    re_path('^record_statistics/?$', EquipmentRecordStatistic.hour_statistics),
    re_path('^record_count_statistics/?$', EquipmentRecordStatistic.record_count_statistics),

    # 设备记录上报
    re_path('^warning/?(?P<pk>\d+)?$', EquipmentWarningReport.as_view()),
    re_path('^warning_list/?$', EquipmentWarningReport.list),
]
