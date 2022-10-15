# coding=utf-8
"""
Helper functions for SIESTA runs or analysis of SIESTA log files
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals
import os
import re
import shutil
import math
import io

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError
try:
    PermissionError
except NameError:
    PermissionError = OSError


def get_it(files):
    """Get a list of iterations"""
    try:
        return [int(re.search("{0}i([0-9]+)".format(os.sep), f).groups(0)[0]) for f in files]
    except AttributeError:
        raise AttributeError(
            "ERROR: The path must be in format of 'path{0}to{0}i1'".format(os.sep)
        )


def read_fdf(fdfpath, geo):
    """Read FDF file"""
    print("Reading {0}".format(fdfpath))
    with io.open(fdfpath, "r", encoding="utf-8") as fdffile:
        fdf = fdffile.read()
        ind = fdf.split(
            "%block ChemicalSpeciesLabel\n"
        )[1].split(
            "%endblock ChemicalSpeciesLabel\n"
        )[0]
        ind = ind.splitlines()
        for i in ind:
            for g in geo:
                if g[0] == i[-1]:
                    geo[geo.index(g)] = "{0}  ".format(g) + re.split(" +", i)[0]
                    g = "{0}  ".format(g) + re.split(" +", i)[0]
                    geo[geo.index(g)] = geo[geo.index(g)].strip(i[-1])
    return fdf, geo


def create_fdf(fdf, geo, newfdfpath, number):
    """Create new FDF file"""
    print("Creating {0}".format(newfdfpath))
    with io.open(newfdfpath, "w", encoding="utf-8") as newfdffile:
        newfdf = fdf.split("%block AtomicCoordinatesAndAtomicSpecies\n")[0]
        newfdf += "%block AtomicCoordinatesAndAtomicSpecies\n"
        for g in geo:
            newfdf += g + "\n"
        newfdf += "%endblock AtomicCoordinatesAndAtomicSpecies\n"
        match = re.search("(NumberOfAtoms +[0-9]+)", newfdf)
        if match is not None:
            newfdf.replace(match.group(0), "NumberOfAtoms   {0}".format(number))
        else:
            newfdf += "\nNumberOfAtoms   {0}\n".format(number)
        newfdffile.write(newfdf)
        print("{0} is created".format(newfdfpath))
        newfdffile.close()


def read_energy(energies=[], files=None, it=[], energytype="total", print_=True):
    """Read energy from log files"""
    energytypes = {
        "bandstruct": "siesta:  Band Struct. =",
        "kinetic": "siesta:       Kinetic =",
        "hartree": "siesta:       Hartree =",
        "edftu": "siesta:       Edftu   =",
        "eso": "siesta:       Eso     =",
        "extfield": "siesta:    Ext. field =",
        "exchcorr": "siesta:   Exch.-corr. =",
        "ionelectron": "siesta:  Ion-electron =",
        "ionion": "siesta:       Ion-ion =",
        "ekinion": "siesta:       Ekinion =",
        "total": "siesta:         Total =",
        "fermi": "siesta:         Fermi ="
    }
    it += get_it(files)
    for f in files:
        if print_:
            print(f)
        with io.open(f, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(energytypes[energytype]):
                    energies.append(float(line.split("=")[1].strip()))
                    if print_:
                        print(line.split("=  ")[1])


def read_force(forces=[], files=None, it=[], atomindex="Tot", forcetype="atomic", print_=True):
    """Read force from log files"""
    forcetypes = {
        "atomic": "siesta: Atomic forces (eV/Ang):",
        "constrained": "siesta: Constrained forces (eV/Ang):"
    }
    it += get_it(files)
    for f in files:
        if print_:
            print(f)
        with io.open(f, "r", encoding="utf-8") as file:
            content = file.read()
            match = re.search(
                r"{0}\n".format(re.escape(forcetypes[forcetype])) +
                r"(siesta: +[0-9]+ +-?[0-9]+\.[0-9]+ +-?[0-9]+\.[0-9]+ +-?[0-9]+\.[0-9]+\n)"
                r"+siesta: ----------------------------------------\n" +
                r"siesta: +Tot +-?[0-9]+\.[0-9]+ +-?[0-9]+\.[0-9]+ +-?[0-9]+\.[0-9]+\n",
                content
            )
            parts = re.findall(
                r"siesta: +" +
                r"([0-9]+|Tot) +" +
                r"(-?[0-9]+\.[0-9]+) +" +
                r"(-?[0-9]+\.[0-9]+) +" +
                r"(-?[0-9]+\.[0-9]+)\n",
                match.group(0)
            )
            for part in parts:
                if part[0] == atomindex:
                    resultant = math.sqrt(
                        float(part[1]) ** 2 + float(part[2]) ** 2 + float(part[3]) ** 2
                    )
                    forces.append([float(part[1]), float(part[2]), float(part[3]), resultant])
                    if print_:
                        print(
                            "x: {0}, ".format(part[1]) +
                            "y: {}, ".format(part[2]) +
                            "z: {0}, ".format(part[3]) +
                            "Resultant: {0}".format(resultant)
                        )


def print_run(for_, cores, conda):
    """Print SIESTA's run information"""
    print(
        "Running SIESTA for {0}{1}{2}".format(
            for_,
            " in parallel with {0} cores".format(cores) if cores is not None else '',
            " in conda" if conda else ''
        )
    )


