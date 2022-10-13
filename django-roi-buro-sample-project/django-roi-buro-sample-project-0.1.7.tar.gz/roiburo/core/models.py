"""Core models"""

from django.db import models

from app.models import BaseModel


class SystemState(BaseModel):
    """System states model"""
    cpu_usage = models.FloatField(verbose_name="CPU usage")
    source_ip = models.GenericIPAddressField()

    class Meta:
        verbose_name = "System status"
        verbose_name_plural = "System statuses"
        db_table = "system_state"
