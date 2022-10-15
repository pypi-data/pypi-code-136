# encoding: utf-8
"""
@project: djangoModel->subitem_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 报名分项记录
@created_time: 2022/10/15 12:38
"""
from django.core.paginator import Paginator

from ..models import EnrollSubitem, EnrollExtendField
from ..utils.model_handle import format_params_handle


def extend_filed_filter():
    try:
        extend_field_list = list(EnrollExtendField.objects.all().values("field_index", "alias_name"))
        extend_field_map = {i["alias_name"]: i["field_index"] for i in extend_field_list}
        filter_filed_list = list(extend_field_map.keys())
        return filter_filed_list, extend_field_map
    except Exception as e:
        print("扩展字段映射错误：", str(e))
        return [], {}


class SubitemService:

    @staticmethod
    def list(params):
        size = params.pop('size', 10)
        page = params.pop('page', 1)
        # 字段过滤
        filter_filed_list, extend_field_map = extend_filed_filter()
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id", "enroll_id", "name", "price", "count", "unit", "description", "remark"] + filter_filed_list,
            alias_dict=extend_field_map
        )

        try:
            fetch_obj = EnrollSubitem.objects.filter(**params).values()
            paginator = Paginator(fetch_obj, size)
            page_obj = paginator.page(page)
            data = {'total': paginator.count, "size": size, 'page': page, 'list': list(page_obj.object_list)}
            return data, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def edit(params, subitem_rule_id):
        subitem_rule_id = params.pop("id", None) or subitem_rule_id

        filter_filed_list, extend_field_map = extend_filed_filter()
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id", "enroll_id", "name", "price", "count", "unit", "description", "remark"] + filter_filed_list,
            alias_dict=extend_field_map
        )

        subitem_enroll_obj = EnrollSubitem.objects.filter(id=subitem_rule_id)
        if not subitem_enroll_obj:
            return None, None
        try:
            subitem_enroll_obj.update(**params)
        except Exception as e:
            return None, "修改异常:" + str(e)
        return None, None

    @staticmethod
    def delete(subitem_rule_id):
        subitem_enroll_obj = EnrollSubitem.objects.filter(id=subitem_rule_id)
        if not subitem_enroll_obj:
            return None, None
        try:
            subitem_enroll_obj.delete()
        except Exception as e:
            return None, "删除异常:" + str(e)
        return None, None

    @staticmethod
    def add(params):
        filter_filed_list, extend_field_map = extend_filed_filter()
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=["enroll_id", "name", "price", "count", "unit", "description", "remark"] + filter_filed_list,
            alias_dict=extend_field_map
        )
        if not params.get("enroll_id"):
            return None, "请填写报名ID"
        try:
            EnrollSubitem.objects.create(**params)
        except Exception as e:
            return None, str(e)

        return None, None
