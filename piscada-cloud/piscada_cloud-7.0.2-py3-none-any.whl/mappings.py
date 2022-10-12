"""
Classes and functions related to the mappings-manager service.

The mappings-manager service is used to map concrete controller/tag combinations to abstract meanings,
which can then be use to run an abstractly defined cloud-function on multiple concrete mapping definitions.
"""
import logging
import os
from typing import Dict, List, Optional, Tuple, Union
from uuid import UUID

import requests

from piscada_cloud.manipulations import get_first_or_default


def _check_env_vars() -> Tuple[str, str]:
    host = os.getenv("MAPPINGSMANAGER_HOST")
    token = os.getenv("MAPPINGSMANAGER_TOKEN")
    if not host or not token:
        raise RuntimeError("Both environment variables MAPPINGSMANAGER_HOST and MAPPINGSMANAGER_TOKEN need to be defined.")
    return host, token


class Tag:
    """
    A tag on a specific controller.

    Attributes
    ----------
    controller_id : UUID
        The ID of the controller this tag belongs to.
    name : str
        The tag's name/id.
    """

    def __init__(self, controller_id: Union[UUID, str], name: Optional[str] = None, uuid: Optional[Union[UUID, str]] = None, path: Optional[str] = None):
        if controller_id is None or (uuid is None and name is None):
            raise ValueError("controller_id and either uuid or name must be supplied")
        self.controller_id: UUID = controller_id if isinstance(controller_id, UUID) else UUID(controller_id)
        self.name = name
        self.path = path
        self.uuid: Optional[UUID] = uuid if uuid is None or isinstance(uuid, UUID) else UUID(uuid)

    def __repr__(self):
        return str(self.controller_id) + "|" + str(self.get_identifier())

    def __key(self):
        return (self.controller_id, str(self.get_identifier()))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.__key() == other.__key()  # pylint: disable=W0212
        return NotImplemented

    def get_identifier(self) -> Union[UUID, str]:
        """Get tag identifier.

        Returns
        -------
        Union[UUID, str]
            Tag uuid if set, otherwise its name
        """
        if self.uuid is not None:
            return self.uuid
        return self.name  # type: ignore

    def get_meta_data(self):
        """Fetch meta data from the Cloud Meta Data API."""
        url = f'https://{os.environ["CLOUD_META_DATA_HOST"]}/v0/tags?controller-uuid={self.controller_id}&'
        if self.uuid is not None:
            url += f"uuid={self.uuid}"
        else:
            url += f"name={self.name}"
        response = requests.request("GET", url, headers={"Authorization": f"Bearer {os.environ['CLOUD_META_DATA_TOKEN']}"})
        if response.status_code != 200:
            raise RuntimeError(f"Cloud Meta Data API gave response: {response.status_code}: {response.text}")
        try:
            response_tag = response.json()[0]
            self.name = response_tag["name"]
            self.uuid = UUID(response_tag["uuid"])
            self.path = response_tag["path"]
        except IndexError:
            logging.debug("Could not find meta data for tag %s", str(self))


class Meaning:
    """A meaning uniquely identifies an input, output or parameter in cloud functions."""

    def __init__(self, title: str, meaning_type: str, uuid: UUID):
        self.title: str = title
        self.type: str = meaning_type
        self.uuid: UUID = uuid

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{self.title} ({self.uuid}) {self.type}"

    def __eq__(self, other):
        return self.uuid == other.uuid


class TagMapping:  # pylint: disable=too-few-public-methods
    """A mapping from meaning to a controller/tag combination."""

    def __init__(self, meaning: Meaning, controller_id: UUID, tag: Union[str, UUID]):
        self.meaning = meaning
        if isinstance(tag, UUID):
            self.tag = Tag(controller_id, uuid=tag)
        else:
            try:
                self.tag = Tag(controller_id, uuid=UUID(tag))
            except ValueError:
                self.tag = Tag(controller_id, name=tag)

    def __repr__(self):
        return f"{self.meaning} ({self.meaning.type}): {self.tag}"


