""" Metadata model
"""
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from core_main_app.commons import exceptions
from core_main_app.components.abstract_data.models import AbstractData
from core_main_app.components.template.models import Template
from core_main_app.components.workspace.models import Workspace


class UserMetadata(AbstractData):
    """Metadata object"""

    template = models.ForeignKey(Template, blank=False, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200)
    workspace = models.ForeignKey(
        Workspace, blank=True, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "User metadata"
        verbose_name_plural = "User metadata"
        indexes = [
            models.Index(
                fields=["title", "last_modification_date", "template", "user_id"]
            ),
        ]

    def get_dict_content(self):
        """Return dict_content

        Returns:

        """
        return self.dict_content

    @staticmethod
    def get_all(order_by_field):
        """Get all data.

        Args:
            order_by_field: Order by field.

        Returns:

        """
        return UserMetadata.objects.all().order_by(
            *[field.replace("+", "") for field in order_by_field]
        )

    @staticmethod
    def get_by_id(data_id):
        """Return the object with the given id.

        Args:
            data_id:

        Returns:
            Data (obj): Data object with the given id

        """
        try:
            return UserMetadata.objects.get(pk=str(data_id))
        except ObjectDoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    def __str__(self):
        """User metadata object as string

        Returns:

        """
        return self.title