def check_restart(fdffile, i, label, cwd, cont, contextensions):
    """Check DM, XV, CG, and LWF parameters in an FDF file"""
    fdf = fdffile.read()
    if "DM" in contextensions:
        check_restart_ext(
            ext="DM",
            fdf=fdf,
            match1=r"# *DM\.UseSaveDM +(\.true\.|T)",
            match2=r"DM\.UseSaveDM +(\.false\.|F)",
            repl="DM.UseSaveDM        .true.",
            out="DM.UseSaveDM",
            cwd=cwd,
            i=i,
            cont=cont,
            label=label
        )
    if "XV" in contextensions:
        check_restart_ext(
            ext="XV",
            fdf=fdf,
            match1=r"# *MD\.UseSaveXV +(\.true\.|T)",
            match2=r"MD\.UseSaveXV +(\.false\.|F)",
            repl="MD.UseSaveXV        .true.",
            out="MD.UseSaveCG",
            cwd=cwd,
            i=i,
            cont=cont,
            label=label
        )
    if "CG" in contextensions:
        check_restart_ext(
            ext="CG",
            fdf=fdf,
            match1=r"# *MD\.UseSaveCG +(\.true\.|T)",
            match2=r"MD\.UseSaveCG +(\.false\.|F)",
            repl="MD.UseSaveCG        .true.",
            out="MD.UseSaveCG",
            cwd=cwd,
            i=i,
            cont=cont,
            label=label
        )
    if "LWF" in contextensions:
        check_restart_ext(
            ext="LWF",
            fdf=fdf,
            match1=r"# *ON\.UseSaveLWF +(\.true\.|T)",
            match2=r"ON\.UseSaveLWF +(\.false\.|F)",
            repl="ON.UseSaveLWF        .true.",
            out="ON.UseSaveLWF",
            cwd=cwd,
            i=i,
            cont=cont,
            label=label
        )
    fdffile.seek(0)
    fdffile.write(fdf)


def check_restart_ext(ext, fdf, match1, match2, repl, out, cwd, i, cont, label):
    """Check DM, XV, CG, and LWF parameters in an FDF file individually"""
    match = re.search(match1, fdf)
    if match is None:
        match = re.search(match2, fdf)
    if match is None:
        print("Setting '{0}' as '.true.' in {1}{2}i{3}{2}{4}{2}{5}.fdf".format(out, cwd, os.sep, i, cont, label))
        fdf += "\n{0}\n".format(repl)
    else:
        print("Setting '{0}' as '.true.' in {1}{2}i{3}{2}{4}{2}{5}.fdf".format(out, cwd, os.sep, i, cont, label))
        fdf = fdf.replace(match.group(0), repl)
    if ext == "DM" and (re.search("WriteDM +.true.", fdf) is None
                        or re.search("# *WriteDM +.true.", fdf) is not None
                        or re.search("WriteDM +.false.", fdf) is not None):
        print(
            "WARNING: 'WriteDM .true.' not found in {0}{1}i{2}{1}{3}".format(cwd, os.sep, i, cont) +
            "{0}{1}.fdf".format(os.sep, label)
        )


def check_userbasis(fdffile):
    """Check if the Userbasis parameter in the fdf file is either true or false"""
    with io.open(fdffile, "r", encoding="utf-8") as f:
        if re.search(r"Userbasis *(\.true\.|T)", f.read()):
            return True
        f.close()
        return False


