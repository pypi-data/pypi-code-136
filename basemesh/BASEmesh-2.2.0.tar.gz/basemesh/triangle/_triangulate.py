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

"""Triangle wrapper functions and subprocess utilities."""

import atexit
import datetime
import functools
import logging
import os
import pathlib
import platform
import subprocess
import stat
import tempfile
from typing import Any, Callable, Collection, Dict, Iterator, Optional, Tuple, Union

from ._geometry import Element, Node, Segment
from .io import read_node, read_ele, write_poly
from ._markers import HoleMarker, RegionMarker

__all__ = [
    'command',
    'read_output',
    'run_triangle',
    'triangulate',
]

# Path to the local Triangle executables
_TRIANGLE_BIN = pathlib.Path(__file__).parent / 'bin'

_log = logging.getLogger('triangle')


def _print(msg: str) -> None:
    """Print a message to the console, stripping trailing whispace."""
    print(msg.rstrip())


def command(**kwargs: Any) -> str:
    """Convert input keyword arguments to a triangle command string.

    The supported keyword arguments alongside their respective triangle
    command strings are.

    Arguments::

        min_angle <float>:      q<value>
        max_area <float>:       a<value>
        max_steiner <int>:      S<value>

    Flags::

        input_is_poly:          p
        conforming_delaunay:    D
        jettison_nodes:         j
        write_edges:            e
        write_neigh:            n
        no_boundary_in_output:  B
        no_iteration_numbers:   I
        ignore_holes:           O
        no_steiner_on_boundary: Y
        no_steiner_on_segment:  YY
        quiet:                  Q
        verbose:                V
        keep_convex_hull:       c
        refine:                 r
        no_output_node:         N
        no_output_ele:          E
        no_output_poly:         P
        use_region_areas:       a
        use_region_attributes:  A

    Debug level (specify multiple times for more output)::

        debug_level:            V[VVVV]
    """
    switches = {
        'input_is_poly': 'p',
        'conforming_delaunay': 'D',
        'jettison_nodes': 'j',
        'write_edges': 'e',
        'write_neigh': 'n',
        'no_boundary_in_output': 'B',
        'no_iteration_numbers': 'I',
        'ignore_holes': 'O',
        'no_steiner_on_boundary': 'Y',
        'no_steiner_on_segment': 'YY',
        'quiet': 'Q',
        'verbose': 'V',
        'keep_convex_hull': 'c',
        'refine': 'r',
        'no_output_node': 'N',
        'no_output_ele': 'E',
        'no_output_poly': 'P',
        'use_region_areas': 'a',
        'use_region_attributes': 'A'
    }
    flags = ''
    for key, value in kwargs.items():
        # Basic switches
        if key in switches:
            if value:
                flags += switches[key]
            continue
        # Switches with arguments
        if key == 'min_angle':
            flags += f'q{value}'
        elif key == 'max_area':
            flags += f'a{value}'
        elif key == 'max_steiner':
            flags += f'S{value}'
        # Debug level
        elif key == 'debug_level':
            flags += 'V' * int(value)
        else:
            raise ValueError(f'Unknown triangle flag: {key}={value}')
    return flags


def read_output(
        path: pathlib.Path) -> Tuple[Iterator[Node], Iterator[Element]]:
    """Return generators over the Triangle nodes and elemnets.

    This function takes the stem of the output files as an input, but
    does expect the files to be named as per Triangle's convention.

    This means that a triangulation performed on the file
    ``input.poly`` will produce the output files ``input.1.node`` and
    ``input.1.ele``. This function then expects to be passed the stem
    ``input.1`` and will add the ``.node`` and ``.ele`` suffixes
    itself.

    This currently only returns the nodes and elements as these fully
    define the triangulation.

    This function returns generators to allow for lazy processing of
    the output files. If your application requires a list of all nodes
    and elements instead, you can pass the generators to two lists:

    .. code-block:: python3

        nodes, elements = [list(n) for n in read_output(path)]

    :param path: Base name of the Triangle output files, without
        extension.
    :type path: :class:`pathlib.Path`
    :return: The node and element generators.
    :rtype: :class:`tuple` [
        :class:`collections.abc.Iterator` [:class:`Node`],
        :class:`collections.abc.Iterator` [:class:`Element`]]
    """
    path_node = path.with_suffix(path.suffix + '.node')
    path_ele = path.with_suffix(path.suffix + '.ele')
    if not path_node.exists() or not path_ele.exists():
        raise FileNotFoundError(
            f'Missing output files: {path_node} and {path_ele}')

    # The node and element generators return a tuple consisting of the ID and
    # object. These generators discard the unused ID.
    return ((n for _, n in read_node(path_node)),
            (e for _, e in read_ele(path_ele)))


