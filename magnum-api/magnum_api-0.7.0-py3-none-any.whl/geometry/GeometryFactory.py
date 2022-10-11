from typing import List, Dict, Union

import pandas as pd
from roxieapi.cadata.CableDatabase import CableDatabase

from magnumapi.geometry.GeometryBuilder import GeometryBuilder, SlottedGeometryBuilder
from magnumapi.geometry.Geometry import Geometry
import pymbse.commons.json_file as json_file
from roxieapi import api


class GeometryFactory:
    """ GeometryFactory implements a factory design pattern and is used to produce:
    - rectangular geometry
    - absolute cos-theta geometry
    - relative cos-theta geometry
    - slotted absolute cos-theta geometry
    - slotted relative cos-theta geometry

    """

    @classmethod
    def init_geometry(cls, geometry_definition: Union[dict, str], cadata: CableDatabase) -> Geometry:
        """
        A class method initializing geometry from a geometry definition. The method supports the following inputs
        - if geometry_definition is a string path
            - if string is a path to a data file
                - a regular geometry is returned
            - if string is a path to a json file
                - read dictionary
                then:
                - either a slotted geometry is returned
                - or a regular geometry is returned
        """
        assert isinstance(geometry_definition, (str, dict)), \
            "Argument geometry_definition has to be either a str or dict"

        # if geometry_definition is a string and ends with .data
        # # return geometry initialized with data
        if isinstance(geometry_definition, str) and geometry_definition.endswith(".data"):
            return cls._init_with_data(geometry_definition, cadata)

        # if geometry is a string and ends with .json
        # # read json as a dict
        if isinstance(geometry_definition, str) and geometry_definition.endswith(".json"):
            geometry_definition = json_file.read(geometry_definition)

        # if the dictionary has keys block_defs, layer_defs, r_aperture
        # #  initialize a slotted geometry
        # else
        # # initialize regular geometry
        if len({"block_defs", "layer_defs", "r_aperture"}.intersection(geometry_definition)) == 3:
            return cls._init_slotted_with_dict(**geometry_definition, cadata=cadata)
        elif len({"block_defs", "layer_defs"}.intersection(geometry_definition)) == 2:
            return cls._init_with_dict(**geometry_definition, cadata=cadata)
        else:
            raise AttributeError("Unsupported combination of input keys in geometry_definition.")

    @classmethod
    def _init_with_dict(cls,
                        block_defs: List[Dict],
                        layer_defs: List[Dict],
                        cadata: CableDatabase,
                        extra_defs=None) -> Geometry:
        """ Class method initializing a Geometry instance from a list of dictionaries with block definition.

        :param block_defs: a list of dictionaries with geometry definition (block definition)
        :param layer_defs: a list of dictionaries with layer definitions
        :param cadata: a CableDatabase instance
        :param extra_defs: an optional dictionary with arbitrary, extra definitions for a geometry
        :return: initialized geometry instance
        """
        return GeometryBuilder() \
            .with_block_defs(block_defs, cadata) \
            .with_layer_defs(layer_defs) \
            .with_extra_defs(extra_defs) \
            .build()

    @classmethod
    def _init_slotted_with_dict(cls,
                                block_defs: List[Dict],
                                layer_defs: List[Dict],
                                cadata: CableDatabase,
                                r_aperture: float,
                                extra_defs=None) -> Geometry:
        """ Class method initializing a Geometry instance from a list of dictionaries with block definition.

        :param block_defs: a list of dictionaries with geometry definition (block definition)
        :param layer_defs: a list of dictionaries with layer definitions
        :param cadata: a CableDatabase instance
        :param r_aperture: aperture radius in mm
        :param extra_defs: an optional dictionary with arbitrary, extra definitions for a geometry
        :return: initialized geometry instance
        """
        return SlottedGeometryBuilder() \
            .with_block_defs(block_defs, cadata) \
            .with_layer_defs(layer_defs) \
            .with_r_aperture(r_aperture) \
            .with_extra_defs(extra_defs) \
            .build()

    @classmethod
    def _init_with_data(cls, data_file_path: str, cadata: CableDatabase) -> Geometry:
        """ Class method initializing a Geometry instance from a DATA ROXIE file.

        :param data_file_path: a path to a json file
        :param cadata: a CableDatabase instance
        :return: initialized geometry instance
        """
        block_df = api.read_bottom_header_table(data_file_path, keyword='BLOCK')
        layer_df = api.read_nested_bottom_header_table(data_file_path, keyword='LAYER')
        return cls._init_with_df(block_df, layer_df, cadata)

    @classmethod
    def _init_with_df(cls, block_df: pd.DataFrame, layer_df, cadata: CableDatabase) -> Geometry:
        """ Class method initializing a Geometry instance from a dataframe with block definition.

        :param block_df: a dataframe with geometry definition (block definition)
        :param layer_df: a dataframe with geometry definition (layer definition)
        :param cadata: a CableDatabase instance
        :return: initialized geometry instance
        """
        return GeometryBuilder() \
            .with_block_df(block_df, cadata) \
            .with_layer_df(layer_df) \
            .build()