def copy_file(sourcefile, destinationfile):
    """Copy and paste a file"""
    if not os.path.isfile(sourcefile):
        raise FileNotFoundError("ERROR: {0} is not found".format(sourcefile))
    try:
        print("Copying {0} to {1}".format(sourcefile, destinationfile))
        if not os.path.exists(destinationfile):
            shutil.copy(sourcefile, destinationfile)
            print("{0} is copied to {1} successfully".format(sourcefile, destinationfile))
        else:
            print("{0} exists".format(destinationfile))
    except shutil.SameFileError:
        raise shutil.SameFileError(
            "ERROR: {0} and {1} represents the same file".format(sourcefile, destinationfile)
        )
    except PermissionError:
        raise PermissionError(
            "ERROR: Permission denied while copying {0} to {1}".format(sourcefile, destinationfile)
        )
    except (shutil.Error, IOError, OSError) as e:
        raise e(
            "ERROR: An error occurred while copying {0} to {1} ({2})".format(
                sourcefile,
                destinationfile,
                e
            )
        )


def sort_(files, path, cont):
    """Naive sort function for directories"""
    path = path.replace("*", "([0-9]+)")
    sortedfiles = []
    match = [re.search("{0}({1}{2}_*([0-9]*))*".format(path, os.sep, cont), f) for f in files]
    sortedmatch = [[m.group(0), m.group(1), m.group(2), m.group(3)] for m in match]
    sortedmatch = [x for _, x in sorted(zip(
        [int("{0}0".format(m[1])) if m[3] is None else
         int("{0}1".format(m[1])) if m[3] == "" else
         int(m[1] + m[3]) for m in sortedmatch
        ], sortedmatch
    ))]
    for s in sortedmatch:
        for f in files:
            fmatch = re.search("{0}({1}{2}_*([0-9]*))*".format(path, os.sep, cont), f)
            if s[0] == fmatch.group(0) and f not in sortedfiles:
                sortedfiles.append(f)
    return sortedfiles


def remove_nones(files, path, cwd, cont, log):
    """Remove the files which do not return any energy values"""
    path = path.replace("*", "[0-9]+")
    active_log = {}
    to_remove = []
    for filename in files:
        logmatch = re.search(
            "({0}{1}({2})({1}{3}(_([0-9]+))?)?{1}{4})".format(cwd, os.sep, path, cont, log),
            filename
        )
        if not logmatch:
            continue
        _, instance, extended, _, increment = logmatch.groups()
        lognumber = 0
        if extended is not None:
            lognumber = 1 if increment is None else int(increment)
        if instance not in active_log:
            active_log[instance] = (lognumber, filename)
        elif active_log[instance][0] > lognumber:
            to_remove.append(filename)
        else:
            to_remove.append(active_log[instance][1])
            active_log[instance] = (lognumber, filename)
    for filename in to_remove:
        files.remove(filename)


def bohr_to_angstrom(bohr):
    """Convert Bohr to Ångström"""
    return bohr * 0.529177249


def lattice_vectors_mag(fdfpath):
    """Return the lattice vectors magnitude from given FDF"""
    x = None
    y = None
    z = None
    print("Opening {0}".format(fdfpath))
    with io.open(fdfpath, "r", encoding="utf-8") as fdffile:
        content = fdffile.read()
        match = re.search(
            r"%block LatticeVectors\n" +
            r"[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*\n" +
            r"[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*\n" +
            r"[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*(-?[0-9]+\.[0-9]+)[ \t]*\n" +
            r"%endblock LatticeVectors\n",
            content
        )
        print("Calculating LatticeVectors magnitude")
        x = math.sqrt(
            float(match.group(1)) ** 2 +
            float(match.group(2)) ** 2 +
            float(match.group(3)) ** 2
        )
        y = math.sqrt(
            float(match.group(4)) ** 2 +
            float(match.group(5)) ** 2 +
            float(match.group(6)) ** 2
        )
        z = math.sqrt(
            float(match.group(7)) ** 2 +
            float(match.group(8)) ** 2 +
            float(match.group(9)) ** 2
        )
        fdffile.close()
    return x, y, z


