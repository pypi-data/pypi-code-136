"""Generated implementation of event_store_creation_request."""

# WARNING DO NOT EDIT
# This code was generated from event-store-creation-request.mcn

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

from ..access_control import AccessRule
from ..attribute import Attribute, SensitiveAttribute
from ..cluster import ClusterId
from ..event_store import EventStoreName, EventStoreTopicColumns, Topic
from ..label import Label
from ..schedule import Schedule


@dataclasses.dataclass(frozen=True)
class EventStoreCreationRequest:
    """Details for an event store.
    
    Args:
        name (EventStoreName): A data field.
        description (str): A data field.
        labels (typing.List[Label]): A data field.
        attributes (typing.List[Attribute]): A data field.
        accessRules (typing.List[AccessRule]): A data field.
        bootstrapServers (str): A data field.
        schemaRegistryUrl (str): A data field.
        kafkaPropertiesProviders (typing.List[SensitiveAttribute]): A data field.
        ingestions (typing.Dict[Topic, EventStoreTopicColumns]): A data field.
        connectBaseURI (typing.Optional[str]): A data field.
        scatterBaseURI (str): A data field.
        glacierBaseURI (str): A data field.
        batchIngestBaseURI (typing.Optional[str]): A data field.
        schedule (Schedule): A data field.
        cluster (ClusterId): A data field.
    """
    
    name: EventStoreName
    description: str
    labels: typing.List[Label]
    attributes: typing.List[Attribute]
    accessRules: typing.List[AccessRule]
    bootstrapServers: str
    schemaRegistryUrl: str
    kafkaPropertiesProviders: typing.List[SensitiveAttribute]
    ingestions: typing.Dict[Topic, EventStoreTopicColumns]
    connectBaseURI: typing.Optional[str]
    scatterBaseURI: str
    glacierBaseURI: str
    batchIngestBaseURI: typing.Optional[str]
    schedule: Schedule
    cluster: ClusterId
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for EventStoreCreationRequest data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "name": EventStoreName.json_schema(),
                "description": {
                    "type": "string"
                },
                "labels": {
                    "type": "array",
                    "item": Label.json_schema()
                },
                "attributes": {
                    "type": "array",
                    "item": Attribute.json_schema()
                },
                "accessRules": {
                    "type": "array",
                    "item": AccessRule.json_schema()
                },
                "bootstrapServers": {
                    "type": "string"
                },
                "schemaRegistryUrl": {
                    "type": "string"
                },
                "kafkaPropertiesProviders": {
                    "type": "array",
                    "item": SensitiveAttribute.json_schema()
                },
                "ingestions": {
                    "type": "object",
                    "additionalProperties": EventStoreTopicColumns.json_schema()
                },
                "connectBaseURI": {
                    "oneOf": [
                        {"type": "null"},
                        {"type": "string"},
                    ]
                },
                "scatterBaseURI": {
                    "type": "string"
                },
                "glacierBaseURI": {
                    "type": "string"
                },
                "batchIngestBaseURI": {
                    "oneOf": [
                        {"type": "null"},
                        {"type": "string"},
                    ]
                },
                "schedule": Schedule.json_schema(),
                "cluster": ClusterId.json_schema()
            },
            "required": [
                "name",
                "description",
                "labels",
                "attributes",
                "accessRules",
                "bootstrapServers",
                "schemaRegistryUrl",
                "kafkaPropertiesProviders",
                "ingestions",
                "scatterBaseURI",
                "glacierBaseURI",
                "schedule",
                "cluster",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> EventStoreCreationRequest:
        """Validate and parse JSON data into an instance of EventStoreCreationRequest.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of EventStoreCreationRequest.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return EventStoreCreationRequest(
                name=EventStoreName.from_json(data["name"]),
                description=str(data["description"]),
                labels=[Label.from_json(v) for v in data["labels"]],
                attributes=[Attribute.from_json(v) for v in data["attributes"]],
                accessRules=[AccessRule.from_json(v) for v in data["accessRules"]],
                bootstrapServers=str(data["bootstrapServers"]),
                schemaRegistryUrl=str(data["schemaRegistryUrl"]),
                kafkaPropertiesProviders=[SensitiveAttribute.from_json(v) for v in data["kafkaPropertiesProviders"]],
                ingestions={
                    Topic.from_json_key(k): EventStoreTopicColumns.from_json(v) for k, v in data["ingestions"].items()
                },
                connectBaseURI=(lambda v: v and str(v))(data.get("connectBaseURI", None)),
                scatterBaseURI=str(data["scatterBaseURI"]),
                glacierBaseURI=str(data["glacierBaseURI"]),
                batchIngestBaseURI=(
                    lambda v: v and str(v)
                )(
                    data.get("batchIngestBaseURI", None)
                ),
                schedule=Schedule.from_json(data["schedule"]),
                cluster=ClusterId.from_json(data["cluster"]),
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing EventStoreCreationRequest",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "name": self.name.to_json(),
            "description": str(self.description),
            "labels": [v.to_json() for v in self.labels],
            "attributes": [v.to_json() for v in self.attributes],
            "accessRules": [v.to_json() for v in self.accessRules],
            "bootstrapServers": str(self.bootstrapServers),
            "schemaRegistryUrl": str(self.schemaRegistryUrl),
            "kafkaPropertiesProviders": [v.to_json() for v in self.kafkaPropertiesProviders],
            "ingestions": {k.to_json_key(): v.to_json() for k, v in self.ingestions.items()},
            "connectBaseURI": (lambda v: v and str(v))(self.connectBaseURI),
            "scatterBaseURI": str(self.scatterBaseURI),
            "glacierBaseURI": str(self.glacierBaseURI),
            "batchIngestBaseURI": (lambda v: v and str(v))(self.batchIngestBaseURI),
            "schedule": self.schedule.to_json(),
            "cluster": self.cluster.to_json()
        }