class Parameter:  # pylint: disable=too-few-public-methods
    """A mapping from meaning to a constant value."""

    def __init__(self, meaning: Meaning, value: str):
        self.meaning: Meaning = meaning
        self.value: str = value

    def __repr__(self):
        return f"{self.meaning}: {self.value}"


# pylint: disable=too-many-arguments
class MappingTable:
    """A collections of TagMappings which connect meanings to concrete tags on specific controllers."""

    def __init__(
        self, title: str, uuid: UUID, tag_mappings: Optional[List[TagMapping]] = None, parameters: Optional[List[Parameter]] = None, active: Optional[bool] = True
    ):
        self.title: str = title
        self.uuid: UUID = uuid
        self.tag_mappings: List[TagMapping] = tag_mappings if tag_mappings is not None else []
        self.parameters: List[Parameter] = parameters if parameters is not None else []
        self.active = active

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.uuid}|{self.title}"

    def get_tag_mappings(self, meaning_uuid: Optional[UUID] = None, meaning_title: Optional[str] = None) -> List[TagMapping]:
        """Get the tag-mappings from the mapping-table relating to a meaning with provided title or UUID.

        Parameters
        ----------
        meaning_title: Optional[str]
            Title of the meaning the tag-mapping relates to.
        meaning_uuid: Optional[UUID]
            UUID of the meaning the tag-mapping relates to.

        Returns
        -------
        List[TagMapping]
            Tag-mapping related to a meaning with the provided attributes.
        """
        if meaning_uuid is not None:
            if not isinstance(meaning_uuid, UUID):
                meaning_uuid = UUID(meaning_uuid)
            return [tag_mapping for tag_mapping in self.tag_mappings if tag_mapping.meaning.uuid == meaning_uuid]
        if meaning_title is not None:
            return [tag_mapping for tag_mapping in self.tag_mappings if tag_mapping.meaning.title == meaning_title]
        return []

    def get_tag(self, meaning_uuid: Optional[UUID] = None, meaning_title: Optional[str] = None, multiple: bool = False) -> Optional[Union[Tag, List[Tag]]]:
        """Get a tag from a tag-mapping relating to a meaning with specific title or UUID.

        Parameters
        ----------
        meaning_title: Optional[str]
            Title of the meaning the tag relates to.
        meaning_uuid: Optional[UUID]
            UUID of the meaning the tag relates to.
        multiple: bool
            If True, the method will attempt to fetch a list of tags for the meaning.

        Returns
        -------
        Tag
            Tag of a tag-mapping related to a meaning with the specified attributes.
        List[Tag]
            A list of tags with the related to the provided meaning.
        None
            If no tag-mapping relates to a meaning with the specified attributes.
        """
        tag_mappings = self.get_tag_mappings(meaning_uuid, meaning_title)
        if len(tag_mappings) == 0:
            return None
        tag_mapping = tag_mappings[0]

        if multiple:
            accepted_meaning_types = ["input_list", "output_list"]
            if tag_mapping.meaning.type not in accepted_meaning_types:
                if tag_mapping.meaning.type in ["input", "output"]:
                    raise ValueError(f"Meaning has type '{tag_mapping.meaning.type}'. You should set the 'multiple' flag to 'False'.")
                raise ValueError(f"Meaning has type '{tag_mapping.meaning.type}'. Expected one of {accepted_meaning_types}.")
            return [tag_mapping.tag for tag_mapping in tag_mappings]

        accepted_meaning_types = ["input", "output"]
        if tag_mapping.meaning.type not in accepted_meaning_types:
            if tag_mapping.meaning.type in ["input_list", "output_list"]:
                raise ValueError(f"Meaning has type '{tag_mapping.meaning.type}'. You should set the 'multiple' flag to 'True'.")
            raise ValueError(f"Meaning has type '{tag_mapping.meaning.type}'. Expected one of {accepted_meaning_types}.")
        return tag_mapping.tag

    def get_parameter(
        self, meaning_uuid: Optional[UUID] = None, meaning_title: Optional[str] = None, multiple: bool = False
    ) -> Optional[Union[Parameter, List[Parameter]]]:
        """Get the parameter from the mapping-table relating to a meaning with provided title or UUID.

        Parameters
        ----------
        meaning_title: Optional[str]
            Title of the meaning the parameter relates to.
        meaning_uuid: Optional[UUID]
            UUID of the meaning the parameter relates to.
        multiple: bool
            If True, the method will attempt to fetch a list of parameters for the meaning.

        Returns
        -------
        str
            Value of the parameter found.
        List[str]
            List of parameters found.
        None
            If no parameter was not found.
        """
        parameters = []
        if meaning_uuid is not None:
            if not isinstance(meaning_uuid, UUID):
                meaning_uuid = UUID(meaning_uuid)
            parameters = [parameter for parameter in self.parameters if parameter.meaning.uuid == meaning_uuid]
        elif meaning_title is not None:
            parameters = [parameter for parameter in self.parameters if parameter.meaning.title == meaning_title]
        if len(parameters) == 0:
            return None
        parameter = parameters[0]

        if multiple:
            if parameter.meaning.type != "parameter_list":
                if parameter.meaning.type == "parameter":
                    raise ValueError(f"Meaning has type '{parameter.meaning.type}'. You should set the 'multiple' flag to 'False'.")
                raise ValueError(f"Got meaning of type '{parameter.meaning.type}'. Expected 'parameter_list'.")
            return parameters

        if parameter.meaning.type != "parameter":
            if parameter.meaning.type == "parameter_list":
                raise ValueError(f"Meaning has type '{parameter.meaning.type}'. You should set the 'multiple' flag to 'True'.")
            raise ValueError(f"Got meaning of type '{parameter.meaning.type}'. Expected 'parameter'.")
        return parameter


