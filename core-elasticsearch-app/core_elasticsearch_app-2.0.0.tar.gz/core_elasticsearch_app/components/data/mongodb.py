""" MongoDB utils for the Data component
"""
import logging

from core_main_app.utils.xml import xpath_to_dot_notation
from core_elasticsearch_app.utils.utils import get_nested_value

logger = logging.getLogger(__name__)


def get_value_from_path(data, path):
    """Get value from xpath

    Args:
        data:
        path:

    Returns:

    """
    value = get_nested_value(data.get_dict_content(), path)
    if value:
        if isinstance(value, dict):
            logger.info("A dict was found at %s for data %s ", path, str(data.id))
            try:
                value = value["#text"]
            except Exception:
                value = None
                logger.warning(
                    "#text was not found at path %s for data %s ", path, str(data.id)
                )
    else:
        logger.warning(
            "No value could be found at path %s for data %s", path, str(data.id)
        )
    return value


def get_exists_query_from_path(path):
    """Return mongodb query that checks if path exists in database

    Args:
        path:

    Returns:

    """
    dot_path = xpath_to_dot_notation(path)
    return {
        "$or": [
            {f"dict_content.{dot_path}": {"$exists": True}},
            {f"dict_content.{dot_path}.#text": {"$exists": True}},
        ]
    }
