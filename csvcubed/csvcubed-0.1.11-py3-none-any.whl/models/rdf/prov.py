"""
PROV Ontology Models
--------------------

This module holds some models in the prov-o ontology. 
"""
from typing import Annotated

from csvcubedmodels.rdf import (
    NewResource,
    Resource,
    Triple,
    PropertyStatus,
    map_resource_to_uri,
    ExistingResource,
)
from csvcubedmodels.rdf.namespaces import PROV


class Activity(NewResource):
    """
    This class represents the PROV-O ontology's activity class.
    prov:used is a property used to describe a prov:activty.
    """

    used: Annotated[
        ExistingResource,
        Triple(PROV.used, PropertyStatus.optional, map_resource_to_uri),
    ]

    def __init__(self, uri: str):
        NewResource.__init__(self, uri)
        self.rdf_types.add(PROV.Activity)


class Entity(NewResource):
    """
    This class represents the PROV-O ontology's entity class.
    prov:wasGeneratedBy is a property used to describe a prov:entity.

    """

    was_generated_by: Annotated[
        Resource[Activity],
        Triple(PROV.wasGeneratedBy, PropertyStatus.optional, map_resource_to_uri),
    ]

    def __init__(self, uri: str):
        NewResource.__init__(self, uri)
        self.rdf_types.add(PROV.Entity)
