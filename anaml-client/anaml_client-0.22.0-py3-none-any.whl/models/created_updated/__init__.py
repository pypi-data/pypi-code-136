"""Generated implementation of created_updated."""

# WARNING DO NOT EDIT
# This code was generated from created-updated.mcn

from __future__ import annotations

import abc  # noqa: F401
import dataclasses  # noqa: F401
import datetime  # noqa: F401
import enum  # noqa: F401
import isodate  # noqa: F401
import json  # noqa: F401
import jsonschema  # noqa: F401
import logging  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
try:
    from anaml_client.utils.serialisation import JsonObject  # noqa: F401
except ImportError:
    pass

from ..cluster import ClusterId
from ..destination import DestinationId
from ..entity import EntityId
from ..entity_mapping import EntityMappingId
from ..entity_population import EntityPopulationId
from ..event_store import EventStoreId
from ..feature_id import FeatureId
from ..feature_set import FeatureSetId
from ..feature_store import FeatureStoreId
from ..feature_template import TemplateId
from ..jobs import TableMonitoringJobId
from ..source import SourceId
from ..table import TableId
from ..table_caching import TableCachingJobId
from ..view_materialisation import ViewMaterialisationJobId
from ..webhook import WebhookId


@dataclasses.dataclass(frozen=True)
class EntityCreatedUpdated:
    """Entity created and updated timestamps.
    
    Args:
        id (EntityId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: EntityId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for EntityCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": EntityId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> EntityCreatedUpdated:
        """Validate and parse JSON data into an instance of EntityCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of EntityCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return EntityCreatedUpdated(
                id=EntityId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing EntityCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class EntityMappingCreatedUpdated:
    """Entity Mapping created and updated timestamps.
    
    Args:
        id (EntityMappingId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: EntityMappingId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for EntityMappingCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": EntityMappingId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> EntityMappingCreatedUpdated:
        """Validate and parse JSON data into an instance of EntityMappingCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of EntityMappingCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return EntityMappingCreatedUpdated(
                id=EntityMappingId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing EntityMappingCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class EntityPopulationCreatedUpdated:
    """Entity Population created and updated timestamps.
    
    Args:
        id (EntityPopulationId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: EntityPopulationId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for EntityPopulationCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": EntityPopulationId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> EntityPopulationCreatedUpdated:
        """Validate and parse JSON data into an instance of EntityPopulationCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of EntityPopulationCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return EntityPopulationCreatedUpdated(
                id=EntityPopulationId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing EntityPopulationCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class FeatureCreatedUpdated:
    """Feature created and updated timestamps.
    
    Args:
        id (FeatureId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: FeatureId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for FeatureCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": FeatureId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> FeatureCreatedUpdated:
        """Validate and parse JSON data into an instance of FeatureCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of FeatureCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return FeatureCreatedUpdated(
                id=FeatureId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing FeatureCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class FeatureSetCreatedUpdated:
    """FeatureSet created and updated timestamps.
    
    Args:
        id (FeatureSetId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: FeatureSetId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for FeatureSetCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": FeatureSetId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> FeatureSetCreatedUpdated:
        """Validate and parse JSON data into an instance of FeatureSetCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of FeatureSetCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return FeatureSetCreatedUpdated(
                id=FeatureSetId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing FeatureSetCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class TemplateCreatedUpdated:
    """Template created and updated timestamps.
    
    Args:
        id (TemplateId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: TemplateId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for TemplateCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": TemplateId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> TemplateCreatedUpdated:
        """Validate and parse JSON data into an instance of TemplateCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of TemplateCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return TemplateCreatedUpdated(
                id=TemplateId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing TemplateCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class TableCreatedUpdated:
    """Table created and updated timestamps.
    
    Args:
        id (TableId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: TableId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for TableCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": TableId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> TableCreatedUpdated:
        """Validate and parse JSON data into an instance of TableCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of TableCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return TableCreatedUpdated(
                id=TableId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing TableCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class FeatureStoreCreatedUpdated:
    """Feature Store created and updated timestamps.
    
    Args:
        id (FeatureStoreId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: FeatureStoreId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for FeatureStoreCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": FeatureStoreId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> FeatureStoreCreatedUpdated:
        """Validate and parse JSON data into an instance of FeatureStoreCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of FeatureStoreCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return FeatureStoreCreatedUpdated(
                id=FeatureStoreId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing FeatureStoreCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class EventStoreCreatedUpdated:
    """Event Store created and updated timestamps.
    
    Args:
        id (EventStoreId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: EventStoreId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for EventStoreCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": EventStoreId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> EventStoreCreatedUpdated:
        """Validate and parse JSON data into an instance of EventStoreCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of EventStoreCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return EventStoreCreatedUpdated(
                id=EventStoreId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing EventStoreCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class SourceCreatedUpdated:
    """Source created and updated timestamps.
    
    Args:
        id (SourceId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: SourceId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for SourceCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": SourceId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> SourceCreatedUpdated:
        """Validate and parse JSON data into an instance of SourceCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of SourceCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return SourceCreatedUpdated(
                id=SourceId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing SourceCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class DestinationCreatedUpdated:
    """Destination created and updated timestamps.
    
    Args:
        id (DestinationId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: DestinationId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for DestinationCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": DestinationId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> DestinationCreatedUpdated:
        """Validate and parse JSON data into an instance of DestinationCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of DestinationCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return DestinationCreatedUpdated(
                id=DestinationId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing DestinationCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class ClusterCreatedUpdated:
    """Cluster created and updated timestamps.
    
    Args:
        id (ClusterId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: ClusterId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for ClusterCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": ClusterId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> ClusterCreatedUpdated:
        """Validate and parse JSON data into an instance of ClusterCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of ClusterCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return ClusterCreatedUpdated(
                id=ClusterId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing ClusterCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class WebhookCreatedUpdated:
    """Webhook created and updated timestamps.
    
    Args:
        id (WebhookId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: WebhookId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for WebhookCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": WebhookId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> WebhookCreatedUpdated:
        """Validate and parse JSON data into an instance of WebhookCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of WebhookCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return WebhookCreatedUpdated(
                id=WebhookId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing WebhookCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class TableMonitoringJobCreatedUpdated:
    """Table Monitoring Job created and updated timestamps.
    
    Args:
        id (TableMonitoringJobId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: TableMonitoringJobId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for TableMonitoringJobCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": TableMonitoringJobId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> TableMonitoringJobCreatedUpdated:
        """Validate and parse JSON data into an instance of TableMonitoringJobCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of TableMonitoringJobCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return TableMonitoringJobCreatedUpdated(
                id=TableMonitoringJobId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing TableMonitoringJobCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class TableCachingJobCreatedUpdated:
    """Table Caching Job created and updated timestamps.
    
    Args:
        id (TableCachingJobId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: TableCachingJobId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for TableCachingJobCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": TableCachingJobId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> TableCachingJobCreatedUpdated:
        """Validate and parse JSON data into an instance of TableCachingJobCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of TableCachingJobCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return TableCachingJobCreatedUpdated(
                id=TableCachingJobId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing TableCachingJobCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }


@dataclasses.dataclass(frozen=True)
class ViewMaterialisationJobCreatedUpdated:
    """View Materialisation Job created and updated timestamps.
    
    Args:
        id (ViewMaterialisationJobId): A data field.
        created (datetime.datetime): A data field.
        updated (datetime.datetime): A data field.
    """
    
    id: ViewMaterialisationJobId
    created: datetime.datetime
    updated: datetime.datetime
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for ViewMaterialisationJobCreatedUpdated data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "id": ViewMaterialisationJobId.json_schema(),
                "created": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "id",
                "created",
                "updated",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> ViewMaterialisationJobCreatedUpdated:
        """Validate and parse JSON data into an instance of ViewMaterialisationJobCreatedUpdated.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of ViewMaterialisationJobCreatedUpdated.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return ViewMaterialisationJobCreatedUpdated(
                id=ViewMaterialisationJobId.from_json(data["id"]),
                created=isodate.parse_datetime(data["created"]),
                updated=isodate.parse_datetime(data["updated"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing ViewMaterialisationJobCreatedUpdated",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "id": self.id.to_json(),
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "updated": self.updated.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }
