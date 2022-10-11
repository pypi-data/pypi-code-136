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

from jsonschema import validate, ValidationError
import os
import re
import caosdb as db
import json
import warnings
from .utils import has_parent
from .stores import GeneralStore, RecordStore
from .structure_elements import (StructureElement, Directory, File, Dict, JSONFile,
                                 DictIntegerElement, DictBooleanElement,
                                 DictFloatElement, DictDictElement,
                                 TextElement, DictTextElement, DictElement, DictListElement)
from typing import Dict as Dict_t, List, Optional, Tuple, Union
from abc import ABCMeta, abstractmethod
from string import Template
import yaml_header_tools

import pandas as pd

import yaml

# These are special properties which are (currently) treated differently
# by the converters:
SPECIAL_PROPERTIES = ("description", "name", "id", "path",
                      "file", "checksum", "size")


def _only_max(children_with_keys):

    return [max(children_with_keys, key=lambda x: x[1])[0]]


def _only_min(children_with_keys):

    return [min(children_with_keys, key=lambda x: x[1])[0]]


# names of functions that can be used to filter children
FILTER_FUNCTIONS = {
    "only_max": _only_max,
    "only_min": _only_min,
}


def str_to_bool(x):
    if str(x).lower() == "true":
        return True
    elif str(x).lower() == "false":
        return False
    else:
        raise RuntimeError("Should be 'true' or 'false'.")


class ConverterValidationError(Exception):
    """To be raised if contents of an element to be converted are invalid."""

    def __init__(self, msg):
        self.message = msg


def replace_variables(propvalue, values: GeneralStore):
    """
    This function replaces variables in property values (and possibly other locations,
    where the crawler can replace cfood-internal variables).

    This function checks whether the value that is to be replaced is of type db.Entity.
    In this case the entity is returned (note that this is of course only possible, if the
    occurrence of the variable is directly at the beginning of the value and e.g. no string
    concatenation is attempted.

    In any other case the variable substitution is carried out and a new string with the
    replaced variables is returned.
    """
    # Check if the replacement is a single variable containing a record:
    match = re.match(r"^\$(\{)?(?P<varname>[0-9a-zA-Z_]+)(\})?$", propvalue)
    if match is not None:
        varname = match.group("varname")
        if varname in values:
            if values[varname] is None:
                return None
            if isinstance(values[varname], db.Entity):
                return values[varname]

    propvalue_template = Template(propvalue)
    return propvalue_template.safe_substitute(**values.get_storage())


def handle_value(value: Union[dict, str, list], values: GeneralStore):
    """
    determines whether the given value needs to set a property, be added to an existing value (create a list) or
    add as an additional property (multiproperty).

    Variable names (starting with a "$") are replaced by the corresponding value stored in the
    `values` GeneralStore.

    Parameters:
    - value: if str, the value to be interpreted. E.g. "4", "hallo" or "$a" etc.
             if dict, must have keys "value" and "collection_mode". The returned tuple is directly
             created from the corresponding values.
             if list, each element is checked for replacement and the resulting list will be used
             as (list) value for the property
    Returns a tuple:
    - the final value of the property; variable names contained in `values` are replaced.
    - the collection mode (can be single, list or multiproperty)
    """
    # @review Florian Spreckelsen 2022-05-13

    if type(value) == dict:
        if "value" not in value:
            # TODO: how do we handle this case? Just ignore?
            #       or disallow?
            raise NotImplementedError()
        propvalue = value["value"]
        # can be "single", "list" or "multiproperty"
        collection_mode = value["collection_mode"]
    elif type(value) == str:
        propvalue = value
        collection_mode = "single"
        if propvalue.startswith("+"):
            collection_mode = "list"
            propvalue = propvalue[1:]
        elif propvalue.startswith("*"):
            collection_mode = "multiproperty"
            propvalue = propvalue[1:]
    elif type(value) == list:
        # TODO: (for review)
        #       This is a bit dirty right now and needed for
        #       being able to directly set list values. Semantics is, however, a bit
        #       different from the two cases above.
        collection_mode = "single"
        propvalue = value

        # variables replacement:
        propvalue = list()
        for element in value:
            # Do the element-wise replacement only, when its type is string:
            if type(element) == str:
                propvalue.append(replace_variables(element, values))
            else:
                propvalue.append(element)

        return (propvalue, collection_mode)
    else:
        # value is another simple type
        collection_mode = "single"
        propvalue = value
        # Return it immediately, otherwise variable substitution would be done and fail:
        return (propvalue, collection_mode)

    propvalue = replace_variables(propvalue, values)
    return (propvalue, collection_mode)


