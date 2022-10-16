"""
Created on 2022-04-11
@description:刘飞
@description:发布子模块逻辑分发
"""
from rest_framework.views import APIView

from ..services.thread_other_list_service import ThreadOtherListServices
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data, request_params_wrapper

t = ThreadOtherListServices()


class CategoryListAPIView(APIView):
    """
    get:类别列表
    """

    @request_params_wrapper
    def get(self, request=None, request_params=None, *args, **kwargs):
        data, error_text = t.thread_category(request_params)
        return util_response(data=data)


class ClassifyListAPIView(APIView):
    """
    get:分类列表
    """

    def get(self, request, *args, **kwargs):
        request_params = parse_data(request)
        print(request_params)
        category_value = request_params.get('category_value', None)
        category_id = request_params.get('category_id', None)
        classify_value = request_params.get('classify_value', None)
        data, error_text = t.thread_classify(category_value=category_value, category_id=category_id, classify_value=classify_value)
        return util_response(data=data)


class ShowListAPIView(APIView):
    """
    get:展示类型列表
    """

    def get(self, request, *args, **kwargs):
        data, error_text = t.thread_show()
        return util_response(data=data)


class AuthListAPIView(APIView):
    """
    get:访问权限列表
    """

    def get(self, request, *args, **kwargs):
        data, error_text = t.thread_auth()
        return util_response(data=data)


class TagListAPIView(APIView):
    """
    get:标签列表
    """

    def get(self, request):
        params = parse_data(request)
        data, error_text = t.thread_tag(params)
        return util_response(data=data)


class ThreadExtendFieldList(APIView):
    """扩展字段列表"""

    def get(self, request):
        params = parse_data(request)
        data, err = t.thread_extend_field_list(params)
        if err:
            return util_response(err=54555, msg=err)
        return util_response(data=data)
