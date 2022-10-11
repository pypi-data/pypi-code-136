#!/usr/bin/env python

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

"""Command line script for the BASEchange channel generator.

This script exposes the core functionality of the BASEchange submodule
and allows the creation of 1D channel geometries from the given input
parameters.

Run this script with the "--help" for additional information and
detailed argument descriptions.
"""

import argparse
import datetime
import sys
import typing

if typing.TYPE_CHECKING:
    from basechange import factories, BaseChainWriter, __version__ as version
else:
    try:
        from basechange import (
            factories, BaseChainWriter, __version__ as version)
    except ImportError:
        from basemesh.basechange import (
            factories, BaseChainWriter, __version__ as version)

from basemesh.triangle import RegionMarker

SKETCH = r"""

  ┌─ DX ─┐      ┌ DXT ┐    ┌─ DXW ─┐
  |      |      |     |
  |      |      |     |    *****************
  |      |      |      ****·   |   ·       ·****
                   ****    ·   |   ·       ·    ****
  *****************   ·    ·   |   ·       ·    ·   ****************
  ·  |   ·      ·     ·    ·   |   ·       ·    ·    ·  |   ·      ·
  ·  WC  ·      ·     ·    ·   WW  ·       ·    ·    ·  WC  ·      ·
  ·  |   ·      ·     ·    ·   |   ·       ·    ·    ·  |   ·      ·
  *****************   ·    ·   |   ·       ·    ·   ****************
                   ****    ·   |   ·       ·    *\**
   \           /       ****·   |   ·       ·****  \
    \___ N ___/            *****************       \
                                                 NT: Number of interpolated
                            \             /      transition cross sections
                             \___ NW ____/

"""


