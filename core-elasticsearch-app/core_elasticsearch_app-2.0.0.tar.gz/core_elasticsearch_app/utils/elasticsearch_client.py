""" Elasticsearch client for the CDCS
"""
from elasticsearch import Elasticsearch

from core_elasticsearch_app.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT


class ElasticsearchClient:
    """Elasticsearch client"""

    _elasticsearch = None

    @classmethod
    def elasticsearch(cls):
        """Return Elasticsearch connection
        Returns:
        """
        if cls._elasticsearch is None:
            cls._elasticsearch = Elasticsearch(
                [{"host": ELASTICSEARCH_HOST, "port": ELASTICSEARCH_PORT}]
            )
        return cls._elasticsearch

    @classmethod
    def delete_index(cls, index_name):
        """delete_index
        Args:
            index_name:

        Returns:
        """
        return cls.elasticsearch().indices.delete(index=index_name, ignore=[400, 404])

    @classmethod
    def create_index(cls, index_name, settings=None):
        """create_index
        Args:
            index_name:
            settings:

        Returns:
        """
        return cls.elasticsearch().indices.create(
            index=index_name, body=settings, ignore=400
        )

    @classmethod
    def index_document(cls, index_name, document_id, document):
        """index_document
        Args:
            index_name:
            document_id:
            document:

        Returns:
        """
        return cls.elasticsearch().index(
            index=index_name, id=document_id, body=document
        )

    @classmethod
    def delete_document(cls, index_name, document_id):
        """delete_document
        Args:
            index_name:
            document_id:

        Returns:
        """
        return cls.elasticsearch().delete(index=index_name, id=document_id)

    @classmethod
    def update_document(cls, index_name, document_id, document):
        """update_document
        Args:
            index_name:
            document_id:
            document:

        Returns:
        """
        return cls.elasticsearch().update(
            index=index_name, id=document_id, body=document
        )

    @classmethod
    def search(cls, index_name, query):
        """search
        Args:
            index_name:
            query:

        Returns:
        """
        return cls.elasticsearch().search(index=index_name, body=query)
