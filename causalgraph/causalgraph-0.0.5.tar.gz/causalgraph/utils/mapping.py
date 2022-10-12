#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

""" Contains functionalities to map a cg graph to and from a dictionary.
"""

# general imports
import owlready2
# causalgraph imports
from causalgraph.utils.logging_utils import init_logger
from causalgraph.utils.owlready2_utils import get_entity_by_name
from causalgraph.utils.owlready2_utils import create_individual_of_type
from causalgraph.utils.owlready2_utils import validate_prop_for_type
from causalgraph.utils.owlready2_utils import validate_data_type_for_property
# Global declearation of the default utils_logger
mapping_logger = init_logger("mapping")


def mapping_dictionary(invert= False) -> dict:
    """Returns a dictionary that maps from cg property names to desired names in the dictionary

    :param invert: if True returns the inverted dictionary
    :type invert: bool, optional
    :return: Dict with desired key names for mapping between property_name and name_in_dict
    :rtype: dict
    """
    mapping = {
        "type": "type",
        "created": "created",
        "hasCausalConnection": "causal_connection",
        "hasCause": "cause",
        "hasCreator": "creator",
        "hasEffect": "effect",
        "isAffectedBy": "affected_by",
        "isCausedBy": "caused_by",
        "hasConfidence": "confidence",
        "hasTimeLag": "time_lag_s",
        "comment": "comment"
        }
    if invert is True:
        return {dict_name: cg_name for cg_name, dict_name in mapping.items()}
    return mapping


### Functions to create dictionary representations of cg individuals/ graphs ###
def all_individuals_to_dict(store: owlready2.World, mapping_dict: dict=mapping_dictionary()) -> dict:
    """Creates and returns a dictionary with all individuals of the graph as keys and all of
    their properties as values. This method iterates over all individuals and appends the
    return value from single_individual_to_dict to a single dictionary.

    :param store: Store of the Graph
    :type store: owlready2.World
    :param mapping_dict: Maps cg properties to properties in the prop_dict
    :type mapping_dict: dict
    :return: Dict with all individuals of the graph as key and all of their properties as
    values, similar to the json format.
    :rtype: dict
    """
    # Create dictionary of the whole graph
    dict_graph = {}
    individuals = list(store.individuals())
    for individual in individuals:
        # append the dict for single individuals to the dict of the whole graph
        dict_single_individual = single_individual_to_dict(individual.name, store, mapping_dict)
        if len(dict_single_individual) > 0:
            dict_graph[individual.name] = dict_single_individual
    return dict_graph


def single_individual_to_dict(individual_name: str, store: owlready2.World, mapping_dict: dict=mapping_dictionary()) -> dict:
    """Creates and returns a dictionary containing all the properties of an individual

    :param individual_name: Name of an individual in the cg graph.
    :type individual_name: str
    :param store: Store of the graph
    :type store: owlready2.World
    :param mapping_dict: Maps cg properties to properties in the prop_dict
    :type mapping_dict: dict
    :return: Dictionary containing all properties of the individual
    :rtype: dict
    """
    # Check if instance exists
    individual = get_entity_by_name(individual_name, store, logger=mapping_logger)
    if individual is None:
        mapping_logger.error(f"Converting properties to dict for {individual_name} failed. " +
                              "There is no such individual.")
        return {}
    # Get the type(s) of the individual
    types_with_prefix = individual.is_a
    types = [type.name for type in types_with_prefix]
    # Init the dictionary for the individual
    if len(types) == 1:
        node_prop_dict = {'type': types[0]}
    else:
        node_prop_dict = {'type': types}
    # Add properties to the dictionary
    return _add_properties_to_dict(individual, node_prop_dict, mapping_dict)


