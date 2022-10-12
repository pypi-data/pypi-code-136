"""Loading and saving files."""
from pathlib import Path
import warnings

import numpy as np

from lacbox import gtsdf


_OPER_NAMES = ["ws_ms", "pitch_deg", "rotor_speed_rpm", "power_kw", "thrust_kn"]
_ST_NAMES = ["s",
             "m",
             "x_cg", "y_cg",
             "ri_x", "ri_y",
             "x_sh", "y_sh",
             "E", "G",
             "I_x", "I_y", "I_p",
             "k_x", "k_y",
             "A", "pitch",
             "x_e",	"y_e"]


def load_ae(path, dset=1, unpack=False):
    """Load data in an AE file to a 2D numpy array or list of 1D arrays.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the AE file.
    dset : int, optional
        Dataset to load. NOTE that this function will only work with dset = 1.
    unpack : boolean, optional
        Whether to unpack the 2D array into a list of 1D arrays. The default is False.

    Returns
    -------
    ae : np.ndarray
        Either a 2D array with 4 columns or a list of 4 1D arrays, one for each column
        in the AE file.
    """
    if dset != 1:
        raise ValueError('Function only supports loading first dataset!')
    ae = np.loadtxt(path, skiprows=2, comments=';', unpack=unpack)
    return ae


def save_ae(path, ae_data):
    """Save the AE data in a 2D numpy array to HAWC2 file.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the AE file to save.
    ae_data : np.ndarray
        2D numpy array of AE data to be saved. Array should have 4 columns.
    """
    n_rows = ae_data.shape[0]  # no. of rows to save
    with open(path, 'w') as ae_file:
        ae_file.write(f'1\n1  {n_rows}\n')  # header of AE file
        np.savetxt(ae_file, ae_data, fmt='%11.4e', delimiter='\t', newline='\t;\n',
                   header='')


def load_c2def(path, bodyname='blade1'):
    """Load the c2_def data from htc file.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the htc with the twist to load.
    bodyname : str, optional
        Name of the body for which you want to load the c2_def information. Default is
        'blade1'.

    Returns
    -------
    c2_def : np.ndarray
        A 2D numpy array with 4 columns, corresponding to the numerical data columns in
        the c2_def block (skipping the section number).
    """
    in_body = False
    with open(path, 'r') as htc_file:
        for line in htc_file.readlines():
            linesplit = line.split(';')[0].split()
            if ('name' in linesplit) and (bodyname in linesplit):
                in_body = True
            if in_body:
                if 'nsec' in linesplit:
                    nsec = int(linesplit[1])
                    c2_def = np.empty((nsec, 4))
                elif 'sec' in linesplit:
                    idx = int(linesplit[1]) - 1
                    vals = [float(x) for x in linesplit[2:6]]
                    c2_def[idx, :] = vals
                elif ('end' in linesplit) and ('main_body' in linesplit):
                    in_body = False

    return c2_def


def save_c2def(path, c2_def, parspace='  '):
    """Save a c2_def array to a text file that can be copied into a htc file.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the text file that we want to create. NOT YOUR HTC FILE!
    c2_def : np.ndarray
        2D numpy array with 4 columns corresponding to x, y, z, and twist.
    parspace : str, optional
        The indentation delimiter. The default is 2 spaces.
    """
    nsec = c2_def.shape[0]
    with open(path, 'w') as file:
        file.write(parspace + 'begin c2_def;\n')
        file.write(2*parspace + f'nsec {nsec};\n')
        for i, vals in enumerate(c2_def):
            file.write(2*parspace +
                       f'sec {i+1:2.0f}{vals[0]:15.5e}{vals[1]:15.5e}' +
                       f'{vals[2]:15.5e}{vals[3]:15.5e} ;\n')
        file.write(parspace + 'end c2_def;\n')


def load_ind(path):
    """Loads a HAWC2S output .ind file as an python dict

    Parameters
    ----------
    path : str or pathlib.Path
        Path for the .ind file

    Returns
    -------
    dict
        each column of the tabular data is an entry in the dict. 
        Units are appended at the end.
    """

    # List of names
    names = [
        "s_m", "a", "ap", 
        "flow_angle_rad", "aoa_rad", "flow_speed_ms", 
        "Fx_Nm", "Fy_Nm", "M_Nmm", 
        "UX0_m", "UY0_m", "UZ0_m", 
        "twist_rad",  
        "X_AC0_m", "Y_AC0_m", "Z_AC0_m", 
        "Cl", "Cd", "Cm", 
        "CLp0_rad", "CDp0_rad", "CMp0_rad", 
        "F0",  "F_rad", "CL_FS0", "CLFS_rad",  
        "V_a_ms", "V_t_ms", "torsion_rad",
        "vx_ms", "vy_ms", "chord_m",
        "CT", "CP", "angle_rad",
        "v_1", "v_2", "v_3"
        ]
    # Read data into 2D array
    data = np.loadtxt(path, skiprows=1)
    # Split 2D array into a dict
    return {name: val for name, val in zip(names, data.T)}


