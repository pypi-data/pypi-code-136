from typing import *
from django.http import JsonResponse
from django.db.models import QuerySet

__all__ = ["APIView"]


class HookClassMixin:
    """钩子函数类"""

    def process_request(self, request):
        """拦截处理request"""
        return request

    def inject_queryset(self, request):
        """ 注入queryset
        inject_queryset需要返回一个queryset,
        该函数在过滤操作之前运行，如果返回了一个queryset，过滤函数会从这个queryset中过滤出结果，
        如果没有定义该函数，或者该函数返回None，queryset就是过滤类中的Meta.model.objects.all()
        可以在该函数中引发异常，使接口返回400错误，表示资源不可访问或不存在。
        注意：
            1.inject_queryset不能对queryset进行切片等破坏性操作，切片会禁止对queryset进行进一步的排序或过滤！
            2.当inject_queryset未定义或返回None时, filter_class一定不能为None！
        """
        return None

    def process_queryset(self, queryset):
        """对过滤之后，分页之前的queryset进行处理"""
        return queryset

    def process_results(self, results):
        """results的拦截函数，可以重写该函数对results 进行修改
        results是序列化后的结果，results一般是由多个字典对象组成的列表或者一个单独的字典"""
        return results

    def process_data(self, data):
        """data拦截函数，data是接口返回给请求的最终数据"""
        return data


class APIView(HookClassMixin):
    # filter_class为None时，一定要定义process_queryset函数，且process_queryset不能返回None
    filter_class = None
    paginator_class = None
    serializer_class = None

    def __init__(self):
        self.request = None
        self.queryset = None

    def _filtering(self, user_query: dict, queryset):
        """过滤，从request中获取查询条件(query),
        如果inject_queryset返回的queryset为None,queryset就是filter_class中的Meta.model.objects.all()"""
        if self.filter_class:
            return self.filter_class(user_query, queryset)
        else:
            return queryset

    def _paging(self, queryset, request) -> Tuple[QuerySet, Dict or None]:
        if self.paginator_class is None:
            return queryset, None
        paginator = self.paginator_class(queryset, request)
        return paginator.sub_set(), paginator.page_count()

    def _build_data(self, results: Dict or List, page_count: Dict or None):
        """生成最终数据，可以被序列化的数据"""
        if page_count:
            data = {'results': results}
            data.update(page_count)
        else:
            data = results
        return data

    def api(self, request):
        """直接暴露给路由的API接口"""
        request = self.process_request(request)  # 处理request
        self.request = request
        # 注入queryset
        try:
            self.queryset = self.inject_queryset(request)
        except Exception as err:
            return JsonResponse({'msg': '资源不可访问，或不存在！', 'errors': str(err)}, status=400)

        if self.queryset is None and self.filter_class is None:
            raise RuntimeError(f'{self.__class__.__name__} inject_queryset返回None,且没有定义filter_class')

        # 过滤
        user_query = getattr(request, request.method)
        try:
            self.queryset = self._filtering(user_query, self.queryset)
        except Exception as err:
            return JsonResponse({'msg': 'filter error！', 'errors': str(err)}, status=400)

        # 处理queryset
        try:
            self.queryset = self.process_queryset(self.queryset)
        except Exception as err:
            return JsonResponse({'msg': 'process queryset error!', 'errors': str(err)}, status=400)

        # 翻页
        # page_count: Dict or None  # page_count为None则证明无需翻页(paginator_class is None)，直接返回queryset
        self.queryset = self.queryset
        self.queryset, page_count = self._paging(self.queryset, request)
        # 序列化
        try:
            results = self.serializer_class(self.queryset)
        except Exception as err:
            return JsonResponse({'msg': 'serializer error！', 'errors': str(err)}, status=400)

        # 处理results
        results = self.process_results(results)

        # 生成data（self.results中填入分页数据）
        data = self._build_data(results, page_count)

        # 处理data
        data = self.process_data(data)
        return JsonResponse(data, safe=False)

    @classmethod
    def as_view(cls):
        def api(request):
            self = cls()
            return self.api(request)

        return api

    def __init_subclass__(cls, **kwargs):
        if not cls.serializer_class:
            raise TypeError(f'{cls.__name__}没有配置serializer_class！')
