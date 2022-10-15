"""
Helper functions for SIESTA runs or analysis of SIESTA log files
"""
from __future__ import absolute_import
import os
import re
import shutil
import math


def get_it(files):
    """Get a list of iterations"""
    try:
        return [int(re.search(f"{os.sep}i([0-9]+)", f).groups(0)[0]) for f in files]
    except AttributeError as e:
        raise AttributeError(
            f"ERROR: The path must be in format of 'path{os.sep}to{os.sep}i1'"
        ) from e


def read_fdf(fdfpath, geo):
    """Read FDF file"""
    print(f"Reading {fdfpath}")
    with open(fdfpath, "r", encoding="utf-8") as fdffile:
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
                    geo[geo.index(g)] = f"{g}  " + re.split(" +", i)[0]
                    g = f"{g}  " + re.split(" +", i)[0]
                    geo[geo.index(g)] = geo[geo.index(g)].strip(i[-1])
    return fdf, geo


def create_fdf(fdf, geo, newfdfpath, number):
    """Create new FDF file"""
    print(f"Creating {newfdfpath}")
    with open(newfdfpath, "w", encoding="utf-8") as newfdffile:
        newfdf = fdf.split("%block AtomicCoordinatesAndAtomicSpecies\n")[0]
        newfdf += "%block AtomicCoordinatesAndAtomicSpecies\n"
        for g in geo:
            newfdf += g + "\n"
        newfdf += "%endblock AtomicCoordinatesAndAtomicSpecies\n"
        match = re.search("(NumberOfAtoms +[0-9]+)", newfdf)
        if match is not None:
            newfdf.replace(match[0], f"NumberOfAtoms   {number}")
        else:
            newfdf += f"\nNumberOfAtoms   {number}\n"
        newfdffile.write(newfdf)
        print(f"{newfdfpath} is created")
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
        with open(f, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(energytypes[energytype]):
                    energies.append(float(line.split("=")[1].strip()))
                    if print_:
                        print(line.split("=  ")[1])


def read_force(*, forces=[], files=None, it=[], atomindex="Tot", forcetype="atomic", print_=True):
    """Read force from log files"""
    forcetypes = {
        "atomic": "siesta: Atomic forces (eV/Ang):",
        "constrained": "siesta: Constrained forces (eV/Ang):"
    }
    it += get_it(files)
    for f in files:
        if print_:
            print(f)
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            match = re.search(
                rf"{re.escape(forcetypes[forcetype])}\n" +
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
                match[0]
            )
            for part in parts:
                if part[0] == atomindex:
                    resultant = math.sqrt(
                        float(part[1]) ** 2 + float(part[2]) ** 2 + float(part[3]) ** 2
                    )
                    forces.append([float(part[1]), float(part[2]), float(part[3]), resultant])
                    if print_:
                        print(
                            f"x: {part[1]}, " +
                            f"y: {part[2]}, " +
                            f"z: {part[3]}, " +
                            f"Resultant: {resultant}"
                        )


def print_run(for_, cores, conda):
    """Print SIESTA's run information"""
    print(
        f"""Running SIESTA for {for_}
        {f' in parallel with {cores} cores' if cores is not None else ''}
        {' in conda' if conda else ''}""".replace("\n", "").replace("        ", "")
    )


def check_restart(*, fdffile, i, label, cwd, cont, contextensions):
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


def check_restart_ext(*, ext, fdf, match1, match2, repl, out, cwd, i, cont, label):
    """Check DM, XV, CG, and LWF parameters in an FDF file individually"""
    match = re.search(match1, fdf)
    if match is None:
        match = re.search(match2, fdf)
    if match is None:
        print(f"Setting '{out}' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
        fdf += f"\n{repl}\n"
    else:
        print(f"Setting '{out}' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
        fdf = fdf.replace(match[0], repl)
    if ext == "DM" and (re.search("WriteDM +.true.", fdf) is None
                        or re.search("# *WriteDM +.true.", fdf) is not None
                        or re.search("WriteDM +.false.", fdf) is not None):
        print(
            f"WARNING: 'WriteDM .true.' not found in {cwd}{os.sep}i{i}{os.sep}{cont}" +
            f"{os.sep}{label}.fdf"
        )


def check_userbasis(fdffile):
    """Check if the Userbasis parameter in the fdf file is either true or false"""
    with open(fdffile, "r", encoding="utf-8") as f:
        if re.search(r"Userbasis *(\.true\.|T)", f.read()):
            return True
        f.close()
        return False


def copy_file(sourcefile, destinationfile):
    """Copy and paste a file"""
    if not os.path.isfile(sourcefile):
        raise FileNotFoundError(f"ERROR: {sourcefile} is not found")
    try:
        print(f"Copying {sourcefile} to {destinationfile}")
        if not os.path.exists(destinationfile):
            shutil.copy(sourcefile, destinationfile)
            print(f"{sourcefile} is copied to {destinationfile} successfully")
        else:
            print(f"{destinationfile} exists")
    except shutil.SameFileError as e:
        raise shutil.SameFileError(
            f"ERROR: {sourcefile} and {destinationfile} represents the same file"
        ) from e
    except PermissionError as e:
        raise PermissionError(
            f"ERROR: Permission denied while copying {sourcefile} to {destinationfile}"
        ) from e
    except (shutil.Error, OSError, IOError) as e:
        raise (
            f"ERROR: An error occurred while copying {sourcefile} to {destinationfile} ({e})"
        ) from e


def sort_(files, path, cont):
    """Naive sort function for directories"""
    path = path.replace("*", "([0-9]+)")
    sortedfiles = []
    match = [re.search(f"{path}({os.sep}{cont}_*([0-9]*))*", f) for f in files]
    sortedmatch = [[m[0], m[1], m[2], m[3]] for m in match]
    sortedmatch = [x for _, x in sorted(zip(
        [int(f"{m[1]}0") if m[3] is None else
         int(f"{m[1]}1") if m[3] == "" else
         int(m[1] + m[3]) for m in sortedmatch
        ], sortedmatch
    ))]
    for s in sortedmatch:
        for f in files:
            fmatch = re.search(f"{path}({os.sep}{cont}_*([0-9]*))*", f)
            if s[0] == fmatch[0] and f not in sortedfiles:
                sortedfiles.append(f)
    return sortedfiles


def remove_nones(files, path, cwd, cont, log):
    """Remove the files which do not return any energy values"""
    path = path.replace("*", "[0-9]+")
    active_log = {}
    to_remove = []
    for filename in files:
        logmatch = re.search(
            f"({cwd}{os.sep}({path})({os.sep}{cont}(_([0-9]+))?)?{os.sep}{log})", filename
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
    print(f"Opening {fdfpath}")
    with open(fdfpath, "r", encoding="utf-8") as fdffile:
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
        x = math.sqrt(float(match[1]) ** 2 + float(match[2]) ** 2 + float(match[3]) ** 2)
        y = math.sqrt(float(match[4]) ** 2 + float(match[5]) ** 2 + float(match[6]) ** 2)
        z = math.sqrt(float(match[7]) ** 2 + float(match[8]) ** 2 + float(match[9]) ** 2)
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
    print(f"Opening {fdfpath}")
    with open(fdfpath, "r", encoding="utf-8") as fdffile:
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
            match[0]
        )
        print(f"Getting coordinates from {fdfpath}")
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
    print(f"Opening {fdfpath}")
    with open(fdfpath, "r", encoding="utf-8") as fdffile:
        match = re.search(
            "%block ChemicalSpeciesLabel\n" +
            "([0-9]+[ \t]+[0-9]+[ \t]+.+\n)+" +
            "%endblock ChemicalSpeciesLabel\n",
            fdffile.read()
        )
        parts = re.findall("([0-9]+)[ \t]+([0-9]+)[ \t]+(.+)\n", match[0])
        print(f"Getting species from {fdfpath}")
        for part in parts:
            ids.append(part[0])
            atomicweights.append(part[1])
            labels.append(part[2].strip())
        fdffile.close()
    return ids, atomicweights, labels
