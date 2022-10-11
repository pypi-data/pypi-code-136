#!/usr/bin/env python3
# encoding: utf-8
#
# ** header v3.0
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2021 Henrik tom Wörden
#               2021 Alexander Schlemmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ** end header
#

"""
Crawl a file structure using a yaml cfood definition and synchronize
the acuired data with CaosDB.
"""

import importlib
from caosadvancedtools.cache import UpdateCache, Cache
import uuid
import sys
import os
import yaml
from enum import Enum
import logging
from importlib_resources import files
import argparse
from argparse import RawTextHelpFormatter
import caosdb as db
from caosadvancedtools.crawler import Crawler as OldCrawler
from caosdb.common.datatype import is_reference
from .stores import GeneralStore, RecordStore
from .identified_cache import IdentifiedCache
from .structure_elements import StructureElement, Directory
from .converters import Converter, DirectoryConverter
from .identifiable_adapters import (IdentifiableAdapter,
                                    LocalStorageIdentifiableAdapter,
                                    CaosDBIdentifiableAdapter)
from collections import defaultdict
from typing import Any, Dict, List, Optional, Type, Union
from caosdb.apiutils import compare_entities, merge_entities
from copy import deepcopy
from jsonschema import validate

from .macros import defmacro_constructor, macro_constructor

logger = logging.getLogger(__name__)

SPECIAL_PROPERTIES_STRICT = ("description", "name", "id", "path")
SPECIAL_PROPERTIES_NOT_STRICT = ("file", "checksum", "size")

# Register the macro functions from the submodule:
yaml.SafeLoader.add_constructor("!defmacro", defmacro_constructor)
yaml.SafeLoader.add_constructor("!macro", macro_constructor)


def check_identical(record1: db.Entity, record2: db.Entity, ignore_id=False):
    """
    This function uses compare_entities to check whether to entities are identical
    in a quite complex fashion:
    - If one of the entities has additional parents or additional properties -> not identical
    - If the value of one of the properties differs -> not identical
    - If datatype, importance or unit are reported different for a property by compare_entities
      return "not_identical" only if these attributes are set explicitely by record1.
      Ignore the difference otherwise.
    - If description, name, id or path appear in list of differences -> not identical.
    - If file, checksum, size appear -> Only different, if explicitely set by record1.

    record1 serves as the reference, so datatype, importance and unit checks are carried
    out using the attributes from record1. In that respect, the function is not symmetrical
    in its arguments.
    """
    comp = compare_entities(record1, record2)

    if ignore_id:
        if "id" in comp[0]:
            del comp[0]["id"]
        if "id" in comp[1]:
            del comp[1]["id"]

    for j in range(2):
        for label in ("parents", ):
            if len(comp[j][label]) > 0:
                return False
    for special_property in SPECIAL_PROPERTIES_STRICT:
        if special_property in comp[0] or special_property in comp[1]:
            return False

    for special_property in SPECIAL_PROPERTIES_NOT_STRICT:
        if special_property in comp[0]:
            attr_val = comp[0][special_property]
            other_attr_val = (comp[1][special_property]
                              if special_property in comp[1] else None)
            if attr_val is not None and attr_val != other_attr_val:
                return False

    for key in comp[0]["properties"]:
        if len(comp[0]["properties"][key]) == 0:
            # This is a new property
            return False
        for attribute in ("datatype", "importance", "unit"):
            # only make an update for those attributes if there is a value difference and
            # the value in the target_data is not None
            if attribute in comp[0]["properties"][key]:
                attr_val = comp[0]["properties"][key][attribute]
                other_attr_val = (comp[1]["properties"][key][attribute]
                                  if attribute in comp[1]["properties"][key] else None)
                if attr_val is not None and attr_val != other_attr_val:
                    return False

        if "value" in comp[0]["properties"][key]:
            return False

    # Check for removed properties:
    for key in comp[1]["properties"]:
        if len(comp[1]["properties"][key]) == 0:
            # This is a removed property
            return False

    return True


def _resolve_datatype(prop: db.Property, remote_entity: db.Entity):
    """ sets the datatype on the given property (side effect) """

    if remote_entity.role == "Property":
        datatype = remote_entity.datatype
    elif remote_entity.role == "RecordType":
        datatype = remote_entity.name
    else:
        raise RuntimeError("Cannot set datatype.")

    # Treat lists separately
    if isinstance(prop.value, list) and not datatype.startswith("LIST"):
        datatype = db.LIST(datatype)

    prop.datatype = datatype
    return prop


class SecurityMode(Enum):
    RETRIEVE = 0
    INSERT = 1
    UPDATE = 2