def load_inds(paths):
    """Loads a HAWC2S output .ind file as an python dict

    Parameters
    ----------
    paths : list
        List of str or pathlib.Path for a set of .ind files

    Returns
    -------
    dict
        each column of the tabular data is an entry in the dict.
        The shape of the data is (n_ind, n_paths)
        Units are appended at the end.
    """
    datas = dict()
    # loop over path
    for ipath, path in enumerate(paths):
        # Load data for single path
        data = load_ind(path)
        # if ipath==0 initialize arrays
        if ipath == 0:
            npaths = len(paths)
            for name, val in data.items():
                datas[name] = np.empty((len(val), npaths))
        # Add single path data to datas
        for name, val in data.items():
            datas[name][:, ipath] = val.copy()
    return datas


def load_pwr(path):
    """Loads a HAWC2S output .pwr file as an python dict

    Parameters
    ----------
    path : str or pathlib.Path
        Path for the .ind file

    Returns
    -------
    dict
        each column of the tabular data is an entry in the dict. 
        Units are appended at the end.
    """
    # List of names
    names = [
        "V_ms",  "P_kW", "T_kN",
        "Cp", "Ct", "Pitch_Q_Nm", 
        "Flap_M_kNm", "Edge_M_kNm", 
        "Pitch_deg", "Speed_rpm", 
        "Tip_x_m", "Tip_y_m", "Tip_z_m",
        "J_rot_kgm2", "J_DT_kgm2", 
        "Torsion_rad", "Torque_kNm"
      ]
    # Read data into 2D array
    data = np.loadtxt(path, skiprows=1)
    # Split 2D array into a dict
    return {name: val for name, val in zip(names, data.T)}


def load_pc(path, dset=None):
    """Load the HAWC2 PC-file.

    Parameters
    ----------
    path : str or pathlib.Path
           path for PC-file
    dset : int, optional
        extract only a single set (first set is 1) default is to return all sets, by default None

    Returns
    -------
    list
        Each entry is a set which by them self is a list of profiles.
        If only one set is present it only return a list of profiles.
        Each of the entries in the profile list is a dict with keys:

        * **tc** : *float*
        * **aoa_deg** : *np.ndarray*
        * **cl** : *np.ndarray*
        * **cd** : *np.ndarray*
        * **cm** : *np.ndarray*
        * **comment** : *str*
    """
    with open(path, "r") as file:
        pc_data = []
        # Get number of sets (skipping comment for now)
        nset = int(file.readline().strip().split()[0])
        for iset in range(nset):
            # Add empty list for profs
            pc_data.append([])
            # Get number of profiles
            nprof = int(file.readline().strip().split()[0])
            # Loop over nprof
            for iprof in range(nprof):
                # Add empty list with dict
                pc_data[iset].append(dict())
                # Read line (number of polar points, relative thickness, comment)
                line = file.readline().strip().split()
                naoa = int(line[1])
                pc_data[iset][iprof]["tc"] = float(line[2])
                pc_data[iset][iprof]["comment"] = " ".join(line[3:])
                # Read data as 2D table
                data = np.loadtxt(file, max_rows=naoa)
                pc_data[iset][iprof]["aoa_deg"] = data[:, 0]
                pc_data[iset][iprof]["cl"] = data[:, 1]
                pc_data[iset][iprof]["cd"] = data[:, 2]
                pc_data[iset][iprof]["cm"] = data[:, 3]
    if dset is None:
        if len(pc_data) == 1:
            # Return only list of prof elements
            return pc_data[0]
        # Return all sets if there are multiple
        return pc_data
    # Return given set
    return pc_data[dset-1]


