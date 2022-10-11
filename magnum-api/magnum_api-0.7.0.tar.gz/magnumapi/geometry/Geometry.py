from __future__ import annotations

import json
import warnings
from copy import deepcopy
from typing import List, Union
from itertools import chain

import numpy as np
import pandas as pd

from magnumapi.geometry import geometry_symmetries
from magnumapi.geometry.GeometryPlot import GeometryPlot
from magnumapi.geometry.blocks.RectangularBlock import RectangularBlock
from magnumapi.geometry.primitives.Line import Line
from magnumapi.geometry.primitives.Area import Area
from magnumapi.geometry.definitions.LayerDefinition import LayerDefinition, SlottedLayerDefinition
from magnumapi.geometry.definitions.RelativeCosThetaBlockDefinition import RelativeCosThetaBlockDefinition
from magnumapi.geometry.definitions.AbsoluteCosThetaBlockDefinition import AbsoluteCosThetaBlockDefinition
from magnumapi.geometry.blocks.Block import Block
from magnumapi.geometry.blocks.CosThetaBlock import RelativeCosThetaBlock, HomogenizedCosThetaBlock, CosThetaBlock, \
    AbsoluteCosThetaBlock


class Geometry:
    """ Geometry class providing a skeleton for all geometry types (CosTheta, Rectangular, etc.).

    """

    def __init__(self,
                 blocks: List[Union[AbsoluteCosThetaBlock, RectangularBlock,
                                    HomogenizedCosThetaBlock, RelativeCosThetaBlock]],
                 layer_defs: List[Union[LayerDefinition, SlottedLayerDefinition]],
                 extra_defs=None
                 ) -> None:
        """ Constructor of a Geometry class

        :param blocks: a list of instances of Block class implementations (e.g., RectangularBlock, CosThetaBlock, etc.)
        :param layer_defs: a list of layer definitions indicating symmetry type,
        and a list of blocks belonging to a layer
        :param extra_defs: an optional dictionary with arbitrary, extra definitions for a geometry
        """
        _check_input_consistency(blocks, layer_defs)
        self._blocks = blocks
        self.layer_defs = layer_defs
        self.extra_defs = {} if extra_defs is None else extra_defs

    @property
    def block_no_to_index(self) -> dict:
        return {block.block_def.no: index for (index, block) in enumerate(self._blocks)}

    @property
    def blocks(self):
        layer_defs_str = json.dumps(self.layer_defs, default=lambda o: o.__dict__)
        n_blocks = self._calc_no_defined_blocks()
        is_block_def_changed = [block._invariant_cache != block.hash_as_str + layer_defs_str
                                for block in self._blocks[:n_blocks]]
        if any(is_block_def_changed):
            self._blocks = self._blocks[:n_blocks]
            self._build_block_areas()
            self._blocks += geometry_symmetries.build_symmetric_block_areas(self)
        return self._blocks

    def _calc_no_defined_blocks(self):
        return sum([len(layer_def.blocks) for layer_def in self.layer_defs])

    def _build_block_areas(self) -> None:
        """
        Method building all blocks for a given geometry definition
        """
        for block in self._blocks:
            # for an absolute geometry, for each block individually check
            # if a block and layer string changed - build block areas again
            # if so, empty block areas
            #        build block areas
            layer_defs_str = json.dumps(self.layer_defs, default=lambda o: o.__dict__)
            if block._invariant_cache != block.hash_as_str + layer_defs_str:
                block.empty_areas()
                block.build_areas()
                block._invariant_cache = block.hash_as_str + layer_defs_str

    def empty_block_areas(self):
        for block in self.blocks:
            block.empty_areas()

    def compute_surface(self) -> float:
        """ Method computing surface of a geometry as sum of all block surfaces

        :return: a surface in mm^2
        """
        return sum([block.compute_surface() for block in self.blocks])

    def compute_surface_cu(self) -> float:
        """ Method computing copper surface of a block as S = ns * S_strand_cu,
        where S_strand_cu = f_cu * pi * d_strand^2 / 4

        :return: a copper surface of a block in mm^2
        """
        return sum([block.compute_surface_cu() for block in self.blocks])

    def compute_surface_nocu(self) -> float:
        """ Method computing copper surface of a block as S = ns * S_strand_nocu,
        where S_strand_nocu = f_nocu * pi * d_strand^2 / 4

        :return: a non-copper surface of a block in mm^2
        """
        return sum([block.compute_surface_nocu() for block in self.blocks])

    def get_min_max_xy_per_layer(self) -> list:
        """
        Method extracting min/max x/y position of insulated cable coordinates per each layer

        :return: an nx4 list of lists, where n is the number of layers;
                 entries of the inner list are min_x, max_x, min_y, max_y
        """
        MIN_X_COL = 0
        MAX_X_COL = 1
        MIN_Y_COL = 2
        MAX_Y_COL = 3

        # Take updated blocks once to avoid recheck
        blocks = self.blocks

        min_max_xys = []
        block_no_to_index = self.create_block_no_to_index()
        for layer_def in self.layer_defs:
            min_max_xy_per_layer = []
            for block_index in layer_def.blocks:
                index_in_blocks = block_no_to_index[block_index]
                block = blocks[index_in_blocks]
                min_max_xy_per_layer.append(block.get_min_max_xy())

            min_max_xy_per_layer = np.array(min_max_xy_per_layer)
            min_max_xys.append([min_max_xy_per_layer[:, MIN_X_COL].min(),
                                min_max_xy_per_layer[:, MAX_X_COL].max(),
                                min_max_xy_per_layer[:, MIN_Y_COL].min(),
                                min_max_xy_per_layer[:, MAX_Y_COL].min()])

        return min_max_xys

    def to_block_df(self) -> pd.DataFrame:
        """ Method concatenates row definition of each block into a ROXIE-compatible dataframe

        :return: a concatenated dataframe with ROXIE block definition for a geometry instance
        """
        n_blocks = self._calc_no_defined_blocks()
        return pd.concat([block.to_block_df() for block in self.blocks[:n_blocks]], axis=0).reset_index(drop=True)

    def to_layer_df(self) -> pd.DataFrame:
        return pd.DataFrame([layer_def.to_roxie_dict() for layer_def in self.layer_defs])

    def to_dict(self) -> dict:
        """ Method returning an absolute geometry definition (block definitions and layer definitions) as a dictionary.

        :return: a dictionary with two keys: block_defs and layer_defs
        """
        # Take updated blocks once to avoid recheck
        blocks = self.blocks

        block_defs = []
        block_no_to_index = self.create_block_no_to_index()
        for layer_def in self.layer_defs:
            for block_index in layer_def.blocks:
                index_in_blocks = block_no_to_index[block_index]
                block_defs.append(blocks[index_in_blocks].to_abs_dict())

        layer_defs = [layer_def.__dict__ for layer_def in self.layer_defs]

        return self.init_geometry_dict(block_defs, layer_defs)

    def create_block_no_to_index(self):
        n_blocks = self._calc_no_defined_blocks()
        return {block.block_def.no: index for (index, block) in enumerate(self._blocks[:n_blocks])}

    def init_geometry_dict(self, block_defs, layer_defs):
        return {'block_defs': block_defs, 'layer_defs': layer_defs, "extra_defs": self.extra_defs}

    def to_df(self) -> pd.DataFrame:
        """ Method concatenating dataframes with area coordinates for each block

        :return: a concatenated dataframe with area coordinates
        """
        n_blocks = self._calc_no_defined_blocks()
        return pd.concat([block.to_df() for block in self.blocks[:n_blocks]], axis=0).reset_index(drop=True)

    def plot_blocks(self, figsize=(10, 10), is_grid=True, xlim=(0, 80), ylim=(0, 80)) -> None:
        GeometryPlot.plot_blocks(self, figsize, is_grid, xlim, ylim)

    def plotly_blocks(self, figsize=(750, 750), xlim=(0, 80), ylim=(0, 80), fill_with_current=False) -> None:
        GeometryPlot.plotly_geometry_blocks(self, figsize, xlim, ylim, fill_with_current)

    def plot_bare_blocks(self, figsize=(15, 15), is_grid=True, xlim=(0, 80), ylim=(0, 80)) -> None:
        GeometryPlot.plot_bare_blocks(self, figsize, is_grid, xlim, ylim)

    def get_bare_areas_for_blocks(self) -> List[List[Area]]:
        """ Method returning a list of list of bare (uninsulated) areas constructed from iterating over all blocks in a
        geometry and all areas in a block.

        :return: a list of list of bare (uninsulated) areas
        """
        return [block.get_bare_areas() for block in self.blocks]

    def to_rel_geometry(self) -> RelativeCosThetaGeometry:
        geometry = deepcopy(self)

        if not all([isinstance(block, CosThetaBlock) for block in self.blocks]):
            raise TypeError('Only a geometry composed of CosThetaBlocks can be converted to a relative geometry.')

        blocks = []
        block_no_to_index = self.create_block_no_to_index()
        for layer_def in geometry.layer_defs:
            for index, block_index in enumerate(layer_def.blocks):
                index_in_blocks = block_no_to_index[block_index]
                block = geometry.blocks[index_in_blocks]
                alpha_ref, phi_ref = retrieve_alpha_and_phi_ref(geometry, layer_def, index, block_no_to_index)
                block_def = RelativeCosThetaBlockDefinition(**block.to_rel_dict(alpha_ref=alpha_ref, phi_ref=phi_ref))
                blocks.append(RelativeCosThetaBlock(cable_def=block.cable_def,
                                                    insul_def=block.insul_def,
                                                    strand_def=block.strand_def,
                                                    conductor_def=block.conductor_def,
                                                    block_def=block_def))

        geometry_rel = self.init_rel_geometry_instance(blocks, geometry)
        return geometry_rel

    def init_rel_geometry_instance(self, blocks, geometry):
        return RelativeCosThetaGeometry(blocks=blocks, layer_defs=geometry.layer_defs)

    def homogenize(self) -> HomogenizedCosThetaGeometry:
        """ Class method creating a homogenized cos-theta geometry from a cos-theta geometry.
        The method assumes that all blocks are CosThetaBlock type

        :return: a HomogenizedCosThetaGeometry instance
        """
        # Take updated blocks once to avoid recheck
        blocks = self.blocks

        homo_blocks = []
        block_no_to_index = self.create_block_no_to_index()
        for layer_index, layer_def in enumerate(self.layer_defs):
            for block_index in layer_def.blocks:
                index_in_blocks = block_no_to_index[block_index]
                block = blocks[index_in_blocks]
                homo_cos_theta_block = block.homogenize()
                homo_blocks.append(homo_cos_theta_block)

        return self.init_homogenized_geometry(homo_blocks, self.layer_defs)

    def init_homogenized_geometry(self, blocks, layer_defs):
        return HomogenizedCosThetaGeometry(blocks, layer_defs)

    def to_abs_geometry(self) -> Geometry:
        geometry_copy = deepcopy(self)
        no_defined_blocks = self._calc_no_defined_blocks()
        geometry_copy._blocks = geometry_copy._blocks[:no_defined_blocks]
        return geometry_copy

    def get_number_of_layers(self) -> int:
        """ Method returning the number of layers in a cos-theta coil

        :return: number of layers
        """
        return len(self.layer_defs)

    def get_number_of_blocks_per_layer(self) -> List[int]:
        """ Method returning the number of blocks per layer in a cos-theta coil

        :return: list with number of blocks per layer
        """
        return [len(layer_def.blocks) for layer_def in self.layer_defs]


