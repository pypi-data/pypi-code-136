from typing import Any, Dict, Iterable, List, NamedTuple, TextIO, Tuple
from os.path import exists, join as join_path
import numpy as np
from pandas import DataFrame
from ase import Atoms
from ase.units import GPa
from ase.io import read, write


def read_loss(filename: str) -> DataFrame:
    """Parses a file in ``loss.out`` format from GPUMD and returns the
    content as a data frame. More information concerning file format,
    content and units can be found at
    https://gpumd.zheyongfan.org/index.php/The_output_files_for_the_nep_executable#The_loss.out_file.

    Parameters
    ----------
    filename
        input file name

    """
    data = np.loadtxt(filename)
    if isinstance(data[0], np.float64):
        # If only a single row in loss.out, append a dimension
        data = data.reshape(1, -1)
    if len(data[0]) != 10:
        raise ValueError(f'Input file contains {len(data[0])} data columns.'
                         f' Expected 10 columns.')
    tags = 'total_loss L1 L2'
    tags += ' RMSE_E_train RMSE_F_train RMSE_V_train'
    tags += ' RMSE_E_test RMSE_F_test RMSE_V_test'
    generations = range(100, len(data) * 100 + 1, 100)
    df = DataFrame(data=data[:, 1:], columns=tags.split(), index=generations)
    return df


def read_potential(filename: str) -> Tuple[Dict[str, tuple], List[float]]:
    """Parses a file in ``nep.txt`` format from GPUMD and returns the
    content as a tuple of a dict and a list. The dict contains the
    information contained in the header, whereas the list contains the
    weights and rescaling factors.

    Parameters
    ----------
    filename
        input file name

    """
    header = []
    parameters = []
    nheader = 6
    with open(filename) as f:
        for k, line in enumerate(f.readlines()):
            flds = line.split()
            if len(flds) == 0:
                continue
            if k == 0 and 'zbl' in flds[0]:
                nheader += 1
            if k <= nheader:
                header.append(tuple(flds))
            elif len(flds) == 1:
                parameters.append(float(flds[0]))
            else:
                raise IOError(f'Failed to parse line {k} from {filename}')
    settings = {}
    for flds in header:
        if flds[0] in ['cutoff']:
            settings[flds[0]] = tuple(map(float, flds[1:]))
        elif flds[0] in ['zbl', 'n_max', 'l_max', 'ANN', 'basis_size']:
            settings[flds[0]] = tuple(map(int, flds[1:]))
        else:
            settings[flds[0]] = flds[1:]
    return settings, parameters


def _write_structure_in_nep_format(structure: Atoms,
                                   f: TextIO) -> None:
    """Write structure block into a file-like object in format readable by nep executable.

    Parameters
    ----------
    structure
        input structure; must hold information regarding energy and forces
    f
        file-like object to which to write
    """

    # Allowed keyword=value pairs. Use ASEs extyz write functionality.:
    #   lattice="ax ay az bx by bz cx cy cz"                    (mandatory)
    #   energy=energy_value                                     (mandatory)
    #   virial="vxx vxy vxz vyx vyy vyz vzx vzy vzz"            (optional)
    #   weight=relative_weight                                  (optional)
    #   properties=property_name:data_type:number_of_columns
    #       species:S:1                      (mandatory)
    #       pos:R:3                          (mandatory)
    #       force:R:3 or forces:R:3          (mandatory)
    try:
        energy = structure.get_potential_energy()
        structure.get_forces()  # calculate forces to have them on the Atoms object
        structure.info['energy'] = energy
    except RuntimeError:
        raise RuntimeError('Failed to retrieve energy and/or forces for structure')
    if np.isclose(structure.get_volume(), 0):
        raise ValueError('Structure cell must have a non-zero volume!')
    try:
        stress = structure.get_stress(voigt=False).flatten()
        stress = ' '.join([f'{s:.6f}' for s in stress])
        structure.info['stress'] = f'\"{stress}\"'
    except RuntimeError:
        print('Warning: Failed to retrieve stresses for structure')
    write(filename=f, images=structure, write_info=True, format='extxyz')


