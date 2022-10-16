# encoding: utf-8
"""
@project: djangoModel->j_subitem_extend
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 报名分项扩展字段映射工具
@created_time: 2022/10/16 13:26
"""
import re

from ..models import EnrollSubitemExtendField


# 扩展字段映射
def extend_filed_map(category_id):
    if not category_id:
        return [], {}

    try:
        query_obj = EnrollSubitemExtendField.objects.filter(category_id=category_id)
        if not query_obj:
            return [], {}
        extend_field_list = list(query_obj.values("field_index", "field"))
        extend_field_map = {i["field"]: i["field_index"] for i in extend_field_list}
        filter_filed_list = list(extend_field_map.keys())
        return filter_filed_list, extend_field_map

    except Exception as e:
        print("扩展字段映射错误：", str(e))
        return [], {}


def filter_field_index(result_list=[], result_dict={}):
    extend_field_list = list(EnrollSubitemExtendField.objects.all().values("category_id", "field_index", "field"))
    extend_field_map = {}
    for item in extend_field_list:
        category_id = extend_field_map.get(item["category_id"])
        if not category_id:
            extend_field_map[item["category_id"]] = {item["field"]: item["field_index"]}
        else:
            extend_field_map[item["category_id"]].update({item["field"]: item["field_index"]})

    for res_item in result_list:
        enroll_id = res_item
        for item_item in res_item:
            if not re.search("field_\d*/", item_item):
                continue