class Crawler(object):
    """
    Crawler class that encapsulates crawling functions.
    Furthermore it keeps track of the storage for records (record store) and the
    storage for values (general store).
    """

    def __init__(self,
                 generalStore: Optional[GeneralStore] = None,
                 debug: bool = False,
                 identifiableAdapter: IdentifiableAdapter = None,
                 securityMode: int = SecurityMode.UPDATE
                 ):
        """
        Create a new crawler and initialize an empty RecordStore and GeneralStore.

        Parameters
        ----------
        recordStore : GeneralStore
             An initial GeneralStore which might store e.g. environment variables.
        debug : bool
             Create a debugging information tree when set to True.
             The debugging information tree is a variable stored in
             self.debug_tree. It is a dictionary mapping directory entries
             to a tuple of general stores and record stores which are valid for
             the directory scope.
             Furthermore, it is stored in a second tree named self.debug_copied whether the
             objects in debug_tree had been copied from a higher level in the hierarchy
             of the structureelements.
        identifiableAdapter : IdentifiableAdapter
             TODO describe
        securityMode : int
             Whether only retrieves are allowed or also inserts or even updates.
             Please use SecurityMode Enum
        """

        # TODO: check if this feature is really needed

        self.identified_cache = IdentifiedCache()
        self.recordStore = RecordStore()
        self.securityMode = securityMode

        self.generalStore = generalStore
        if generalStore is None:
            self.generalStore = GeneralStore()

        self.identifiableAdapter = identifiableAdapter
        if identifiableAdapter is None:
            self.identifiableAdapter = LocalStorageIdentifiableAdapter()
        # If a directory is crawled this may hold the path to that directory
        self.crawled_directory = None
        self.debug = debug
        if self.debug:
            # order in the tuple:
            # 0: generalStore
            # 1: recordStore
            self.debug_tree: Dict[str, tuple] = dict()
            self.debug_metadata: Dict[str, dict] = dict()
            self.debug_metadata["copied"] = dict()
            self.debug_metadata["provenance"] = defaultdict(lambda: dict())
            self.debug_metadata["usage"] = defaultdict(lambda: set())

    def load_definition(self, crawler_definition_path: str):
        """
        Load a cfood from a crawler definition defined by
        crawler definition path and validate it using cfood-schema.yml.
        """

        # Load the cfood from a yaml file:
        with open(crawler_definition_path, "r") as f:
            crawler_definitions = list(yaml.safe_load_all(f))

        crawler_definition = self._load_definition_from_yaml_dict(
            crawler_definitions)

        return self._resolve_validator_paths(crawler_definition, crawler_definition_path)

    def _load_definition_from_yaml_dict(self, crawler_definitions: List[Dict]):
        """Load crawler definitions from a list of (yaml) dicts `crawler_definitions` which
        contains either one or two documents.

        Doesn't resolve the validator paths in the cfood definition, so for
        internal and testing use only.

        """
        if len(crawler_definitions) == 1:
            # Simple case, just one document:
            crawler_definition = crawler_definitions[0]
        elif len(crawler_definitions) == 2:
            crawler_definition = crawler_definitions[1]
        else:
            raise RuntimeError(
                "Crawler definition must not contain more than two documents.")

        # TODO: at this point this function can already load the cfood schema extensions
        #       from the crawler definition and add them to the yaml schema that will be
        #       tested in the next lines of code:

        # Load the cfood schema:
        with open(files('caoscrawler').joinpath('cfood-schema.yml'), "r") as f:
            schema = yaml.safe_load(f)

        # Add custom converters to converter enum in schema:
        if "Converters" in crawler_definition:
            for key in crawler_definition["Converters"]:
                schema["cfood"]["$defs"]["converter"]["properties"]["type"]["enum"].append(
                    key)
        if len(crawler_definitions) == 2:
            if "Converters" in crawler_definitions[0]["metadata"]:
                for key in crawler_definitions[0]["metadata"]["Converters"]:
                    schema["cfood"]["$defs"]["converter"]["properties"]["type"]["enum"].append(
                        key)

        # Validate the cfood schema:
        validate(instance=crawler_definition, schema=schema["cfood"])

        return crawler_definition

    def _resolve_validator_paths(self, definition: dict, definition_path: str):
        """Resolve path to validation files with respect to the file in which
        the crawler was defined.

        """

        for key, value in definition.items():

            if key == "validate" and isinstance(value, str):
                # Validator is given by a path
                if not value.startswith('/'):
                    # Not an absolute path
                    definition[key] = os.path.join(
                        os.path.dirname(definition_path), value)
                    if not os.path.isfile(definition[key]):
                        raise FileNotFoundError(
                            f"Couldn't find validation file {definition[key]}")
            elif isinstance(value, dict):
                # Recursively resolve all validators
                definition[key] = self._resolve_validator_paths(
                    value, definition_path)

        return definition

    def load_converters(self, definition: dict):
        """
        Currently the converter registry is a dictionary containing for each converter:
        - key is the short code, abbreviation for the converter class name
        - module is the name of the module to be imported which must be installed
        - class is the converter class to load and associate with this converter entry

        all other info for the converter needs to be included in the converter plugin
        directory:
        schema.yml file
        README.md documentation
        """

        # Defaults for the converter registry:
        converter_registry: Dict[str, Dict[str, str]] = {
            "Directory": {
                "converter": "DirectoryConverter",
                "package": "caoscrawler.converters"},
            "SimpleFile": {
                "converter": "SimpleFileConverter",
                "package": "caoscrawler.converters"},
            "MarkdownFile": {
                "converter": "MarkdownFileConverter",
                "package": "caoscrawler.converters"},
            "File": {
                "converter": "FileConverter",
                "package": "caoscrawler.converters"},
            "JSONFile": {
                "converter": "JSONFileConverter",
                "package": "caoscrawler.converters"},
            "CSVTableConverter": {
                "converter": "CSVTableConverter",
                "package": "caoscrawler.converters"},
            "XLSXTableConverter": {
                "converter": "XLSXTableConverter",
                "package": "caoscrawler.converters"},
            "Dict": {
                "converter": "DictConverter",
                "package": "caoscrawler.converters"},
            "DictBooleanElement": {
                "converter": "DictBooleanElementConverter",
                "package": "caoscrawler.converters"},
            "DictFloatElement": {
                "converter": "DictFloatElementConverter",
                "package": "caoscrawler.converters"},
            "DictTextElement": {
                "converter": "DictTextElementConverter",
                "package": "caoscrawler.converters"},
            "DictIntegerElement": {
                "converter": "DictIntegerElementConverter",
                "package": "caoscrawler.converters"},
            "DictListElement": {
                "converter": "DictListElementConverter",
                "package": "caoscrawler.converters"},
            "DictDictElement": {
                "converter": "DictDictElementConverter",
                "package": "caoscrawler.converters"},
            "TextElement": {
                "converter": "TextElementConverter",
                "package": "caoscrawler.converters"}
        }

        # More converters from definition file:
        if "Converters" in definition:
            for key, entry in definition["Converters"].items():
                converter_registry[key] = {
                    "converter": entry["converter"],
                    "package": entry["package"]
                }

        # Load modules and associate classes:
        for key, value in converter_registry.items():
            module = importlib.import_module(value["package"])
            value["class"] = getattr(module, value["converter"])
        return converter_registry

    def crawl_directory(self, dirname: str, crawler_definition_path: str):
        """ Crawl a single directory.

        Convenience function that starts the crawler (calls start_crawling)
        with a single directory as the StructureElement.
        """

        crawler_definition = self.load_definition(crawler_definition_path)
        # Load and register converter packages:
        converter_registry = self.load_converters(crawler_definition)

        if not dirname:
            raise ValueError(
                "You have to provide a non-empty path for crawling.")
        dir_structure_name = os.path.basename(dirname)
        self.crawled_directory = dirname
        if not dir_structure_name and dirname.endswith('/'):
            if dirname == '/':
                # Crawling the entire file system
                dir_structure_name = "root"
            else:
                # dirname had a trailing '/'
                dir_structure_name = os.path.basename(dirname[:-1])

        self.start_crawling(Directory(dir_structure_name,
                                      dirname),
                            crawler_definition,
                            converter_registry)

    @staticmethod
    def initialize_converters(crawler_definition: dict, converter_registry: dict):
        """
        takes the cfood as dict (`crawler_definition`) and creates the converter objects that
        are defined on the highest level. Child Converters will in turn be created during the
        initialization of the Converters.
        """
        converters = []

        for key, value in crawler_definition.items():
            # Definitions and Converters are reserved keywords
            # on the top level of the yaml file.
            # TODO: there should also be a top level keyword for the actual
            #       CFood to avoid confusion between top level keywords
            #       and the CFood.
            if key == "Definitions":
                continue
            elif key == "Converters":
                continue
            converters.append(Converter.converter_factory(
                value, key, converter_registry))

        return converters

    def start_crawling(self, items: Union[List[StructureElement], StructureElement],
                       crawler_definition: dict,
                       converter_registry: dict):
        """
        Start point of the crawler recursion.

        Parameters
        ----------
        items: list
             A list of structure elements (or a single StructureElement) that is used for
             generating the initial items for the crawler. This could e.g. be a Directory.
        crawler_definition : dict
             A dictionary representing the crawler definition, possibly from a yaml
             file.

        Returns
        -------
        target_data : list
            the final list with the target state of Records.
        """

        # This function builds the tree of converters out of the crawler definition.

        if self.generalStore is None:
            raise RuntimeError("Should not happen.")

        if not isinstance(items, list):
            items = [items]

        self.run_id = uuid.uuid1()
        local_converters = Crawler.initialize_converters(
            crawler_definition, converter_registry)
        # This recursive crawling procedure generates the update list:
        self.target_data: List[db.Record] = []
        self._crawl(items, local_converters, self.generalStore,
                    self.recordStore, [], [])

        if self.debug:
            self.debug_converters = local_converters

        return self.target_data

    def synchronize(self, commit_changes: bool = True, unique_names=True):
        """
        Carry out the actual synchronization.
        """

        # After the crawling, the actual synchronization with the database, based on the
        # update list is carried out:

        return self._synchronize(self.target_data, commit_changes, unique_names=unique_names)

    def can_be_checked_externally(self, record: db.Record):
        """
        Returns False if there is at least one property in record which:
        a) is a reference property AND
        b) where the value is set to a db.Entity (instead of an ID) AND
        c) where the ID of the value is not set (to an integer)

        Returns True otherwise.
        """
        for p in record.properties:
            if isinstance(p.value, list):
                for el in p.value:
                    if isinstance(el, db.Entity) and el.id is None:
                        return False
            # TODO: please check!
            #       I removed the condition "is_reference", because the datatype field
            #       that is checked within this function is not always present for references
            #       parsed from the file structure. We have to rely on the condition, that
            #       if a property value is of type entity, it can be assumed to be a reference.
            # elif (is_reference(p) and isinstance(p.value, db.Entity)
            #         and p.value.id is None):
            elif isinstance(p.value, db.Entity) and p.value.id is None:
                return False
        return True

    def create_flat_list(self, ent_list: List[db.Entity], flat: List[db.Entity]):
        """
        Recursively adds all properties contained in entities from ent_list to
        the output list flat. Each element will only be added once to the list.

        TODO: This function will be moved to pylib as it is also needed by the
              high level API.
        """
        for ent in ent_list:
            for p in ent.properties:
                # For lists append each element that is of type Entity to flat:
                if isinstance(p.value, list):
                    for el in p.value:
                        if isinstance(el, db.Entity):
                            if el not in flat:
                                flat.append(el)
                            # TODO: move inside if block?
                            self.create_flat_list([el], flat)
                elif isinstance(p.value, db.Entity):
                    if p.value not in flat:
                        flat.append(p.value)
                    # TODO: move inside if block?
                    self.create_flat_list([p.value], flat)

    def all_references_are_existing_already(self, record: db.Record):
        """
        returns true if all references either have IDs or were checked remotely and not found (i.e.
        they exist in the local cache)
        """
        for p in record.properties:
            # if (is_reference(p)
            # Entity instead of ID and not cached locally
            if (isinstance(p.value, list)):
                for el in p.value:
                    if (isinstance(el, db.Entity) and el.id is None
                            and self.get_identified_record_from_local_cache(el) is None):
                        return False
            if (isinstance(p.value, db.Entity) and p.value.id is None
                    and self.get_identified_record_from_local_cache(p.value) is None):
                # might be checked when reference is resolved
                return False
        return True

    def replace_references_with_cached(self, record: db.Record):
        """
        Replace all references with the versions stored in the cache.

        If the cache version is not identical, raise an error.
        """
        for p in record.properties:
            if (isinstance(p.value, list)):
                lst = []
                for el in p.value:
                    if (isinstance(el, db.Entity) and el.id is None):
                        cached = self.get_identified_record_from_local_cache(
                            el)
                        if cached is None:
                            raise RuntimeError("Not in cache.")
                        if not check_identical(cached, el, True):
                            if isinstance(p.value, db.File):
                                if p.value.path != cached.path:
                                    raise RuntimeError("Not identical.")
                            else:
                                raise RuntimeError("Not identical.")
                        lst.append(cached)
                    else:
                        lst.append(el)
                p.value = lst
            if (isinstance(p.value, db.Entity) and p.value.id is None):
                cached = self.get_identified_record_from_local_cache(p.value)
                if cached is None:
                    raise RuntimeError("Not in cache.")
                if not check_identical(cached, p.value, True):
                    if isinstance(p.value, db.File):
                        if p.value.path != cached.path:
                            raise RuntimeError("Not identical.")
                    else:
                        raise RuntimeError("Not identical.")
                p.value = cached

    def get_identified_record_from_local_cache(self, record: db.Record):
        """
        returns the identifiable if an identifiable with the same values already exists locally
        (Each identifiable that is not found on the remote server, is 'cached' locally to prevent
        that the same identifiable exists twice)
        """
        if self.identifiableAdapter is None:
            raise RuntimeError("Should not happen.")
        identifiable = self.identifiableAdapter.get_identifiable(record)
        if identifiable is None:
            # TODO: check whether the same idea as below works here
            identifiable = record
            # return None

        if identifiable in self.identified_cache:
            return self.identified_cache[identifiable]
        else:
            return None

    def add_identified_record_to_local_cache(self, record: db.Record):
        """
        adds the given identifiable to the local cache

        No identifiable with the same values must exist locally.
        (Each identifiable that is not found on the remote server, is 'cached' locally to prevent
        that the same identifiable exists twice)

        Return False if there is no identifiable for this record and True otherwise.
        """
        if self.identifiableAdapter is None:
            raise RuntimeError("Should not happen.")
        identifiable = self.identifiableAdapter.get_identifiable(record)
        if identifiable is None:
            # TODO: this error report is bad
            #       we need appropriate handling for records without an identifiable
            #       or at least a simple fallback definition if tehre is no identifiable.

            # print(record)
            # raise RuntimeError("No identifiable for record.")

            # TODO: check whether that holds:
            #       if there is no identifiable, for the cache that is the same
            #       as if the complete entity is the identifiable:
            identifiable = record
        self.identified_cache.add(identifiable=identifiable, record=record)

    def copy_attributes(self, fro: db.Entity, to: db.Entity):
        """
        Copy all attributes from one entity to another entity.
        """

        merge_entities(to, fro)

    def split_into_inserts_and_updates(self, ent_list: List[db.Entity]):
        if self.identifiableAdapter is None:
            raise RuntimeError("Should not happen.")
        to_be_inserted: List[db.Entity] = []
        to_be_updated: List[db.Entity] = []
        flat = list(ent_list)
        # assure all entities are direct members TODO Can this be removed at some point?Check only?
        self.create_flat_list(ent_list, flat)

        # TODO: can the following be removed at some point
        for ent in flat:
            if ent.role == "Record" and len(ent.parents) == 0:
                raise RuntimeError("Records must have a parent.")

        resolved_references = True
        # flat contains Entities which could not yet be checked against the remote server
        while resolved_references and len(flat) > 0:
            resolved_references = False

            for i in reversed(range(len(flat))):
                record = flat[i]

                # TODO remove if the exception is never raised
                if (record.id is not None or record in to_be_inserted):
                    raise RuntimeError("This should not be reached since treated elements"
                                       "are removed from the list")
                # Check the local cache first for duplicate
                elif self.get_identified_record_from_local_cache(record) is not None:

                    # This record is a duplicate that can be removed. Make sure we do not lose
                    # information
                    # Update an (local) identified record that will be inserted
                    newrecord = self.get_identified_record_from_local_cache(
                        record)
                    self.copy_attributes(fro=record, to=newrecord)
                    # Bend references to the other object
                    # TODO refactor this
                    for el in flat + to_be_inserted + to_be_updated:
                        for p in el.properties:
                            if isinstance(p.value, list):
                                for index, val in enumerate(p.value):
                                    if val is record:
                                        p.value[index] = newrecord
                            else:
                                if p.value is record:
                                    p.value = newrecord

                    del flat[i]

                # all references need to be IDs that exist on the remote server
                elif self.can_be_checked_externally(record):

                    # Check remotely
                    # TODO: remove deepcopy?
                    identified_record = self.identifiableAdapter.retrieve_identified_record_for_record(
                        deepcopy(record))
                    if identified_record is None:
                        # identifiable does not exist remotely
                        to_be_inserted.append(record)
                        self.add_identified_record_to_local_cache(record)
                        del flat[i]
                    else:
                        # side effect
                        record.id = identified_record.id
                        # On update every property needs to have an ID.
                        # This will be achieved by the function execute_updates_in_list below.
                        # For files this is not enough, we also need to copy over
                        # checksum and size:
                        if isinstance(record, db.File):
                            record._size = identified_record._size
                            record._checksum = identified_record._checksum

                        to_be_updated.append(record)
                        # TODO think this through
                        self.add_identified_record_to_local_cache(record)
                        del flat[i]
                    resolved_references = True

                # e.g. references an identifiable that does not exist remotely
                elif self.all_references_are_existing_already(record):

                    # TODO: (for review)
                    # This was the old version, but also for this case the
                    # check for identifiables has to be done.
                    # to_be_inserted.append(record)
                    # self.add_identified_record_to_local_cache(record)
                    # del flat[i]

                    # TODO: (for review)
                    # If the following replacement is not done, the cache will
                    # be invalid as soon as references are resolved.
                    # replace references by versions from cache:
                    self.replace_references_with_cached(record)

                    identified_record = self.identifiableAdapter.retrieve_identified_record_for_record(
                        deepcopy(record))
                    if identified_record is None:
                        # identifiable does not exist remotely
                        to_be_inserted.append(record)
                        self.add_identified_record_to_local_cache(record)
                        del flat[i]
                    else:
                        # side effect
                        record.id = identified_record.id
                        # On update every property needs to have an ID.
                        # This will be achieved by the function execute_updates_in_list below.

                        to_be_updated.append(record)
                        # TODO think this through
                        self.add_identified_record_to_local_cache(record)
                        del flat[i]

                    resolved_references = True

        if len(flat) > 0:
            raise RuntimeError(
                "Could not resolve all Entity references. Circular Dependency?")

        return to_be_inserted, to_be_updated

    def replace_entities_with_ids(self, rec: db.Record):
        for el in rec.properties:
            if isinstance(el.value, db.Entity):
                if el.value.id is not None:
                    el.value = el.value.id
            elif isinstance(el.value, list):
                for index, val in enumerate(el.value):
                    if isinstance(val, db.Entity):
                        if val.id is not None:
                            el.value[index] = val.id

    @staticmethod
    def remove_unnecessary_updates(target_data: List[db.Record],
                                   identified_records: List[db.Record]):
        """
        checks whether all relevant attributes (especially Property values) are equal

        Returns (in future)
        -------
        update list without unecessary updates

        """
        if len(target_data) != len(identified_records):
            raise RuntimeError("The lists of updates and of identified records need to be of the "
                               "same length!")
        # TODO this can now easily be changed to a function without side effect
        for i in reversed(range(len(target_data))):
            identical = check_identical(target_data[i], identified_records[i])

            if identical:
                del target_data[i]
                continue
            else:
                pass

    @staticmethod
    def execute_parent_updates_in_list(to_be_updated, securityMode, run_id, unique_names):
        """
        Execute the updates of changed parents.

        This method is used before the standard inserts and needed
        because some changes in parents (e.g. of Files) might fail
        if they are not updated first.
        """
        Crawler.set_ids_and_datatype_of_parents_and_properties(to_be_updated)
        parent_updates = db.Container()

        for record in to_be_updated:
            old_entity = Crawler._get_entity_by_id(record.id)

            # Check whether the parents have been changed and add them if missing
            # in the old entity:
            changes_made = False
            for parent in record.parents:
                found = False
                for old_parent in old_entity.parents:
                    if old_parent.id == parent.id:
                        found = True
                        break
                if not found:
                    old_entity.add_parent(id=parent.id)
                    changes_made = True
            if changes_made:
                parent_updates.append(old_entity)
        logger.debug("RecordTypes need to be added to the following entities:")
        logger.debug(parent_updates)
        if len(parent_updates) > 0:
            if securityMode.value > SecurityMode.INSERT.value:
                parent_updates.update(unique=False)
            elif run_id is not None:
                update_cache = UpdateCache()
                update_cache.insert(parent_updates, run_id)
                logger.info("Some entities need to be updated because they are missing a parent "
                            "RecordType. The update was NOT executed due to the chosen security "
                            "mode. This might lead to a failure of inserts that follow.")
                logger.info(parent_updates)

    @staticmethod
    def _get_entity_by_name(name):
        return db.Entity(name=name).retrieve()

    @staticmethod
    def _get_entity_by_id(id):
        return db.Entity(id=id).retrieve()

    @staticmethod
    def execute_inserts_in_list(to_be_inserted, securityMode, run_id: int = None,
                                unique_names=True):
        for record in to_be_inserted:
            for prop in record.properties:
                entity = Crawler._get_entity_by_name(prop.name)
                _resolve_datatype(prop, entity)
        logger.debug("INSERT")
        logger.debug(to_be_inserted)
        if len(to_be_inserted) > 0:
            if securityMode.value > SecurityMode.RETRIEVE.value:
                db.Container().extend(to_be_inserted).insert(unique=unique_names)
            elif run_id is not None:
                update_cache = UpdateCache()
                update_cache.insert(to_be_inserted, run_id, insert=True)

    @staticmethod
    def set_ids_and_datatype_of_parents_and_properties(rec_list):
        for record in rec_list:
            for parent in record.parents:
                if parent.id is None:
                    parent.id = Crawler._get_entity_by_name(parent.name).id
            for prop in record.properties:
                if prop.id is None:
                    entity = Crawler._get_entity_by_name(prop.name)
                    prop.id = entity.id
                    _resolve_datatype(prop, entity)

    @staticmethod
    def execute_updates_in_list(to_be_updated, securityMode, run_id: int = None,
                                unique_names=True):
        Crawler.set_ids_and_datatype_of_parents_and_properties(to_be_updated)
        logger.debug("UPDATE")
        logger.debug(to_be_updated)
        if len(to_be_updated) > 0:
            if securityMode.value > SecurityMode.INSERT.value:
                db.Container().extend(to_be_updated).update(unique=unique_names)
            elif run_id is not None:
                update_cache = UpdateCache()
                update_cache.insert(to_be_updated, run_id)

    def _synchronize(self, target_data: List[db.Record], commit_changes: bool = True,
                     unique_names=True):
        """
        This function applies several stages:
        1) Retrieve identifiables for all records in target_data.
        2) Compare target_data with existing records.
        3) Insert and update records based on the set of identified differences.

        This function makes use of an IdentifiableAdapter which is used to retrieve
        register and retrieve identifiables.

        if commit_changes is True, the changes are synchronized to the CaosDB server.
        For debugging in can be useful to set this to False.

        Return the final to_be_inserted and to_be_updated as tuple.
        """

        if self.identifiableAdapter is None:
            raise RuntimeError("Should not happen.")

        to_be_inserted, to_be_updated = self.split_into_inserts_and_updates(
            target_data)

        # TODO: refactoring of typo
        for el in to_be_updated:
            # all entity objects are replaced by their IDs except for the not yet inserted ones
            self.replace_entities_with_ids(el)

        identified_records = [
            self.identifiableAdapter.retrieve_identified_record_for_record(
                record)
            for record in to_be_updated]
        # remove unnecessary updates from list by comparing the target records to the existing ones
        self.remove_unnecessary_updates(to_be_updated, identified_records)

        if commit_changes:
            self.execute_parent_updates_in_list(to_be_updated, securityMode=self.securityMode,
                                                run_id=self.run_id, unique_names=unique_names)
            self.execute_inserts_in_list(
                to_be_inserted, self.securityMode, self.run_id, unique_names=unique_names)
            self.execute_updates_in_list(
                to_be_updated, self.securityMode, self.run_id, unique_names=unique_names)

        update_cache = UpdateCache()
        pending_inserts = update_cache.get_inserts(self.run_id)
        if pending_inserts:
            Crawler.inform_about_pending_changes(
                pending_inserts, self.run_id, self.crawled_directory)

        pending_updates = update_cache.get_updates(self.run_id)
        if pending_updates:
            Crawler.inform_about_pending_changes(
                pending_updates, self.run_id, self.crawled_directory)

        return (to_be_inserted, to_be_updated)

    @staticmethod
    def inform_about_pending_changes(pending_changes, run_id, path, inserts=False):
        # Sending an Email with a link to a form to authorize updates is
        # only done in SSS mode

        if "SHARED_DIR" in os.environ:
            filename = OldCrawler.save_form(
                [el[3] for el in pending_changes], path, run_id)
            OldCrawler.send_mail([el[3] for el in pending_changes], filename)

        for i, el in enumerate(pending_changes):

            logger.debug(
                """
UNAUTHORIZED UPDATE ({} of {}):
____________________\n""".format(i + 1, len(pending_changes)) + str(el[3]))
        logger.info("There were unauthorized changes (see above). An "
                    "email was sent to the curator.\n"
                    "You can authorize the " +
                    ("inserts" if inserts else "updates")
                    + " by invoking the crawler"
                    " with the run id: {rid}\n".format(rid=run_id))

    @staticmethod
    def debug_build_usage_tree(converter: Converter):
        res: Dict[str, Dict[str, Any]] = {
            converter.name: {
                "usage": ", ".join(converter.metadata["usage"]),
                "subtree": {}
            }
        }

        for subconv in converter.converters:
            d = Crawler.debug_build_usage_tree(subconv)
            k = list(d.keys())
            if len(k) != 1:
                raise RuntimeError(
                    "Unkonwn error during building of usage tree.")
            res[converter.name]["subtree"][k[0]] = d[k[0]]
        return res

    def save_debug_data(self, filename: str):
        paths: Dict[str, Union[dict, list]] = dict()

        def flatten_debug_info(key):
            mod_info = self.debug_metadata[key]
            paths[key] = dict()
            for record_name in mod_info:
                if key == "provenance":
                    paths[key][record_name] = dict()
                    for prop_name in mod_info[record_name]:
                        paths[key][record_name][prop_name] = {
                            "structure_elements_path": "/".join(
                                mod_info[record_name][prop_name][0]),
                            "converters_path": "/".join(
                                mod_info[record_name][prop_name][1])}
                elif key == "usage":
                    paths[key][record_name] = ", ".join(mod_info[record_name])
        for key in ("provenance", "usage"):
            flatten_debug_info(key)

        paths["converters_usage"] = [self.debug_build_usage_tree(
            cv) for cv in self.debug_converters]

        with open(filename, "w") as f:
            f.write(yaml.dump(paths, sort_keys=False))

    def _crawl(self, items: List[StructureElement],
               local_converters: List[Converter],
               generalStore: GeneralStore,
               recordStore: RecordStore,
               structure_elements_path: List[str], converters_path: List[str]):
        """
        Crawl a list of StructureElements and apply any matching converters.

        items: structure_elements (e.g. files and folders on one level on the hierarchy)
        local_converters: locally defined converters for
                            treating structure elements. A locally defined converter could be
                            one that is only valid for a specific subtree of the originally
                            cralwed StructureElement structure.
        generalStore and recordStore: This recursion of the crawl function should only operate on copies of the
                            global stores of the Crawler object.
        """
        for element in items:
            for converter in local_converters:

                # type is something like "matches files", replace isinstance with "type_matches"
                # match function tests regexp for example
                if (converter.typecheck(element) and
                        converter.match(element) is not None):
                    generalStore_copy = generalStore.create_scoped_copy()
                    recordStore_copy = recordStore.create_scoped_copy()

                    # Create an entry for this matched structure element:
                    generalStore_copy[converter.name] = (
                        os.path.join(*(structure_elements_path + [element.get_name()])))

                    # extracts values from structure element and stores them in the
                    # variable store
                    converter.create_values(generalStore_copy, element)

                    keys_modified = converter.create_records(
                        generalStore_copy, recordStore_copy, element)

                    children = converter.create_children(
                        generalStore_copy, element)
                    if self.debug:
                        # add provenance information for each varaible
                        self.debug_tree[str(element)] = (
                            generalStore_copy.get_storage(), recordStore_copy.get_storage())
                        self.debug_metadata["copied"][str(element)] = (
                            generalStore_copy.get_dict_copied(),
                            recordStore_copy.get_dict_copied())
                        self.debug_metadata["usage"][str(element)].add(
                            "/".join(converters_path + [converter.name]))
                        mod_info = self.debug_metadata["provenance"]
                        for record_name, prop_name in keys_modified:
                            # TODO: check
                            internal_id = recordStore_copy.get_internal_id(
                                record_name)
                            record_identifier = record_name + \
                                "_" + str(internal_id)
                            converter.metadata["usage"].add(record_identifier)
                            mod_info[record_identifier][prop_name] = (
                                structure_elements_path + [element.get_name()],
                                converters_path + [converter.name])

                    self._crawl(children, converter.converters,
                                generalStore_copy, recordStore_copy,
                                structure_elements_path + [element.get_name()],
                                converters_path + [converter.name])
        # if the crawler is running out of scope, copy all records in
        # the recordStore, that were created in this scope
        # to the general update container.
        scoped_records = recordStore.get_records_current_scope()
        for record in scoped_records:
            self.target_data.append(record)

        # TODO: the scoped variables should be cleaned up as soon if the variables
        #       are no longer in the current scope. This can be implemented as follows,
        #       but this breaks the test "test_record_structure_generation", because
        #       some debug info is also deleted. This implementation can be used as soon
        #       as the remaining problems with the debug_tree are fixed.
        # Delete the variables that are no longer needed:
        # scoped_names = recordStore.get_names_current_scope()
        # for name in scoped_names:
        #     del recordStore[name]
        #     del generalStore[name]

        return self.target_data


