from rest_framework.views import APIView

from dry_django.contrib.rest_framework.mixins import (
    ApiDefaultMixin,
    ModelListAPIMixin,
    ModelRetrieveAPIMixin,
    ModelCreateAPIMixin,
    ModelUpdateAPIMixin,
    ModelDestroyAPIMixin,
)


class DefaultAPIView(ApiDefaultMixin, APIView):
    """
    Базовый класс для создания представлений, включающий миксины по умолчанию
    """

    pass


###################################
#  Generic Dry Django views
###################################


class ModelListAPIView(ModelListAPIMixin, DefaultAPIView):
    pass


class ModelListCreateAPIView(ModelListAPIMixin, ModelCreateAPIMixin, DefaultAPIView):
    pass


class ModelRetrieveUpdateDestroyAPIView(
    ModelRetrieveAPIMixin, ModelUpdateAPIMixin, ModelDestroyAPIMixin, DefaultAPIView
):
    pass
