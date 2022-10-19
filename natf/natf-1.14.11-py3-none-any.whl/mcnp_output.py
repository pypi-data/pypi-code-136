#!/usr/bin/env python3
# -*- coding:utf-8 -*- import numpy as np import re
import argparse
import re
import os
from natf.cell import get_cell_index, Cell, get_cell_index_by_mid
from natf import utils
from natf import mcnp_input


def is_tally_result_start(line, tally_num=None):
    """
    Check whether a line is the tally result start.

    Parameters:
    -----------
    line: str
        The line to be checked.
    tally_num: int or None
        None: Check this is the start of any tally
        int: Check for the specific tally number.
    """
    tally_start_pattern = re.compile("^1tally .*nps =", re.IGNORECASE)
    if re.match(tally_start_pattern, line):
        # check tally id
        if tally_num is None:
            return True
        else:
            return get_tally_id(line) == tally_num
    else:
        return False


def is_tally_result_end(line):
    tally_end_pattern1 = re.compile(".*tfc bin check", re.IGNORECASE)
    tally_end_pattern2 = re.compile(".*===", re.IGNORECASE)
    if re.match(tally_end_pattern1, line) or re.match(tally_end_pattern2, line):
        return True
    else:
        return False


def get_tally_id(line):
    if not is_tally_result_start(line):
        raise ValueError(f"line: {line} is not tally result start")
    line_ele = line.strip().split()
    return int(line_ele[1])


def has_tally_result(filename, tally_num=[4]):
    """Check whether the file contain specific tally result"""
    if filename is None or filename == '':
        return False
    if not os.path.isfile(filename):
        return False
    if isinstance(tally_num, int):
        tally_num = [tally_num]
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                return False
            if is_tally_result_start(line):
                if get_tally_id(line) in tally_num:
                    return True
    return False


def get_tally_file(mcnp_output, continue_output, tally_number):
    """
    Check which file to use when both mcnp_output and continue_output are provided.
    """
    # check tally results
    if has_tally_result(mcnp_output, tally_number) and \
            not has_tally_result(continue_output, tally_number):
        return mcnp_output
    if has_tally_result(continue_output, tally_number):
        print(f"Tally {tally_number} results in {continue_output} will be used")
        return continue_output
    if not has_tally_result(mcnp_output, tally_number) and \
            not has_tally_result(continue_output, tally_number):
        raise ValueError(
            f"ERROR: {mcnp_output} and {continue_output} do not have tally result")


def get_cell_names_from_line(line):
    """
    """
    cell_names = []
    ls = line.strip().split()
    for i in range(1, len(ls)):
        cell_names.append(int(ls[i]))
    return cell_names


def read_tally_result_single_cell_single_group(filename, tally_num=4, with_fm=False):
    """
    Get the result for a tally that has only single cell, single energy group and with FM card.
    This can be used for the tbr calculation for new tallies.

    Parameters:
    -----------
    filename: str
        the mcnp output file to be read
    tally_number: int
        tally number
    """
    cids, results, errs = [], [], []
    dumped_nps = get_dumped_nps(filename)
    fin = open(filename)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                f'1tally {tally_num} not found in the file, wrong file!')
        if not is_tally_result_start(line):
            continue
        # check nps
        nps = float(line.strip().split()[-1])
        if nps < dumped_nps[-1]:
            continue
        if get_tally_id(line) == tally_num:
            while True:
                line1 = fin.readline()
                line_ele1 = line1.split()
                if utils.is_blank_line(line1):
                    continue
                if is_tally_result_end(line1):
                    break
                if " cell " in line1:
                    cid = get_cell_names_from_line(line1)
                    cids.extend(cid)
                    line = fin.readline()
                    if with_fm:
                        line = fin.readline()
                    line_ele = line.split()
                    for j in range(len(cid)):
                        results.append(float(line_ele[2 * j]))
                        errs.append(float(line_ele[2 * j + 1]))
            break
    fin.close()
    return cids, results, errs