def save_pc(path, pc_data):
    """Save a HAWC2 PC-file.

    Parameters
    ----------
    path : str or pathlib.Path
        path for PC-file
    pc_data : list
        Can be a list of sets each with a list of profiles or just a list of profiles.
        Each of the entries in the profile list is a dict with keys:

        * **tc** : *float*
        * **aoa_deg** : *np.ndarray or list*
        * **cl** : *np.ndarray or list*
        * **cd** : *np.ndarray or list*
        * **cm** : *np.ndarray or list*
        * **comment** : *str, optional*
    """
    # Ensure that pc_data is list of sets with list of profile data
    if isinstance(pc_data, list):
        if isinstance(pc_data[0], list):
            # Data is a list of list
            pass
        elif isinstance(pc_data[0], dict):
            # Data is a list of profile data and a list is added to be a list of lists
            pc_data = [pc_data]
        else:
            raise ValueError(
                """pc_data need to be a list of profile data dict
                (containing keys: tc, aoa_deg, cl, cd, cm)
                or a list of sets each with a list of profile data."""
                )
    else:
        raise ValueError(
                """pc_data need to be a list of profile data dict
                (containing keys: tc, aoa_deg, cl, cd, cm)
                or a list of sets each with a list of profile data."""
                )
    # Open output file
    with open(path, "w") as file:
        # Write the number of sets
        nsets = len(pc_data)
        file.write(f"{nsets}\n")
        # Loop over the sets
        for set in pc_data:
            # Write the number of profiles
            nprof = len(set)
            file.write(f"{nprof}\n")
            # Loop over profs
            for iprof, prof in enumerate(set, 1):
                naoa = len(prof["aoa_deg"])
                file.write(f"{iprof}  {naoa}  {prof['tc']}  {prof.get('comment', '')}\n")
                np.savetxt(file, np.array([prof["aoa_deg"], prof["cl"], prof["cd"], prof["cm"]]).T)


def load_st(path, dset=None, dsubset=None):
    """Load as HAWC2 ST-file

    Parameters
    ----------
    path : str or pathlib.Path
        path for ST-file
    dset : int, optional
        extract only a single set (first set is 1) default is to return all sets, by default None
    dsubset : _type_, optional
        similar to dset, by default None

    Returns
    -------
    list
        Each entry is a set which by them self is a list of subsets.
        Each of the entries in the subset list is a dict with keys:

        * **s** : *np.ndarray*
        * **m** : *np.ndarray*
        * **x_cg** : *np.ndarray*
        * **y_cg** : *np.ndarray*
        * **ri_x** : *np.ndarray*
        * **ri_y** : *np.ndarray*
        * **x_sh** : *np.ndarray*
        * **y_sh** : *np.ndarray*
        * **E** : *np.ndarray*
        * **G** : *np.ndarray*
        * **I_x** : *np.ndarray*
        * **I_y** : *np.ndarray*
        * **I_p** : *np.ndarray*
        * **k_x** : *np.ndarray*
        * **k_y** : *np.ndarray*
        * **A** : *np.ndarray*
        * **pitch** : *np.ndarray*
        * **x_e** : *np.ndarray*
        * **y_e** : *np.ndarray*
    """
    with open(path, "r") as file:
        line = file.readline()
        st_data = []
        while line:
            # Start with # -> add set
            if line and line.strip()[0] == "#":
                st_data.append([])
            # Start with $ -> add subset
            if line and line.strip()[0] == "$":
                st_data[-1].append(dict())
                nst = int(line.strip().split()[1])
                # Read data a 2D array
                data = np.loadtxt(file, max_rows=nst)
                # Adding data to dict
                for iname, name in enumerate(_ST_NAMES):
                    st_data[-1][-1][name] = data[:, iname]
            # Read next line
            line = file.readline()

    if dset is None:
        if dsubset is None:
            return st_data
        return st_data[:][dsubset]
    st_data = st_data[dset]
    if dsubset is None:
        return st_data
    return st_data[dsubset]


def save_st(path, st_data):
    """Save a HAWC2 ST-file.

    Parameters
    ----------
    path : str or pathlib.Path
        path for PC-file
    st_data : list
        Can be a list of sets each with a list of subset or list of subsets.
        Each of the entries in the subset list is a dict with keys:

        * **s** : *np.ndarray*
        * **m** : *np.ndarray*
        * **x_cg** : *np.ndarray*
        * **y_cg** : *np.ndarray*
        * **ri_x** : *np.ndarray*
        * **ri_y** : *np.ndarray*
        * **x_sh** : *np.ndarray*
        * **y_sh** : *np.ndarray*
        * **E** : *np.ndarray*
        * **G** : *np.ndarray*
        * **I_x** : *np.ndarray*
        * **I_y** : *np.ndarray*
        * **I_p** : *np.ndarray*
        * **k_x** : *np.ndarray*
        * **k_y** : *np.ndarray*
        * **A** : *np.ndarray*
        * **pitch** : *np.ndarray*
        * **x_e** : *np.ndarray*
        * **y_e** : *np.ndarray*
    """
    # Ensure that pc_data is list of sets with list of profile data
    if isinstance(st_data, list):
        if isinstance(st_data[0], list):
            # Data is a list of list
            pass
        elif isinstance(st_data[0], dict):
            # Data is a list of subsets and a list is added to be a list of lists
            st_data = [st_data]
        else:
            raise ValueError(
                """st_data need to be a list of dicts
                (containing keys: %s)
                or a list of sets each with a list subset data.""" % (_ST_NAMES)
                )
    elif isinstance(st_data, dict):
        # Data is a single subset and is wrapped in two lists
        st_data = [[st_data]]
    else:
        raise ValueError(
                """st_data need to be a list of dicts
                (containing keys: %s)
                or a list of sets each with a list subset data.""" % (_ST_NAMES)
                )

    # Open output file
    with open(path, "w") as file:
        # Write the number of sets
        nsets = len(st_data)
        file.write(f"{nsets} number of sets\n")
        # Loop over the sets
        for iset, set in enumerate(st_data, 1):
            # Write the set number
            file.write(f"#{iset}\n")
            # Loop over subsets
            for isubset, subset in enumerate(set, 1):
                nst = len(subset["s"])  # length of subset
                file.write(f"${isubset}  {nst}\n")  # write subset number and length
                data = np.array([subset[name] for name in _ST_NAMES])  # create 2D array
                np.savetxt(file, data.T)  # write 2D data


