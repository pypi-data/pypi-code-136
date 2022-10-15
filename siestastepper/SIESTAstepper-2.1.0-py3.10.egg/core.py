"""
Module bundling all functions needed to run a SIESTA calculation or analyse SIESTA output files
"""
from __future__ import absolute_import
from __future__ import division
import glob
import os
from subprocess import Popen
from subprocess import run as sprun
import shlex
from itertools import zip_longest
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmin, argrelmax
from sh import tail
from .helpers import (
    create_fdf,
    read_fdf,
    read_energy,
    read_force,
    get_it,
    print_run,
    check_restart,
    check_userbasis,
    copy_file,
    sort_,
    remove_nones,
    bohr_to_angstrom,
    lattice_vectors_mag,
    element_diameter,
    coords,
    species
)


class Settings:
    """Settings"""

    def __init__(self):
        """Initialise settings"""
        self.cwd = os.getcwd()
        self.log = "log"
        self.cores = None
        self.conda = None
        self.cont = "continue"
        self.contfrom = "log"
        self.contfiles = []
        self.contextensions = ["psf", "fdf"]
        self.siesta = "siesta"

    def get_cwd(self):
        """Get cwd value"""
        return self.cwd

    def set_cwd(self, newcwd):
        """Set cwd value"""
        self.cwd = newcwd

    def get_log(self):
        """Get log value"""
        return self.log

    def set_log(self, newlog):
        """Set log value"""
        self.log = newlog

    def get_cores(self):
        """Get cores value"""
        return self.cores

    def set_cores(self, newcores):
        """Set cores value"""
        self.cores = newcores

    def get_conda(self):
        """Get conda value"""
        return self.conda

    def set_conda(self, newconda):
        """Set conda value"""
        self.conda = newconda

    def get_cont(self):
        """Get cont value"""
        return self.cont

    def set_cont(self, newcont):
        """Set cont value"""
        self.cont = newcont

    def get_contfrom(self):
        """Get contfrom value"""
        return self.contfrom

    def set_contfrom(self, newcontfrom):
        """Set cont value"""
        self.contfrom = newcontfrom

    def get_siesta(self):
        """Get siesta value"""
        return self.siesta

    def set_siesta(self, newsiesta):
        """Set siesta value"""
        self.siesta = newsiesta


settings = Settings()