def read_tally_result_single_group(filename, tally_num=4):
    """
    Get the single group neutron flux for a tally.
    This is used for the volume calculation.

    Parameters:
    -----------
    filename: str
        the mcnp output file to be read
    tally_number: int
        tally number
    """
    cids, results, errs = [], [], []
    dumped_nps = get_dumped_nps(filename)
    fin = open(filename)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                f'1tally {tally_num} not found in the file, wrong file!')
        if not is_tally_result_start(line):
            continue
        # check nps
        nps = float(line.strip().split()[-1])
        if nps < dumped_nps[-1]:
            continue
        if get_tally_id(line) == tally_num:
            while True:
                line1 = fin.readline()
                line_ele1 = line1.split()
                if utils.is_blank_line(line1):
                    continue
                if is_tally_result_end(line1):
                    break
                if " cell " in line1:
                    cid = get_cell_names_from_line(line1)
                    cids.extend(cid)
                    line = fin.readline()
                    if 'multiplier' in line:
                        line = fin.readline()
                    line_ele = line.split()
                    for j in range(len(cid)):
                        results.append(float(line_ele[2 * j]))
                        errs.append(float(line_ele[2 * j + 1]))
            break
    fin.close()
    return cids, results, errs


def get_dumped_nps(filename):
    """
    Get the dumped nps.

    Parameters:
    -----------
    filename : str
        The mcnp output file

    Returns:
    --------
    dumped_nps : list
        The list of dumped nps
    """
    dumped_nps = []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '' or 'computer time =' in line:
                break
            if is_tally_result_start(line):
                nps = float(line.strip().split()[-1])
                if nps not in dumped_nps:
                    dumped_nps.append(nps)
            else:
                continue
    if len(dumped_nps) == 0:
        raise ValueError(f"file {filename} does not have valid dumped nps")
    print(f"    the dumped nps in {filename} are {dumped_nps}")
    return dumped_nps


def read_cell_neutron_flux_single_tally(filename, tally_num=4, n_group_size=175):
    """
    Get the neutron flux for a single tally.

    Parameters:
    -----------
    filename: str
        the mcnp output file to be read
    tally_number: int
        tally number
    n_group_size: int
        Number of group size, 69, 175, 315 or 709.
    """
    cids, fluxes, errs = [], [], []
    dumped_nps = get_dumped_nps(filename)
    fin = open(filename)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                f'1tally {tally_num} not found in the file, wrong file!')
        if not is_tally_result_start(line):
            continue
        # check nps
        nps = float(line.strip().split()[-1])
        if nps < dumped_nps[-1]:
            continue
        if get_tally_id(line) == tally_num:
            while True:
                line1 = fin.readline()
                line_ele1 = line1.split()
                if utils.is_blank_line(line1):
                    continue
                # end of the cell neutron flux information part
                if is_tally_result_end(line1):
                    break
                if 'cell' in line1:
                    line2 = fin.readline()
                    if 'energy' in line2:  # the folowing 176/710 lines are neutron flux information
                        cid = get_cell_names_from_line(line1)
                        cids.extend(cid)
                        cell_flux = []
                        cell_error = []
                        if n_group_size >= 2:
                            num_data = n_group_size + 1
                        else:
                            raise ValueError(
                                f"Wrong n_group_size:{n_group_size}")
                        for i in range(num_data):
                            line = fin.readline()
                            # check the neutron energy group
                            if i == n_group_size:
                                if 'total' not in line:
                                    errormessage = ''.join(
                                        [
                                            'ERROR in reading cell neutron flux\n',
                                            'Neutron energy group is ',
                                            str(n_group_size),
                                            ' in input file\n',
                                            'But keyword: \'total\' not found in the end!\n',
                                            'Check the neutron energy group in the output file\n'])
                                    raise ValueError(errormessage)
                            line_ele = line.split()
                            erg_flux = []
                            erg_error = []
                            for j in range(len(cid)):
                                erg_flux.append(float(line_ele[2 * j + 1]))
                                erg_error.append(float(line_ele[2 * j + 2]))
                            cell_flux.append(erg_flux)
                            cell_error.append(erg_error)
                        for i in range(len(cid)):
                            temp_flux = []
                            temp_error = []
                            for j in range(num_data):
                                temp_flux.append(cell_flux[j][i])
                                temp_error.append(cell_error[j][i])
                            fluxes.append(temp_flux)
                            errs.append(temp_error)
            break
    fin.close()
    print(
        f"    finish reading neutron flux from {filename} tally {tally_num} at nps of {nps:.5E}")
    return cids, fluxes, errs


