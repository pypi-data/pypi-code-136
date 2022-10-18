import json
from django.dispatch import receiver
from django.db.models.signals import pre_save
import sys
from .models import Object

DISABLE_SIGNALS = 'makemigrations' in sys.argv or 'migrate' in sys.argv #or 'test' in sys.argv


@receiver(pre_save, dispatch_uid="pre_save_signal")
def pre_save_signal(sender, instance, **kwargs):
    """
    Increments an Object version if before the are saved anywhere in the project
    """
    if DISABLE_SIGNALS: return
    if isinstance(instance, Object):
        instance.version += 1
