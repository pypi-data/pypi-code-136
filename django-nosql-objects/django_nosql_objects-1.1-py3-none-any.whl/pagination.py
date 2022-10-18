from rest_framework.pagination import LimitOffsetPagination


class ObjectViewSetPagination(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100