def run_next(i, label):
    """Run SIESTA for given step"""
    logs = glob.glob(f"i{int(i) - 1}{os.sep}{settings.get_log()}")
    logs += glob.glob(f"i{int(i) - 1}{os.sep}{settings.get_cont()}*{os.sep}{settings.get_log()}")
    logs = sort_(logs, "i*", settings.get_cont())
    if logs and settings.get_cont() in logs[-1]:
        match = re.search(f"i{int(i) - 1}{os.sep}{settings.get_cont()}(_*[0-9]*)", logs[-1])
        if not os.path.isfile(f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{label}.fdf"):
            if settings.get_contfrom() == "log":
                log_to_fdf(
                    f"i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}{os.sep}" +
                    f"{settings.get_log()}",
                    f"i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}{os.sep}{label}.fdf",
                    f"i{i}{os.sep}{label}.fdf"
                )
            elif settings.get_contfrom() == "XV":
                xv_to_fdf(
                    f"i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}{os.sep}{label}.XV",
                    f"i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}{os.sep}{label}.fdf",
                    f"i{i}{os.sep}{label}.fdf"
                )
            elif settings.get_contfrom() == "ANI":
                ani_to_fdf(
                    f"i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}{os.sep}{label}.ANI",
                    f"i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}{os.sep}{label}.fdf",
                    f"i{i}{os.sep}{label}.fdf"
                )
        copy_files(
            ["ion" if check_userbasis(f"i{i}{os.sep}{label}.fdf") else "psf"],
            label,
            f"{settings.get_cwd()}{os.sep}i{int(i) - 1}{os.sep}{settings.get_cont()}{match[1]}",
            f"{settings.get_cwd()}{os.sep}i{i}"
        )
    elif int(i) > 1:
        if not os.path.isfile(f"{settings.get_cwd()}{os.sep}i{str(int(i) + 1)}{os.sep}{label}.fdf"):
            if settings.get_contfrom() == "log":
                log_to_fdf(
                    f"i{int(i) - 1}{os.sep}{settings.get_log()}",
                    f"i{int(i) - 1}{os.sep}{label}.fdf",
                    f"i{i}{os.sep}{label}.fdf"
                )
            elif settings.get_contfrom() == "XV":
                xv_to_fdf(
                    f"i{int(i) - 1}{os.sep}{label}.XV",
                    f"i{int(i) - 1}{os.sep}{label}.fdf",
                    f"i{i}{os.sep}{label}.fdf"
                )
            elif settings.get_contfrom() == "ANI":
                ani_to_fdf(
                    f"i{int(i) - 1}{os.sep}{label}.ANI",
                    f"i{int(i) - 1}{os.sep}{label}.fdf",
                    f"i{i}{os.sep}{label}.fdf"
                )
        copy_files(
            ["ion" if check_userbasis(f"i{i}{os.sep}{label}.fdf") else "psf"],
            label,
            f"{settings.get_cwd()}{os.sep}i{int(i) - 1}",
            f"{settings.get_cwd()}{os.sep}i{i}"
        )
    os.chdir(f"{settings.get_cwd()}{os.sep}i{i}")
    print(f"Changed directory to {os.getcwd()}")
    print_run(f"i{i}", settings.get_cores(), settings.get_conda())
    _command(label=label)


def single_run(i, label):
    """Run SIESTA for given step without continuing next step"""
    os.chdir(f"{settings.get_cwd()}{os.sep}i{i}")
    print(f"Changed directory to {os.getcwd()}")
    if int(i) == 1:
        _command(label=label, issingle=True)
    else:
        folder = glob.glob(f"{settings.get_cwd()}{os.sep}i{int(i) - 1}")
        folder += glob.glob(f"{settings.get_cwd()}{os.sep}i{int(i) - 1}{os.sep}{settings.get_cont()}*")
        folder = sort_(folder, "i*", settings.get_cont())[-1]
        with open(
            f"{folder}{os.sep}{settings.get_log()}",
            "r",
            encoding="utf-8"
        ) as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(f"{folder}{os.sep}{settings.get_log()}: Job completed")
            if int(i) > 1:
                if not os.path.isfile(f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{label}.fdf"):
                    if settings.get_contfrom() == "log":
                        log_to_fdf(
                            f"{folder}{os.sep}{settings.get_log()}",
                            f"{folder}{os.sep}{label}.fdf",
                            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{label}.fdf"
                        )
                    elif settings.get_contfrom() == "XV":
                        xv_to_fdf(
                            f"{folder}{os.sep}{label}.XV",
                            f"{folder}{os.sep}{label}.fdf",
                            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{label}.fdf"
                        )
                    elif settings.get_contfrom() == "ANI":
                        ani_to_fdf(
                            f"{folder}{os.sep}{label}.ANI",
                            f"{folder}{os.sep}{label}.fdf",
                            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{label}.fdf"
                        )
                copy_files(
                    ["ion" if check_userbasis(
                        f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{label}.fdf"
                    ) else "psf"],
                    label,
                    folder,
                    f"{settings.get_cwd()}{os.sep}i{i}"
                )
            print_run(f"i{i}", settings.get_cores(), settings.get_conda())
            _command(label=label, issingle=True)


def ani_to_fdf(anipath, fdfpath, newfdfpath):
    """Convert last geometry of an ANI to FDF by using the previous FDF and ANI files"""
    print(f"Reading {anipath}")
    with open(anipath, "r", encoding="utf-8") as anifile:
        geo = anifile.read()
        number = geo.split("\n", 1)[0].strip()
        geo = geo.split(number + "\n \n")[-1]
        geo = geo.splitlines()
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, number)
        anifile.close()


def xyz_to_fdf(xyzpath, fdfpath, newfdfpath):
    """Convert XYZ to FDF by using the previous FDF and XYZ files"""
    print(f"Reading {xyzpath}")
    with open(xyzpath, "r", encoding="utf-8") as xyzfile:
        geo = xyzfile.read()
        number = geo.split("\n", 1)[0].strip()
        geo = geo.splitlines()[2:]
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, number)
        xyzfile.close()