if __name__ == '__main__':
    print('\n'
          '---------------------------------------\n'
          f'BASEchange - Version {version}\n'
          '---------------------------------------\n')

    # Set up argument parser
    parser = argparse.ArgumentParser(
        'BASEchange', description=SKETCH,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '--version', action='version')

    # Core options
    group = parser.add_argument_group(
        'channel definition', description='Core options for defining a '
        '1D channel geometry')

    group.add_argument(
        '-DX', metavar='dx', dest='dx', default=40.0, type=float,
        help='inter-cross-sectional distance for the channel '
             '(default %(default)s)')
    group.add_argument(
        '-N', metavar='num_cs', dest='num_cs', default=10, type=int,
        help='number of cross sections for the channel. When setting the '
             '--widening flag, this value is used for the first and last '
             'section of the channel (default %(default)s)')
    group.add_argument(
        '-S', metavar='slope_channel', dest='slope_channel', default='0.0015',
        type=float, help='channel slope [m] (default %(default)s)')
    group.add_argument(
        '-WC', metavar='bed_width', dest='bed_width', default=50.0, type=float,
        help='channel bed width [m] (default: %(default)s)')
    group.add_argument(
        '-B', metavar='slope_banks', dest='slope_banks', default='1.0',
        type=float, help='slope of channel banks [h:v] (default: %(default)s)')
    group.add_argument(
        '-H', metavar='height', dest='height', default=5.0, type=float,
        help='height of the floodplain relative to the channel bed [m] '
             '(default: %(default)s)')

    # Frictions
    group.add_argument(
        '-KS', metavar='ks_bed', dest='ks_bed', default=35.0, type=float,
        help='channel bed Strickler friction value [m^(1/3)/s] '
             '(default %(default)s)')
    group.add_argument(
        '-KSB', metavar='ks_banks', dest='ks_banks', default=20.0, type=float,
        help='channel banks Strickler friction value [m^(1/3)/s] '
             '(default %(default)s)')

    # Offsets
    group.add_argument(
        '-X', metavar='offset_x', dest='offset_x', default=0.0, type=float,
        help='channel offset along flow axis [m] (default: %(default)s)')
    group.add_argument(
        '-Z', metavar='offset_z', dest='offset_z', default=0.0, type=float,
        help='reference elevation for the channel bed [m] '
             '(default: %(default)s)')
    group.add_argument(
        '-MPS', metavar='mp_shift', dest='mp_shift', default=0.5, type=float,
        help='relative position of the channel bank midpoint '
             '(default: %(default)s)')

    # Widening options
    group = parser.add_argument_group(
        'widening options', description='Additional options for channels '
        'featuring a widening')
    group.add_argument(
        '-W', '--widening', dest='widening', action='store_true',
        help='include widening; other arguments in this group are only used '
             'if this flag was set (default %(default)s)')
    group.add_argument(
        '-WW', metavar='w_bed_width', dest='w_bed_width', default=100.0,
        type=float, help='bed width of the widened section [m] '
        '(default: %(default)s)')
    group.add_argument(
        '-KSW', metavar='w_ks_bed', dest='w_ks_bed', default=30.0, type=float,
        help='widening and transitionings Strickler value [m^(1/3)/s] '
             '(default %(default)s)')
    group.add_argument(
        '-KSWB', metavar='w_ks_banks', dest='w_ks_banks', default=20.0,
        type=float, help='widening and transitionings Strickler value '
        'for the banks [m^(1/3)/s] (default %(default)s)')
    group.add_argument(
        '-DXW', metavar='w_dx', dest='w_dx', default=30.0, type=float,
        help='inter-cross-sectional distance for the widening '
        '(default %(default)s)')
    group.add_argument(
        '-NW', metavar='w_num_cs', dest='w_num_cs', default=5, type=int,
        help='number of cross sections for the widening '
        '(default %(default)s)')
    group.add_argument(
        '-DXT', metavar='t_dx', dest='t_dx', default=20.0, type=float,
        help='inter-cross-sectional distance for the transitions '
        '(default %(default)s)')
    group.add_argument(
        '-NT', metavar='t_num_cs', dest='t_num_cs', default=3, type=int,
        help='number of cross sections per transition '
        '(default %(default)s)')

    # File input
    parser.add_argument(
        '-F', '--file', type=str, default='',
        help='a CSV file specifying custom parameters based on a '
        'cross section\'s distance_coord')

    # Output options
    output = parser.add_argument_group(
        'output options', description='Options controlling the generated '
        'output files')
    output.add_argument(
        '--2D', dest='output_2dm', action='store_true',
        help='generate 2DM mesh instead of 1D channel (default: %(default)s)')
    output.add_argument(
        '--BED', dest='bed', action='store_true',
        help='include a SOILDEF block in the output (default: %(default)s)')
    output.add_argument(
        '-BS', metavar='bed_start', dest='bed_start', default=3, type=int,
        help='starting index for channel bed definition [-] '
        '(default: %(default)s)')

    output.add_argument(
        '--R', '--reverse', dest='reverse', action='store_true',
        help='reverse cross section order (default: %(default)s)')
    output.add_argument(
        '-CS', metavar='prefix', dest='prefix', default='CS_', type=str,
        help='cross section name prefix (default: %(default)s)')
    output.add_argument(
        '--precision', default=2, type=int,
        help='limit coordinate precision to N decimal places, set to '
        'a negative value to disable (default: %(default)s)')

    # Parse user input
    args = parser.parse_args()

    # Set up channel factory
    factory: factories.AbstractChannelFactory
    if args.file:
        if args.widening:
            print('BASEchange: error: The --file and --widening flags are '
                  'mutually exclusive')
            sys.exit(1)
        factory = factories.TabulatedFactory(
            filepath=args.file,
            dist_cs=args.dx,
            num_cs=args.num_cs,
            bed_width=args.bed_width,
            height=args.height,
            bed_slope=args.slope_channel,
            bank_slope=args.slope_banks,
            friction_bed=args.ks_bed,
            friction_bank=args.ks_banks,
            midpoint_shift=args.mp_shift,
            raise_by=args.offset_z)

    elif args.widening:
        factory = factories.TrapezoidalChannelWidening(
            dist_cs=args.dx,
            num_cs=args.num_cs,
            bed_width=args.bed_width,
            height=args.height,
            bed_slope=args.slope_channel,
            bank_slope=args.slope_banks,
            friction_bed=args.ks_bed,
            friction_bank=args.ks_banks,
            # Start of widening args
            widening_bed_width=args.w_bed_width,
            widening_friction_banks=args.w_ks_banks,
            widening_friction=args.w_ks_bed,
            widening_dist_cs=args.w_dx,
            widening_num_cs=args.w_num_cs,
            transition_dist_cs=args.t_dx,
            transition_num_cs=args.t_num_cs,
            # End of widening args
            midpoint_shift=args.mp_shift,
            raise_by=args.offset_z)
    else:
        factory = factories.TrapezoidalChannel(
            dist_cs=args.dx,
            num_cs=args.num_cs,
            bed_width=args.bed_width,
            height=args.height,
            bed_slope=args.slope_channel,
            bank_slope=args.slope_banks,
            friction_bed=args.ks_bed,
            friction_bank=args.ks_banks,
            midpoint_shift=args.mp_shift,
            raise_by=args.offset_z)

    geometry = factory.build_channel()
    geometry.name = 'geometry'
    # Update cross sections
    print('Processing cross sections...')
    prefix = str(args.prefix)
    for index, cs_ in enumerate(geometry.cross_sections):
        cs_.flow_axis_coord += args.offset_x
        cs_.name = f'{prefix}{index+1}'
        cs_.angle = 90.0
        if args.precision >= 0:
            cs_.limit_coordinate_precision(args.precision)

        # Define bottom range
        if args.bed:
            offset: int = args.bed_start
            vtx_count = len(cs_.vertices)
            cs_.bottom_slice = offset, vtx_count-offset
            cs_.soil_defs[1] = offset, vtx_count-offset

    if args.output_2dm:
        print('Writing 2D mesh geometry...')

        # Create MATID markers for all channel sections
        region_markers: typing.List[RegionMarker] = []
        for index, cs_ in enumerate(geometry.cross_sections[:-1]):
            next_cs = geometry.cross_sections[index+1]
            dist = cs_.flow_axis_coord + (
                next_cs.flow_axis_coord - cs_.flow_axis_coord) * 0.5
            offsets_bank_r: typing.List[float] = []
            for v_a, v_b in zip(cs_.vertices[4:7], next_cs.vertices[4:7]):
                offsets_bank_r.append((v_a.pos[0] + v_b.pos[0]) * 0.5)
            # Coordinates of the markers to create (right side only)
            marker_bank_bot = (offsets_bank_r[0] + offsets_bank_r[1]) * 0.5
            marker_bank_top = (offsets_bank_r[1] + offsets_bank_r[2]) * 0.5
            # Check whether this marker falls inside a widened cell
            this_bed_width = cs_.vertices[-3].pos[0] - cs_.vertices[2].pos[0]
            next_bed_width = (
                next_cs.vertices[-3].pos[0] - next_cs.vertices[2].pos[0])
            is_widened = (this_bed_width + next_bed_width) / 2 > args.bed_width
            # Region markers to insert
            region_markers.extend(
                (RegionMarker(dist, -marker_bank_top, attribute=3),
                 RegionMarker(dist, -marker_bank_bot, attribute=3),
                 RegionMarker(dist, 0.0, attribute=2 if is_widened else 1),
                 RegionMarker(dist, marker_bank_bot, attribute=3),
                 RegionMarker(dist, marker_bank_top,  attribute=3)))

        mesh = geometry.to_mesh(regions=region_markers)
        mesh.save(f'{prefix}geometry.2dm')

    else:
        print('Writing 1D mesh geometry...')
        with BaseChainWriter(f'{prefix}geometry.bmg') as writer:
            writer.write_channel(geometry)

        print('Writing BASEMENT command file...')
        # Reverse list if required
        cs_numbering = [i+1 for i in range(factory.cs_total)]
        if args.reverse:
            cs_numbering = list(reversed(cs_numbering))
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        filename = f'{prefix.rstrip("_-.")}.bmc'
        with open(filename, 'w', encoding='utf-8') as cmd_file:
            cmd_file.write(
                '// BASEMENT v2.8 command file\n'
                f'// Generated {timestamp} using BASEchange {version}\n'
                'PROJECT {\n}\n'
                'DOMAIN {\n'
                '\tBASECHAIN_1D {\n'
                '\t\tGEOMETRY {\n'
                '\t\t\ttype = basement\n'
                f'\t\t\tfile = {prefix}geometry.bmg\n'
                f'\t\t\tcross_section_order = ('
                + ' '.join((f'{prefix}{i}' for i in cs_numbering))
                + ')\n'
                '\t\t}\n'
                '\t}\n'
                '}\n')
