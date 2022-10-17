"""Generated implementation of lineage."""

# WARNING DO NOT EDIT
# This code was generated from lineage.mcn

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

from ..destination import Destination
from ..event_store import EventStore
from ..feature import Feature
from ..feature_set import FeatureSet
from ..feature_store import FeatureStore
from ..source import Source
from ..table import Table


@dataclasses.dataclass(frozen=True)
class Lineage:
    """Representation of data lineage.
    
    Args:
        eventStores (typing.List[EventStore]): A data field.
        sources (typing.List[Source]): A data field.
        tables (typing.List[Table]): A data field.
        features (typing.List[Feature]): A data field.
        featureSets (typing.List[FeatureSet]): A data field.
        featureStores (typing.List[FeatureStore]): A data field.
        destinations (typing.List[Destination]): A data field.
    """
    
    eventStores: typing.List[EventStore]
    sources: typing.List[Source]
    tables: typing.List[Table]
    features: typing.List[Feature]
    featureSets: typing.List[FeatureSet]
    featureStores: typing.List[FeatureStore]
    destinations: typing.List[Destination]
    
    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for Lineage data.
        
        Returns:
            A Python dictionary describing the JSON schema.
        """
        return {
            "type": "object",
            "properties": {
                "eventStores": {
                    "type": "array",
                    "item": EventStore.json_schema()
                },
                "sources": {
                    "type": "array",
                    "item": Source.json_schema()
                },
                "tables": {
                    "type": "array",
                    "item": Table.json_schema()
                },
                "features": {
                    "type": "array",
                    "item": Feature.json_schema()
                },
                "featureSets": {
                    "type": "array",
                    "item": FeatureSet.json_schema()
                },
                "featureStores": {
                    "type": "array",
                    "item": FeatureStore.json_schema()
                },
                "destinations": {
                    "type": "array",
                    "item": Destination.json_schema()
                }
            },
            "required": [
                "eventStores",
                "sources",
                "tables",
                "features",
                "featureSets",
                "featureStores",
                "destinations",
            ]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> Lineage:
        """Validate and parse JSON data into an instance of Lineage.
        
        Args:
            data (dict): JSON data to validate and parse.
        
        Returns:
            An instance of Lineage.
        
        Raises:
            ValidationError: When schema validation fails.
            KeyError: When a required field is missing from the JSON.
        """
        try:
            jsonschema.validate(data, cls.json_schema())
            return Lineage(
                eventStores=[EventStore.from_json(v) for v in data["eventStores"]],
                sources=[Source.from_json(v) for v in data["sources"]],
                tables=[Table.from_json(v) for v in data["tables"]],
                features=[Feature.from_json(v) for v in data["features"]],
                featureSets=[FeatureSet.from_json(v) for v in data["featureSets"]],
                featureStores=[FeatureStore.from_json(v) for v in data["featureStores"]],
                destinations=[Destination.from_json(v) for v in data["destinations"]],
            )
        except jsonschema.exceptions.ValidationError as ex:
            logging.debug(
                "Invalid JSON data received while parsing Lineage",
                exc_info=ex
            )
            raise
    
    def to_json(self) -> dict:
        """Serialise this instance as JSON.
        
        Returns:
            Data ready to serialise as JSON.
        """
        return {
            "eventStores": [v.to_json() for v in self.eventStores],
            "sources": [v.to_json() for v in self.sources],
            "tables": [v.to_json() for v in self.tables],
            "features": [v.to_json() for v in self.features],
            "featureSets": [v.to_json() for v in self.featureSets],
            "featureStores": [v.to_json() for v in self.featureStores],
            "destinations": [v.to_json() for v in self.destinations]
        }
