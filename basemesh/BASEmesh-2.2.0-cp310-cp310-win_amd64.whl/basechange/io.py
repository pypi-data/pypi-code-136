# A component of the BASEmesh pre-processing toolkit.
# Copyright (C) 2020  ETH Zürich
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""I/O module for 1D BASEchain geometry (BMG) files."""

import ast
import dataclasses
import datetime
import warnings
from types import TracebackType
from typing import (Any, Dict, IO, Iterable, Iterator, List, Optional,
                    Sequence, Tuple, Type)

from basemesh.errors import TokenError

from .geometry import ChannelGeometry, CrossSection, Vertex


@dataclasses.dataclass()
class BaseChainSoilDef:
    """Data class for BMG "SOIL_DEF" blocks.

    Soil definition indices must be unique, and their ranges/indexes
    may not overlap.

    Attributes
    ----------
    index: int
        The unique ID of the soil definition
    range : Tuple[float, float], optional
        The range this soil definition applies to, by default None
        .. seealso:: :attr:`slice_indexes`
    slice_indexes: Tuple[int, int], optional
        Like :attr:`range`, but uses edge indexes instead of
        coordinates, by default None

    """

    index: int
    range: Optional[Tuple[float, float]] = None
    slice_indexes: Optional[Tuple[int, int]] = None


@dataclasses.dataclass()
class BaseChainCrossSection:  # pylint: disable=too-many-instance-attributes
    """Data class for BMG "CROSS_SECTION" blocks.

    Every element in the 1D computational grid is based around a cross
    section object, which describes the hydraulic and topological
    information for the element.

    Attributes
    ----------
    name : str
        The unique name of the cross section.
    distance_coord : float
        Distance coordinate of the cross section. This is measured from
        up- to downstream and positions the cross section. Please note
        that this value is given in kilometres.
    node_coords : List[Tuple[float, float]]
        The list of nodes defining the cross section geometry.

        This uses a relative coordinate system whose first element
        represents the distance from the leftmost node relative to the
        river flow direction. The second tuple element specifies the
        absolute elevation of the given node.
    sternberg : float, optional
        Sternberg-factor for the reduction of volume by abrasion
        ``V = V0e**(s*Dx)``, by default 0.0
    reference_height : float, optional
        A height offset to apply to any node-specific elevation values,
        by default 0.0
    left_point_global_coords : Tuple[float, float, float], optional
        Global coordinates of the leftmost cross section node. Allows
        converting the 1D channel back into a 2D geometry. In addition,
        it is used by the cross section interpolator to account for
        curvatures, etc., by default (0.0, 0.0, 0.0)
        .. seealso:: :attr:`orientation_angle`
    orientation_angle : float, optional
        In-plane angle of the cross section line with the leftmost node
        as the axis of rotation. The angle is measured counter
        clockwise with the vector ``(1,0)`` representing an angle of 0
        degrees, by default 0.0
        .. seealso:: :attr:`left_point_global_coords`
    interpolation_fixpoints : List[int], optional
        The interpolation fixpoints are used to specify break lines
        in-between existing cross sections. This can be used to insert
        new cross sections, as well as to improve the quality of a 2D
        mesh export.

        The first and last node in a cross section are always
        connected. Nodes are numbered starting at 1, by default None
    water_flow_range : Tuple[float, float], optional
        Used to limit the part of the part of the cross section that
        will be used for solving of the momentum equation, the rest of
        the cross section is considered to be only storage area in the
        continuity equation. By default, the whole cross section area
        is flowing.

        Avoid defining storage areas in the main channel as this can
        cause instability if only the non-flowing part of the channel
        is wetted.

        Additionally, the non-flowing areas are not taken into account
        for sediment deposition and erosion, by default None
        .. warning:: Mutually exclusive with
            :attr:`water_flow_slice_indexes`
        .. seealso:: :attr:`water_flow_slice_indexes`
    water_flow_slice_indexes : Tuple[int, int], optional
        Like :attr:`water_flow_range`, but uses edge indexes instead of
        coordinates, by default None
        .. warning:: Mutually exclusive with :attr:`water_flow_range`
        .. seealso:: :attr:`water_flow_range`
    main_channel_range : Tuple[float, float], optional
        Range defining the span of the main channel. Everything outside
        of the main channel is treated as floodplain. If not defined,
        the whole cross section is assumed to belong to the main
        channel, by default None
        .. warning:: Mutually exclusive with
            :attr:`main_channel_slice_indexes`
        .. seealso:: :attr:`main_channel_slice_indexes`
    main_channel_slice_indexes : Tuple[int, int], optional
        Like :attr:`main_channel_range`, but uses edge indexes instead
        of coordinates, by default None
        .. warning:: Mutually exclusive with :attr:`main_channel_range`
        .. seealso:: :attr:`main_channel_range`
    bottom_range : Tuple[float, float], optional
        Range defining the span of the bottom/bedload active zone, by
        default None
        .. warning:: Mutually exclusive with
            :attr:`bottom_slice_indexes`
        .. seealso:: :attr:`bottom_slice_indexes`
    bottom_slice_indexes : Tuple[float, float], optional
        Like :attr`bottom_range`, but uses edge indexes instead of
        coordinates, by default None
        .. warning:: Mutually exclusive with :attr:`bottom_range`
        .. seealso:: :attr:`bottom_range`
    active_range : Tuple[float, float], optional
        This range defines the active part of the cross section and
        must span from the left to the right dike. If not specified,
        the whole cross section is assumed to be active, and the
        elevation of the first and last point will be assumed to
        correspond to the dike elevation, by default None
        .. warning:: Mutually exclusive with
            :attr:`active_slice_indexes`
        .. seealso:: :attr:`active_slice_indexes`
    active_slice_indexes : Tuple[int, int], optional
        Like :attr:`active_range`, but uses edge indexes instead of
        coordinates, by default None
        .. warning:: Mutually exclusive with :attr:`active_range`
        .. seealso:: :attr:`active_range`
    bed_form_factor : float, optional
        Factor considering the influence of bed forms on bottom shear
        stress (ripple factor). This factor reduces the bottom shear
        stress due to bedforms with a constant value. If this factor is
        set to 1.0 (default), there is no influence and the standard
        shear stress is used, by default 1.0
        .. seealso:: :attr:`theta_critic`
    theta_critic : float, optional
        User-defined dimensionless critical bottom shear stress
        (Shields parameter) for this cross section. If specified, this
        local theta critic is used for this cross section. Permissible
        values range from 0.0 to 1.0. Set to a negative value to use
        the standard theta critical as defined in the
        ``BEDLOAD_PARAMETER`` block, by default -1.0
        .. seealso:: :attr:`bed_form_factor`
    friction_calibration_factor : float, optional
        Calibration factor between 0.0 and 10.0 to locally modify the
        friction value for this cross section, by default 1.0
    default_friction : float, optional
        Default Strickler friction value to use for this cross section,
        by default None
    friction_coefficients : List[float], optional
        Strickler values to apply to the segments in the groups defined
        in :attr:`friction_ranges` or :attr:`friction_slice_indexes`
        respectively, by default None
    friction_ranges : List[Tuple[float, float]], optional
        The ranges to which to apply the coefficients defined in
        :attr:`friction_coefficients`, by default None
        .. warning:: Mutually exclusive with
            :attr:`friction_slice_indexes`
        .. seealso:: :attr:`friction_slice_indexes`
    friction_slice_indexes : List[Tuple[int, int]], optional
        Like :attr:`friction_ranges`, but uses edge indexes instead of
        coordinates, by default None
        .. warning:: Mutually exclusive with :attr:`friction_ranges`
        .. seealso:: :attr:`friction_ranges`
    table_fixed_points : List[float], optional
        Fixed points which should be included in the table calculation.
        Note that these values are only used if you use lookup tables
        for hydraulic properties (see ``SECTION_COMPUTATION`` in the
        BASEMENT command file documentation for details), by default
        None
    table_fixed_lower_limit : float, optional
        Allows to fix the lowest water surface elevation used in the
        lookup table for ``A(z)`` to a different value than the lowest
        elevation in the cross section. This option is useful if you
        include a deep lake in your model containing a large water
        volume not participating in the dynamics of your river system,
        by default None
    interpolated : bool, optional
        This is an internal tag used to indicate that the cross section
        is the result of an interpolation of two user-defined cross
        sections, by default False
    soil_defs : List[BaseChainSoilDef], optional
        A list of soil definition blocks for the given cross section.
        See the :class:`BaseChainSoilDef` class for details, by default
        None

    """

    name: str
    distance_coord: float
    node_coords: List[Tuple[float, float]]
    sternberg: float = 0.0
    reference_height: float = 0.0
    left_point_global_coords: Optional[Tuple[float, float, float]] = None
    orientation_angle: float = 0.0
    interpolation_fixpoints: Optional[List[int]] = None
    water_flow_range: Optional[Tuple[float, float]] = None
    water_flow_slice_indexes: Optional[Tuple[int, int]] = None
    main_channel_range: Optional[Tuple[float, float]] = None
    main_channel_slice_indexes: Optional[Tuple[int, int]] = None
    bottom_range: Optional[Tuple[float, float]] = None
    bottom_slice_indexes: Optional[Tuple[int, int]] = None
    active_range: Optional[Tuple[float, float]] = None
    active_slice_indexes: Optional[Tuple[int, int]] = None
    bed_form_factor: float = 1.0
    theta_critic: float = -1.0
    friction_calibration_factor: float = 1.0
    default_friction: Optional[float] = None
    friction_coefficients: Optional[List[float]] = None
    friction_ranges: Optional[List[Tuple[float, float]]] = None
    friction_slice_indexes: Optional[List[Tuple[int, int]]] = None
    table_fixed_points: Optional[List[float]] = None
    table_fixed_lower_limit: Optional[float] = None
    interpolated: bool = False
    soil_defs: Optional[List[BaseChainSoilDef]] = None


class BaseChainReader:
    """Reader method for BMG files."""

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self._file: Optional[IO[str]] = None

    def __enter__(self) -> 'BaseChainReader':
        self._file = open(self.filepath, encoding='utf-8')
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> bool:
        self.close()
        return False

    def close(self) -> None:
        """Close the file.

        You do not need to call this method when using the parser as a
        context manager. It is only required if you manually called
        :meth:`BaseChainReader` earlier.
        """
        if self._file is not None:
            self._file.close()

    @staticmethod
    def _convert_values(data: Dict[str, Any]) -> BaseChainCrossSection:
        """Convert the string literals read from file to proper values.

        This is specific to the :class:`CrossSection` data class and
        will ignore any unexpected keys. The provided dictionary will
        get altered by this method.
        """
        # This table is used to look up the conversion type for a given key
        types: Dict[str, List[str]] = {
            'float': [
                'distance_coord', 'sternberg', 'reference_height',
                'orientation_angle', 'bed_form_factor', 'theta_critic',
                'friction_calibration_factor', 'default_friction',
                'table_fixed_lower_limit'],
            'str': [
                'name'],
            'tuple_2_float': [
                'water_flow_range',
                'main_channel_range',
                'bottom_range',
                'active_range'
            ],
            'tuple_2_int': [
                'water_flow_slice_indexes', 'main_channel_slice_indexes',
                'bottom_slice_indexes', 'active_slice_indexes'
            ],
            'tuple_3_float': [
                'left_point_global_coords'],
            'list_tuples_2_float': [
                'node_coords', 'friction_ranges'],
            'list_int': [
                'interpolation_fixpoints'],
            'list_float': [
                'friction_coefficients', 'table_fixed_points'],
            'list_tuples_2_int': [
                'friction_slice_indexes'],
            'bool': [
                'interpolated']
        }

        for key, value in data.items():
            if key in types['float']:
                data[key] = float(value)
            elif key in types['str']:
                data[key] = str(value)
            elif key in types['tuple_2_float']:
                value = f'{value[:-1]},)'
                tuple_: Tuple[Any, ...] = ast.literal_eval(value)
                assert isinstance(tuple_, tuple), f'Unexpected literal {value}'
                assert len(tuple_) == 2, f'Unexpected tuple size for {key}'
                data[key] = tuple(float(e) for e in tuple_)
            elif key in types['tuple_3_float']:
                value = f'{value[:-1]},)'
                tuple_ = ast.literal_eval(value)
                assert isinstance(tuple_, tuple), f'Unexpected literal {value}'
                assert len(tuple_) == 3, f'Unexpected tuple size for {key}'
                data[key] = tuple(float(e) for e in tuple_)
            elif key in types['tuple_2_int']:
                value = f'{value[:-1]},)'
                tuple_ = ast.literal_eval(value)
                assert isinstance(tuple_, tuple), f'Unexpected literal {value}'
                assert len(tuple_) == 2, f'Unexpected tuple size for {key}'
                data[key] = tuple(int(e) for e in tuple_)
            elif key in types['list_tuples_2_float']:
                value = f'{value[:-1]},)'
                tuple_ = ast.literal_eval(value)
                assert isinstance(tuple_, tuple), f'Unexpected literal {value}'
                assert len(tuple_[0]) == 2, f'Unexpected tuple size for {key}'
                data[key] = [tuple(float(e) for e in t) for t in tuple_]
            elif key in types['list_tuples_2_int']:
                value = f'{value[:-1]},)'
                tuple_ = ast.literal_eval(value)
                assert isinstance(
                    tuple_, tuple), f'Unexpected literal {value}'
                assert len(tuple_[0]) == 2, f'Unexpected tuple size for {key}'
                data[key] = [tuple(int(e) for e in t) for t in tuple_]
            elif key in types['list_int']:
                value = f'{value[:-1]},)'
                tuple_ = ast.literal_eval(value)
                assert isinstance(tuple_, tuple), f'Unexpected literal {value}'
                data[key] = [int(e) for e in tuple_]
            elif key in types['list_float']:
                value = f'{value[:-1]},)'
                tuple_ = ast.literal_eval(value)
                assert isinstance(tuple_, tuple), f'Unexpected literal {value}'
                data[key] = [float(e) for e in tuple_]
            elif key in types['bool']:
                data[key] = bool(value)

        return BaseChainCrossSection(**data)

    def cross_sections(self) -> Iterator[BaseChainCrossSection]:
        """Iterate over the file returning any cross sections found."""
        if self._file is None:
            raise RuntimeError('Cannot iterate over closed file')

        # This variable holds the last few lines of the file
        cache: str = ''
        for line in self._file:
            # Handle comments
            line, *_ = line.split('//', maxsplit=1)
            cache += ''.join(line.strip(' \t'))

        offset = 0
        while 'CROSS_SECTION' in cache:
            start, end = match_tokens(cache[offset:], '{', '}')
            if start == -1 and end == -1:
                break
            yield self._process_block(cache[start:end])
            cache = cache[end:]

    @staticmethod
    def _parse_soildef(string: str) -> BaseChainSoilDef:
        """Process the given soil definition substring."""
        assert string.startswith('{')
        assert string.endswith('}')
        string = string[1:-1].strip()
        data: Dict[str, Any] = {}
        for line in string.splitlines():
            key, _, *values = line.split()
            value = ''.join(values)
            if key == 'index':
                data[key] = int(value)
            elif key == 'range':
                tuple_ = ast.literal_eval(value)
                data[key] = tuple(float(i) for i in tuple_)
            elif key == 'slice_indexes':
                tuple_ = ast.literal_eval(value)
                data[key] = tuple(int(i) for i in tuple_)

        return BaseChainSoilDef(**data)

    def _process_block(self, string: str) -> BaseChainCrossSection:
        """Process a given substring to extract a cross section.

        The provided string will be modified in the process.
        """
        assert string.startswith('{')
        assert string.endswith('}')
        string = string[1:-1].strip()

        # This will store the key-value pairs read from the file
        data: Dict[str, Any] = {}

        # Extract any SOIL_DEF keys
        while True:
            if '{' not in string:
                break
            sd_start, sd_end = match_tokens(string, '{', '}')
            # Extract the tag name
            pre = string[:sd_start]
            pre, tag = pre.strip().rsplit(maxsplit=1)
            # Extract soil definitions
            if tag == 'SOIL_DEF':
                soil_def = self._parse_soildef(string[sd_start:sd_end])
                try:
                    data['soil_defs'].append(soil_def)
                except KeyError:
                    data['soil_defs'] = [soil_def]
            else:
                warnings.warn(f'Ignoring unknown tag {tag}')
            string = pre + string[sd_end:]

        while True:
            # NOTE: This uses equal signs to separate two arguments. I found
            # this to be easier/faster than parsing the parentheses due to the
            # overhead involved.

            # Get the first two equal signs in the string
            first = string.index('=')
            try:
                second: Optional[int] = string.index('=', first+1)
            except ValueError:
                second = None

            # The substring before the first is the name of the key
            key = string[:first].strip()

            # The "body" is the chunk between the two equal signs, including
            # the next key (will be trimmed later).
            if second is None:
                inner = body = string[first+1:]
                next_key = None
            else:
                body = string[first+1:second]
                inner, next_key = body.rsplit('\n', maxsplit=1)

            # The value of a key may be serialised as newlines no longer act as
            # separators
            data[key] = ''.join(inner.split())

            if next_key is None:
                break

            string = string[string.index(next_key):]

        return self._convert_values(data)

    def open(self, **kwargs: Any) -> IO[str]:
        """Manually open the wrapped file.

        It is recommended to use the parser as a context manager
        instead. If you do use this method, make sure to call
        :meth:`BaseChainReader.close()` afterwards.
        """
        self._file = open(self.filepath, **kwargs)
        assert self._file is not None
        return self._file


class BaseChainWriter:
    """Writer class for BMG files."""

    def __init__(self, filepath: str,
                 sections: Optional[Iterable[BaseChainCrossSection]] = None
                 ) -> None:
        self._sections: List[BaseChainCrossSection] = list(sections or ())
        self.filepath = filepath
        self._file: Optional[IO[str]] = None

        if sections:
            self._write_header()
            for section in sections:
                self._write_section(section)

    def __enter__(self) -> 'BaseChainWriter':
        self._file = self.open('w', encoding='utf-8')
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> bool:
        self.close()
        return False

    def close(self) -> None:
        """Close the file.

        You do not need to call this method when using the parser as a
        context manager. It is only required if you manually called
        :meth:`BaseChainReader` earlier.
        """
        if self._file is not None:
            self._file.close()

    def open(self, *args: Any, **kwargs: Any) -> IO[str]:
        """Manually open the wrapped file.

        It is recommended to use the writer as a context manager
        instead. If you do use this method, make sure to call
        :meth:`BaseChainWriter.close()` afterwards.
        """
        self._file = open(self.filepath, *args, **kwargs)
        assert self._file is not None
        return self._file

    def write_channel(self, channel: 'ChannelGeometry') -> None:
        """Write a channel geometry to disk."""
        self._write_header()
        sections = channel_to_basechain(channel)
        for index, section in enumerate(sections):
            self._write_section(section)
            if index+1 != len(sections):
                self._file.write('\n')  # type: ignore

    def _write_header(self) -> None:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        assert self._file is not None
        self._file.write(f'// BASEMENT 1D Geometry\n// Generated {now} using '
                         'BASEchange v0.1.0\n')

    def _write_section(self, section: BaseChainCrossSection) -> None:
        assert self._file is not None
        # Required tokens
        text = [
            'CROSS_SECTION {',
            f'\tname = {section.name}',
            f'\tdistance_coord = {section.distance_coord}',
            '\tnode_coords = '
            + '(' + ','.join(
                (_compact_list(n) for n in section.node_coords)) + ')']
        # Optional tags
        if section.sternberg != 0.0:
            text.append(f'\tsternberg = {section.sternberg}')
        if section.reference_height != 0.0:
            text.append(f'\treference_height = {section.reference_height}')
        if section.left_point_global_coords is not None:
            text.append('\tleft_point_global_coords = '
                        + _compact_list(section.left_point_global_coords))
        if section.orientation_angle != 0.0:
            text.append(f'\torientation_angle = {section.orientation_angle}')
        if section.interpolation_fixpoints is not None:
            text.append('\tinterpolation_fixpoints = '
                        f'{_compact_list(section.interpolation_fixpoints)}')
        if section.water_flow_range is not None:
            text.append('\twater_flow_range = '
                        f'{_compact_list(section.water_flow_range)}')
        if section.water_flow_slice_indexes is not None:
            text.append('\twater_flow_slice_indexes = '
                        f'{_compact_list(section.water_flow_slice_indexes)}')
        if section.main_channel_range is not None:
            text.append(f'\tmain_channel_range = '
                        f'{_compact_list(section.main_channel_range)}')
        if section.main_channel_slice_indexes is not None:
            text.append(f'\tmain_channel_slice_indexes = '
                        f'{_compact_list(section.main_channel_slice_indexes)}')
        if section.bottom_range is not None:
            text.append(f'\tbottom_range = '
                        f'{_compact_list(section.bottom_range)}')
        if section.bottom_slice_indexes is not None:
            text.append(f'\tbottom_slice_indexes = '
                        f'{_compact_list(section.bottom_slice_indexes)}')
        if section.active_range is not None:
            text.append(f'\tactive_range = '
                        f'{_compact_list(section.active_range)}')
        if section.active_slice_indexes is not None:
            text.append(f'\tactive_slice_indexes = '
                        f'{_compact_list(section.active_slice_indexes)}')
        if section.bed_form_factor != 1.0:
            text.append(f'\tbed_form_factor = {section.bed_form_factor}')
        if section.theta_critic != -1.0:
            text.append(f'\ttheta_critic = {section.theta_critic}')
        if section.friction_calibration_factor != 1.0:
            text.append('\tfriction_calibration_factor = '
                        f'{section.friction_calibration_factor}')
        if section.default_friction is not None:
            text.append(f'\tdefault_friction = {section.default_friction}')
        if section.friction_coefficients is not None:
            text.append(f'\tfriction_coefficients = '
                        f'{_compact_list(section.friction_coefficients)}')
        if section.friction_ranges is not None:
            line = '\tfriction_ranges = ('
            line += ','.join(
                (_compact_list(r) for r in section.friction_ranges))
            line += ')'
            text.append(line)
        if section.friction_slice_indexes is not None:
            line = '\tfriction_slice_indexes = ('
            line += ','.join(
                (_compact_list(r) for r in section.friction_slice_indexes))
            line += ')'
            text.append(line)
        if section.table_fixed_points is not None:
            text.append('\ttable_fixed_points = '
                        f'{_compact_list(section.table_fixed_points)}')
        if section.table_fixed_lower_limit is not None:
            text.append('\ttable_fixed_lower_limit = '
                        f'{section.table_fixed_lower_limit}')
        if section.soil_defs is not None:
            for def_ in section.soil_defs:
                line = ('\tSOIL_DEF {\n'
                        f'\t\tindex = {def_.index}\n')
                if def_.slice_indexes is not None:
                    line += ('\t\tslice_indexes = '
                             f'{_compact_list(def_.slice_indexes)}')
                elif def_.range is not None:
                    line += f'\t\trange = {_compact_list(def_.range)}'
                line += '\n\t}'
                text.append(line)
        text.append('}')
        out_file: IO[str] = self._file
        out_file.write('\n'.join(text))


def match_tokens(text: str, start: str, end: Optional[str] = None
                 ) -> Tuple[int, int]:
    """Extract the substring enclosed between the two tokens.

    This scans the given string for the start token and extracts the
    start and end indices of the enclosed substring. The tokens are not
    included in this substring.

    This will return ``(-1, -1)`` if neither token is found.

    If multiple nested pairs of start and end tokens are found, the
    inner tokens must be matched before the outer tokens. For example,
    in the string ``animal ( feline ( cat ) )``, the substring matched
    for the parentheses would be `` feline ( cat ) ``.

    This method is intended for non-serialisable, multiline strings
    potentially containing nested sets of matching tokens, performance
    for short strings is likely not great compared to other solutions
    like :meth:`str.find()`` or regular expressions.

    Parameters
    ----------
    text : str
        The input text to process.
    start : str
        The opening token to scan for.
    end : str or None, optional
        The closing token. If None, the starting token will be used,
        by default None

    Returns
    -------
    Tuple[int, int]
        The start and end index of the matching substring in slice
        notation, or ``(-1, -1)`` if neither was found.

    Raises
    ------
    TokenError
        Raised if a mismatch between an opening and closing token is
        encountered.

    """
    if end is None:
        end = start
    match_start = match_end = -1
    # This variable keeps track of any nested sets of tokens. 0 means no match
    # yet, higher numbers indicate the current depth.
    nested = 0

    chunk = text  # The active substring that is searched for tokens
    chunk_offset = 0  # Conversion between the global index and the chunk
    while chunk:
        next_ = ''

        # Find the next token in the active substring
        if start in chunk:
            next_ = start
            index = chunk.index(start)
            # If there is an end token before the start token, use that instead
            if end in chunk and chunk.index(end) < index:
                next_ = end
                index = chunk.index(end)
        elif end in chunk:
            next_ = end
            index = chunk.index(end)
        else:
            # TODO: Validate else block
            continue

        if next_ == start:
            # The first starting token found automatically becomes the start of
            # the match
            if not nested:
                match_start = chunk_offset + index
            chunk_offset += index + len(start)
            nested += 1

        elif next_ == end:
            # Closing tokens with no matching opening token are not permitted
            if not nested:
                raise TokenError(
                    f'Unexpected closing token {end} encountered; no matching '
                    'opening token found')
            chunk_offset += index + len(end)
            nested -= 1
            if nested < 1:
                match_end = chunk_offset
                break
        # Advance the current chunk
        chunk = text[chunk_offset:]
    # Check for unmatched end tokens
    if match_start != -1 and match_end == -1:
        raise TokenError(f'Unmatched opening token {start}')
    return match_start, match_end


def _compact_list(data: Sequence[Any], inline: bool = True,
                  newline_indent: str = '\t') -> str:
    """Write a tuple without spaces."""
    text = '('
    if inline:
        text += ','.join((str(d) for d in data))
    else:
        text += ''.join(f'{newline_indent}{d},\n' for d in data)
        text += newline_indent
    text += ')'
    return text


def channel_from_basechain(filepath: str,
                           flow_axis_shift: float = 0.5) -> ChannelGeometry:
    """Create a channel geometry from a BASEchain geometry file."""
    # Create a geometry to parse the file into
    instance = ChannelGeometry()
    with BaseChainReader(filepath) as parser:
        for data in parser.cross_sections():
            cs_ = cross_section_from_basechain(data)
            cs_.flow_axis_shift = flow_axis_shift
            instance.cross_sections.append(cs_)
    return instance


def cross_section_from_basechain(data: BaseChainCrossSection) -> CrossSection:
    """Create a new cross section from a BMG data class."""
    cs_ = CrossSection(data.name, (Vertex(*pos) for pos in data.node_coords))
    cs_.distance_coord = data.distance_coord
    cs_.sternberg = data.sternberg
    cs_.reference_height = data.reference_height
    if data.left_point_global_coords is not None:
        *anchor, cs_.reference_height = data.left_point_global_coords
        cs_.anchor = tuple(anchor)
        # left_point_global_coords include the relative elevation of the
        # leftmost vertex which must be removed
        cs_.reference_height -= cs_.vertices[0].pos[1]
        # Check for conflicting data
        difference = cs_.reference_height - data.reference_height
        if difference > 1e-10:
            warnings.warn(
                'Reference height mismatch for cross section '
                f'"{cs_.name}": {cs_.reference_height}'
                f'!= {data.reference_height}\n'
                f'Using global value {cs_.reference_height}')
    cs_.angle = data.orientation_angle
    cs_.interpolation_fixpoints = data.interpolation_fixpoints
    # Water flow range
    if data.water_flow_slice_indexes is not None:
        cs_.water_flow_slice = data.water_flow_slice_indexes
        if data.water_flow_range is not None:
            warnings.warn('water_flow_range value is redundant, ignoring')
    elif data.water_flow_range is not None:
        cs_.water_flow_slice = cs_.range_to_slice(
            data.water_flow_range)
    # Main channel range
    if data.main_channel_slice_indexes is not None:
        cs_.main_channel_slice = data.main_channel_slice_indexes
        if data.main_channel_range is not None:
            warnings.warn(
                'main_channel_range value is redundant, ignoring')
    elif data.main_channel_range is not None:
        cs_.main_channel_slice = cs_.range_to_slice(
            data.main_channel_range)
    # Bottom range
    if data.bottom_slice_indexes is not None:
        cs_.bottom_slice = data.bottom_slice_indexes
        if data.bottom_range is not None:
            warnings.warn('bottom_range value is redundant, ignoring')
    elif data.bottom_range is not None:
        cs_.bottom_slice = cs_.range_to_slice(data.bottom_range)
    # Active range
    if data.active_slice_indexes is not None:
        cs_.active_slice = data.active_slice_indexes
        if data.active_range is not None:
            warnings.warn('active_range value is redundant, ignoring')
    elif data.active_range is not None:
        cs_.active_slice = cs_.range_to_slice(data.active_range)
    cs_.bed_form_factor = data.bed_form_factor
    cs_.theta_critic = data.theta_critic
    cs_.friction_calibration_factor = data.friction_calibration_factor
    cs_.default_friction = data.default_friction
    cs_.friction_coefficients = data.friction_coefficients
    # Friction ranges
    if data.friction_slice_indexes is not None:
        cs_.friction_slices = data.friction_slice_indexes
        if data.friction_ranges is not None:
            warnings.warn('friction_ranges value is redundant, ignoring')
    elif data.friction_ranges is not None:
        cs_.friction_slices = [cs_.range_to_slice(d)
                               for d in data.friction_ranges]
    cs_.table_fixed_points = data.table_fixed_points
    cs_.table_fixed_lower_limit = data.table_fixed_lower_limit
    # Soil definitions
    if data.soil_defs is not None:
        for def_ in data.soil_defs:
            index = def_.index
            if def_.slice_indexes is not None:
                nodes = def_.slice_indexes
            elif def_.range is not None:
                nodes = cs_.range_to_slice(def_.range)
            else:
                warnings.warn(
                    f'Undefined soil definition ignored: {index}')
                continue
            cs_.soil_defs[index] = nodes
    return cs_


def cross_section_to_basechain(cs_: CrossSection) -> BaseChainCrossSection:
    """Convert the cross section into a BMG dataclass.

    Returns
    -------
    BaseChainCrossSection
        The BMG cross section equivalent of this section.

    """
    bmg_cs = BaseChainCrossSection(
        name=cs_.name,
        distance_coord=cs_.distance_coord,
        node_coords=[v.pos for v in cs_.vertices],
        sternberg=cs_.sternberg,
        reference_height=cs_.reference_height,
        orientation_angle=cs_.angle,
        interpolation_fixpoints=cs_.interpolation_fixpoints,
        water_flow_slice_indexes=cs_.water_flow_slice,
        main_channel_slice_indexes=cs_.main_channel_slice,
        bottom_slice_indexes=cs_.bottom_slice,
        active_slice_indexes=cs_.active_slice,
        bed_form_factor=cs_.bed_form_factor,
        theta_critic=cs_.theta_critic,
        friction_calibration_factor=cs_.friction_calibration_factor,
        default_friction=cs_.default_friction,
        friction_coefficients=cs_.friction_coefficients,
        friction_slice_indexes=cs_.friction_slices,
        table_fixed_points=cs_.table_fixed_points,
        table_fixed_lower_limit=cs_.table_fixed_lower_limit)
    if cs_.anchor is not None:
        bmg_cs.left_point_global_coords = (
            *cs_.anchor,
            cs_.reference_height + cs_.vertices[0].pos[1])
    if cs_.soil_defs:
        bmg_cs.soil_defs = []
        for index, sd_indices in cs_.soil_defs.items():
            bmg_cs.soil_defs.append(
                BaseChainSoilDef(index, slice_indexes=sd_indices))
    return bmg_cs


def channel_to_basechain(
        channel: ChannelGeometry) -> List[BaseChainCrossSection]:
    """Convert the geometry into a list of BMG cross sections."""
    return list(map(cross_section_to_basechain, channel.cross_sections))
