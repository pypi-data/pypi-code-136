""" Watchers for the data collection
"""
from django.db.models.signals import post_save

from core_main_app.components.data.models import Data
from core_elasticsearch_app.settings import ELASTICSEARCH_AUTO_INDEX
from core_elasticsearch_app.tasks import index_data


def post_save_data(sender, instance, **kwargs):
    """Method executed after a saving of a Data object.
    Args:
        sender: Class.
        instance: Data document.
        **kwargs: Args.

    """
    # only deal with data in a workspace
    if not instance.workspace:
        return

    # only deal with public data
    from core_main_app.components.workspace import api as workspace_api

    public_workspaces = workspace_api.get_all_public_workspaces().values_list(
        "id", flat=True
    )
    if instance.workspace.id not in public_workspaces:
        return

    # Creates or updates a document in the index.
    index_data.apply_async((str(instance.id),))


def init():
    """Connect to Data object events."""
    if ELASTICSEARCH_AUTO_INDEX:
        post_save.connect(post_save_data, sender=Data)