def tallied_vol_to_tally(inp="outp", output="tally_card.txt", n_group_size=175):
    """
    Read the f4 tally for volume, get the cids, vols, errs info and write
    tally card.
    """
    tallied_vol_to_tally_help = ('This script read a volume tally output file and\n'
                                 'return a tally style string.\n')

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="outp",
                        help="output of the vol tally file path, default: outp")
    parser.add_argument("-o", "--output", required=False, default="tally_card.txt",
                        help="save the tally_card to output file, default: tally_card.txt")
    parser.add_argument("-t", "--tally_num", required=False, default=4,
                        help="the tally number of volume info, default: 4")
    parser.add_argument("-g", "--group", required=False, default=175,
                        help="the neutron energy group used in tally, default: 175")

    args = vars(parser.parse_args())

    outp_file = args['input']
    tally_num = int(args['tally_num'])
    e_group_size = 175
    if args['group'] is not None:
        e_group_size = int(args['group'])
    e_groups = utils.get_e_group(e_group_size, reverse=False)

    cids, vols, errs = read_tally_result_single_group(
        outp_file, tally_num=tally_num)
    # check calculated vol
    zero_vol_cids = []
    large_err_cids = []
    for i in range(len(cids)):
        if vols[i] <= 0.0:
            zero_vol_cids.append(cids[i])
        if errs[i] >= 0.05:
            large_err_cids.append(cids[i])
    # remove zero vol from tally card
    if len(zero_vol_cids) > 0:
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=f'  ERROR: {len(zero_vol_cids)} cells have invalid (0.0) vols:', cids=zero_vol_cids)
        print(warn_str)
        new_cids = []
        new_vols = []
        new_errs = []
        for i in range(len(cids)):
            if vols[i] > 0.0:
                new_cids.append(cids[i])
                new_vols.append(vols[i])
                new_errs.append(errs[i])
        cids = new_cids
        vols = new_vols
        errs = new_errs
    if len(large_err_cids) > 0:
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=f"  warning: {len(large_err_cids)} cells have large relative error:", cids=large_err_cids)
    # save valid data into a tally style card
    output = "tally_card.txt"
    if args['output'] is not None:
        output = args['output']
    mcnp_input.mcnp_tally_style(
        cids, sds=vols, output=output, e_group_size=e_group_size)


def update_cell_flux(cells, cids, fluxes, dict_cid_idx=None):
    """
    Update the cell volume according to the given cids and volumes.
    """
    for i in range(len(cids)):
        cidx = get_cell_index(cells, cids[i], dict_cid_idx=dict_cid_idx)
        cells[cidx].neutron_flux = fluxes[i]
    return cells


@utils.log
def get_cell_neutron_flux(mcnp_output, cells, tally_number, n_group_size, continue_output=None, dict_cid_idx=None):
    """get_cell_neutron_flux: read the mcnp output file and get the neutron flux of the cell

    Parameters:
    -----------
    mcnp_output: str
        the mcnp output file
    cells: list
        the list of Cell
    tally_number: int
        tally number
    n_group_size: int
        Number of group size, 69, 175, 315 or 709.
    continue_output: str, optional
       The output file of continue run, contains neutron flux info. Used when
       the mcnp_output file does not contian neutron flux info.

    Returns:
    --------
    cells: list
        cells that have the neutron flux information in it
    """
    tally_file = get_tally_file(mcnp_output, continue_output, tally_number)
    if isinstance(tally_number, int):
        cids, fluxes, errs = read_cell_neutron_flux_single_tally(
            tally_file, tally_number, n_group_size)
        cells = update_cell_flux(
            cells, cids, fluxes, dict_cid_idx=dict_cid_idx)
    elif isinstance(tally_number, list):
        for i in range(len(tally_number)):
            cids, fluxes, errs = read_cell_neutron_flux_single_tally(
                tally_file, tally_number[i], n_group_size)
            cells = update_cell_flux(
                cells, cids, fluxes, dict_cid_idx=dict_cid_idx)
    print('    read cell neutron flux completed')
    return cells


def read_cell_vol_single_tally(filename, tally_num):
    """
    Read the cell, volume and mass information for specific tally.
    """
    cids, vols = [], []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                raise ValueError(
                    f'tally result not found in the file, wrong file!')
            if is_tally_result_start(line, tally_num):
                # read the following line
                line = fin.readline()
                line = fin.readline()
                line = fin.readline()
                line = fin.readline()
                while True:
                    line = fin.readline()
                    line_ele = line.split()
                    if len(line_ele) == 0:  # end of the volumes
                        break
                    # otherwise, there are volume information
                    if line_ele[0] == 'cell:':  # this line contains cell names
                        cell_names = get_cell_names_from_line(line)
                        line = fin.readline()  # this is the volume information
                        line_ele = line.split()
                        cell_vols = get_cell_vols_from_line(line)
                        cids.extend(cell_names)
                        vols.extend(cell_vols)
                break
    return cids, vols