def xv_to_fdf(xvpath, fdfpath, newfdfpath):
    """Convert XV to FDF by using the previous FDF and XV files"""
    print(f"Reading {xvpath}")
    with open(xvpath, "r", encoding="utf-8") as xvfile:
        lines = xvfile.readlines()
        geo = []
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)
        number = lines[0].strip()
        lines.pop(0)
        for line in lines:
            parts = line.split("     ")
            geo.append(
                f"       {bohr_to_angstrom(float(parts[2].strip()))}" +
                f"   {bohr_to_angstrom(float(parts[3].strip()))}" +
                f"   {bohr_to_angstrom(float(parts[4].strip()))}" +
                f"  {parts[0].strip()}\n"
            )
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, number)
        xvfile.close()


def log_to_fdf(logpath, fdfpath, newfdfpath):
    """Convert the last coordinates from a SIESTA log file to FDF by using previous log and FDF
    files"""
    print(f"Reading {logpath}")
    with open(logpath, "r", encoding="utf-8") as logfile:
        content = logfile.read()
        match = re.search(
            r"outcoor: Relaxed atomic coordinates \(Ang\): {18}\n" +
            r"( {3,4}-?[0-9]+\.[0-9]+" +
            r" {3,4}-?[0-9]+\.[0-9]+" +
            r" {3,4}-?[0-9]+\.[0-9]+" +
            r" {1,3}[0-9]+" +
            r" {1,7}[0-9]+" +
            r" {1,2} .+\n)+",
            content
        )
        if match is None:
            raise RuntimeError(f"ERROR: {logpath} is not converged")
        parts = re.findall(
            r" {3,4}(-?[0-9]+\.[0-9]+)" +
            r" {3,4}(-?[0-9]+\.[0-9]+)" +
            r" {3,4}(-?[0-9]+\.[0-9]+)" +
            r" {1,3}([0-9]+)" +
            r" {1,7}[0-9]+" +
            r" {1,2} .+\n",
            match[0]
        )
        geo = [
            (
                f"       {part[0]}" +
                f"   {part[1]}" +
                f"   {part[2]}" +
                f"  {part[3]}\n"
            ) for part in parts]
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, len(geo))
        logfile.close()


def xv_to_ani(label=None, path="i*"):
    """Convert XV files to ANI"""
    if label is None:
        raise ValueError("ERROR: Please set a label")
    files = glob.glob(f"{settings.get_cwd()}{os.sep}{path}{os.sep}{label}.XV")
    files += glob.glob(
        f"{settings.get_cwd()}{os.sep}{path}{os.sep}{settings.get_cont()}*{os.sep}{label}.XV"
    )
    fdfpath = glob.glob(f"{settings.get_cwd()}{os.sep}{path}{os.sep}{label}.fdf")[-1]
    files = sort_(files, path, settings.get_cont())
    if files is not None:
        ani = ""
        inds = None
        it = get_it(files)
        if [*set(it)] != list(range(min(it), max(it) + 1)):
            print("WARNING: There are missing XV files!")
        print(f"Opening {fdfpath}")
        with open(fdfpath, "r", encoding="utf-8") as fdffile:
            fdf = fdffile.read()
            inds = fdf.split(
                "%block ChemicalSpeciesLabel\n"
            )[1].split(
                "%endblock ChemicalSpeciesLabel\n"
            )[0]
            inds = inds.splitlines()
        for file in files:
            print(f"Opening {file}")
            with open(file, "r", encoding="utf-8") as f:
                match = re.search(
                    r" +([0-9]+)\n" +
                    r"( +[0-9]+" +
                    r" +[0-9]+" +
                    r" +-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+\n)+",
                    f.read()
                )
                ani += f"    {match[1]}\n\n"
                parts = re.findall(
                    r" +([0-9]+) +" +
                    r"[0-9]+ +" +
                    r"(-?[0-9]+\.[0-9]+) +" +
                    r"(-?[0-9]+\.[0-9]+) +" +
                    r"(-?[0-9]+\.[0-9]+) +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+\n",
                    match[0]
                )
                for part in parts:
                    part0 = None
                    for ind in inds:
                        if ind.startswith(part[0]):
                            part0 = ind.split(" ")[-1]
                    ani += f"{part0}       {part[1]}    {part[2]}    {part[3]}\n"
                f.close()
        print(f"Writing to {label}-XV.ANI")
        with open(f"{label}-XV.ANI", "w", encoding="utf-8") as anifile:
            anifile.write(ani)
            anifile.close()
        print("All XV files converted to ANI")