def write_structures(outfile: str,
                     structures: List[Atoms]) -> None:
    """Writes structures for training/testing in format readable by nep executable.

    Parameters
    ----------
    outfile
        output filename
    structures
        list of structures with energy, forces, and (possibly) stresses
    """
    with open(outfile, 'w') as f:
        for structure in structures:
            _write_structure_in_nep_format(structure, f)


def write_nepfile(parameters: NamedTuple,
                  dirname: str) -> None:
    """Writes parameters file for NEP construction.

    Parameters
    ----------
    parameters
        input parameters; see https://gpumd.zheyongfan.org/index.php/The_nep.in_input_file
    dirname
        directory in which to place input file and links
    """
    with open(join_path(dirname, 'nep.in'), 'w') as f:
        for key, val in parameters.items():
            f.write(f'{key}  ')
            if isinstance(val, Iterable):
                f.write(' '.join([f'{v}' for v in val]))
            else:
                f.write(f'{val}')
            f.write('\n')


def read_nepfile(filename: str) -> Dict[str, Any]:
    """Returns the content of a configuration file (`nep.in`) as a dictionary.

    Parameters
    ----------
    filename
        input file name
    """
    settings = {}
    with open(filename) as f:
        for line in f.readlines():
            flds = line.split()
            if len(flds) == 0:
                continue
            if flds[0].startswith('#'):
                continue
            settings[flds[0]] = ' '.join(flds[1:])
    return settings


def read_structures(dirname: str) -> Tuple[List[Atoms], List[Atoms]]:
    """Parses the energy_*.out, force_*.out, and virial_*.out files from a
    nep run and returns their content as lists.  The first and
    second list contain the structures from the training and
    test sets, respectively. Each list entry corresponds to an
    ASE Atoms object, which in turn contains predicted and target
    energies, forces and virials/stresses stored in the `info`
    property.

    Parameters
    ----------
    dirname
        directory from which to read output files
    """
    path = join_path(dirname)
    if not exists(path):
        raise ValueError(f'Directory {path} does not exist')

    structures = {}

    for stype in ['train', 'test']:
        structures[stype] = read(join_path(dirname, f'{stype}.xyz'), format='extxyz', index=':')
        n_atoms = [len(atom) for atom in structures[stype]]
        cells = [atom.cell for atom in structures[stype]]
        n_structures = len(structures[stype])

        ts, ps = _read_data_file(path, f'energy_{stype}.out')
        assert len(ts) == n_structures, \
            f'Number of structures in energy_{stype}.out ({len(ts)})' \
            f' and {stype}.xyz ({n_structures}) inconsistent'
        for k, t, p in zip(range(n_structures), ts, ps):
            structures[stype][k].info['energy_target'] = t
            structures[stype][k].info['energy_predicted'] = p

        ts, ps = _read_data_file(path, f'force_{stype}.out')
        assert len(ts) == sum(n_atoms), \
            f'Number of structures in force_{stype}.out ({len(ts)})' \
            f' and {stype}.xyz ({n_structures}) inconsistent'
        n = 0
        for k, nat in zip(range(n_structures), n_atoms):
            structures[stype][k].info['force_target'] = np.array(ts[n:n+nat]).reshape(nat, 3)
            structures[stype][k].info['force_predicted'] = np.array(ps[n:n+nat]).reshape(nat, 3)
            n += nat

        ts, ps = _read_data_file(path, f'virial_{stype}.out')
        assert len(ts) == 6 * n_structures, \
            f'Number of structures in virial_{stype}.out ({len(ts)})' \
            f' and {stype}.xyz ({n_structures}) inconsistent'
        ts = np.array(ts).reshape((6, n_structures)).T
        ps = np.array(ps).reshape((6, n_structures)).T
        for k, nat, cell, t, p in zip(range(n_structures), n_atoms, cells, ts, ps):
            assert np.shape(t) == (6,)
            structures[stype][k].info['virial_target'] = t
            structures[stype][k].info['virial_predicted'] = p
            conv = nat / np.linalg.det(cell) / GPa
            structures[stype][k].info['stress_target'] = t * conv
            structures[stype][k].info['stress_predicted'] = p * conv
    return structures['train'], structures['test']