def _check_input_consistency(blocks: List[Block], layer_defs: List[LayerDefinition]) -> None:
    block_nos = [block.block_def.no for block in blocks]
    # are there any duplications in block numbers
    if len(block_nos) != len(set(block_nos)):
        raise AttributeError('The block numbering ({}) contains duplications!'.format(block_nos))

    # are there any duplications in layer numbers
    layer_nos = [layer_def.no for layer_def in layer_defs]
    if len(layer_nos) != len(set(layer_nos)):
        raise AttributeError('The layer numbering ({}) contains duplications!'.format(layer_nos))

    # are there any duplications in layer block numbers
    layer_blocks = list(chain.from_iterable([layer_def.blocks for layer_def in layer_defs]))
    if len(layer_blocks) != len(set(layer_blocks)):
        raise AttributeError('The layer numbering of blocks ({}) contains duplications!'.format(layer_blocks))

    # are the block nos matching the layer block numbers
    if set(block_nos) != set(layer_blocks):
        raise AttributeError('The numbering in block {} and layer {} do not match!'.format(block_nos, layer_blocks))


def retrieve_alpha_and_phi_ref(geometry, layer_def, index, block_no_to_index):
    if index == 0:
        return 0.0, 0.0
    else:
        index_prev_in_blocks = block_no_to_index[layer_def.blocks[index - 1]]
        block_prev = geometry._blocks[index_prev_in_blocks]
        area_prev = block_prev.areas[-1]
        radius = block_prev.get_radius()
        phi_ref = Line.calculate_positioning_angle(area_prev.get_line(2), radius)
        alpha_ref = Line.calculate_relative_alpha_angle(area_prev.get_line(2))
        return alpha_ref, phi_ref