def load_oper(path):
    """Load HAWC2S operational data file

    Parameters
    ----------
    path : str or pathlib.Path
        path for operational data file

    Returns
    -------
    dict
        contain the following keys:

        * **ws_ms** : *ndarray*
        * **pitch_deg** : *ndarray*
        * **rotor_speed_rpm** : *ndarray*
        * **power_kw** : *ndarray (if present)*
        * **thrust_kn** : *ndarray (if present)*
    """
    # Load data as 2D array
    data = np.loadtxt(path, skiprows=1)
    # Ensure data is 2D
    if len(data.shape) == 1:
        data = np.array([data])
    # Return data as dict
    return {name: val for name, val in zip(_OPER_NAMES, data.T)}


def save_oper(path, oper_data):
    """Save an operational data file

    Parameters
    ----------
    path : _type_
        _description_
    oper_data : dict
        With the following keys:
        
        * **ws_ms** : *ndarray*
        * **pitch_deg** : *ndarray*
        * **rotor_speed_rpm** : *ndarray*
        * **power_kw** : *ndarray (if present)*
        * **thrust_kn** : *ndarray (if present)*
    """
    noper = len(oper_data["ws_ms"])
    with open(path, "w") as file:
        file.write(f"{noper}  wind speed [m/s]  pitch [deg]  rot. speed [rpm]")
        if "power_kw" in oper_data:
            file.write("  power [kW]  thrust [kN]\n")
            data = [oper_data[name] for name in _OPER_NAMES]
        else:
            file.write("\n")
            data = [oper_data[name] for name in _OPER_NAMES[:-2]]
        np.savetxt(file, np.array(data).T)


class ReadHAWC2(object):
    """Read a HAWC2 time-marching simulation into an object.
    
    Usage
    ------
    >>> h2res = ReadHAWC2(fname, loaddata=False)


    Parameters
    ----------
    fname : pathlib.Path or str
        Path to file to load. Currently only GTSDF (HDF5) format is supported.
    loaddata : boolean
        Whether to load the data itself (True) or just the metadata (False). Default is
        True.
    """

    def __init__(self, fname, loaddata=True):
        """Initialize the object. Sanitize inputs and call subsequent method."""
        # sanitize inputs and initialize variables
        fname = Path(fname)
        self.fname = fname
        self.data = None
        self.chaninfo = None
        self.nrch = None
        self.nrsc = None
        self.freq = None
        self.fformat = None
        self.t = None
        # self.Iknown = []  # to keep track of what has been read all ready
        
        # check if file exists and file extension given
        if not fname.is_file():
            raise OSError(f'File "{fname.as_posix()}" is not found! ' +
                          'Verify the path is correct.')
        
        # call different readers for different types of files
        if '.hdf5' in fname.suffix:
            self._read_gtsdf(loaddata=loaddata)
        elif '.sel' in fname.suffix:
            warnings.warn('Reading sel files is not yet implemented! Sorry. :(')
        elif '.dat' in fname.suffix:
            warnings.warn('Reading dat files is not yet implemented! Sorry. :(')
        elif '.int' in fname.suffix:
            warnings.warn('Reading int files is not yet implemented! Sorry. :(')
        else:
            raise ValueError(f'File extension "{fname.suffix}" is unknown!'
                             + ' Please see function documentation.')
        
    def _read_gtsdf(self, loaddata=True):
        """Read HAWC2 file format gtsdf. Assign default attributes plus
        gtsdf_description."""
        self.t, data, info = gtsdf.load(self.fname)
        self.chaninfo = [['Time'] + info['attribute_names'],
                         ['s'] + info['attribute_units'],
                         ['Time'] + info['attribute_descriptions']]
        self.nrch = data.shape[1] + 1
        self.nrsc = data.shape[0]
        self.freq = self.nrsc / self.t
        self.fformat = 'GTSDF'
        self.gtsdf_description = info['description']
        if loaddata:
            self.data = np.hstack([self.t[:, np.newaxis], data])
