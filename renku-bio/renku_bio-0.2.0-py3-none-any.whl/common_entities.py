import requests
from urllib.parse import urlsplit
from typing import Optional, List, Dict
from dataclasses import dataclass, field
from calamus import fields
from calamus.schema import JsonLDSchema
from renkubio import logger

schema = fields.Namespace("http://schema.org/")
bio = fields.Namespace("http://bioschemas.org/")


@dataclass
class Entity:
    """Base for specific entities"""

    _id: str
    name: str


@dataclass
class EnrichableEntity(Entity):
    """An entity whose properties can be enriched by querying an API with its name."""

    _api_url: Optional[str] = field(default=None)

    def query(self) -> List[Dict[str, str]]:
        """Query the API using the name attribute and
        returns the list of matching records."""

        base_url = urlsplit(self.api_url).netloc
        logger.debug(f"Querying {base_url} API for {self.name}...")
        resp = requests.get(self.api_url).json()

        if len(resp):
            records = resp
        else:
            logger.warning(
                f"No match for {self.name} in {urlsplit(self.api_url).netloc}: "
                f"{self.__class__.__name__} metadata will be left empty."
            )
            records = None
        return records

    @property
    def api_url(self):
        try:
            return self._api_url % self.name
        except TypeError:
            logger.error(
                f"No API URL available in class {self.__class__.__name__}. Cannot run query()"
            )
            raise

    def enrich(self, _: Dict[str, str]):
        """Update object with a JSON record from an API. The dictionary values
        are used to fill-in the instance's attributes"""

        logger.error("enrich must be implemented by the specific entity")
        raise NotImplementedError


@dataclass
class Place(EnrichableEntity):
    _id: str
    _api_url: str = field(
        default="https://nominatim.openstreetmap.org/search?q=%s&format=json"
    )
    name: str
    latitude: Optional[int] = None
    longitude: Optional[int] = None

    def enrich(self, geo_data: Dict[str, str]):
        """Update object with a geo record from Nominatim"""
        self.name = geo_data.get("display_name", self.name)
        self.latitude = float(geo_data.get("lat", self.latitude))
        self.longitude = float(geo_data.get("lon", self.longitude))


class PlaceSchema(JsonLDSchema):
    _id = fields.Id()
    name = fields.String(schema.name)
    latitude = fields.Float(schema.latitude)
    longitude = fields.Float(schema.longitude)

    class Meta:
        rdf_type = schema.Place
        model = Place


@dataclass
class Taxon(EnrichableEntity):
    _id: str
    _api_url: str = "https://www.ebi.ac.uk/ena/taxonomy/rest/any-name/%s"
    name: str
    parent_taxon: Optional[str] = None
    scientific_name: Optional[str] = None
    taxon_rank: Optional[str] = None

    def enrich(self, ebi_taxon: Dict[str, str]):
        """Update object with a taxonomy record from  EBI"""

        self.taxon_rank = ebi_taxon.get("rank", self.taxon_rank)
        try:
            self.parent_taxon = ebi_taxon["lineage"].split(";")[-3].strip()
        except KeyError:
            pass
        self.scientific_name = ebi_taxon.get("scientificName", self.scientific_name)
        self.name = ebi_taxon.get("commonName", self.name)


class TaxonSchema(JsonLDSchema):
    _id = fields.Id()
    name = fields.String(schema.name)
    scientific_name = fields.String(bio.scientificName)
    taxon_rank = fields.String(bio.taxonRank)
    parent_taxon = fields.String(bio.parentTaxon)

    class Meta:
        rdf_type = bio.Taxon
        model = Taxon


@dataclass
class Organization(EnrichableEntity):
    _id: str
    _api_url: str = "https://api.ror.org/organizations?affiliation=%s"
    name: str

    def query(self) -> List[Dict[str, str]]:
        """Query the ROR API using the name attribute and
        returns the list of matching organizations"""

        base_url = urlsplit(self.api_url).netloc
        logger.debug(f"Querying {base_url} API for {self.name}...")
        resp = requests.get(self.api_url).json()

        if resp["number_of_results"] > 0:
            records = [rec["organization"] for rec in resp["items"]]
        else:
            logger.warning(
                f"No match for {self.name} in {base_url}: "
                f"{self.__class__.__name__} metadata will be left empty."
            )
            records = None
        return records

    def enrich(self, ror_record: Dict[str, str]):
        """Update object with a record from ROR"""
        self.name = ror_record.get("name", self.name)
        self._id = ror_record.get("id", self._id)


class OrganizationSchema(JsonLDSchema):
    _id = fields.Id()
    name = fields.String(schema.name)

    class Meta:
        rdf_type = schema.Organization
        model = Organization