def merge_ani(label=None, path="i*"):
    """Merge ANI files"""
    if label is None:
        raise ValueError("ERROR: Please set a label")
    files = glob.glob(f"{settings.get_cwd()}{os.sep}{path}{os.sep}{label}.ANI")
    files += glob.glob(
        f"{settings.get_cwd()}{os.sep}{path}{os.sep}{settings.get_cont()}*{os.sep}{label}.ANI"
    )
    files = sort_(files, path, settings.get_cont())
    if files is not None:
        it = get_it(files)
        if [*set(it)] != list(range(min(it), max(it) + 1)):
            print("WARNING: There are missing ANI files!")
        with open(
            f"{settings.get_cwd()}{os.sep}{label}-merged.ANI",
            "w",
            encoding="utf-8"
        ) as outfile:
            print(f"{settings.get_cwd()}{os.sep}{label}-merged.ANI is opened")
            for f in files:
                with open(f, encoding="utf-8") as infile:
                    print(f"Writing {f}")
                    content = infile.read()
                    outfile.write(content)
                    infile.close()
            outfile.close()
        print("All ANI files are merged")
    else:
        print("No ANI files found")


def run(label):
    """Execute"""
    os.chdir(settings.get_cwd())
    folders = glob.glob(f"i*{os.sep}")
    logs = glob.glob(f"i*{os.sep}{settings.get_log()}")
    folders += glob.glob(f"i*{os.sep}{settings.get_cont()}*")
    logs += glob.glob(f"i*{os.sep}{settings.get_cont()}*{os.sep}{settings.get_log()}")
    folders = sort_(folders, "i*", settings.get_cont())
    logs = sort_(logs, "i*", settings.get_cont())
    if not logs:
        run_next("1", label)
    else:
        with open(logs[-1], "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(f"{logs[-1]}: Job completed")
                if len(folders) != len(logs) and not os.path.isfile(
                        f"{settings.get_cwd()}" +
                        f"{os.sep}i{str(int(logs[-1].split(os.sep)[0].strip('i')) + 1)}" +
                        f"{os.sep}{label}.fdf"
                ):
                    if settings.get_cont() in logs[-1]:
                        match = re.search(
                            f"i([0-9]+){os.sep}{settings.get_cont()}(_*[0-9]*)",
                            logs[-1]
                        )
                        if settings.get_contfrom() == "log":
                            log_to_fdf(
                                f"i{match[1]}{os.sep}{settings.get_cont()}{match[2]}" +
                                f"{os.sep}{settings.get_log()}",
                                f"i{match[1]}{os.sep}{settings.get_cont()}{match[2]}" +
                                f"{os.sep}{label}.fdf",
                                f"i{int(match[1]) + 1}{os.sep}{label}.fdf"
                            )
                        elif settings.get_contfrom() == "XV":
                            xv_to_fdf(
                                f"i{match[1]}{os.sep}{settings.get_cont()}{match[2]}" +
                                f"{os.sep}{label}.XV",
                                f"i{match[1]}{os.sep}{settings.get_cont()}{match[2]}" +
                                f"{os.sep}{label}.fdf",
                                f"i{int(match[1]) + 1}{os.sep}{label}.fdf"
                            )
                        elif settings.get_contfrom() == "ANI":
                            ani_to_fdf(
                                f"i{match[1]}{os.sep}{settings.get_cont()}{match[2]}" +
                                f"{os.sep}{label}.ANI",
                                f"i{match[1]}{os.sep}{settings.get_cont()}{match[2]}" +
                                f"{os.sep}{label}.fdf",
                                f"i{int(match[1]) + 1}{os.sep}{label}.fdf"
                            )
                    else:
                        if settings.get_contfrom() == "log":
                            log_to_fdf(
                                logs[-1].rsplit(os.sep)[0] + os.sep + settings.get_log(),
                                logs[-1].rsplit(os.sep)[0] + os.sep + label + ".fdf",
                                "i" +
                                str(int(logs[-1].split(os.sep)[0].strip("i")) + 1) +
                                os.sep +
                                label +
                                ".fdf"
                            )
                        elif settings.get_contfrom() == "XV":
                            xv_to_fdf(
                                logs[-1].rsplit(os.sep)[0] + os.sep + label + ".XV",
                                logs[-1].rsplit(os.sep)[0] + os.sep + label + ".fdf",
                                "i" +
                                str(int(logs[-1].split(os.sep)[0].strip("i")) + 1) +
                                os.sep +
                                label +
                                ".fdf"
                            )
                        elif settings.get_contfrom() == "ANI":
                            ani_to_fdf(
                                logs[-1].rsplit(os.sep)[0] + os.sep + label + ".ANI",
                                logs[-1].rsplit(os.sep)[0] + os.sep + label + ".fdf",
                                "i" +
                                str(int(logs[-1].split(os.sep)[0].strip("i")) + 1) +
                                os.sep +
                                label +
                                ".fdf"
                            )
                file.close()
                if len(folders) > len(logs):
                    run_next(str(int(logs[-1].split(os.sep)[0].strip("i")) + 1), label)
            elif not run_interrupted(str(int(logs[-1].split(os.sep)[0].strip("i"))), label):
                run_next(str(int(logs[-1].split(os.sep)[0].strip("i")) + 1), label)
    print("All iterations are completed")
    if settings.get_conda():
        sprun(
            [f"{os.sep}usr{os.sep}bin{os.sep}conda", "deactivate"] if os.name == "posix"
            else [f"C:{os.sep}{os.sep}Anaconda3{os.sep}Scripts{os.sep}deactivate"],
            check=True,
            shell=False
        )


def run_interrupted(i, label):
    """Continue to an interrupted calculation"""
    folders = glob.glob(f"i{i}{os.sep}{settings.get_cont()}*")
    folders = sort_(folders, "i*", settings.get_cont())
    if folders:
        with open(f"{folders[-1]}{os.sep}{settings.get_log()}", encoding="utf-8") as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(
                    f"i{i}{os.sep}{settings.get_cont()}{os.sep}{settings.get_log()}: Job completed"
                )
                return False
            match = re.search(f"i[0-9]+{os.sep}{settings.get_cont()}_*[0-9]*", folders[-1])
            if match[0].endswith(settings.get_cont()):
                _cont_step(f"{settings.get_cont()}_2", i, label)
                return True
            contnum = re.search(f"{os.sep}{settings.get_cont()}_([0-9]+)", match[0])[1]
            _cont_step(f"{settings.get_cont()}_{int(contnum) + 1}", i, label)
    _cont_step(settings.get_cont(), i, label)
    return True


def single_run_interrupted(i, label):
    """Continue to an interrupted calculation without continuing next step"""
    folders = glob.glob(f"i*{os.sep}{settings.get_cont()}*")
    folders = sort_(folders, "i*", settings.get_cont())
    if folders:
        with open(f"{folders[-1]}{os.sep}{settings.get_log()}", encoding="utf-8") as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(
                    f"i{i}{os.sep}{settings.get_cont()}{os.sep}{settings.get_log()}: Job completed"
                )
                return False
            match = re.search(f"i[0-9]+{os.sep}{settings.get_cont()}_*[0-9]*", folders[-1])
            if match[0].endswith(settings.get_cont()):
                _cont_step(f"{settings.get_cont()}_2", i, label, issingle=True)
                return True
            contnum = re.search(f"{os.sep}{settings.get_cont()}_([0-9]+)", match[0])[1]
            _cont_step(f"{settings.get_cont()}_{int(contnum) + 1}", i, label, issingle=True)
    _cont_step(settings.get_cont(), i, label, issingle=True)
    return True


def make_directories(n):
    """Create given number of i* folders"""
    for i in range(1, n + 1):
        if not os.path.exists(f"{settings.get_cwd()}{os.sep}i{i}"):
            print(f"Making directory i{i} under {settings.get_cwd().split(os.sep)[-1]}")
            os.mkdir(f"{settings.get_cwd()}{os.sep}i{i}")
            print(f"Directory i{i} is created")
        else:
            print(f"Directory i{i} exists")


def copy_files(extensions, label, source_, destination):
    """Copy and paste files"""
    if extensions is not None:
        for ext in extensions:
            if ext == "psf":
                files = glob.glob(f"{source_}{os.sep}*.psf")
                for f in files:
                    file = f.split(os.sep)[-1]
                    copy_file(f, f"{destination}{os.sep}{file}")
            elif ext == "ion":
                files = glob.glob(f"{source_}{os.sep}*.ion")
                for f in files:
                    file = f.split(os.sep)[-1]
                    copy_file(f, f"{destination}{os.sep}{file}")
            else:
                copy_file(
                    f"{source_}{os.sep}{label}.{ext}",
                    f"{destination}{os.sep}{label}.{ext}"
                )
    for cf in settings.contfiles:
        copy_file(f"{source_}{os.sep}{cf}", f"{destination}{os.sep}{cf}")


def energy_analysis(energytype="total", path="i*", plot_=True, print_=True):
    """Plot and return energies from log files"""
    files = glob.glob(f"{settings.get_cwd()}{os.sep}{path}{os.sep}{settings.get_log()}")
    files += glob.glob(
        f"{settings.get_cwd()}{os.sep}{path}{os.sep}{settings.get_cont()}*" +
        f"{os.sep}{settings.get_log()}"
    )
    files = sort_(files, path, settings.get_cont())
    energies = []
    it = []
    remove_nones(files, path, settings.get_cwd(), settings.get_cont(), settings.get_log())
    read_energy(energies=energies, files=files, it=it, energytype=energytype, print_=print_)
    if sorted(it) != list(range(min(it), max(it) + 1)) or None in energies:
        print("WARNING: There are missing values!")
    if None in energies:
        print("WARNING: There are missing energy values!")
    if plot_:
        plt.scatter(it, energies)
        plt.xlabel("Step")
        plt.ylabel(f"{energytype.capitalize()} energy (eV)")
        plt.show()
    return list(zip_longest(it, energies))


def force_analysis(atomindex="Tot", forcetype="atomic", path="i*", plot_=True, print_=True):
    """Plot and return atomic forces from log files"""
    files = glob.glob(f"{settings.get_cwd()}{os.sep}{path}{os.sep}{settings.get_log()}")
    files += glob.glob(
        f"{settings.get_cwd()}{os.sep}{path}{os.sep}{settings.get_cont()}*" +
        f"{os.sep}{settings.get_log()}"
    )
    files = sort_(files, path, settings.get_cont())
    remove_nones(files, path, settings.get_cwd(), settings.get_cont(), settings.get_log())
    forces = []
    it = []
    read_force(
        forces=forces,
        files=files,
        it=it,
        atomindex=atomindex,
        forcetype=forcetype,
        print_=print_
    )
    if sorted(it) != list(range(min(it), max(it) + 1)) or None in forces:
        print("WARNING: There are missing values!")
    if None in forces:
        print("WARNING: There are missing force values!")
    if plot_:
        _, axs = plt.subplots(2, 2)
        axs[0, 0].scatter(it, [row[0] for row in forces])
        axs[0, 0].set_title("x")
        axs[0, 1].scatter(it, [row[1] for row in forces])
        axs[0, 1].set_title("y")
        axs[1, 0].scatter(it, [row[2] for row in forces])
        axs[1, 0].set_title("z")
        axs[1, 1].scatter(it, [row[3] for row in forces])
        axs[1, 1].set_title("Resultant")
        for ax in axs.flat:
            ax.set(xlabel='Step', ylabel=f'{forcetype.capitalize()} force (eV/Ang)')
        for ax in axs.flat:
            ax.label_outer()
    return list(
        zip_longest(
            it,
            [row[0] for row in forces],
            [row[1] for row in forces],
            [row[2] for row in forces],
            [row[3] for row in forces]
        )
    )


def energy_diff(energytype="total", path="i*"):
    """Return energy differences between minima and maxima"""
    data = energy_analysis(energytype=energytype, path=path, plot_=False, print_=False)
    energies = np.array([_[1] for _ in data])
    it = np.array([_[0] for _ in data])
    min_idx = np.where(energies == np.amin(energies)) \
        if len(argrelmin(energies)) == 1 else argrelmin(energies)
    print(f"Minima: {energies[min_idx]}")
    max_idx = np.where(energies == np.amax(energies)) \
        if len(argrelmax(energies)) == 1 else argrelmax(energies)
    print(f"Maxima: {energies[max_idx]}")
    diff = np.absolute(energies[min_idx] - energies[max_idx])
    print(f"{energytype.capitalize()} energy difference: {diff}")
    return list(zip_longest(energies[min_idx], energies[max_idx], it[min_idx], it[max_idx], diff))


def force_diff(atomindex="Tot", forcetype="atomic", path="i*"):
    """Return force differences between minima and maxima"""
    data = force_analysis(
        atomindex=atomindex,
        forcetype=forcetype,
        path=path,
        plot_=False,
        print_=False
    )
    forcesx = np.array([_[1] for _ in data])
    forcesy = np.array([_[2] for _ in data])
    forcesz = np.array([_[3] for _ in data])
    forcesr = np.array([_[4] for _ in data])
    it = np.array([_[0] for _ in data])
    print("x")
    min_idxx = np.where(forcesx == np.amin(forcesx)) \
        if len(argrelmin(forcesx)) == 1 else argrelmin(forcesx)
    print(f"    Minima: {forcesx[min_idxx]}")
    max_idxx = np.where(forcesx == np.amax(forcesx)) \
        if len(argrelmax(forcesx)) == 1 else argrelmax(forcesx)
    print(f"    Maxima: {forcesx[max_idxx]}")
    diffx = np.absolute(forcesx[min_idxx] - forcesx[max_idxx])
    print(f"    {forcetype.capitalize()} force difference: {diffx}")
    print("y")
    min_idxy = np.where(forcesy == np.amin(forcesy)) \
        if len(argrelmin(forcesy)) == 1 else argrelmin(forcesy)
    print(f"    Minima: {forcesy[min_idxy]}")
    max_idxy = np.where(forcesy == np.amax(forcesy)) \
        if len(argrelmax(forcesy)) == 1 else argrelmax(forcesy)
    print(f"    Maxima: {forcesy[max_idxy]}")
    diffy = np.absolute(forcesy[min_idxy] - forcesy[max_idxy])
    print(f"    {forcetype.capitalize()} force difference: {diffy}")
    print("z")
    min_idxz = np.where(forcesz == np.amin(forcesz)) \
        if len(argrelmin(forcesz)) == 1 else argrelmin(forcesz)
    print(f"    Minima: {forcesz[min_idxz]}")
    max_idxz = np.where(forcesz == np.amax(forcesz)) \
        if len(argrelmax(forcesz)) == 1 else argrelmax(forcesz)
    print(f"    Maxima: {forcesz[max_idxz]}")
    diffz = np.absolute(forcesz[min_idxz] - forcesz[max_idxz])
    print(f"    {forcetype.capitalize()} force difference: {diffz}")
    print("Resultant")
    min_idxr = np.where(forcesr == np.amin(forcesr)) \
        if len(argrelmin(forcesr)) == 1 else argrelmin(forcesr)
    print(f"    Minima: {forcesr[min_idxr]}")
    max_idxr = np.where(forcesr == np.amax(forcesr)) \
        if len(argrelmax(forcesr)) == 1 else argrelmax(forcesr)
    print(f"    Maxima: {forcesr[max_idxr]}")
    diffr = np.absolute(forcesr[min_idxr] - forcesr[max_idxr])
    print(f"    {forcetype.capitalize()} force difference: {diffr}")
    return [
        list(zip_longest(forcesx[min_idxx], forcesx[max_idxx], it[min_idxx], it[max_idxx], diffx)),
        list(zip_longest(forcesy[min_idxy], forcesy[max_idxy], it[min_idxy], it[max_idxy], diffy)),
        list(zip_longest(forcesz[min_idxz], forcesz[max_idxz], it[min_idxz], it[max_idxz], diffz)),
        list(zip_longest(forcesr[min_idxr], forcesr[max_idxr], it[min_idxr], it[max_idxr], diffr)),
    ]


def pair_correlation_function(label=None, path="i*", dr=0.1, plot_=True):
    """Compute the three-dimensional pair correlation function for a set of spherical particles
    contained in the LatticeVectors. This simple function finds reference particles such that a
    sphere of radius rmax drawn around the particle will fit entirely within the cube, eliminating
    the need to compensate for edge effects.  If no such particles exist, an error is returned.
    Returns a tuple: (g, radii, interior_indices)
        g(r)            a numpy array containing the correlation function g(r)
        radii           a numpy array containing the radii of the spherical shells used to compute
                        g(r)
        reference_indices   indices of reference particles
    """
    fdfpath = glob.glob(f"{path}{os.sep}{label}.fdf")
    fdfpath += glob.glob(f"{path}{os.sep}{settings.get_cont()}*{os.sep}{label}.fdf")
    fdfpath = sort_(fdfpath, path, settings.get_cont())[-1]
    x, y, z = coords(fdfpath)
    x = np.array([_ * 0.1 for _ in x])
    y = np.array([_ * 0.1 for _ in y])
    z = np.array([_ * 0.1 for _ in z])
    sx, sy, sz = lattice_vectors_mag(fdfpath)
    sx = sx * 0.1
    sy = sy * 0.1
    sz = sz * 0.1
    _, _, species_ = species(fdfpath)
    rmax = max(element_diameter(specie) for specie in species_)
    print("Calculating the pair correlation function")
    bools1 = x > rmax
    bools2 = x < sx - rmax
    bools3 = y > rmax
    bools4 = y < sy - rmax
    bools5 = z > rmax
    bools6 = z < sz - rmax
    (interior_indices,) = np.where(bools1 * bools2 * bools3 * bools4 * bools5 * bools6)
    num_interior_particles = len(interior_indices)
    if num_interior_particles < 1:
        raise RuntimeError("No particles found. Increase the LatticeVectors or add more atoms.")
    edges = np.arange(0.0, rmax + 1.1 * dr, dr)
    num_increments = len(edges) - 1
    g = np.zeros([num_interior_particles, num_increments])
    radii = np.zeros(num_increments)
    numberdensity = len(x) / (sx * sy * sz)
    for p in range(num_interior_particles):
        index = interior_indices[p]
        d = np.sqrt((x[index] - x) ** 2 + (y[index] - y) ** 2 + (z[index] - z) ** 2)
        d[index] = 2 * rmax
        result, _ = np.histogram(d, bins=edges, density=False)
        g[p, :] = result / numberdensity
    g_average = np.zeros(num_increments)
    for i in range(num_increments):
        radii[i] = (edges[i] + edges[i + 1]) / 2.0
        router = edges[i + 1]
        rinner = edges[i]
        g_average[i] = np.mean(g[:, i]) / (4.0 / 3.0 * np.pi * (router ** 3 - rinner ** 3))
    print("The pair correlation function is calculated")
    if plot_:
        plt.figure()
        plt.plot(radii, g_average, color='black')
        plt.xlabel('r')
        plt.ylabel('g(r)')
        plt.xlim((0, rmax))
        plt.ylim((0, 1.05 * g_average.max()))
        plt.show()
    return g_average, radii, interior_indices


def _command(label=None, issingle=False):
    """SIESTA's run command"""
    if settings.get_conda():
        sprun(
            [f"{os.sep}usr{os.sep}bin{os.sep}conda", "activate", settings.get_conda()]
            if os.name == "posix"
            else
            [f"C:{os.sep}{os.sep}Anaconda3{os.sep}Scripts{os.sep}activate", settings.get_conda()],
            check=True,
            shell=False
        )
    with open(settings.get_log(), "w", encoding="utf-8") as logger:
        with Popen(
            shlex.split(
                f"mpirun -np {settings.get_cores()} " if settings.get_cores() is not None else "" +
                f"{settings.get_siesta()} {label}.fdf"
            ),
            shell=False,
            stdout=logger
        ) as job:
            print(f"PID is {job.pid}")
            for line in tail("-f", settings.get_log(), _iter=True):
                print(line.strip("\n"))
                if line == "Job completed\n" and issingle is False:
                    run(label)


def _cont_step(contfolder, i, label, issingle=False):
    print(f"Making directory '{contfolder}' under i{i}")
    os.mkdir(f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{contfolder}")
    contnummatch = re.search(f"{settings.get_cont()}_([0-9]+)", contfolder)
    contnum = contnummatch[1] if contnummatch is not None else "-1"
    if int(contnum) == 2:
        copy_files(
            settings.contextensions,
            label,
            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{settings.get_cont()}",
            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{contfolder}"
        )
    elif int(contnum) > 2:
        copy_files(
            settings.contextensions,
            label,
            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{settings.get_cont()}_{int(contnum) - 1}",
            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{contfolder}"
        )
    elif contnummatch is None:
        copy_files(
            settings.contextensions,
            label,
            f"{settings.get_cwd()}{os.sep}i{i}",
            f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{contfolder}"
        )
    os.chdir(f"{settings.get_cwd()}{os.sep}i{i}{os.sep}{contfolder}")
    print(f"Changed directory to {os.getcwd()}")
    print(f"Opening {settings.get_cwd()}{os.sep}i{i}{os.sep}{contfolder}{os.sep}{label}.fdf")
    with open(f"{label}.fdf", "r+", encoding="utf-8") as fdffile:
        check_restart(
            fdffile=fdffile,
            i=i,
            label=label,
            cwd=settings.get_cwd(),
            cont=contfolder,
            contextensions=settings.contextensions
        )
        fdffile.close()
    print_run(f"i{i}{os.sep}{contfolder}", settings.get_cores(), settings.get_conda())
    _command(label=label, issingle=issingle)
