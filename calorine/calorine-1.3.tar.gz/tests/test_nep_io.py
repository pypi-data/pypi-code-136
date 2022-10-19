import pytest
import numpy as np
from ase.io import read
from ase import Atoms
from ase.build import bulk
from ase.calculators.lj import LennardJones
from calorine.nep import (read_loss, read_nepfile, read_potential,
                          write_structures, get_parity_data)


@pytest.fixture
def PbTe():
    PbTeBulk = bulk('PbTe', crystalstructure='rocksalt', a=4)
    PbTeBulk[0].position += np.array([0.03, 0.02, 0])
    return PbTeBulk


@pytest.fixture
def TenPbTeWithInfo(PbTe):
    n_structures = 10
    structures = []
    for i in range(n_structures):
        # Test with differently sized structures in the test set
        atoms = PbTe.copy().repeat(i+1)
        natoms = len(atoms)
        atoms.info['energy_target'] = float(i)
        atoms.info['energy_predicted'] = float(i)
        atoms.info['force_target'] = np.arange(i, natoms*3+i).reshape((natoms, 3))
        atoms.info['force_predicted'] = np.arange(i, natoms*3+i).reshape((natoms, 3))
        atoms.info['virial_target'] = -np.arange(i, natoms*6+i).reshape((natoms, 6))
        atoms.info['virial_predicted'] = -np.arange(i, natoms*6+i).reshape((natoms, 6))
        atoms.info['stress_target'] = -np.arange(i, natoms*6+i).reshape((natoms, 6))
        atoms.info['stress_predicted'] = -np.arange(i, natoms*6+i).reshape((natoms, 6))
        structures.append(atoms)
    return structures


