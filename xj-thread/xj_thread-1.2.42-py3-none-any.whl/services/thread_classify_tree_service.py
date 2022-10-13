"""
Created on 2022-04-11
@author:刘飞
@description:发布子模块逻辑处理
"""
import logging

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import F
from rest_framework import serializers

from ..models import ThreadAuth
from ..models import ThreadClassify
from ..models import ThreadClassify
from ..models import ThreadExtendField
from ..models import ThreadShow
from ..models import ThreadTag
from ..serializers import ThreadAuthListSerializer
from ..serializers import ThreadTagSerializer
from ..utils.model_handle import format_params_handle
from ..utils.j_recur import JRecur

log = logging.getLogger()


class ThreadClassifyTreeServices:
    def __init__(self):
        pass

    @staticmethod
    def get_classify_tree(classify_id=None, classify_value=None):
        """
        类别树。
        """
        # 第一步，把类别列表全部读出来
        classify_set = ThreadClassify.objects.annotate(
            classify_value=F('value'),
            category_value=F('category_id__value'),
            show_value=F('show_id__value'),
        ).order_by('sort').values(
            'id',
            'classify_value',
            'name',
            'show_value',
            'category_value',
            'description',
            'icon',
            'sort',
            'parent_id',
        )
        # print("> classify_set:", classify_set)
        classify_list = list(classify_set)
        # print("> classify_list:", classify_list)

        # 第二步，遍历列表，把数据存放在dict里
        filter_key = 'id' if classify_id else ('classify_value' if classify_value else None)
        filter_value = classify_id if classify_id else (classify_value if classify_value else None)
        if filter_key and filter_value:
            classify_tree = JRecur.create_tree(source_list=classify_list, search_root_key=filter_key, search_root_value=filter_value)

        return classify_tree, None

    @staticmethod
    def get_classify_all_tree(classify_value=None, classify_id=None):
        pass