def create_records(values: GeneralStore,
                   records: RecordStore,
                   def_records: dict):
    # list of keys to identify, which variables have been set by which paths:
    # the items are tuples:
    # 0: record name
    # 1: property name
    keys_modified = []

    for name, record in def_records.items():
        role = "Record"
        # This allows us to create e.g. Files
        if "role" in record:
            role = record["role"]

        # whether the record already exists in the store or not are actually really
        # different distinct cases for treating the setting and updating of variables:
        if name not in records:
            if role == "Record":
                c_record = db.Record()
            elif role == "File":
                c_record = db.File()
            else:
                raise RuntimeError("Role {} not supported.".format(role))
            # add the new record to the record store:
            records[name] = c_record
            # additionally add the new record to the general store:
            values[name] = c_record

        c_record = records[name]

        for key, value in record.items():
            if key == "parents" or key == "role":
                continue

            # Allow replacing variables in keys / names of properties:
            key_template = Template(key)
            key = key_template.safe_substitute(**values.get_storage())

            keys_modified.append((name, key))
            propvalue, collection_mode = handle_value(value, values)

            if key.lower() in SPECIAL_PROPERTIES:
                # e.g. description, name, etc.
                # list mode does not work for them
                if key.lower() == "path" and not propvalue.startswith(os.path.sep):
                    propvalue = os.path.sep + propvalue

                    # Convert relative to absolute paths:
                    propvalue = os.path.normpath(propvalue)
                setattr(c_record, key.lower(), propvalue)
            else:

                if c_record.get_property(key) is None:

                    if collection_mode == "list":
                        c_record.add_property(name=key, value=[propvalue])
                    elif (collection_mode == "multiproperty" or
                          collection_mode == "single"):
                        c_record.add_property(name=key, value=propvalue)
                else:
                    if collection_mode == "list":
                        c_record.get_property(key).value.append(propvalue)
                    elif collection_mode == "multiproperty":
                        c_record.add_property(name=key, value=propvalue)
                    elif collection_mode == "single":
                        c_record.get_property(key).value = propvalue

        # no matter whether the record existed in the record store or not,
        # parents will be added when they aren't present in the record yet:
        if "parents" in record:
            for parent in record["parents"]:
                # Do the variables replacement:
                var_replaced_parent = replace_variables(parent, values)
                if not has_parent(c_record, var_replaced_parent):
                    c_record.add_parent(var_replaced_parent)
        else:
            # add the "fallback" parent only for Records, not for Files:
            if role == "Record":
                # if not has_parent(c_record, name):
                if len(c_record.parents) == 0:
                    c_record.add_parent(name)
    return keys_modified


class Converter(object, metaclass=ABCMeta):
    """
    Converters treat StructureElements contained in the hierarchical sturcture.
    """

    def __init__(self, definition: dict,
                 name: str,
                 converter_registry: dict):
        self.definition = definition
        self.name = name

        # Used to store usage information for debugging:
        self.metadata: Dict_t[str, set[str]] = {
            "usage": set()
        }

        self.converters = []

        if "subtree" in definition:
            for converter_name in definition['subtree']:
                converter_definition = definition["subtree"][converter_name]
                self.converters.append(Converter.converter_factory(
                    converter_definition, converter_name, converter_registry))

    @staticmethod
    def converter_factory(definition: dict,
                          name: str,
                          converter_registry: dict):
        """creates a Converter instance of the appropriate class.

        The `type` key in the `definition` defines the Converter class which is being used.
        """

        if "type" not in definition:
            raise RuntimeError(
                "Type is mandatory for converter entries in CFood definition.")

        if definition["type"] not in converter_registry:
            raise RuntimeError("Unknown Type: {}".format(definition["type"]))

        if "class" not in converter_registry[definition["type"]]:
            raise RuntimeError("Converter class not loaded correctly.")

        # instatiates an object of the required class, e.g. DirectoryConverter(definition, name)
        converter = converter_registry[definition["type"]]["class"](definition, name,
                                                                    converter_registry)

        return converter

    def create_values(self,
                      values: GeneralStore,
                      element: StructureElement):
        """
        Extract information from the structure element and store them as values in the
        general store.

        values: The GeneralStore to store values in.
        element: The StructureElement to extract values from.
        """
        m = self.match(element)
        if m is None:
            # this should never happen as the condition was checked before already
            raise RuntimeError("Condition does not match.")
        values.update(m)

    @abstractmethod
    def create_children(self, values: GeneralStore,
                        element: StructureElement):
        pass

    def create_records(self, values: GeneralStore,
                       records: RecordStore,
                       element: StructureElement):

        if "records" not in self.definition:
            return []

        return create_records(values,
                              records,
                              self.definition["records"])

    def filter_children(self, children_with_strings:
                        List[Tuple[StructureElement, str]], expr: str,
                        group: str, rule: str):
        """Filter children according to regexp `expr` and `rule`."""

        if rule not in FILTER_FUNCTIONS:
            raise RuntimeError(
                f"{rule} is not a known filter rule. Only {list(FILTER_FUNCTIONS.keys())} are implemented."
            )

        to_be_filtered = []
        unmatched_children = []

        for (child, name) in children_with_strings:

            m = re.match(expr, name)
            if m is None:
                unmatched_children.append(child)
            else:
                to_be_filtered.append((child, m.groupdict()[group]))

        filtered_children = FILTER_FUNCTIONS[rule](to_be_filtered)

        return filtered_children+unmatched_children

    @abstractmethod
    def typecheck(self, element: StructureElement):
        pass

    @abstractmethod
    def match(self, element: StructureElement) -> Optional[dict]:
        pass