def run_triangle(input_path: pathlib.Path, triangle_cmd: str,
                 redirect_stdout: Union[Callable[[str], None], None] = _print,
                 ) -> None:
    """Run Triangle on the given input file.

    By default, all Triangle output is redirected to the Python
    console. This can be overridden by passing another function to the
    `redirect_stdout` argument. Setting this to `None` will disable
    output entirely.

    :param input_path: Path to the input file.
    :type input_path: :class:`pathlib.Path`
    :param triangle_cmd: Command string to pass to Triangle.
    :type triangle_cmd: :class:`str`
    :param redirect_stdout: Function to call with each line of output.
    :type redirect_stdout: :class:`collections.abc.Callable` [
        [:class:`str`], :obj:`None`] | :obj:`None`
    """
    triangle_path = _find_triangle_executable()
    cmd = f'"{triangle_path}" -{triangle_cmd} "{input_path}"'

    # Instantiate a new subprocess
    _log.info('Running Triangle: %s', cmd)
    kwargs: Dict[str, Any] = {}
    if os.name == 'nt':
        kwargs.update({'creationflags': subprocess.CREATE_NO_WINDOW})
    else:
        # TODO: The explicit "shell=True" flag risks shell injection, in
        # particular if we add generic arguments as part of this call. Double-
        # check if this flag is really needed on Linux and MacOS as it is an
        # ongoing security consideration.
        kwargs.update({'shell': True})

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               universal_newlines=True, **kwargs)
    _log.debug('Triangle subprocess spawned (PID %d)', process.pid)
    stdout = process.stdout
    assert stdout is not None
    try:
        for line in iter(stdout.readline, ''):
            _log.debug('Subprocess: %s', line.rstrip())
            if redirect_stdout is not None:
                redirect_stdout(line)
    finally:
        stdout.close()
    return_code = process.wait()
    _log.debug('Triangle subprocess exited with return code %d', return_code)
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def triangulate(nodes: Collection[Node], segments: Collection[Segment],
                holes: Optional[Collection[HoleMarker]] = None,
                regions: Optional[Collection[RegionMarker]] = None,
                write_markers: bool = False,
                triangle_io_dir: Optional[Union[str, pathlib.Path]] = None,
                triangle_cmd: str = 'p',
                redirect_stdout: Union[Callable[[str], None], None] = _print,
                ) -> pathlib.Path:
    """Run the Triangle executable on the given input geometries.

    :param nodes: The nodes of the input geometry.
    :type nodes: :class:`collections.abc.Collection` [
        :class:`Node`]
    :param segments: The segments of the input geometry.
    :type segments: :class:`collections.abc.Collection` [
        :class:`Segment`]
    :param holes: The holes of the input geometry.
    :type holes: :class:`collections.abc.Collection` [
        :class:`HoleMarker`] | :obj:`None`
    :param regions: The regions of the input geometry.
    :type regions: :class:`collections.abc.Collection` [
        :class:`RegionMarker`] | :obj:`None`
    :param write_markers: Whether to write boundary markers in the
        input files. A marker of 0 is used if no marker is given for a
        given node or segment.
    :type write_markers: :class:`bool`
    :param triangle_io_dir: The directory to write the Triangle input
        and output files to. If None, a temporary directory is created
        and will be deleted when Python exits.
    :type triangle_io_dir:
        :class:`pathlib.Path` | :class:`str` | :obj:`None`
    :param triangle_cmd: Command string to pass to Triangle.
    :type triangle_cmd: :class:`str`
    :param redirect_stdout: Function to call with each line of output.
    :type redirect_stdout: :class:`collections.abc.Callable` [
        [:class:`str`], :obj:`None`] | :obj:`None`
    :return: The stem of the Triangle output files. If the stem is
        ``box.1``, the files may be named ``box.1.node`` and
        ``box.1.ele``. 
    :rtype: :class:`pathlib.Path`
    """
    _log.info('Triangle run requested')

    # Find executables
    _log.debug('Locating executable for operating system "%s" (%s)' % (
        os.name, ', '.join(platform.architecture())))

    # Set up the directory containing the triangle input and output files
    if isinstance(triangle_io_dir, str):
        triangle_io_dir = pathlib.Path(triangle_io_dir)
    if triangle_io_dir is None:
        # Create temporary directory
        triangle_io_dir = pathlib.Path(tempfile.mkdtemp())
        # Schedule temporary directory for deletion on exit
        atexit.register(functools.partial(_clear_dir, triangle_io_dir))
    triangle_io_dir.mkdir(parents=True, exist_ok=True)

    # Generate input file
    _log.debug('Generating input file')
    input_path = triangle_io_dir / _get_input_filename('poly')
    write_poly(input_path, nodes, segments, holes, regions, write_markers)

    # Run Triangle
    run_triangle(input_path, triangle_cmd, redirect_stdout)

    # Open output
    return _get_output_path(input_path)


