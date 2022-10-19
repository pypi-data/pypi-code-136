from django.db import models


class ShopBase(models.Model):

    shopify_domain = models.CharField(max_length=50, default="")
    shopify_token = models.CharField(max_length=150, default="")
    access_scopes = models.CharField(max_length=50, default="")

    class Meta:
        abstract = True
