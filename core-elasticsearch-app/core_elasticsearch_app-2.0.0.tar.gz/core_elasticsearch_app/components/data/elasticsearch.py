""" Utils for managing CDCS data in elasticsearch
"""
import logging

from core_main_app.commons import exceptions
from xml_utils.xsd_tree.xsd_tree import XSDTree

from core_elasticsearch_app.components.data.autocomplete_settings import (
    DATA_AUTOCOMPLETE_SETTINGS,
)
from core_elasticsearch_app.components.data.mongodb import get_value_from_path
from core_elasticsearch_app.settings import (
    ELASTICSEARCH_CDCS_DATA_INDEX,
)
from core_elasticsearch_app.utils.elasticsearch_client import ElasticsearchClient
from core_elasticsearch_app.components.elasticsearch_template import (
    api as elasticsearch_template_api,
)

logger = logging.getLogger(__name__)


def create_data_index():
    """Create autocomplete index on data titles

    Returns:

    """
    return ElasticsearchClient.create_index(
        ELASTICSEARCH_CDCS_DATA_INDEX, DATA_AUTOCOMPLETE_SETTINGS
    )


def index_data(data):
    """Build json document for elasticsearch from CDCS data

    Args:
        data:

    Returns:

    """

    try:
        es_template = elasticsearch_template_api.get_by_template(data.template)
        es_data = {
            "data_id": str(data.id),
            "title": get_value_from_path(data, es_template.title_path)
            if es_template.title_path
            else data.title,
            "description": " ".join(
                [
                    _get_string_value(get_value_from_path(data, path))
                    for path in es_template.description_paths
                ]
            )
            if es_template.description_paths
            else XSDTree.fromstring(data.xml_content).xpath("//text()"),
        }
        # TODO: could use global PID instead of id
        return ElasticsearchClient.index_document(
            ELASTICSEARCH_CDCS_DATA_INDEX, str(data.id), es_data
        )
    except exceptions.DoesNotExist:
        logger.warning(
            "Data with id %s will not be indexed. No template configured.", str(data.id)
        )
    except Exception as exception:
        logger.error(str(exception))


def get_suggestions(query, fuzziness=1, prefix_length=3, fragment_size=100):
    """Get suggestions from query

    Args:
        query:
        fuzziness:
        prefix_length:
        fragment_size:

    Returns:

    """
    query = {
        "query": {
            "multi_match": {
                "query": query,
                "fuzziness": fuzziness,
                "prefix_length": prefix_length,
            }
        },
        "highlight": {
            "number_of_fragments": 1,
            "fragment_size": fragment_size,
            "fields": {"title": {}, "description": {}},
        },
    }
    result = ElasticsearchClient.search(ELASTICSEARCH_CDCS_DATA_INDEX, query)
    return result["hits"]["hits"]


def _get_string_value(value):
    """Get string value

    Args:
        value:

    Returns:

    """
    if value:
        return value
    return ""