class DirectoryConverter(Converter):

    def __init__(self, definition: dict, name: str,
                 converter_registry: dict):
        """
        Initialize a new directory converter.
        """
        super().__init__(definition, name, converter_registry)

    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        if not isinstance(element, Directory):
            raise RuntimeError(
                "Directory converters can only create children from directories.")

        children = self.create_children_from_directory(element)

        if "filter" in self.definition:

            tuple_list = [(c, c.name) for c in children]

            return self.filter_children(tuple_list, **self.definition["filter"])

        return children

    def typecheck(self, element: StructureElement):
        return isinstance(element, Directory)

    def match(self, element: StructureElement):
        if not isinstance(element, Directory):
            raise RuntimeError("Element must be a directory.")
        m = re.match(self.definition["match"], element.name)
        if m is None:
            return None
        return m.groupdict()

    @staticmethod
    def create_children_from_directory(element: Directory):
        """
        Creates a list of files (of type File) and directories (of type Directory) for a
        given directory. No recursion.

        element: A directory (of type Directory) which will be traversed.
        """
        children: List[StructureElement] = []

        for name in sorted(os.listdir(element.path)):
            path = os.path.join(element.path, name)

            if os.path.isdir(path):
                children.append(Directory(name, path))
            elif os.path.isfile(path):
                children.append(File(name, path))

        return children


class SimpleFileConverter(Converter):
    """
    Just a file, ignore the contents.
    """

    def typecheck(self, element: StructureElement):
        return isinstance(element, File)

    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        return list()

    def match(self, element: StructureElement):
        if not isinstance(element, File):
            raise RuntimeError("Element must be a file.")
        m = re.match(self.definition["match"], element.name)
        if m is None:
            return None
        return m.groupdict()


class MarkdownFileConverter(Converter):
    def __init__(self, definition: dict, name: str,
                 converter_registry: dict):
        """
        Initialize a new directory converter.
        """
        super().__init__(definition, name, converter_registry)

    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        if not isinstance(element, File):
            raise RuntimeError("A markdown file is needed to create children.")

        header = yaml_header_tools.get_header_from_file(
            element.path, clean=False)
        children: List[StructureElement] = []

        for name, entry in header.items():
            if type(entry) == list:
                children.append(DictListElement(name, entry))
            elif type(entry) == str:
                children.append(DictTextElement(name, entry))
            else:
                raise RuntimeError(
                    "Header entry {} has incompatible type.".format(name))
        return children

    def typecheck(self, element: StructureElement):
        return isinstance(element, File)

    def match(self, element: StructureElement):
        if not isinstance(element, File):
            raise RuntimeError("Element must be a file.")
        m = re.match(self.definition["match"], element.name)
        if m is None:
            return None
        try:
            yaml_header_tools.get_header_from_file(element.path)
        except yaml_header_tools.NoValidHeader:
            # TODO(salexan): Raise a validation error instead of just not
            # matching silently.
            return None
        return m.groupdict()


