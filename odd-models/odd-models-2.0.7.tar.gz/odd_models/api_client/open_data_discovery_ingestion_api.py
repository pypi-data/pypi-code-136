from typing import Optional, Dict, Union

from odd_models import models
from odd_models.api_client.http_client import HttpClient, validate_schema
from pydantic import BaseModel


class ODDApiClient(HttpClient):
    base_url = None

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip('/')

    @validate_schema(models.IngestionAlertList)
    def create_alerts(
            self,
            data: Union[dict, BaseModel],
            headers: Optional[Dict] = None,
            timeout: Optional[int] = None,
    ):
        request_data = {
            'path': '/ingestion/alerts',
            'data': data,
            'headers': headers,
            'timeout': timeout,
        }
        return self.post(**request_data)

    @validate_schema(models.DataSourceList)
    def create_data_source(
            self,
            data: Union[dict, BaseModel],
            headers: Optional[Dict] = None,
            timeout: Optional[int] = None,
    ):
        request_data = {
            'path': '/ingestion/datasources',
            'data': data,
            'headers': headers,
            'timeout': timeout,
        }
        return self.post(**request_data)

    def get_data_entities_by_deg_oddrn(
            self,
            deg_oddrn,
            headers: Optional[Dict] = None,
            timeout: Optional[int] = None,
    ):
        request_data = {
            'path': '/ingestion/dataentities',
            'params': {
                'deg_oddrn': deg_oddrn,
            },
            'headers': headers,
            'timeout': timeout,
        }
        return self.get(**request_data)

    @validate_schema(models.DataEntityList)
    def post_data_entity_list(
            self,
            data: Union[dict, BaseModel],
            headers: Optional[Dict] = None,
            timeout: Optional[int] = None,
    ):
        request_data = {
            'path': '/ingestion/entities',
            'data': data,
            'headers': headers,
            'timeout': timeout,
        }
        return self.post(**request_data)

