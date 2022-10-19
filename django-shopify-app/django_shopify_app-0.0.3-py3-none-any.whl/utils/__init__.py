from django.apps import apps
from django.conf import settings


def get_shop_model():
    Model = apps.get_model(settings.SHOPIFY_SHOP_MODEL)
    return Model
