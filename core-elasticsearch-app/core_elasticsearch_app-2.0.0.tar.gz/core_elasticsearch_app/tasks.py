""" Elasticsearch tasks
"""
import logging

from celery import shared_task

from core_main_app.system import api as data_system_api
from core_elasticsearch_app.components.data import elasticsearch

logger = logging.getLogger(__name__)


@shared_task
def index_all_data_from_template(template):
    """Index all data"""
    try:
        data = data_system_api.get_all_by_template(template=template)
        for document in data:
            try:
                elasticsearch.index_data(document)
            except Exception as exception:
                logger.error(
                    "ERROR : An error occurred while indexing data : %s", str(exception)
                )
    except Exception as exception:
        logger.error(
            "ERROR : An error occurred while indexing data : %s", str(exception)
        )


@shared_task
def index_data(data_id):
    """Index a data"""
    try:
        data = data_system_api.get_data_by_id(data_id)
        try:
            elasticsearch.index_data(data)
        except Exception as exception:
            logger.error(
                "ERROR : An error occurred while indexing data :  %s", str(exception)
            )
    except Exception as exception:
        logger.error(
            "ERROR : An error occurred while indexing data :  %s", str(exception)
        )