def update_cell_vol(cells, cids, vols, dict_cid_idx=None):
    """
    Update the cell volume according to the given cids and volumes.
    """
    for i in range(len(cids)):
        cidx = get_cell_index(cells, cids[i], dict_cid_idx=dict_cid_idx)
        cells[cidx].vol = vols[i]
    return cells


@utils.log
def get_cell_vol_mass(mcnp_output, cells, tally_number, continue_output=None,
                      dict_cid_idx=None, verbose=True):
    """
    Read the mcnp output file and get the volumes and masses defined in SD cards.

    Parameters:
    -----------
    mcnp_output : string
        The mcnp output file
    cells : list of Cell
        The cells list
    tally_number : int or list of int
        The tally numbers
    continue_output : string
        The output filename of continue run
    dict_cid_idx: dict
        The cell id index dict
    verbose: bool
        Whether to print warning messages

    Returns:
    --------
    cells : list of Cell
        The cells with updated volume and mass
    """

    # open the mcnp output file
    tally_file = get_tally_file(mcnp_output, continue_output, tally_number)
    if isinstance(tally_number, int):
        cids, vols = read_cell_vol_single_tally(tally_file, tally_number)
        cells = update_cell_vol(cells, cids, vols, dict_cid_idx=dict_cid_idx)
    elif isinstance(tally_number, list):
        for i in range(len(tally_number)):
            cids, vols = read_cell_vol_single_tally(
                tally_file, tally_number[i])
            cells = update_cell_vol(
                cells, cids, vols, dict_cid_idx=dict_cid_idx)

    # update the mass of the cells
    cids_invalid_vol = []
    for c in cells:
        if c.vol > 0:
            c.mass = c.density * c.vol
        else:
            cids_invalid_vol.append(c.id)
    if verbose:
        warn_title = '    warning: cells without valid vol/mass:'
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=warn_title, cids=cids_invalid_vol)
        print(warn_str)
    return cells


@utils.log
def get_cell_tally_info(mcnp_output, cells, tally_number, n_group_size,
                        continue_output=None, dict_cid_idx=None):
    """get_cell_tally_info: run this only for the cell tally condition"""
    cells = get_cell_vol_mass(mcnp_output, cells, tally_number,
                              continue_output=continue_output, dict_cid_idx=dict_cid_idx)
    cells = get_cell_neutron_flux(mcnp_output, cells, tally_number,
                                  n_group_size, continue_output=continue_output, dict_cid_idx=dict_cid_idx)
    return cells


def get_cell_vols_from_line(line):
    cell_vols = []
    ls = line.strip().split()
    for i in range(len(ls)):
        cell_vols.append(float(ls[i]))
    return cell_vols


def is_cell_info_start(line):
    """
    Check if this line is the cells info start.
    """
    # This check works for MCNP5 1.2
    if "cells" in line and "print table 60" in line:
        return True
    else:
        return False


@utils.log
def get_cell_basic_info(mcnp_output):
    """
    Get the basic information of cells.
    The basic info include:
        - icl : the problem number (index) of the cell
        - id : the id (named by user in input file) of the cell
        - mid : material id (named by user) of the cell
        - gram density : the material density in [g/cm3]
        - vol : the volume calculated by mcnp
        - mass : the mass calculated by mcnp
        - imp_n : the neutron importance

    Parameters:
    -----------
    mcnp_output : string
        The mcnp outp file. It contains '1cells' info

    Returns:
    --------
    cells : list of Cell
        The list of cells in the problem.
    """

    cells = []
    fin = open(mcnp_output, 'r')
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError('1cells not found in the file, wrong file!')
        if is_cell_info_start(line):  # read 1cells
            # read the following line
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            while True:
                temp_c = Cell()
                line = fin.readline()
                if ' total' in line:  # end of the cell information part
                    break
                # check data
                line_ele = line.split()
                if len(line_ele) == 0:  # skip the blank line
                    continue
                if str(line_ele[0]).isdigit():  # the first element is int number
                    temp_c.icl = int(line_ele[0])
                    temp_c.id = int(line_ele[1])
                    temp_c.mid = int(line_ele[2])
                    temp_c.density = float(line_ele[4])
                    temp_c.vol = float(line_ele[5])
                    temp_c.mass = float(line_ele[6])
                    temp_c.imp_n = float(line_ele[8])
                    if len(line_ele) >= 10:
                        temp_c.imp_p = float(line_ele[9])
                cells.append(temp_c)
            break
    fin.close()
    return cells