def sel2idx(select: str) -> int:
    map = {
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
    return map[select]


# --- read_nepfile ---
def test_read_nepfile_unknown_setting(tmpdir):
    """Reads a nep.in file with a comment"""
    p = tmpdir.join('nep.in')
    p.write('test 1\n')
    settings = read_nepfile(str(p))
    assert settings['test'] == '1'


def test_read_nepfile_run_comment(tmpdir):
    """Reads a nep.in file with a comment"""
    p = tmpdir.join('nep.in')
    p.write('#basis_size 10 6\n')
    settings = read_nepfile(str(p))
    assert settings == {}


def test_read_nepfile_nep():
    """Reads a nep.in file"""
    settings = read_nepfile('tests/example_files/nep.in')
    assert settings['version'] == '4'
    assert settings['type'] == '2 C H'
    assert settings['cutoff'] == '8 4'
    assert settings['n_max'] == '8 6'
    assert settings['l_max'] == '4'
    assert settings['neuron'] == '50'
    assert settings['lambda_1'] == '0.01'
    assert settings['lambda_2'] == '0.01'
    assert settings['batch'] == '100'
    assert settings['population'] == '50'
    assert settings['generation'] == '50000'
    assert settings['lambda_e'] == '1'
    assert 'lambda_f' not in settings.keys()


def test_read_nepfile_nep_blank_line(tmpdir):
    """Reads a nep.in file with a blank line"""
    p = tmpdir.join('nep.in')
    p.write('\n')
    settings = read_nepfile(str(p))
    assert settings == {}


# --- read_loss ---
def test_read_loss():
    """Reads a loss.out file"""
    loss = read_loss('tests/example_files/loss.out')
    columns_check = loss.columns == ['total_loss', 'L1', 'L2',
                                     'RMSE_E_train', 'RMSE_F_train', 'RMSE_V_train',
                                     'RMSE_E_test', 'RMSE_F_test', 'RMSE_V_test']
    assert columns_check.all()
    assert isinstance(loss.index[0], int)
    assert loss.index[0] == 100
    assert len(loss) == 95


def test_read_loss_single_row(tmpdir):
    """Tries to read a loss.out file that has only a single row"""
    p = tmpdir.join('loss.out')
    p.write('100 2 3 4 5 6 7 8 9 10\n')
    loss = read_loss(str(p))
    columns_check = loss.columns == ['total_loss', 'L1', 'L2',
                                     'RMSE_E_train', 'RMSE_F_train', 'RMSE_V_train',
                                     'RMSE_E_test', 'RMSE_F_test', 'RMSE_V_test']
    assert columns_check.all()
    assert isinstance(loss.index[0], int)
    assert loss.index[0] == 100


def test_read_loss_malformed_file(tmpdir):
    """Tries to read a malformed loss.out file"""
    p = tmpdir.join('loss_invalid.out')
    p.write('0 0 0 0 0 0\n')
    with pytest.raises(ValueError) as e:
        read_loss(str(p))
    assert 'Input file contains 6 data columns. Expected 10 columns.' in str(e)


# --- read_potential ---
def test_read_potential():
    """Reads a NEP3 nep.txt file"""
    settings, parameters = read_potential('tests/example_files/nep.txt')
    assert settings['zbl'] == (1, 2)
    assert settings['cutoff'] == (8, 4)
    assert settings['n_max'] == (4, 4)
    assert settings['l_max'] == (4, 2, 0)
    assert settings['basis_size'] == (8, 8)
    assert settings['ANN'] == (30, 0)
    assert len(parameters) == 1350


def test_read_potential_malformed_file(tmpdir):
    """Tries to read an invalid nep.in file"""
    p = tmpdir.join('nep.in')
    p.write("""nep123 x x\nnep123 x x\nnep123 x x\nnep123 x x\nnep123 x x\nnep123 x x\n
            nep123 x x\nnep123 x x\n  6.2799901e-02""")
    with pytest.raises(ValueError) as e:
        read_loss(str(p))
    assert 'could not convert string' in str(e)


# --- write_structures ---
def test_write_structures_single_structure(tmpdir, PbTe):
    """Writes a structure to a extxyz-file"""
    p = tmpdir.join('train.xyz')
    PbTe.calc = LennardJones()
    write_structures(str(p), [PbTe])
    read_structure = read(str(p), format='extxyz')
    assert np.isclose(read_structure.cell.volume, PbTe.cell.volume, atol=1e-12, rtol=1e-6)
    assert np.isclose(read_structure.get_potential_energy(),
                      PbTe.get_potential_energy(), atol=1e-12, rtol=1e-6)
    assert np.allclose(read_structure.positions, PbTe.positions, atol=1e-12, rtol=1e-6)
    assert np.allclose(read_structure.get_forces(), PbTe.get_forces(), atol=1e-12, rtol=1e-6)
    # Written accuracy is around 2e-6
    assert np.allclose(read_structure.get_stress(),
                       PbTe.get_stress(voigt=True), atol=1e-12, rtol=1e-5)


def test_write_structures_with_weight(tmpdir, PbTe):
    """Writes structures with weight to an extxyz-file"""
    p = tmpdir.join('train.xyz')
    structure1 = PbTe.copy()
    structure2 = PbTe.copy()
    structure1.calc = LennardJones()
    structure2.calc = LennardJones()
    structure1.info['weight'] = 1
    structure2.info['weight'] = 50
    write_structures(str(p), [structure1, structure2])
    with open(str(p), 'r') as f:
        lines = f.readlines()
        assert 'weight=1' in lines[1]
        assert 'weight=50' in lines[5]


def test_write_structure_with_filename(tmpdir, PbTe):
    """Writes with a filename to an extxyz-file"""
    p = tmpdir.join('train.xyz')
    PbTe.calc = LennardJones()
    PbTe.info['filename'] = 'result.testcar'
    write_structures(str(p), [PbTe])
    read_structure = read(str(p), format='extxyz')
    print(read_structure.info)
    assert read_structure.info['filename'] == 'result.testcar'
    with open(str(p), 'r') as f:
        lines = f.readlines()
        assert 'filename=result.testcar' in lines[1]


def test_write_structure_without_energy_or_forces(tmpdir):
    """Tries to write a structure without a calculator attached"""
    p = tmpdir.join('train.xyz')
    C = Atoms('C', positions=[(0, 0, 0)])
    with pytest.raises(RuntimeError) as e:
        write_structures(str(p), [C])
    assert 'Failed to retrieve energy and/or forces for structure' in str(e)


def test_write_structure_without_cell(tmpdir):
    """Tries to write a structure without a calculator attached"""
    p = tmpdir.join('train.xyz')
    C = Atoms('C', positions=[(0, 0, 0)])
    C.calc = LennardJones()
    with pytest.raises(ValueError) as e:
        write_structures(str(p), [C])
    assert 'You have 0 lattice vectors: volume not defined' in str(e)


# get_parity_data
@pytest.mark.parametrize('property',
                         ['energy', 'force', 'virial', 'stress'])
def test_get_parity_data(property, TenPbTeWithInfo):
    """Extracts parity data from a list of structures"""
    df = get_parity_data(structures=TenPbTeWithInfo, property=property)
    assert np.all(df.columns == ['predicted', 'target'])
    assert len(df['target']) == 10
    assert len(df['target']) == len(df['predicted'])
    if not property == 'energy':
        assert df['target'][0].shape == df['predicted'][0].shape


@pytest.mark.parametrize('property, selection',
                         [('force', ['x']),
                          ('virial', ['x', 'y', 'z']),
                          ('stress', ['xx', 'yy', 'zz'])
                          ])
def test_get_parity_data_diagonal_components(TenPbTeWithInfo, property, selection):
    """Extracts parity data from a list of structures, selecting properties on the diagonal."""
    df = get_parity_data(structures=TenPbTeWithInfo, property=property, selection=selection)
    for i, structure in enumerate(TenPbTeWithInfo):
        assert len(df['target'][i]) == len(selection)
        assert len(df['target'][i]) == len(df['predicted'][i])
        for j, select in enumerate(selection):
            expected_target = structure.info[f'{property}_target'][:, sel2idx(select)]
            expected_predicted = structure.info[f'{property}_predicted'][:, sel2idx(select)]
            assert np.all(df['target'][i][j] == expected_target)
            assert np.all(df['predicted'][i][j] == expected_predicted)


@pytest.mark.parametrize('property, selection',
                         [('virial', ['yz', 'xz', 'xy']),
                          ('stress', ['yz', 'xz', 'xy'])
                          ])
def test_get_parity_data_off_diagonal_components(TenPbTeWithInfo, property, selection):
    """Extracts parity data from a list of structures, selecting properties on the off-diagonal."""
    df = get_parity_data(structures=TenPbTeWithInfo, property=property, selection=selection)
    for i, structure in enumerate(TenPbTeWithInfo):
        assert len(df['target'][i]) == len(selection)
        assert len(df['target'][i]) == len(df['predicted'][i])
        for j, select in enumerate(selection):
            expected_target = structure.info[f'{property}_target'][:, sel2idx(select)]
            expected_predicted = structure.info[f'{property}_predicted'][:, sel2idx(select)]
            assert np.all(df['target'][i][j] == expected_target)
            assert np.all(df['predicted'][i][j] == expected_predicted)


@pytest.mark.parametrize('property, selection',
                         [('force', ['abs']),
                          ('virial', ['abs']),
                          ('stress', ['abs'])
                          ])
def test_get_parity_data_abs(TenPbTeWithInfo, property, selection):
    """Extracts parity data from a list of structures, calculating the absolute value"""
    df = get_parity_data(structures=TenPbTeWithInfo, property=property, selection=selection)
    for i, structure in enumerate(TenPbTeWithInfo):
        assert len(df['target'][i]) == len(selection)
        assert len(df['target'][i]) == len(df['predicted'][i])
        for j, _ in enumerate(selection):
            expected_target = np.linalg.norm(structure.info[f'{property}_target'], axis=1)
            expected_predicted = np.linalg.norm(structure.info[f'{property}_predicted'], axis=1)
            assert np.all(df['target'][i][j] == expected_target)
            assert np.all(df['predicted'][i][j] == expected_predicted)


@pytest.mark.parametrize('property, selection',
                         [('stress', ['pressure'])])
def test_get_parity_data_pressure(TenPbTeWithInfo, property, selection):
    """Extracts parity data from a list of structures, calculating the pressure"""
    df = get_parity_data(structures=TenPbTeWithInfo, property=property, selection=selection)
    for i, structure in enumerate(TenPbTeWithInfo):
        assert len(df['target'][i]) == len(selection)
        assert len(df['target'][i]) == len(df['predicted'][i])
        for j, _ in enumerate(selection):
            target_stress = np.sum(structure.info[f'{property}_target'], axis=0)
            predicted_stress = np.sum(structure.info[f'{property}_predicted'], axis=0)
            assert len(target_stress) == 6
            assert len(predicted_stress) == 6
            expected_target = -np.sum(target_stress[:3]) / 3
            expected_predicted = -np.sum(predicted_stress[:3]) / 3
            assert np.all(df['target'][i][j] == expected_target)
            assert np.all(df['predicted'][i][j] == expected_predicted)


@pytest.mark.parametrize('property, selection, output',
                         [('energy', ['x'],
                           'Selection does nothing for scalar-valued `energy`.'),
                          ('force', ['pressure'],
                          'Cannot calculate pressure for `force`.'),
                          ('force', ['xy'],
                          'Selection `xy` is not compatible with property `force`.'),
                          ('virial', ['zy'],
                          'Selection `zy` is not allowed.')
                          ])
def test_get_parity_data_invalid_selection(TenPbTeWithInfo, property, selection, output):
    """Tries to extract parity data from structures with an invalid selection"""
    with pytest.raises(ValueError) as e:
        get_parity_data(structures=TenPbTeWithInfo, property=property, selection=selection)
    assert output in str(e)


@pytest.mark.parametrize('property, output',
                         [('bounciness',
                           "`property` must be one of 'energy', 'force', 'virial', 'stress'."),
                          ])
def test_get_parity_data_invalid_property(TenPbTeWithInfo, property, output):
    """Tries to extract parity data from structures with an invalid property"""
    with pytest.raises(ValueError) as e:
        get_parity_data(structures=TenPbTeWithInfo, property=property)
    assert output in str(e)


def test_get_parity_data_missing_info():
    """Raises error when property(ies) is missing in atom info dictionary"""
    n_structures = 10
    structures = []
    for _ in range(n_structures):
        # Test with differently sized structures in the test set
        natoms = np.random.randint(1, 10)
        atoms = Atoms('C'*natoms)
        atoms.info['energy_target'] = 1.0
        structures.append(atoms)
    with pytest.raises(KeyError) as e:
        get_parity_data(structures, property='energy')
    assert 'energy_predicted does not exist in info object!' in str(e)