class DictConverter(Converter):
    # TODO use Dict as typecheck?
    def create_children(self, generalStore: GeneralStore, element: StructureElement):
        if not self.typecheck(element):
            raise RuntimeError("A dict is needed to create children")

        return self._create_children_from_dict(element.value)

    def _create_children_from_dict(self, data):
        children = []

        for name, value in data.items():
            if type(value) == list:
                children.append(DictListElement(name, value))
            elif type(value) == str:
                children.append(DictTextElement(name, value))
            elif type(value) == dict:
                children.append(DictDictElement(name, value))
            elif type(value) == int:
                children.append(DictIntegerElement(name, value))
            elif type(value) == bool:
                children.append(DictBooleanElement(name, value))
            elif type(value) == float:
                children.append(DictFloatElement(name, value))
            elif type(value) == type(None):
                continue
            else:
                children.append(DictElement(name, value))
                warnings.warn(f"The value in the dict for key:{name} has an unknown type. "
                              "The fallback type DictElement is used.")

        return children

    # TODO use Dict as typecheck?
    def typecheck(self, element: StructureElement):
        return isinstance(element, Dict)

    def match(self, element: StructureElement):
        """
        Allways matches if the element has the right type.
        """
        if not isinstance(element, Dict):
            raise RuntimeError("Element must be a DictElement.")
        return {}


# TODO: difference to SimpleFileConverter? Do we need both?
class FileConverter(Converter):
    def typecheck(self, element: StructureElement):
        return isinstance(element, File)

    def match(self, element: StructureElement):
        if not self.typecheck(element):
            raise RuntimeError("Element must be a file")
        m = re.match(self.definition["match"], element.name)
        if m is None:
            return None
        return m.groupdict()

    def create_children(self, generalStore: GeneralStore, element: StructureElement):
        return []


class JSONFileConverter(DictConverter):
    def typecheck(self, element: StructureElement):
        return isinstance(element, File)

    def match(self, element: StructureElement):
        if not self.typecheck(element):
            raise RuntimeError("Element must be a file")
        m = re.match(self.definition["match"], element.name)
        if m is None:
            return None
        return m.groupdict()

    def create_children(self, generalStore: GeneralStore, element: StructureElement):
        if not self.typecheck(element):
            raise RuntimeError("A JSON file is needed to create children")
        # TODO: either add explicit time check for File structure element here,
        #       or add a comment to suppress mypy type warning.
        with open(element.path, 'r') as json_file:
            json_data = json.load(json_file)
        if not isinstance(json_data, dict):
            raise NotImplementedError("JSON file must contain a dict")
        if "validate" in self.definition and self.definition["validate"]:
            if isinstance(self.definition["validate"], dict):
                schema = self.definition["validate"]
            elif isinstance(self.definition["validate"], str):

                with open(self.definition["validate"], 'r') as json_file:
                    schema = json.load(json_file)
            else:
                raise ValueError("The value of 'validate' has to be a string describing the path "
                                 "to the json schema file (relative to the cfood yml)  "
                                 "or a dict containing the schema.")
            # Validate the json content
            try:
                validate(instance=json_data, schema=schema)
            except ValidationError as err:
                raise ConverterValidationError(
                    f"Couldn't validate {json_data}:\n{err.message}")

        return self._create_children_from_dict(json_data)


class _AbstractDictElementConverter(Converter):

    def create_children(self, generalStore: GeneralStore, element: StructureElement):
        return []

    def typecheck(self, element: StructureElement):
        return True

    def match(self, element: StructureElement):
        """
        Try to match the given structure element.

        If it does not match, return None.

        Else return a dictionary containing the variables from the matched regexp
        as key value pairs.
        """
        if not self.typecheck(element):
            raise RuntimeError(
                f"Element has an invalid type: {type(element)}.")
        m1 = re.match(self.definition["match_name"], element.name)
        if m1 is None:
            return None
        m2 = re.match(self.definition["match_value"], str(element.value))
        if m2 is None:
            return None
        values = dict()
        values.update(m1.groupdict())
        values.update(m2.groupdict())
        return values


class DictBooleanElementConverter(_AbstractDictElementConverter):
    def typecheck(self, element: StructureElement):
        return isinstance(element, DictBooleanElement)


class DictFloatElementConverter(_AbstractDictElementConverter):
    def typecheck(self, element: StructureElement):
        return isinstance(element, DictFloatElement)


class DictTextElementConverter(_AbstractDictElementConverter):
    def typecheck(self, element: StructureElement):
        return isinstance(element, DictTextElement)


class DictIntegerElementConverter(_AbstractDictElementConverter):
    def typecheck(self, element: StructureElement):
        return isinstance(element, DictIntegerElement)


