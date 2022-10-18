from collections import OrderedDict
from typing import Type

from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination as _LimitOffsetPagination
from rest_framework.response import Response

from logging import getLogger

logger = getLogger(__name__)


class LimitOffsetPagination(_LimitOffsetPagination):
    default_limit = 50
    max_limit = 200

    def get_paginated_data(self, data):
        return OrderedDict(
            [
                ("limit", self.limit),
                ("offset", self.offset),
                ("count", self.count),
                ("next", self.get_next_link()),
                ("previous", self.get_previous_link()),
                ("results", data),
            ]
        )

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("limit", self.limit),
                    ("offset", self.offset),
                    ("count", self.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )


def generate_paginated_response_serializer(
    instance_serializer: Type[serializers.Serializer], *, reference_name: str = None
):
    if reference_name is None:
        try:
            reference_name = instance_serializer.Meta.ref_name
        except AttributeError:
            reference_name = instance_serializer.__qualname__
    reference_name = "PaginatedResponse." + reference_name

    class ResponseSerializer(serializers.Serializer):
        limit = serializers.IntegerField(
            read_only=True,
        )
        offset = serializers.IntegerField(
            read_only=True,
        )
        count = serializers.IntegerField(
            read_only=True,
        )
        next = serializers.URLField(
            read_only=True,
        )
        previous = serializers.URLField(
            read_only=True,
        )
        results = serializers.ListSerializer(child=instance_serializer())

        class Meta:
            ref_name = reference_name

    return ResponseSerializer