def get_mid_nucs_fracs(line):
    """
    Get the material id, nuclide list and fraction.
    """
    tokens = line.strip().split()
    mid = int(tokens[0])
    nucs, fracs = [], []
    for i in range(1, len(tokens), 2):
        nucs.append(tokens[i][:-1])
        fracs.append(float(tokens[i+1]))
    return mid, nucs, fracs


def get_nucs_fracs(line):
    """
    Get the material nuclide list and fraction.
    """
    tokens = line.strip().split()
    nucs, fracs = [], []
    for i in range(0, len(tokens), 2):
        nucs.append(tokens[i][:-1])
        fracs.append(float(tokens[i+1]))
    return nucs, fracs


def get_material_basic_info(mcnp_output):
    """
    Get the basic information of the material.
    - mat_number
    - density
    - nuc_vec: dict of nuclide/mass_fraction pair
    """
    cells = get_cell_basic_info(mcnp_output)
    # get used materials ids
    mids, densities, nuc_vecs = [], [], []
    mid = 0
    # read material composition
    with open(mcnp_output, 'r', encoding='utf-8') as fin:
        while True:
            line = fin.readline()
            if line == '':
                raise ValueError("material composition not found in the file")
            if 'number     component nuclide, mass fraction' in line:  # start of material composition
                while True:
                    line = fin.readline()
                    if 'cell volumes and masses' in line:  # end of material composition
                        # save the last material
                        mids.append(mid)
                        cidx = get_cell_index_by_mid(cells, mid)
                        densities.append(cells[cidx].density)
                        nuc_vecs.append(nuc_vec)
                        break
                    if utils.is_blank_line(line) or 'warning' in line:
                        continue
                    tokens = line.strip().split()
                    if len(tokens) % 2 != 0:  # this line contain mid
                        if mid > 0:  # not the first material, save the previous one
                            mids.append(mid)
                            cidx = get_cell_index_by_mid(cells, mid)
                            densities.append(cells[cidx].density)
                            nuc_vecs.append(nuc_vec)
                        nuc_vec = {}
                        mid, nucs, fracs = get_mid_nucs_fracs(line)
                    else:  # this line do not have mid
                        nucs, fracs = get_nucs_fracs(line)
                    # update the nuc_vec
                    for i, nuc in enumerate(nucs):
                        if nuc not in nuc_vec.keys():
                            nuc_vec[nuc] = fracs[i]
                        else:
                            nuc_vec[nuc] += fracs[i]
                break
    return mids, densities, nuc_vecs


def get_tbr_from_mcnp_output(filename, tallies):
    """
    Read the MCNP output file to get the tbr.
    The TBR for each breeder cells may distributed in difference tallies.

    Parameters:
    -----------
    filename: str
        The MCNP output file.
    tallies: list of int
        The tally number that contains TBR information.
    """
    tbr_total = 0.0
    for tid in tallies:
        cids, tbr_tmps, errs = read_tally_result_single_cell_single_group(
            filename, tally_num=tid, with_fm=True)
        tbr_total += tbr_tmps[0]
    return tbr_total


def read_cpu_time(filename):
    """
    read the mcnp output file to get the cpu time

    Returns:
    cpu_time : float
        The CPU time in [minutes]
    """
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            # start read data
            if "computer time =" in line:
                row = line.split('=')
                cpu_time = float(row[-1].split()[0])
                break
    return cpu_time


def ptrac_to_hdf5(ptrac_filename):
    """
    Convert binary ptrac file to hdf5 format.
    """
    from pyne import mcnp
    import tables
    ptrac = mcnp.PtracReader(ptrac_filename)
    hdf5_filename = f"{ptrac_filename}.h5"

    # open HDF5 file and create table if it doesn't exist yet
    h5file = tables.open_file(hdf5_filename, mode="a",
                              title=ptrac.problem_title)
    table_name = 'ptrac'
    table_title = 'Ptrac data'
    table_path = "/" + table_name
    if table_path in h5file:
        table = h5file.get_node(table_path)
    else:
        table = h5file.create_table(
            "/", table_name, mcnp.PtracEvent, table_title)

    print("Writing ptrac.h5 ...")
    ptrac.write_to_hdf5_table(table, print_progress=1000000)

    table.flush()
    h5file.close()