class Rating:
    """A collection of rating scores for different business aspects."""

    def __init__(self, comfort: float, energy: float, operation: float):
        self.comfort = comfort
        self.energy = energy
        self.operation = operation

    def __add__(self, other):
        return Rating(self.comfort + other, self.energy + other, self.operation + other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __sum__(self):
        return self.comfort + self.energy + self.operation

    def __mul__(self, other):
        return Rating(self.comfort * other, self.energy * other, self.operation * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"(Comfort: {round(self.comfort, 2)}, Energy: {round(self.energy, 2)}, Operation: {round(self.operation, 2)})"

    def __eq__(self, other):
        return self.comfort == other.comfort and self.energy == other.energy and self.operation == other.operation


class Mapping:
    """A collection of meanings which are used to uniquely identify inputs and outputs in cloud functions."""

    # pylint: disable=too-many-instance-attributes,too-many-arguments
    def __init__(
        self,
        title: str,
        uuid: UUID,
        cause: Dict[str, str],
        consequence: Dict[str, str],
        description: str,
        level: str,
        meanings: List[Meaning],
        rating: Rating,
        cypher_query: Optional[str] = None,
    ):
        self.title = title
        self.uuid = uuid
        self.cause = cause
        self.consequence = consequence
        self.description = description
        self.level = level
        self.meanings = meanings
        self.rating = rating
        self.cypher_query = cypher_query

    def __str__(self):
        return f"{self.title}: {self.meanings}"

    def __repr__(self):
        return f"{self.title} ({self.uuid}): {self.meanings}"

    def get_mapping_tables(self, active: Optional[bool] = None) -> List[MappingTable]:
        """Retrieve the mapping tables associated with the mapping.

        Parameters
        ----------
        active: Optional[bool]
            If True, only fetch active mapping tables.
            If False, only fetch inactive mapping tables.

        Returns
        -------
        mapping_tables: List[MappingTable]
            A list of mapping tables associated with the mapping.
        """
        mapping_tables: List[MappingTable] = []
        host, token = _check_env_vars()
        header = {"Authorization": "Bearer " + token}
        response = requests.get(f"https://{host}/v0/mapping-tables/{self.uuid}", headers=header)
        if response and response.status_code == 200:
            mapping_tables_json = response.json()
            if active is not None:
                mapping_tables_json = [table for table in mapping_tables_json if table["active"] == active]
            for mapping_table_json in mapping_tables_json:
                mapping_table = MappingTable(mapping_table_json["title"], UUID(mapping_table_json["uuid"]), active=mapping_table_json["active"])
                for tag_mapping_json in mapping_table_json["tag-mappings"]:
                    try:
                        controller_id: UUID = UUID(tag_mapping_json["controller-id"])
                    except ValueError:
                        logging.error("Invalid controller-id: %s", tag_mapping_json["controller-id"])
                    else:
                        meaning = get_first_or_default([meaning for meaning in self.meanings if meaning.uuid == UUID(tag_mapping_json["meaning-uuid"])], None)
                        mapping_table.tag_mappings.append(TagMapping(meaning, controller_id, tag_mapping_json["tag"]))
                for parameter_json in mapping_table_json["parameters"]:
                    meaning = get_first_or_default([meaning for meaning in self.meanings if meaning.uuid == UUID(parameter_json["meaning-uuid"])], None)
                    mapping_table.parameters.append(Parameter(meaning, value=parameter_json["value"]))
                mapping_tables.append(mapping_table)
        else:
            logging.error("No mapping tables received: %s", response.content)
        return mapping_tables


def get_mapping(uuid: UUID) -> Optional[Mapping]:
    """Fetch a specific mapping.

    Parameters
    ----------
    uuid: UUID
        UUID of the mapping that will be fetched.

    Returns
    -------
    mapping: Mapping
        The mapping with the specified UUID.
    None
        If not mapping was found for the specified UUID.
    """
    host, token = _check_env_vars()
    header = {"Authorization": "Bearer " + token}
    response = requests.get(f"https://{host}/v0/mappings/{uuid}", headers=header)
    if response and response.status_code == 200:
        mapping_json = response.json()
        try:
            mapping = Mapping(
                title=mapping_json["title"],
                uuid=UUID(mapping_json["uuid"]),
                cause=mapping_json["cause"],
                consequence=mapping_json["consequence"],
                description=mapping_json["description"],
                level=mapping_json["level"],
                rating=Rating(**mapping_json["ratings"]),
                meanings=[
                    Meaning(title=meaning_json["title"], uuid=UUID(meaning_json["uuid"]), meaning_type=meaning_json["type"]) for meaning_json in mapping_json["meanings"]
                ],
                cypher_query=mapping_json["cypher_query"],
            )
        except KeyError as exc:
            raise KeyError(f"Mapping with uuid {uuid} is missing the attribute '{exc.args[0]}'. You may have to use piscada-cloud<=6.0.0 to read this mapping.") from exc
        return mapping
    logging.error("No mapping received: %s", response.content)
    return None


def get_mappings() -> List[Mapping]:
    """Fetch all mappings.

    Returns
    -------
    mappings: List[Mapping]
        All mappings from the mappings manager service.
    """
    host, token = _check_env_vars()
    header = {"Authorization": "Bearer " + token}
    response = requests.get(f"https://{host}/v0/mappings", headers=header)
    mappings: List[Mapping] = []
    if response and response.status_code == 200:
        mappings_json = response.json()
        mappings_skipped = []
        for mapping_json in mappings_json:
            try:
                mapping = Mapping(
                    title=mapping_json["title"],
                    uuid=UUID(mapping_json["uuid"]),
                    cause=mapping_json["cause"],
                    consequence=mapping_json["consequence"],
                    description=mapping_json["description"],
                    level=mapping_json["level"],
                    rating=Rating(**mapping_json["ratings"]),
                    meanings=[
                        Meaning(title=meaning_json["title"], uuid=UUID(meaning_json["uuid"]), meaning_type=meaning_json["type"])
                        for meaning_json in mapping_json["meanings"]
                    ],
                    cypher_query=mapping_json["cypher_query"],
                )
            except KeyError:
                mappings_skipped.append(mapping_json["uuid"])
                continue
            mappings.append(mapping)
        logging.warning(
            "Skipping mappings %s since they're not formatted properly. You may have to use piscada-cloud<=6.0.0 to read them.",
            mappings_skipped,
        )
    else:
        logging.error("No mappings received: %s", response.content)
    return mappings
