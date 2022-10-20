from django.contrib import admin

from config.config import Config
from .models import Equipment, EquipmentRecord, EquipmentFlag, EquipmentUint, EquipmentUse, EquipmentUseToMap, \
    EquipmentType, EquipmentWarn, EquipmentAttribute


class EquipmentManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'equip_code', 'region_code', 'equip_type']
    list_editable = ['name', 'address', 'equip_code']
    search_fields = ['equip_code']
    list_filter = ['equip_type_id']
    fields = ('name', 'address', 'equip_code', 'region_code', 'equip_type', 'longitude', 'latitude', 'account', 'password', 'url', 'mac')
    list_per_page = 20


class EquipmentAttributeManager(admin.ModelAdmin):
    list_display = ['id', 'name', "equip", "equip_group", "equip_type", "description"]
    fields = ['id', 'name', "equip", "equip_group", "equip_type", "description"]
    readonly_fields = ["id"]
    list_per_page = 20


class EquipmentRecordManager(admin.ModelAdmin):
    list_display = ['equip', 'summary', 'flag', 'unit', 'created_time', 'value']
    fields = ['equip', 'summary', 'flag', 'unit', 'created_time', 'value']
    search_fields = ['equip', 'flag', 'unit']
    list_per_page = 20


class EquipmentFlagManager(admin.ModelAdmin):
    list_display = ['id', 'flag']
    search_fields = ['id', 'flag']
    list_per_page = 20


class EquipmentUintManager(admin.ModelAdmin):
    list_display = ['id', 'flag', 'uint']
    list_filter = ['flag']
    list_per_page = 20


class EquipmentUseManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    list_editable = ['title', 'desc']
    search_fields = ['id', 'title', 'desc']
    list_per_page = 20


class EquipmentUseToMapManager(admin.ModelAdmin):
    list_display = ['id', 'equip', 'use']
    list_filter = ['use_id']
    list_per_page = 20


class EquipmentTypeManager(admin.ModelAdmin):
    list_display = ['id', 'equip_type']
    search_fields = ['id', 'equip_type']
    list_per_page = 20


class equipmentWarnManager(admin.ModelAdmin):
    list_display = ["id", 'equip', 'equip_record', 'summary', 'work_level', "warn_type", "is_manual_report", "created_time", "report_time"]
    search_fields = ['id', 'equip', 'equip_record', 'summary', 'get_warning_level']
    fields = ["id", 'equip', 'equip_record', 'summary', 'work_level', "warn_type", "is_manual_report", "created_time", "report_time"]
    readonly_fields = ["id"]
    list_per_page = 20


admin.site.register(Equipment, EquipmentManager)
admin.site.register(EquipmentRecord, EquipmentRecordManager)
admin.site.register(EquipmentFlag, EquipmentFlagManager)
admin.site.register(EquipmentUint, EquipmentUintManager)
admin.site.register(EquipmentUse, EquipmentUseManager)
admin.site.register(EquipmentUseToMap, EquipmentUseToMapManager)
admin.site.register(EquipmentType, EquipmentTypeManager)
admin.site.register(EquipmentWarn, equipmentWarnManager)
admin.site.register(EquipmentAttribute, EquipmentAttributeManager)

admin.site.site_header = Config.getIns().get('main', 'app_name', 'msa一体化管理后台')
admin.site.site_title = Config.getIns().get('main', 'app_name', 'msa一体化管理后台')
