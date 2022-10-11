"""
Base Repository for Cosmos DB
"""
import json
from typing import Dict, List, NamedTuple, Optional, Union, Any
from azure.core import MatchConditions
from azure.cosmos import CosmosClient, ContainerProxy
from azure.cosmos.exceptions import CosmosResourceNotFoundError
from pydantic import BaseModel, parse_obj_as


class BaseRepository:
    """
    Base class for handling state in a CosmosDB
    Inspired in the work done here:
        https://github.com/microsoft/AzureTRE/blob/main/api_app/db/repositories/base.py

    Define as sub class a Config with the following attributes:
        - Model: The model class to use for parsing the items. [Required]
        - FixPartitionValue: If all documents have the same partition value, set this value.
    """

    def __init__(
        self,
        client: CosmosClient,
        db_name: str,
    ) -> None:
        """
        Initializes the base repository.

        Args:
            client: The CosmosDB client.
            db_name: The name of the database.
        """

        if not hasattr(self, "Config"):
            raise NotImplementedError("Config class is not defined.")

        config = getattr(self, "Config")

        if not hasattr(config, "Model"):
            raise NotImplementedError("Config must have a Model attribute.")
        self._model_cls = getattr(config, "Model")

        if not hasattr(config, "ContainerName"):
            raise NotImplementedError("Config must have a ContainerName attribute.")
        container_name = getattr(config, "ContainerName")

        if hasattr(config, "PartitionValue"):
            if not hasattr(config, "PartitionPath"):
                raise NotImplementedError(
                    "Config must have a PartitionPath attribute if PartitionValue is defined."
                )
            self._fix_partition_value = getattr(config, "PartitionValue")
            self._fix_partition_path = getattr(config, "PartitionPath")
        else:
            self._fix_partition_path = None
            self._fix_partition_value = None

        if not client:
            raise ValueError("client is required")
        self._client = client

        self._container = self._get_container(db_name, container_name)

    def _get_container(self, db_name, container_name) -> ContainerProxy:
        database = self._client.get_database_client(db_name)
        return database.get_container_client(container_name)

    @staticmethod
    def _convert_to_entity(item: BaseModel) -> dict:
        """
        Converts a model to a dictionary.
        The CosmosDb client requires a dictionary to create/update items.
        """

        if not isinstance(item, BaseModel):
            raise ValueError(f"Unsupported type: {type(item)}")

        return json.loads(item.json(by_alias=True))

    def _resolve_partition_key(self, partition_key: str = None) -> Optional[str]:
        return partition_key or self._fix_partition_value

    def query(
        self,
        query: str,
        parameters: Optional[List[Dict[str, object]]] = None,
        partition_key: str = None,
        enable_cross_partition_query: bool = False,
    ) -> List[BaseModel]:
        """
        Queries the database returning a list of items.
        """

        if not enable_cross_partition_query:
            partition_key = self._resolve_partition_key(partition_key)
        else:
            if partition_key:
                raise ValueError(
                    "Partition key cannot be used with cross partition query."
                )

        res = list(
            self._container.query_items(
                query=query,
                parameters=parameters,
                partition_key=partition_key,
                enable_cross_partition_query=enable_cross_partition_query,
            )
        )

        if self._model_cls:
            return [parse_obj_as(self._model_cls, item) for item in res]

        return res

    def get(self, item_id: str, partition_key: Any = None) -> Optional[BaseModel]:
        """
        Gets an item from the database.
        """
        partition_key = self._resolve_partition_key(partition_key)

        try:
            result = self._container.read_item(
                item=item_id, partition_key=partition_key
            )
        except CosmosResourceNotFoundError:
            return None

        return parse_obj_as(self._model_cls, result) if self._model_cls else result

    def create(self, item: BaseModel) -> Union[BaseModel, dict]:
        """
        Creates an item in the database.
        Raises CosmosResourceExistsError if the item already exists.
        """
        result = self._container.create_item(body=self._convert_to_entity(item))
        return parse_obj_as(self._model_cls, result) if self._model_cls else result

    def create_or_update(self, item: Union[BaseModel, NamedTuple, dict]) -> None:
        """
        Updates an existing item in the database.
        """
        result = self._container.upsert_item(self._convert_to_entity(item))
        return parse_obj_as(self._model_cls, result) if self._model_cls else result

    def update(self, item: BaseModel) -> Union[BaseModel, Dict[str, str]]:
        """
        Updates an existing item in the database.
        Returns the updated item with updated etag (if applicable).
        Raises CosmosResourceNotFoundError if the item does not exist.
        """
        entity = self._convert_to_entity(item)
        item_id = str(entity.get("id"))
        if not item_id:
            raise ValueError("The item must have an 'id' property")

        additional_params = {}
        etag = entity.get("_etag")
        if etag:
            additional_params["etag"] = etag
            additional_params["match_condition"] = MatchConditions.IfNotModified

        result = self._container.replace_item(
            item=item_id, body=entity, **additional_params
        )
        return parse_obj_as(self._model_cls, result) if self._model_cls else result

    def delete(self, item_id: str, partition_key: str = None) -> None:
        """
        Deletes an item from the database.
        """
        partition_key = self._resolve_partition_key(partition_key)
        if not partition_key:
            raise ValueError("A partition_key is required")

        self._container.delete_item(item=item_id, partition_key=partition_key)