def element_diameter(element):
    """Return the outer diameter in nm of a given element"""
    data = {"H": 0.106, "He": 0.062, "Li": 0.334, "Be": 0.224, "B": 0.174, "C": 0.134, "N": 0.112,
            "O": 0.096, "F": 0.084, "Ne": 0.076, "Na": 0.38, "Mg": 0.29, "Al": 0.236, "Si": 0.222,
            "P": 0.196, "S": 0.176, "Cl": 0.158, "Ar": 0.142, "K": 0.486, "Ca": 0.388, "Sc": 0.368,
            "Ti": 0.352, "V": 0.342, "Cr": 0.332, "Mn": 0.322, "Fe": 0.312, "Co": 0.304,
            "Ni": 0.298, "Cu": 0.145, "Zn": 0.284, "Ga": 0.272, "Ge": 0.25, "As": 0.228,
            "Se": 0.206, "Br": 0.094, "Kr": 0.176, "Rb": 0.53, "Sr": 0.438, "Y": 0.424,
            "Zr": 0.412, "Nb": 0.396, "Mo": 0.38, "Tc": 0.366, "Ru": 0.356, "Rh": 0.346,
            "Pd": 0.338, "Ag": 0.33, "Cd": 0.322, "In": 0.312, "Sn": 0.29, "Sb": 0.266,
            "Te": 0.246, "I": 0.23, "Xe": 0.216, "Cs": 0.596, "Ba": 0.506, "Ce": 0.37,
            "Pr": 0.494, "Nd": 0.412, "Pm": 0.41, "Sm": 0.476, "Eu": 0.462, "Gd": 0.466,
            "Tb": 0.45, "Dy": 0.456, "Ho": 0.452, "Er": 0.452, "Tm": 0.444, "Yb": 0.444,
            "Lu": 0.434, "Hf": 0.416, "Ta": 0.4, "W": 0.386, "Re": 0.376, "Os": 0.37,
            "Ir": 0.36, "Pt": 0.354, "Au": 0.348, "Hg": 0.342, "Tl": 0.312, "Pb": 0.308,
            "Bi": 0.286, "Po": 0.27, "At": 0.254, "Rn": 0.24, "Fr": None, "Ra": None, "Ac": 0.39,
            "Th": 0.36, "Pa": 0.36, "U": 0.35, "Np": 0.35, "Pu": 0.35, "Am": 0.35, "Cm": None}
    if element not in data:
        raise ValueError("ERROR: Element is not valid")
    return data[element]


def coords(fdfpath):
    """Return coordinates from a given FDF file"""
    xs = []
    ys = []
    zs = []
    print("Opening {0}".format(fdfpath))
    with io.open(fdfpath, "r", encoding="utf-8") as fdffile:
        match = re.search(
            r"%block AtomicCoordinatesAndAtomicSpecies\n" +
            r"((([ \t]*-?[0-9]+\.[0-9]+){3})[ \t]+[0-9]+[ \t]*\n)+" +
            r"%endblock AtomicCoordinatesAndAtomicSpecies",
            fdffile.read()
        )
        parts = re.findall(
            r"[ \t]*(-?[0-9]+\.[0-9]+)" +
            r"[ \t]*(-?[0-9]+\.[0-9]+)" +
            r"[ \t]*(-?[0-9]+\.[0-9]+)" +
            r"[ \t]+[0-9]+[ \t]*\n",
            match.group(0)
        )
        print("Getting coordinates from {0}".format(fdfpath))
        for part in parts:
            xs.append(float(part[0]))
            ys.append(float(part[1]))
            zs.append(float(part[2]))
            fdffile.close()
    return xs, ys, zs


def species(fdfpath):
    """Return species from a given FDF file"""
    ids = []
    atomicweights = []
    labels = []
    print("Opening {0}".format(fdfpath))
    with io.open(fdfpath, "r", encoding="utf-8") as fdffile:
        match = re.search(
            "%block ChemicalSpeciesLabel\n" +
            "([0-9]+[ \t]+[0-9]+[ \t]+.+\n)+" +
            "%endblock ChemicalSpeciesLabel\n",
            fdffile.read()
        )
        parts = re.findall("([0-9]+)[ \t]+([0-9]+)[ \t]+(.+)\n", match.group(0))
        print("Getting species from {0}".format(fdfpath))
        for part in parts:
            ids.append(part[0])
            atomicweights.append(part[1])
            labels.append(part[2].strip())
        fdffile.close()
    return ids, atomicweights, labels


def unique(list1):
    """Return the distinct values of a list"""
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