def crawler_main(crawled_directory_path: str,
                 cfood_file_name: str,
                 identifiables_definition_file: str = None,
                 debug: bool = False,
                 provenance_file: str = None,
                 dry_run: bool = False,
                 prefix: str = "",
                 securityMode: int = SecurityMode.UPDATE,
                 unique_names=True,
                 ):
    """

    Parameters
    ----------
    crawled_directory_path : str
        path to be crawled
    cfood_file_name : str
        filename of the cfood to be used
    identifiables_definition_file : str
        filename of an identifiable definition yaml file
    debug : bool
        whether or not to run in debug mode
    provenance_file : str
        provenance information will be stored in a file with given filename
    dry_run : bool
        do not commit any chnages to the server
    prefix : str
        remove the given prefix from file paths
    securityMode : int
        securityMode of Crawler
    unique_names : bool
        whether or not to update or insert entities inspite of name conflicts

    Returns
    -------
    return_value : int
        0 if successful
    """
    crawler = Crawler(debug=debug, securityMode=securityMode)
    crawler.crawl_directory(crawled_directory_path, cfood_file_name)
    if provenance_file is not None:
        crawler.save_debug_data(provenance_file)

    if identifiables_definition_file is not None:

        ident = CaosDBIdentifiableAdapter()
        ident.load_from_yaml_definition(identifiables_definition_file)
        crawler.identifiableAdapter = ident

    if dry_run:
        ins, upd = crawler.synchronize(commit_changes=False)
        inserts = [str(i) for i in ins]
        updates = [str(i) for i in upd]
        with open("dry.yml", "w") as f:
            f.write(yaml.dump({
                "insert": inserts,
                "update": updates}))
    else:
        rtsfinder = dict()
        for elem in crawler.target_data:
            if isinstance(elem, db.File):
                # correct the file path:
                # elem.file = os.path.join(args.path, elem.file)
                if prefix is None:
                    raise RuntimeError(
                        "No prefix set. Prefix must be set if files are used.")
                if elem.path.startswith(prefix):
                    elem.path = elem.path[len(prefix):]
                elem.file = None
                # TODO: as long as the new file backend is not finished
                #       we are using the loadFiles function to insert symlinks.
                #       Therefore, I am setting the files to None here.
                #       Otherwise, the symlinks in the database would be replaced
                #       by uploads of the files which we currently do not want to happen.

            # Check whether all needed RecordTypes exist:
            if len(elem.parents) > 0:
                for parent in elem.parents:
                    if parent.name in rtsfinder:
                        continue

                    rt = db.RecordType(name=parent.name)
                    try:
                        rt.retrieve()
                        rtsfinder[parent.name] = True
                    except db.TransactionError:
                        rtsfinder[parent.name] = False
        notfound = [k for k, v in rtsfinder.items() if not v]
        if len(notfound) > 0:
            raise RuntimeError("Missing RecordTypes: {}".
                               format(", ".join(notfound)))

        crawler.synchronize(commit_changes=True, unique_names=unique_names)
    return 0


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument("cfood_file_name",
                        help="Path name of the cfood yaml file to be used.")
    parser.add_argument("--provenance", required=False,
                        help="Path name of the provenance yaml file. "
                        "This file will only be generated if this option is set.")
    parser.add_argument("--debug", required=False, action="store_true",
                        help="Path name of the cfood yaml file to be used.")
    parser.add_argument("crawled_directory_path",
                        help="The subtree of files below the given path will "
                        "be considered. Use '/' for everything.")
    parser.add_argument("-s", "--security-mode", choices=["retrieve", "insert", "update"],
                        default="retrieve",
                        help="Determines whether entities may only be read from the server, or "
                        "whether inserts or even updates may be done.")
    parser.add_argument("-n", "--dry-run", action="store_true",
                        help="Create two files dry.yml to show"
                        "what would actually be committed without doing the synchronization.")

    # TODO: load identifiables is a dirty implementation currently
    parser.add_argument("-i", "--load-identifiables",
                        help="Load identifiables from the given yaml file.")
    parser.add_argument("-u", "--unique-names",
                        help="Insert or updates entities even if name conflicts exist.")
    parser.add_argument("-p", "--prefix",
                        help="Remove the given prefix from the paths "
                        "of all file objects.")

    return parser.parse_args()


def main():
    args = parse_args()

    conlogger = logging.getLogger("connection")
    conlogger.setLevel(level=logging.ERROR)

    # logging config for local execution
    logger.addHandler(logging.StreamHandler(sys.stdout))
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    sys.exit(crawler_main(
        crawled_directory_path=args.crawled_directory_path,
        cfood_file_name=args.cfood_file_name,
        identifiables_definition_file=args.load_identifiables,
        debug=args.debug,
        provenance_file=args.provenance,
        dry_run=args.dry_run,
        prefix=args.prefix,
        securityMode={"retrieve": SecurityMode.RETRIEVE,
                      "insert": SecurityMode.INSERT,
                      "update": SecurityMode.UPDATE}[args.security_mode],
        unique_names=args.unique_names,
    ))


if __name__ == "__main__":
    main()
