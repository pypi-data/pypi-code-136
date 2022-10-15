"""
Module bundling all functions needed to run a SIESTA calculation or analyse SIESTA output files
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals
import glob
import os
from subprocess import Popen
try:
    from subprocess import run as sprun
except ImportError:
    from subprocess import call as sprun
import shlex
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest
import re
import io
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmin, argrelmax
import ANIAnimator
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
    species,
    unique
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
    logs = glob.glob("i{0}{1}{2}".format(int(i) - 1, os.sep, settings.get_log()))
    logs += glob.glob("i{0}{1}{2}*{1}{3}".format(
        int(i) - 1,
        os.sep,
        settings.get_cont(),
        settings.get_log()
    ))
    logs = sort_(logs, "i*", settings.get_cont())
    if logs and settings.get_cont() in logs[-1]:
        match = re.search(
            "i{0}{1}{2}(_*[0-9]*)".format(int(i) - 1, os.sep, settings.get_cont()),
            logs[-1]
        )
        if not os.path.isfile("{0}{1}i{2}{1}{3}.fdf".format(
                settings.get_cwd(),
                os.sep,
                i,
                label
        )):
            if settings.get_contfrom() == "log":
                log_to_fdf(
                    "i{0}{1}{2}{3}{1}{4}".format(
                        int(i) - 1,
                        os.sep,
                        settings.get_cont(),
                        match.group(1),
                        settings.get_log()
                    ),
                    "i{0}{1}{2}{3}{1}{4}.fdf".format(
                        int(i) - 1,
                        os.sep,
                        settings.get_cont(),
                        match.group(1),
                        label
                    ),
                    "i{0}{1}{2}.fdf".format(i, os.sep, label)
                )
            elif settings.get_contfrom() == "XV":
                xv_to_fdf(
                    "i{0}{1}{2}{3}{1}{4}.XV".format(
                        int(i) - 1,
                        os.sep,
                        settings.get_cont(),
                        match.group(1),
                        label),
                    "i{0}{1}{2}{3}{1}{4}.fdf".format(
                        int(i) - 1,
                        os.sep,
                        settings.get_cont(),
                        match.group(1),
                        label
                    ),
                    "i{0}{1}{2}.fdf".format(i, os.sep, label)
                )
            elif settings.get_contfrom() == "ANI":
                ani_to_fdf(
                    "i{0}{1}{2}{3}{1}{4}.ANI".format(
                        int(i) - 1,
                        os.sep,
                        settings.get_cont(),
                        match.group(1),
                        label
                    ),
                    "i{0}{1}{2}{3}{1}{4}.fdf".format(
                        int(i) - 1,
                        os.sep,
                        settings.get_cont(),
                        match.group(1),
                        label
                    ),
                    "i{0}{1}{2}.fdf".format(i, os.sep, label)
                )
        copy_files(
            ["ion" if check_userbasis("i{0}{1}{2}.fdf".format(i, os.sep, label)) else "psf"],
            label,
            "{0}{1}i{2}{1}{3}{4}".format(
                settings.get_cwd(),
                os.sep,
                int(i) - 1,
                settings.get_cont(),
                match.group(1)
            ),
            "{0}{1}i{2}".format(settings.get_cwd(), os.sep, i)
        )
    elif int(i) > 1:
        if not os.path.isfile("{0}{1}i{2}{1}{3}.fdf".format(
                settings.get_cwd(),
                os.sep,
                int(i) - 1,
                label
        )):
            if settings.get_contfrom() == "log":
                log_to_fdf(
                    "i{0}{1}{2}".format(int(i) - 1, os.sep, settings.get_log()),
                    "i{0}{1}{2}.fdf".format(int(i) - 1, os.sep, label),
                    "i{0}{1}{2}.fdf".format(i, os.sep, label)
                )
            elif settings.get_contfrom() == "XV":
                xv_to_fdf(
                    "i{0}{1}{2}.XV".format(int(i) - 1, os.sep, label),
                    "i{0}{1}{2}.fdf".format(int(i) - 1, os.sep, label),
                    "i{0}{1}{2}.fdf".format(i, os.sep, label)
                )
            elif settings.get_contfrom() == "ANI":
                ani_to_fdf(
                    "i{0}{1}{2}.ANI".format(int(i) - 1, os.sep, label),
                    "i{0}{1}{2}.fdf".format(int(i) - 1, os.sep, label),
                    "i{0}{1}{2}.fdf".format(i, os.sep, label)
                )
        copy_files(
            ["ion" if check_userbasis("i{0}{1}{2}.fdf".format(i, os.sep, label)) else "psf"],
            label,
            "{0}{1}i{2}".format(settings.get_cwd(), os.sep, int(i) - 1),
            "{0}{1}i{2}".format(settings.get_cwd(), os.sep, i)
        )
    os.chdir("{0}{1}i{2}".format(settings.get_cwd(), os.sep, i))
    print("Changed directory to {0}".format(os.getcwd()))
    print_run("i{0}".format(i), settings.get_cores(), settings.get_conda())
    _command(label=label)


def single_run(i, label):
    """Run SIESTA for given step without continuing next step"""
    os.chdir("{0}{1}i{2}".format(settings.get_cwd(), os.sep, i))
    print("Changed directory to {0}".format(os.getcwd()))
    if int(i) == 1:
        _command(label=label, issingle=True)
    else:
        folder = glob.glob("{0}{1}i{2}".format(settings.get_cwd(), os.sep, int(i) - 1))
        folder += glob.glob(
            "{0}{1}i{2}{1}{3}*".format(settings.get_cwd(), os.sep, int(i) - 1, settings.get_cont())
            )
        folder = sort_(folder, "i*", settings.get_cont())[-1]
        with io.open(
            "{0}{1}{2}".format(folder, os.sep, settings.get_log()),
            "r",
            encoding="utf-8"
        ) as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print("{0}{1}{2}: Job completed".format(folder, os.sep, settings.get_log()))
            if int(i) > 1:
                if not os.path.isfile("{0}{1}i{2}{1}{3}.fdf".format(
                        settings.get_cwd(),
                        os.sep,
                        i,
                        label
                )):
                    if settings.get_contfrom() == "log":
                        log_to_fdf(
                            "{0}{1}{2}".format(folder, os.sep, settings.get_log()),
                            "{0}{1}{2}.fdf".format(folder, os.sep, label),
                            "{0}{1}i{2}{1}{3}.fdf".format(settings.get_cwd(), os.sep, i, label)
                        )
                    elif settings.get_contfrom() == "XV":
                        xv_to_fdf(
                            "{0}{1}{2}.XV".format(folder, os.sep, label),
                            "{0}{1}{2}.fdf".format(folder, os.sep, label),
                            "{0}{1}i{2}{1}{3}.fdf".format(settings.get_cwd(), os.sep, i, label)
                        )
                    elif settings.get_contfrom() == "ANI":
                        ani_to_fdf(
                            "{0}{1}{2}.ANI".format(folder, os.sep, label),
                            "{0}{1}{2}.fdf".format(folder, os.sep, label),
                            "{0}{1}i{2}{1}{3}.fdf".format(settings.get_cwd(), os.sep, i, label)
                        )
                copy_files(
                    ["ion" if check_userbasis(
                        "{0}{1}i{2}{1}{3}.fdf".format(settings.get_cwd(), os.sep, i, label)
                    ) else "psf"],
                    label,
                    folder,
                    "{0}{1}i{2}".format(settings.get_cwd(), os.sep, i)
                )
            print_run("i{0}".format(i), settings.get_cores(), settings.get_conda())
            _command(label=label, issingle=True)


def ani_to_fdf(anipath, fdfpath, newfdfpath):
    """Convert last geometry of an ANI to FDF by using the previous FDF and ANI files"""
    print("Reading {0}".format(anipath))
    with io.open(anipath, "r", encoding="utf-8") as anifile:
        geo = anifile.read()
        number = geo.split("\n", 1)[0].strip()
        geo = geo.split(number + "\n \n")[-1]
        geo = geo.splitlines()
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, number)
        anifile.close()


def xyz_to_fdf(xyzpath, fdfpath, newfdfpath):
    """Convert XYZ to FDF by using the previous FDF and XYZ files"""
    print("Reading {0}".format(xyzpath))
    with io.open(xyzpath, "r", encoding="utf-8") as xyzfile:
        geo = xyzfile.read()
        number = geo.split("\n", 1)[0].strip()
        geo = geo.splitlines()[2:]
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, number)
        xyzfile.close()


def xv_to_fdf(xvpath, fdfpath, newfdfpath):
    """Convert XV to FDF by using the previous FDF and XV files"""
    print("Reading {0}".format(xvpath))
    with io.open(xvpath, "r", encoding="utf-8") as xvfile:
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
                "       {0}".format(bohr_to_angstrom(float(parts[2].strip()))) +
                "   {0}".format(bohr_to_angstrom(float(parts[3].strip()))) +
                "   {0}".format(bohr_to_angstrom(float(parts[4].strip()))) +
                "  {0}\n".format(parts[0].strip())
            )
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, number)
        xvfile.close()


def log_to_fdf(logpath, fdfpath, newfdfpath):
    """Convert the last coordinates from a SIESTA log file to FDF by using previous log and FDF
    files"""
    print("Reading {0}".format(logpath))
    with io.open(logpath, "r", encoding="utf-8") as logfile:
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
            raise RuntimeError("ERROR: {0} is not converged".format(logpath))
        parts = re.findall(
            r" {3,4}(-?[0-9]+\.[0-9]+)" +
            r" {3,4}(-?[0-9]+\.[0-9]+)" +
            r" {3,4}(-?[0-9]+\.[0-9]+)" +
            r" {1,3}([0-9]+)" +
            r" {1,7}[0-9]+" +
            r" {1,2} .+\n",
            match.group(0)
        )
        geo = [
            (
                "       {0}".format(part[0]) +
                "   {0}".format(part[1]) +
                "   {0}".format(part[2]) +
                "  {0}\n".format(part[3])
            ) for part in parts]
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath, len(geo))
        logfile.close()


def xv_to_ani(label=None, path="i*"):
    """Convert XV files to ANI"""
    if label is None:
        raise ValueError("ERROR: Please set a label")
    files = glob.glob("{0}{1}{2}{1}{3}.XV".format(settings.get_cwd(), os.sep, path, label))
    files += glob.glob("{0}{1}{2}{1}{3}*{1}{4}.XV".format(
        settings.get_cwd(),
        os.sep,
        path,
        settings.get_cont(),
        label
    ))
    fdfpath = glob.glob("{0}{1}{2}{1}{3}.fdf".format(settings.get_cwd(), os.sep, path, label))[-1]
    files = sort_(files, path, settings.get_cont())
    if files is not None:
        ani = ""
        inds = None
        it = get_it(files)
        if unique(it) != list(range(min(it), max(it) + 1)):
            print("WARNING: There are missing XV files!")
        print("Opening {0}".format(fdfpath))
        with io.open(fdfpath, "r", encoding="utf-8") as fdffile:
            fdf = fdffile.read()
            inds = fdf.split(
                "%block ChemicalSpeciesLabel\n"
            )[1].split(
                "%endblock ChemicalSpeciesLabel\n"
            )[0]
            inds = inds.splitlines()
        for file in files:
            print("Opening {0}".format(file))
            with io.open(file, "r", encoding="utf-8") as f:
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
                ani += "    {0}\n\n".format(match.group(1))
                parts = re.findall(
                    r" +([0-9]+) +" +
                    r"[0-9]+ +" +
                    r"(-?[0-9]+\.[0-9]+) +" +
                    r"(-?[0-9]+\.[0-9]+) +" +
                    r"(-?[0-9]+\.[0-9]+) +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+ +" +
                    r"-?[0-9]+\.[0-9]+\n",
                    match.group(0)
                )
                for part in parts:
                    part0 = None
                    for ind in inds:
                        if ind.startswith(part[0]):
                            part0 = ind.split(" ")[-1]
                    ani += "{0}       {1}    {2}    {3}\n".format(part0, part[1], part[2], part[3])
                f.close()
        print("Writing to {0}-XV.ANI".format(label))
        with io.open("{0}-XV.ANI".format(label), "w", encoding="utf-8") as anifile:
            anifile.write(ani)
            anifile.close()
        print("All XV files are converted to ANI")


def merge_ani(label=None, path="i*"):
    """Merge ANI files"""
    if label is None:
        raise ValueError("ERROR: Please set a label")
    files = glob.glob("{0}{1}{2}{1}{3}.ANI".format(settings.get_cwd(), os.sep, path, label))
    files += glob.glob(
        "{0}{1}{2}{1}{3}*{1}{4}.ANI".format(
            settings.get_cwd(),
            os.sep,
            path,
            settings.get_cont(),
            label
        )
    )
    files = sort_(files, path, settings.get_cont())
    if files is not None:
        it = get_it(files)
        if unique(it) != list(range(min(it), max(it) + 1)):
            print("WARNING: There are missing ANI files!")
        with io.open(
            "{0}{1}{2}-merged.ANI".format(settings.get_cwd(), os.sep, label),
            "w",
            encoding="utf-8"
        ) as outfile:
            print("{0}{1}{2}-merged.ANI is opened".format(settings.get_cwd(), os.sep, label))
            for f in files:
                with io.open(f, encoding="utf-8") as infile:
                    print("Writing {0}".format(f))
                    content = infile.read()
                    outfile.write(content)
                    infile.close()
            outfile.close()
        print("All ANI files are merged")
    else:
        print("No ANI files found")


def ani_to_gif(anifile=None, width=None, height=None, bonds_param=None, camera=None):
    """Convert ANI to GIF"""
    ANIAnimator.animate(
        anifile=anifile,
        width=width,
        height=height,
        bonds_param=bonds_param,
        camera=camera
    )


def run(label):
    """Execute"""
    os.chdir(settings.get_cwd())
    folders = glob.glob("i*{0}".format(os.sep))
    logs = glob.glob("i*{0}{1}".format(os.sep, settings.get_log()))
    folders += glob.glob("i*{0}{1}*".format(os.sep, settings.get_cont()))
    logs += glob.glob("i*{0}{1}*{0}{2}".format(os.sep, settings.get_cont(), settings.get_log()))
    folders = sort_(folders, "i*", settings.get_cont())
    logs = sort_(logs, "i*", settings.get_cont())
    if not logs:
        run_next("1", label)
    else:
        with io.open(logs[-1], "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print("{0}: Job completed".format(logs[-1]))
                if len(folders) != len(logs) and not os.path.isfile(
                        "{0}".format(settings.get_cwd()) +
                        "{0}i{str(int(logs[-1].split(os.sep)[0].strip('i'.format(os.sep))) + 1)}" +
                        "{0}{1}.fdf".format(os.sep, label)
                ):
                    if settings.get_cont() in logs[-1]:
                        match = re.search(
                            "i([0-9]+){0}{1}(_*[0-9]*)".format(os.sep, settings.get_cont()),
                            logs[-1]
                        )
                        if settings.get_contfrom() == "log":
                            log_to_fdf(
                                "i{0}{1}{2}{3}{1}{4}".format(
                                    match.group(1),
                                    os.sep,
                                    settings.get_cont(),
                                    match.group(2),
                                    settings.get_log()
                                ),
                                "i{0}{1}{2}{3}{1}{4}.fdf".format(
                                    match.group(1),
                                    os.sep,
                                    settings.get_cont(),
                                    match.group(2),
                                    label
                                ),
                                "i{0}{1}{2}.fdf".format(int(match.group(1)) + 1, os.sep, label)
                            )
                        elif settings.get_contfrom() == "XV":
                            xv_to_fdf(
                                "i{0}{1}{2}{3}{1}{4}.XV".format(
                                    match.group(1),
                                    os.sep,
                                    settings.get_cont(),
                                    match.group(2),
                                    label
                                ),
                                "i{0}{1}{2}{3}{1}{4}.fdf".format(
                                    match.group(1),
                                    os.sep,
                                    settings.get_cont(),
                                    match.group(2),
                                    label
                                ),
                                "i{0}{1}{2}.fdf".format(int(match.group(1)) + 1, os.sep, label)
                            )
                        elif settings.get_contfrom() == "ANI":
                            ani_to_fdf(
                                "i{0}{1}{2}{3}{1}{4}.ANI".format(
                                    match.group(1),
                                    os.sep,
                                    settings.get_cont(),
                                    match.group(2),
                                    label
                                ),
                                "i{0}{1}{2}{3}{1}{4}.fdf".format(
                                    match.group(1),
                                    os.sep,
                                    settings.get_cont(),
                                    match.group(2),
                                    label
                                ),
                                "i{0}{1}{2}.fdf".format(int(match.group(1)) + 1, os.sep, label)
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
            ["{0}usr{0}bin{0}conda".format(os.sep), "deactivate"] if os.name == "posix"
            else ["C:{0}{0}Anaconda3{0}Scripts{0}deactivate".format(os.sep)],
            check=True,
            shell=False
        )


def run_interrupted(i, label):
    """Continue to an interrupted calculation"""
    folders = glob.glob("i{0}{1}{2}*".format(i, os.sep, settings.get_cont()))
    folders = sort_(folders, "i*", settings.get_cont())
    if folders:
        with io.open(
            "{0}{1}{2}".format(folders[-1], os.sep, settings.get_log()),
            "r",
            encoding="utf-8"
        ) as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(
                    "i{0}{1}{2}{1}{3}: Job completed".format(
                        i,
                        os.sep,
                        settings.get_cont(),
                        settings.get_log()
                    )
                )
                return False
            match = re.search(
                "i[0-9]+{0}{1}_*[0-9]*".format(os.sep, settings.get_cont()),
                folders[-1]
            )
            if match.group(0).endswith(settings.get_cont()):
                _cont_step("{0}_2".format(settings.get_cont()), i, label)
                return True
            contnum = re.search(
                "{0}{1}_([0-9]+)".format(os.sep, settings.get_cont()),
                match.group(0)
            )[1]
            _cont_step("{0}_{1}".format(settings.get_cont(), int(contnum) + 1), i, label)
    _cont_step(settings.get_cont(), i, label)
    return True


def single_run_interrupted(i, label):
    """Continue to an interrupted calculation without continuing next step"""
    folders = glob.glob("i*{0}{1}*".format(os.sep, settings.get_cont()))
    folders = sort_(folders, "i*", settings.get_cont())
    if folders:
        with io.open(
            "{0}{1}{2}".format(folders[-1], os.sep, settings.get_log()),
            "r",
            encoding="utf-8"
        ) as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(
                    "i{0}{1}{2}{1}{3}: Job completed".format(
                        i,
                        os.sep,
                        settings.get_cont(),
                        settings.get_log()
                    )
                )
                return False
            match = re.search(
                "i[0-9]+{0}{1}_*[0-9]*".format(os.sep, settings.get_cont()),
                folders[-1]
            )
            if match.group(0).endswith(settings.get_cont()):
                _cont_step("{0}_2".format(settings.get_cont()), i, label, issingle=True)
                return True
            contnum = re.search(
                "{0}{1}_([0-9]+)".format(os.sep, settings.get_cont()),
                match.group(0)
            )[1]
            _cont_step(
                "{0}_{1}".format(settings.get_cont(), int(contnum) + 1),
                i,
                label,
                issingle=True
            )
    _cont_step(settings.get_cont(), i, label, issingle=True)
    return True


def make_directories(n):
    """Create given number of i* folders"""
    for i in range(1, n + 1):
        if not os.path.exists("{0}{1}i{2}".format(settings.get_cwd(), os.sep, i)):
            print("Making directory i{0} under {1}".format(i, settings.get_cwd().split(os.sep)[-1]))
            os.mkdir("{0}{1}i{2}".format(settings.get_cwd(), os.sep, i))
            print("Directory i{0} is created".format(i))
        else:
            print("Directory i{0} exists".format(i))


def copy_files(extensions, label, source_, destination):
    """Copy and paste files"""
    if extensions is not None:
        for ext in extensions:
            if ext == "psf":
                files = glob.glob("{0}{1}*.psf".format(source_, os.sep))
                for f in files:
                    file = f.split(os.sep)[-1]
                    copy_file(f, "{0}{1}{2}".format(destination, os.sep, file))
            elif ext == "ion":
                files = glob.glob("{0}{1}*.ion".format(source_, os.sep))
                for f in files:
                    file = f.split(os.sep)[-1]
                    copy_file(f, "{0}{1}{2}".format(destination, os.sep, file))
            else:
                copy_file(
                    "{0}{1}{2}.{3}".format(source_, os.sep, label, ext),
                    "{0}{1}{2}.{3}".format(destination, os.sep, label, ext)
                )
    for cf in settings.contfiles:
        copy_file(
            "{0}{1}{2}".format(source_, os.sep, cf),
            "{0}{1}{2}".format(destination, os.sep, cf)
        )


def energy_analysis(energytype="total", path="i*", plot_=True, print_=True):
    """Plot and return energies from log files"""
    files = glob.glob("{0}{1}{2}{1}{3}".format(
        settings.get_cwd(),
        os.sep,
        path,
        settings.get_log()
    ))
    files += glob.glob(
        "{0}{1}{2}{1}{3}*".format(settings.get_cwd(), os.sep, path, settings.get_cont()) +
        "{0}{1}".format(os.sep, settings.get_log())
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
        plt.ylabel("{0} energy (eV)".format(energytype.capitalize()))
        plt.show()
    return list(zip_longest(it, energies))


def force_analysis(atomindex="Tot", forcetype="atomic", path="i*", plot_=True, print_=True):
    """Plot and return forces from log files"""
    files = glob.glob("{0}{1}{2}{1}{3}".format(
        settings.get_cwd(),
        os.sep,
        path,
        settings.get_log()
    ))
    files += glob.glob(
        "{0}{1}{2}{1}{3}*".format(settings.get_cwd(), os.sep, path, settings.get_cont()) +
        "{0}{1}".format(os.sep, settings.get_log())
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
            ax.set(xlabel='Step', ylabel='{0} force (eV/Ang)'.format(forcetype.capitalize()))
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
    print("Minima: {0}".format(energies[min_idx]))
    max_idx = np.where(energies == np.amax(energies)) \
        if len(argrelmax(energies)) == 1 else argrelmax(energies)
    print("Maxima: {0}".format(energies[max_idx]))
    diff = np.absolute(energies[min_idx] - energies[max_idx])
    print("{0} energy difference: {1}".format(energytype.capitalize(), diff))
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
    print("    Minima: {0}".format(forcesx[min_idxx]))
    max_idxx = np.where(forcesx == np.amax(forcesx)) \
        if len(argrelmax(forcesx)) == 1 else argrelmax(forcesx)
    print("    Maxima: {0}".format(forcesx[max_idxx]))
    diffx = np.absolute(forcesx[min_idxx] - forcesx[max_idxx])
    print("    {0} force difference: {1}".format(forcetype.capitalize(), diffx))
    print("y")
    min_idxy = np.where(forcesy == np.amin(forcesy)) \
        if len(argrelmin(forcesy)) == 1 else argrelmin(forcesy)
    print("    Minima: {0}".format(forcesy[min_idxy]))
    max_idxy = np.where(forcesy == np.amax(forcesy)) \
        if len(argrelmax(forcesy)) == 1 else argrelmax(forcesy)
    print("    Maxima: {0}".format(forcesy[max_idxy]))
    diffy = np.absolute(forcesy[min_idxy] - forcesy[max_idxy])
    print("    {0} force difference: {1}".format(forcetype.capitalize(), diffy))
    print("z")
    min_idxz = np.where(forcesz == np.amin(forcesz)) \
        if len(argrelmin(forcesz)) == 1 else argrelmin(forcesz)
    print("    Minima: {0}".format(forcesz[min_idxz]))
    max_idxz = np.where(forcesz == np.amax(forcesz)) \
        if len(argrelmax(forcesz)) == 1 else argrelmax(forcesz)
    print("    Maxima: {0}".format(forcesz[max_idxz]))
    diffz = np.absolute(forcesz[min_idxz] - forcesz[max_idxz])
    print("    {0} force difference: {1}".format(forcetype.capitalize(), diffz))
    print("Resultant")
    min_idxr = np.where(forcesr == np.amin(forcesr)) \
        if len(argrelmin(forcesr)) == 1 else argrelmin(forcesr)
    print("    Minima: {0}".format(forcesr[min_idxr]))
    max_idxr = np.where(forcesr == np.amax(forcesr)) \
        if len(argrelmax(forcesr)) == 1 else argrelmax(forcesr)
    print("    Maxima: {0}".format(forcesr[max_idxr]))
    diffr = np.absolute(forcesr[min_idxr] - forcesr[max_idxr])
    print("    {0} force difference: {1}".format(forcetype.capitalize(), diffr))
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
    fdfpath = glob.glob("{0}{1}{2}.fdf".format(path, os.sep, label))
    fdfpath += glob.glob("{0}{1}{2}*{1}{3}.fdf".format(path, os.sep, settings.get_cont(), label))
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
            ["{0}usr{0}bin{0}conda".format(os.sep), "activate", settings.get_conda()]
            if os.name == "posix"
            else
            ["C:{0}{0}Anaconda3{0}Scripts{0}activate".format(os.sep), settings.get_conda()],
            check=True,
            shell=False
        )
    with io.open(settings.get_log(), "w", encoding="utf-8") as logger:
        with Popen(
            shlex.split("{0}{1} {2}.fdf".format(
                "mpirun -np {0} ".format(
                    settings.get_cores()
                ) if settings.get_cores() is not None else "",
                settings.get_siesta(),
                label
            )),
            shell=False,
            stdout=logger
        ) as job:
            print("PID is {0}".format(job.pid))
            for line in tail("-f", settings.get_log(), _iter=True):
                print(line.strip("\n"))
                if line == "Job completed\n" and issingle is False:
                    run(label)


def _cont_step(contfolder, i, label, issingle=False):
    print("Making directory '{0}' under i{1}".format(contfolder, i))
    os.mkdir("{0}{1}i{2}{1}{3}".format(settings.get_cwd(), os.sep, i, contfolder))
    contnummatch = re.search("{0}_([0-9]+)".format(settings.get_cont()), contfolder)
    contnum = contnummatch.group(1) if contnummatch is not None else "-1"
    if int(contnum) == 2:
        copy_files(
            settings.contextensions,
            label,
            "{0}{1}i{2}{1}{3}".format(settings.get_cwd(), os.sep, i, settings.get_cont()),
            "{0}{1}i{2}{1}{3}".format(settings.get_cwd(), os.sep, i, contfolder)
        )
    elif int(contnum) > 2:
        copy_files(
            settings.contextensions,
            label,
            "{0}{1}i{2}{1}{3}_{4}".format(
                settings.get_cwd(),
                os.sep,
                i,
                settings.get_cont(),
                int(contnum) - 1
            ),
            "{0}{1}i{2}{1}{3}".format(settings.get_cwd(), os.sep, i, contfolder)
        )
    elif contnummatch is None:
        copy_files(
            settings.contextensions,
            label,
            "{0}{1}i{2}".format(settings.get_cwd(), os.sep, i),
            "{0}{1}i{2}{1}{3}".format(settings.get_cwd(), os.sep, i, contfolder)
        )
    os.chdir("{0}{1}i{2}{1}{3}".format(settings.get_cwd(), os.sep, i, contfolder))
    print("Changed directory to {0}".format(os.getcwd()))
    print("Opening {0}{1}i{2}{1}{3}{1}{4}.fdf".format(
        settings.get_cwd(),
        os.sep,
        i,
        contfolder,
        label
    ))
    with io.open("{0}.fdf".format(label), "r+", encoding="utf-8") as fdffile:
        check_restart(
            fdffile=fdffile,
            i=i,
            label=label,
            cwd=settings.get_cwd(),
            cont=contfolder,
            contextensions=settings.contextensions
        )
        fdffile.close()
    print_run(
        "i{0}{1}{2}".format(i, os.sep, contfolder),
        settings.get_cores(),
        settings.get_conda()
    )
    _command(label=label, issingle=issingle)