def _clear_dir(path: pathlib.Path) -> None:
    """Delete a directory and all its contents.

    :param path: The directory to delete.
    :type path: :class:`pathlib.Path`
    """
    if not path.exists():
        return
    for entry in path.iterdir():
        if entry.is_dir():
            _clear_dir(entry)
        else:
            try:
                entry.unlink()
            except PermissionError:
                print(f'Unable to delete temporary file {entry}')
    try:
        path.rmdir()
    except OSError:
        print(f'Unable to delete temporary directory {path}')


def _find_triangle_executable() -> pathlib.Path:
    """Find the appropriate Triangle executable for this system."""

    # Microsoft Windows (NT)
    if os.name == 'nt':
        filename = 'triangle_32.exe'
    # Unix-like systems (Linux, MacOS, BSD, etc.)
    elif os.name == 'posix':
        # MacOS
        if platform.system() == 'Darwin':
            raise NotImplementedError('MacOS not yet supported')
        # Linux
        if '32bit' in platform.architecture():
            filename = 'triangle_linux_32'
        else:
            filename = 'triangle_linux_64'
    # Other (unsupported)
    else:
        raise NotImplementedError(f'Unsupported operating system: {os.name}')

    # Look for executable
    triangle_path = _TRIANGLE_BIN / filename
    if not os.path.isfile(triangle_path):
        raise RuntimeError(f'Unable to locate executable "{triangle_path}"')
    # Set executable flag for unix systems
    if os.name == 'posix':
        os.chmod(triangle_path, stat.S_IXUSR)
    _log.info('Compatible Triangle binary found: %s', filename)
    return triangle_path


def _get_input_filename(suffix: str) -> str:
    """Generate a unique base filename for Triangle input files."""
    if not suffix.startswith('.'):
        suffix = f'.{suffix}'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'triangle_{timestamp}{suffix}'


def _get_output_path(input_path: pathlib.Path) -> pathlib.Path:
    """Determine the name of the Triangle output files.

    This only returns the base name, e.g. ``example.1``. The extensions
    ``.node``, ``.ele``, or ``.neigh`` must be added by the caller
    using :math:`pathlib.Path.with_suffix`.

    :param input_path: The input file name.
    :type input_path: :class:`pathlib.Path`
    :return: The base name of the output files.
    :rtype: :class:`pathlib.Path`
    """
    # Strip extension
    base_name = input_path.with_suffix('')
    # Determine current iteration number
    try:
        iter_num = int(base_name.suffix[1:])
    except ValueError:
        iter_num = 0
    # Increment iteration number
    iter_num += 1
    # Return new base name
    return base_name.with_suffix(f'.{iter_num}')
