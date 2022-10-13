"""App base models"""

import uuid

from django.db import models


class BaseModel(models.Model):
    """Base model with timestamp fields"""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Create date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    class Meta:
        abstract = True