def _add_properties_to_dict(individual: object, prop_dict:dict, mapping_dict: dict=mapping_dictionary()) -> dict:
    """Fills the property dictionary with the properties of the individual

    :param individual: cg individual (CausalNode, CausalEdge, ...)
    :type individual: object
    :param prop_dict: Dictionary where the properties of the individual are written to
    :type prop_dict: dict
    :param mapping_dict: Maps cg properties to properties in the prop_dict
    :type mapping_dict: dict, optional
    :return: Updated property dictionary
    :rtype: dict
    """
    # Iteratively fill the property dictionary
    for prop in individual.get_properties():
        # validate that the property is in the mapping_dict
        if prop.name not in mapping_dict.keys():
            raise ValueError(f'{prop.name} is not a valid property since it is not contained in the mapping_dict!')
        # get the value of the property
        prop_value = getattr(individual, prop.name)
        try: # for lists of individuals get their names
            extracted_values = [i.name for i in prop_value]
        except: # otherwise just get the value
            extracted_values = prop_value
        # get property name for the dictionary representation and insert
        translated_prop_name = mapping_dict[prop.name]
        prop_dict[translated_prop_name] = extracted_values
    return prop_dict


### Functions to update cg individuals/ graphs from a dictionary ###
def update_graph_from_dict(store: owlready2.World, graph_dict: dict):
    """This method creates or updates all individuals in the Graph from a dictionary representation of an entire graph.

    :param store: Store of the graph G that should be updated
    :type store: owlready2.World
    :param graph_dict: Dictionary representation of the updated graph
    :type graph_dict: dict
    """
    # only update the graph if all the properties in the dictionary are allowed for each individual
    for individual in graph_dict:
        _validate_dictionary(individual, graph_dict[individual], store)

    individual_name = None
    individual_sub_dict = None
    # Iterate over all individuals in the graph_dict and create new individuals
    # or update their properties
    for individual in graph_dict:
        # Current individual with its individual_dict
        individual_name = individual
        individual_sub_dict = graph_dict[individual]
        # Create or update current individual. Will possibly be called recursively
        # within update_individual_from_dict
        update_individual_from_dict(individual_name,
                                    store=store,
                                    individual_dict=individual_sub_dict,
                                    graph_dict=graph_dict,
                                    check_properties=False)


def update_individual_from_dict(individual_name: str,
                                store: owlready2.World,
                                individual_dict: dict,
                                graph_dict: dict,
                                check_properties= True) -> bool:
    """This method creates or updates an individual based on its parsed property dictionary.
    It is necessary to parse the dict for the whole graph/batch, because we also need the
    information of other individuals that have to be created while processing the current
    individual. This will be done by calling this method recursively.

    :param individual_name: String containing the name of the individual.
    :type individual_name: str
    :param store: Store of the current Graph
    :type store: owlready2.World
    :param individual_dict: Dictionary with the properties of the current individual.
    :type individual_dict: dict
    :param graph_dict: Dictionary with the properties and names of all individuals for
    the current processing batch.
    :type graph_dict: dict
    :param check_properties: If True, checks if the individual is allowewd to have the
    properties given in the dictionary
    :type check_properties: bool
    """
    # Invert mapping_dictionary() for easy property extraction
    inv_mapping_dict = mapping_dictionary(invert=True)
    # Get current individual type (CausalEdge, CausalNode or Creator)
    individual_type = individual_dict['type']
    # Validate that the individual is allowed to have the given properties
    if check_properties is True:
        _validate_dictionary(individual_name, individual_dict, store)

    # Update the property dictionary
    individual_prop_dict = {}
    for prop, value in individual_dict.items():
        prop_name = inv_mapping_dict[prop] # Get the cg name of the property
        # Add data properties (e.g. hasTimeLag or hasConfidence) to the property dictionary
        if is_object_property(prop_name) is False and prop_name != 'type':
            if prop == 'comment':
                value = list(value)
            individual_prop_dict[prop_name] = value
        # Add object properties (e.g. hasCause or hasEffect) to the property dictionary
        if is_object_property(prop_name) is True:
            object_names = value
            individual_prop_dict = _add_object_properties(individual_prop_dict, prop_name, object_names, graph_dict, store)
    # Create new individual
    if isinstance(individual_type, str):
        new_indi_name = create_individual_of_type(individual_type, store, individual_name, **individual_prop_dict)
    if isinstance(individual_type, list):
        new_indi_name = create_individual_of_type(individual_type[0], store, individual_name, **individual_prop_dict)
        new_individual = get_entity_by_name(new_indi_name, store, suppress_warn=True)
        new_individual.is_a = [get_entity_by_name(class_name, store, suppress_warn=True)
                                for class_name in individual_type]
    if new_indi_name is None:
        mapping_logger.error("Creating individuals or updating properties for existing individual" +
                             "hasn't been successful.")
        return False
    # Persist changes
    store.world.save()
    mapping_logger.info("Creating individuals or updating properties for existing individual" +
                        "has been successful.")
    return True