class RelativeCosThetaGeometry(Geometry):
    """RelativeCosThetaGeometry class for relative cos-theta geometry. Needed to implement the relative creation of
    cos-theta blocks.

    """

    def __init__(self, blocks: List[RelativeCosThetaBlock], layer_defs: List[LayerDefinition], extra_defs=None) -> None:
        """Constructor of RelativeCosThetaGeometry class

        :param blocks: list of RelativeCosThetaBlock definitions
        :param layer_defs: a list of layer definitions
        :param extra_defs: an optional dictionary with arbitrary, extra definitions for a geometry
        """
        super().__init__(blocks, layer_defs, extra_defs)
        self._blocks = blocks  # Superfluous assignment to fix attribute warnings of mypy

    def _build_block_areas(self):
        # for a relative geometry, check for all blocks
        # if at least one block and layer string changed - rebuild all block areas again
        # if so, empty all block areas
        #        build all block areas
        layer_defs_str = json.dumps(self.layer_defs, default=lambda o: o.__dict__)
        block_no_to_index = self.create_block_no_to_index()
        for layer_index, layer_def in enumerate(self.layer_defs):
            for index, block_index in enumerate(layer_def.blocks):
                index_in_blocks = block_no_to_index[block_index]
                block = self._blocks[index_in_blocks]
                alpha_ref, phi_ref = retrieve_alpha_and_phi_ref(self, layer_def, index, block_no_to_index)
                block.build_areas(phi_ref=phi_ref, alpha_ref=alpha_ref)
                block._invariant_cache = block.hash_as_str + layer_defs_str

    def to_abs_geometry(self) -> Geometry:
        geometry = deepcopy(self)

        no_defined_blocks = self._calc_no_defined_blocks()
        blocks = []
        for block in geometry.blocks[:no_defined_blocks]:
            abs_block_def = AbsoluteCosThetaBlockDefinition(**block.to_abs_dict())
            abs_block = AbsoluteCosThetaBlock(cable_def=block.cable_def,
                                              insul_def=block.insul_def,
                                              strand_def=block.strand_def,
                                              conductor_def=block.conductor_def,
                                              block_def=abs_block_def)
            blocks.append(abs_block)

        geometry_abs = self.init_rel_geometry_instance(blocks, geometry.layer_defs)
        return geometry_abs

    def init_rel_geometry_instance(self, blocks, layer_defs):
        return Geometry(blocks=blocks, layer_defs=self.layer_defs)

    def to_rel_geometry(self) -> RelativeCosThetaGeometry:
        return deepcopy(self)

    def to_dict(self) -> dict:
        """ Method returning a relative geometry definition (block definitions and layer definitions) as a dictionary.

        :return: a dictionary with two keys: block_defs and layer_defs
        """
        # Take updated blocks once to avoid recheck
        blocks = self.blocks
        block_defs = []
        block_no_to_index = self.create_block_no_to_index()
        for layer_def in self.layer_defs:
            for block_index in layer_def.blocks:
                index_in_blocks = block_no_to_index[block_index]
                block_defs.append(blocks[index_in_blocks].to_rel_dict())

        layer_defs = [layer_def.__dict__ for layer_def in self.layer_defs]

        return self.init_geometry_dict(block_defs, layer_defs)

    def init_geometry_dict(self, block_defs, layer_defs):
        return {'block_defs': block_defs, 'layer_defs': layer_defs, "extra_defs": self.extra_defs}