class DictListElementConverter(Converter):
    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        if not isinstance(element, DictListElement):
            raise RuntimeError(
                "This converter can only process DictListElements.")
        children = []
        for index, list_element in enumerate(element.value):
            # TODO(fspreck): Refactor this and merge with DictXXXElements maybe?
            if isinstance(list_element, str):
                children.append(TextElement(str(index), list_element))
            elif isinstance(list_element, dict):
                children.append(Dict(str(index), list_element))
            else:
                raise NotImplementedError(
                    f"Unkown type {type(list_element)} in list element {list_element}.")
        return children

    def typecheck(self, element: StructureElement):
        return isinstance(element, DictListElement)

    def match(self, element: StructureElement):
        if not isinstance(element, DictListElement):
            raise RuntimeError("Element must be a DictListElement.")
        m = re.match(self.definition["match_name"], element.name)
        if m is None:
            return None
        if "match" in self.definition:
            raise NotImplementedError(
                "Match is not implemented for DictListElement.")
        return m.groupdict()


class DictDictElementConverter(DictConverter):
    def create_children(self, generalStore: GeneralStore, element: StructureElement):
        if not self.typecheck(element):
            raise RuntimeError("A dict is needed to create children")

        return self._create_children_from_dict(element.value)

    def typecheck(self, element: StructureElement):
        return isinstance(element, DictDictElement)

    def match(self, element: StructureElement):
        if not self.typecheck(element):
            raise RuntimeError("Element must be a DictDictElement.")
        m = re.match(self.definition["match_name"], element.name)
        if m is None:
            return None
        if "match" in self.definition:
            raise NotImplementedError(
                "Match is not implemented for DictDictElement.")
        return m.groupdict()


class TextElementConverter(Converter):
    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        return []

    def typecheck(self, element: StructureElement):
        return isinstance(element, TextElement)

    def match(self, element: StructureElement):
        if not isinstance(element, TextElement):
            raise RuntimeError("Element must be a TextElement.")
        m = re.match(self.definition["match"], element.value)
        if m is None:
            return None
        return m.groupdict()


class TableConverter(Converter):
    """
    This converter reads tables in different formats line by line and
    allows matching the corresponding rows.

    The subtree generated by the table converter consists of DictDictElements, each being
    a row. The corresponding header elements will become the dictionary keys.

    The rows can be matched using a DictDictElementConverter.
    """
    @abstractmethod
    def get_options(self):
        """
        This method needs to be overwritten by the specific table converter to provide
        information about the possible options.
        """
        pass

    def _get_options(self, possible_options):
        option_dict = dict()
        for opt_name, opt_conversion in possible_options:
            if opt_name in self.definition:
                el = self.definition[opt_name]
                # The option can often either be a single value or a list of values.
                # In the latter case each element of the list will be converted to the defined type.
                if isinstance(el, list):
                    option_dict[opt_name] = [
                        opt_conversion(el_el) for el_el in el]
                else:
                    option_dict[opt_name] = opt_conversion(el)
        return option_dict

    def typecheck(self, element: StructureElement):
        return isinstance(element, File)

    def match(self, element: StructureElement):
        if not isinstance(element, File):
            raise RuntimeError("Element must be a File.")
        m = re.match(self.definition["match"], element.name)
        if m is None:
            return None
        return m.groupdict()


class XLSXTableConverter(TableConverter):
    def get_options(self):
        return self._get_options([
            ("sheet_name", str),
            ("header", int),
            ("names", str),
            ("index_col", int),
            ("usecols", int),
            ("true_values", str),
            ("false_values", str),
            ("na_values", str),
            ("skiprows", int),
            ("nrows", int),
            ("keep_default_na", str_to_bool), ]
        )

    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        if not isinstance(element, File):
            raise RuntimeError("Element must be a File.")
        table = pd.read_excel(element.path, **self.get_options())
        child_elements = list()
        for index, row in table.iterrows():
            child_elements.append(
                DictDictElement(str(index), row.to_dict()))
        return child_elements


class CSVTableConverter(TableConverter):
    def get_options(self):
        return self._get_options([
            ("sep", str),
            ("delimiter", str),
            ("header", int),
            ("names", str),
            ("index_col", int),
            ("usecols", int),
            ("true_values", str),
            ("false_values", str),
            ("na_values", str),
            ("skiprows", int),
            ("nrows", int),
            ("keep_default_na", str_to_bool), ])

    def create_children(self, generalStore: GeneralStore,
                        element: StructureElement):
        if not isinstance(element, File):
            raise RuntimeError("Element must be a File.")
        table = pd.read_csv(element.path, **self.get_options())
        child_elements = list()
        for index, row in table.iterrows():
            child_elements.append(
                DictDictElement(str(index), row.to_dict()))
        return child_elements