def _add_object_properties( individual_prop_dict: dict,
                            prop_name: str,
                            object_names: list,
                            graph_dict: dict,
                            store: owlready2.World) -> dict:
    """This method handles properties whose values are lists of entities like Node1: hasCreator=
    ['Creator1', 'Creator2']. The method is given the list of entities and inserts the updated
    information in the property dictionary of the individual.

    :param individual_prop_dict: Dictionary that will be filled with the updated property values
    of the individual
    :type individual_prop_dict: dict
    :param prop_name: Name of the current property like 'hasCreator'
    :type prop_name: str
    :param object_names: List of entity names that should be inserted in the property dictionary
    :type object_names: list
    :param graph_dict: Mapping dictionary for mapping properties, defaults to mapping_dict()
    :type graph_dict: dict
    :param store: Store of the current Graph
    :type store: owlready2.World
    :return: Updated property dictionary of the individual
    :rtype: dict
    """
    # Iterate over all objects in the list
    for object_name in object_names:
        # Check if the object exists
        obj = get_entity_by_name(object_name, store, suppress_warn=True)
        # If the object does not exist there are two options
        # OPTION 1: for properties like 'hasCreator': do nothing because if the property 'created'
        # of the Creator is updated, this property will be updated automatically
        # OPTION 2: for properties like 'hasCause': if the object does not exist (object is None)
        # and the properties won't be updated automatically later on, we need to create the object
        if obj is None and prop_name in ['created', 'hasCause', 'hasEffect']:
            object_dict = graph_dict[object_name]
            update_individual_from_dict(object_name, store, object_dict, graph_dict)
            # now try again if object exists
            obj = get_entity_by_name(object_name, store)
        # If the object exists: Update the property dictionary
        if obj is not None:
            individual_prop_dict.setdefault(prop_name, []).append(obj)
    # return the updated property dictionary
    return individual_prop_dict


def _validate_dictionary(individual_name: str, individual_dict: dict, store: owlready2.World):
    """Checks if all the properties in the individual_dict are valid for the individual e.g.
    Nodes are not allowed to have the property hasConfidence.

    :param individual_name: Name of the individual
    :type individual_name: str
    :param individual_dict: Dictionary containing the properties of the individual
    :type individual_dict: dict
    :param store: Store of the current Graph.
    :type store: owlready2.World
    :raises ValueError: If the property is not valid for the individual
    :return: True if all properties are valid for the individual
    :rtype: bool
    """
    inv_mapping_dict = mapping_dictionary(invert= True)
    individual_type = individual_dict['type']

    for prop, value in individual_dict.items():
        # Validate that the individual is allowed to have the given property
        cg_prop = inv_mapping_dict[prop]
        property_allowed = validate_prop_for_type(individual_type, cg_prop, store, mapping_logger)
        if property_allowed is False:
            raise ValueError(f"The property '{cg_prop}' is not allowed for '{individual_name}' " +
                             f"of type '{individual_type}'!")
        # Validate that the value of the property has the right data type
        data_type_allowed = validate_data_type_for_property(prop, value, mapping_logger)
        if data_type_allowed is False:
            raise ValueError(f"The value {value} does not have the right data type for " +
                             f"property {prop}!")
    # Return True if all properties and data types are correct for the individual
    return True


def is_object_property(property_type: str):
    """Checks if the parsed property type is an object or data property. Properties like hasCause or
    hasEffect are object properties since they are lists of cg individuals while properties like
    hasTimeLag and hasConfidence are data properties.

    :param property_type: String containing the property type ("hasCause", "hasConfidence" ...)
    :type property_type: str
    :return: True or False
    :rtype: boolean
    """
    allowed_props = ["hasCause", "hasCreator", "hasEffect", "isAffectedBy", "isCausedBy", "created"]
    return property_type in allowed_props
