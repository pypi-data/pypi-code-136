from datetime import datetime
from typing import Optional, Union
from dataclasses import dataclass
from calamus import fields
from calamus.schema import JsonLDSchema
from renkubio.common_entities import (
    bio,
    schema,
    Place,
    PlaceSchema,
    Organization,
    OrganizationSchema,
    Taxon,
    TaxonSchema,
)


@dataclass
class BioSample:
    """Represents a biological sample, according to the biosample profile from bioschemas.org"""

    _id: str
    name: str
    url: str
    description: str
    collector: Optional[Union[str, Organization]] = None
    taxonomic_range: Optional[Union[str, Taxon]] = None
    sampling_age: Optional[int] = None
    gender: Optional[str] = None
    location_created: Optional[str] = None
    date_created: Optional[datetime] = None
    is_control: Optional[bool] = None

    def __post_init__(self):
        """instantiate object properties and assign ids."""

        if self.location_created:
            self.location_created = Place(
                _id=self._id + "/loc", name=self.location_created
            )
        if self.taxonomic_range:
            self.taxonomic_range = Taxon(
                _id=self._id + "/tax", name=self.taxonomic_range
            )
        if self.collector:
            self.collector = Organization(_id=self._id + "/org", name=self.collector)


class BioSampleSchema(JsonLDSchema):
    _id = fields.Id()
    name = fields.String(schema.name)
    url = fields.IRI(schema.url)
    description = fields.String(schema.description)
    sampling_age = fields.Integer(bio.samplingAge)
    gender = fields.String(schema.gender)
    is_control = fields.Boolean(bio.isControl)
    date_created = fields.Date(schema.dateCreated)
    location_created = fields.Nested(bio.locationCreated, PlaceSchema)
    taxonomic_range = fields.Nested(bio.taxonomicRange, TaxonSchema)
    collector = fields.Nested(bio.collector, OrganizationSchema)

    class Meta:
        rdf_type = bio.BioSample
        model = BioSample