def _read_data_file(dirname: str,
                    fname: str):
    """Private function that parses energy/force/virial_*.out files and
    returns their content for further processing.
    """
    path = join_path(dirname, fname)
    if not exists(path):
        raise ValueError(f'Directory {path} does not exist')
    with open(path, 'r') as f:
        lines = f.readlines()
    target, predicted = [], []
    for line in lines:
        flds = line.split()
        if len(flds) == 6:
            predicted.append([float(s) for s in flds[0:3]])
            target.append([float(s) for s in flds[3:6]])
        elif len(flds) == 2:
            predicted.append(float(flds[0]))
            target.append(float(flds[1]))
    return target, predicted


def get_parity_data(structures: List[Atoms],
                    property: str,
                    selection: List[str] = None) -> DataFrame:
    """Returns the predicted and target energies, forces, virials or stresses
    from a list of structures in a format suitable for generating parity plots.

    The structures should  have been read using :func:`read_structures
    <calorine.nep.io.read_structures>`, such that the ``info``-object is
    populated with keys on the form ``{property}_{type}`` where :attr:`{property}`
    is one of energy, force, virial, and stress, and ``{type}`` is one
    of predicted or target.

    The resulting parity data is returned as a tuple of dicts, where each entry
    corresponds to a list.

    Parameters
    ----------
    structures
        List of structures as read with `read_structures`.
    property
        One of 'energy', 'force', 'virial', 'stress'.
    selection
        A list containing which components to return, and/or the absolute value.
        Possible values are 'x', 'y', 'z', 'xx', 'yy', 'zz', 'yz', 'xz', 'xy', 'abs', 'pressure'.
    """
    data = {
        'predicted': [],
        'target': []
    }
    voigt_mapping = {
        'x': 0,
        'y': 1,
        'z': 2,
        'xx': 0,
        'yy': 1,
        'zz': 2,
        'yz': 3,
        'xz': 4,
        'xy': 5
    }
    if property not in ('energy', 'force', 'virial', 'stress'):
        raise ValueError("`property` must be one of 'energy', 'force', 'virial', 'stress'.")
    if property == 'energy' and selection:
        raise ValueError('Selection does nothing for scalar-valued `energy`.')
    if property != 'stress' and selection and 'pressure' in selection:
        raise ValueError(f'Cannot calculate pressure for `{property}`.')
    for structure in structures:
        for stype in data:
            property_with_stype = f'{property}_{stype}'
            if property_with_stype not in structure.info.keys():
                raise KeyError(f'{property_with_stype} does not exist in info object!')
            extracted_property = np.array(structure.info[property_with_stype])

            if selection is None or len(selection) == 0:
                data[stype].append(extracted_property)
                continue

            selected_values = []
            for select in selection:
                if select == 'abs':
                    selected_values.append(np.linalg.norm(extracted_property, axis=1))
                    continue

                if select == 'pressure' and property == 'stress':
                    total_stress = np.sum(extracted_property, axis=0)
                    selected_values.append(- np.sum(total_stress[:3]) / 3)
                    continue

                if select not in voigt_mapping:
                    raise ValueError(f'Selection `{select}` is not allowed.')
                index = voigt_mapping[select]
                if index >= extracted_property.shape[1]:
                    raise ValueError(
                        f'Selection `{select}` is not compatible with property `{property}`.')
                selected_values.append(extracted_property[:, index])
            data[stype].append(selected_values)
    return DataFrame(data)