class HomogenizedCosThetaGeometry(Geometry):
    """HomogenizedCosThetaGeometry class for homogenized cos-theta geometry. Creates a homogenized geometry from both
    relative and absolute cos-theta geometry definition. Used for creation of ANSYS models.

    """

    def __init__(self,
                 blocks: List[HomogenizedCosThetaBlock],
                 layer_defs: List[LayerDefinition],
                 extra_defs=None) -> None:
        """
        Constructor of HomogenizedCosThetaGeometry class

        :param blocks: list of HomogenizedCosThetaBlock blocks
        :param layer_defs: a list of layer definitions
        :param extra_defs: an optional dictionary with arbitrary, extra definitions for a geometry
        """
        super().__init__(blocks, layer_defs, extra_defs)
        self._blocks = blocks  # Superfluous assignment to fix attribute warnings of mypy

    def to_block_df(self):
        raise NotImplementedError('This method is not implemented for this class')

    def plotly_blocks(self, figsize=(750, 750), xlim=(0, 80), ylim=(0, 80), with_current_sign=False):
        GeometryPlot.plotly_homogenized_geometry_blocks(self, figsize, xlim, ylim)

    def to_dict(self) -> dict:
        no_defined_blocks = self._calc_no_defined_blocks()
        return {'blocks': [deepcopy(block.block_def.__dict__) for block in self.blocks[:no_defined_blocks]],
                'layers_def': [layer_def.__dict__ for layer_def in self.layer_defs]}
