from typing import Iterable, Optional
from django.db import models
from django.conf import settings
from guardian.models import UserObjectPermissionBase
from guardian.models import GroupObjectPermissionBase

class ObjectClass(models.Model):
    """ 
    Declares a type of objects for querying and behaviour control
    """

    name = models.CharField(max_length=255, unique=True,
        help_text= 'Identifying name for this class.')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_object_classes")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_object_classes")

    updated_at = models.DateTimeField(auto_now=True,
        help_text= 'Time of last update.')

    allow_anonymous = models.BooleanField(default=True)

    allow_user_permissions = models.BooleanField(default=True, 
        help_text= 'Allow users to change permissions on objects from this class.')    
    
    class Meta:
        verbose_name = 'object class'
        verbose_name_plural = 'object classes'
        indexes = [
            models.Index(fields=['name',])
            ]



class ObjectClassUserObjectPermission(UserObjectPermissionBase):
    """
    Implements direct foreign keys for django-guardian:
    https://django-guardian.readthedocs.io/en/stable/userguide/performance.html#direct-foreign-keys
    """
    content_object = models.ForeignKey(ObjectClass, on_delete=models.CASCADE)


class ObjectClassGroupObjectPermission(GroupObjectPermissionBase):
    """
    Implements direct foreign keys for django-guardian:
    https://django-guardian.readthedocs.io/en/stable/userguide/performance.html#direct-foreign-keys
    """
    content_object = models.ForeignKey(ObjectClass, on_delete=models.CASCADE)


class Object(models.Model):
    """ 
    Model for user generated objects serialized in JSONFields
    """    
    object_class = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, null=False, blank=False, related_name="objects_in_class")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_objects")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_objects")

    updated_at = models.DateTimeField(auto_now=True,
        help_text= 'Time of last update.')

    version = models.IntegerField(
        help_text= 'Incrementing number after each update to the object.', default=0)

    data = models.JSONField(
        help_text= 'Serialized object as a JSON document.')

    class Meta:
        verbose_name = 'object'
        verbose_name_plural = 'objects'
        indexes = [
            models.Index(fields=['object_class',])
            ]
        
#    def increment(self) -> None:
#        self.version += 1
#
#    def save(self, force_insert: bool = ..., force_update: bool = ..., using: Optional[str] = ..., update_fields: Optional[Iterable[str]] = ...) -> None:
#        self.version += 1
#        return super().save(force_insert, force_update, using, update_fields)


class ObjectUserObjectPermission(UserObjectPermissionBase):
    """
    Implements direct foreign keys for django-guardian:
    https://django-guardian.readthedocs.io/en/stable/userguide/performance.html#direct-foreign-keys
    """
    content_object = models.ForeignKey(Object, on_delete=models.CASCADE)


class ObjectGroupObjectPermission(GroupObjectPermissionBase):
    """
    Implements direct foreign keys for django-guardian:
    https://django-guardian.readthedocs.io/en/stable/userguide/performance.html#direct-foreign-keys
    """
    content_object = models.ForeignKey(Object, on_delete=models.CASCADE)
