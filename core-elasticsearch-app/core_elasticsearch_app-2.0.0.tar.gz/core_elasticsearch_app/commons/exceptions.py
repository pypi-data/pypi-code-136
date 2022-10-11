""" Elasticsearch Exceptions
"""


class ElasticsearchError(Exception):
    """Exception raised by the Elasticsearch app."""

    def __init__(self, message):
        self.message = message
