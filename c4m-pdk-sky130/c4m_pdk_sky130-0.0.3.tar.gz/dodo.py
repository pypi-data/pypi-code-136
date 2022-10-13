# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import os, sys, site
from os.path import relpath, basename
from itertools import chain
from pathlib import Path
from textwrap import dedent
import yaml
from typing import List, Dict, Tuple, Generator

from doit import get_var
from doit.action import BaseAction, CmdAction
from doit.tools import check_timestamp_unchanged, create_folder

import pdkmaster, c4m, c4m.flexcell, c4m.flexio, c4m.flexmem


### Config


DOIT_CONFIG = {
    "default_tasks": [
        "install", "open_pdk", "coriolis", "klayout", "spice_models", "spice", "gds",
        "rtl", "liberty",
    ],
}

### support functions


def get_var_env(name, default=None):
    """Uses get_var to get a command line variable, also checks
    environment variables for default value

    If os.environ[name.upper()] exists that value will override the
    default value given.
    """
    try:
        default = os.environ[name.upper()]
    except:
        # Keep the specified default
        pass
    return get_var(name, default=default)


class AVTScriptAction(BaseAction):
    def __init__(self, avt_script, tmp=None):
        if tmp is None:
            tmp = tmp_dir
        self.script = avt_script
        self.tmp = tmp

        self.out = None
        self.err = None
        self.result = None
        self.values = {}

    def execute(self, out=None, err=None):
        # Create new action on every new call so we can always write
        # the script to the stdin of the subprocess.
        if avt_shell is None:
            action = CmdAction('echo "disabled because lack of avt_shell"')
        else:
            pr, pw = os.pipe()
            fpw = os.fdopen(pw, "w")
            fpw.write(self.script)
            fpw.close()

            action = CmdAction(avt_shell, stdin=pr, cwd=self.tmp)

        r = action.execute(out=out, err=err)
        self.values = action.values
        self.result = action.result
        self.out = action.out
        self.err = action.err
        return r


### globals


top_dir = Path(__file__).parent
tmp_dir = top_dir.joinpath("tmp")
scripts_dir = top_dir.joinpath("scripts")
dist_dir = top_dir.joinpath("dist")
open_pdk_dir = top_dir.joinpath("open_pdk")
open_pdk_sky130_dir = open_pdk_dir.joinpath("C4M.Sky130")
open_pdk_tech_dir = open_pdk_sky130_dir.joinpath("libs.tech")
open_pdk_ref_dir = open_pdk_sky130_dir.joinpath("libs.ref")

override_dir = top_dir.joinpath("override")

# variables
pdkmaster_pip = get_var_env("pdkmaster_pip", default="pip3")
pdkmaster_python = get_var_env("pdkmaster_python", default="python3")
coriolis_python = get_var_env("coriolis_python", default="python2")
avertec_top = get_var_env("avertec_top")
avt_shell = get_var_env(
    "avt_shell", default=(
        f"{avertec_top}/bin/avt_shell" if avertec_top is not None else None
    ),
)
sky130_pdk = get_var_env("sky130_pdk")
if sky130_pdk is None:
    raise EnvironmentError(
        "sky130_pdk variable or SKY130_PDK environment variable not given"
    )
os.environ["SKY130_PDK"] = sky130_pdk
sky130_pdk_dir = Path(sky130_pdk)
sky130_pdk_tech_spice_dir = sky130_pdk_dir.joinpath("libs.tech", "ngspice")
sky130_pdk_ref_spice_dir = sky130_pdk_dir.joinpath("libs.ref", "sky130_fd_pr", "spice")

# Module dirs are derived with a task as they are dependent on pdkmasteR_python
pdkmaster_inst_dir = Path(pdkmaster.__file__).parent
c4m_local_dir = top_dir.joinpath("c4m")
sky130_local_dir = c4m_local_dir.joinpath("pdk", "sky130")
# Don't use local module for c4m
c4m_inst_dir = Path(site.getsitepackages()[0]).joinpath("c4m")
sky130_inst_dir = c4m_inst_dir.joinpath("pdk", "sky130")
flexcell_inst_dir = Path(c4m.flexcell.__file__).parent
flexio_inst_dir = Path(c4m.flexio.__file__).parent
flexmem_inst_dir = Path(c4m.flexmem.__file__).parent

c4m_py_files = tuple(c4m_local_dir.rglob("*.py"))

### cell list

cell_list_file = top_dir.joinpath("cell_list.yml")

def task_cell_list():
    """Regenerate cell list.

    This task is not run by default. It needs to be run manually when the cell list
    has been changed and then the updated file has to be commit to git.
    """
    def write_list():
        import yaml

        from doitlib import libs

        cell_list = {
            lib.name: list(cell.name for cell in lib.cells)
            for lib in libs.__libs__
        }
        with cell_list_file.open("w") as f:
            yaml.dump(cell_list, f)

    return {
        "title": lambda _: "Creating cell list file",
        "targets": (
            cell_list_file,
        ),
        "actions": (
            write_list,
        ),
    }

# We assume that the cell list is stored in git and is available in the top directory.
assert cell_list_file.exists()
with cell_list_file.open("r") as f:
    cell_list: Dict[str, List[str]]
    cell_list = yaml.safe_load(f)

# Which python modules are used for the libraries
lib_module_paths = {
    "StdCellLib": (pdkmaster_inst_dir, flexcell_inst_dir),
    "IOLib": (pdkmaster_inst_dir, flexcell_inst_dir, flexio_inst_dir),
    "ExampleSRAMs": (pdkmaster_inst_dir, flexcell_inst_dir, flexmem_inst_dir),
    "MacroLib": (pdkmaster_inst_dir,),
}

### main tasks


# cell_list


#
# spice_models
open_pdk_spice_dir = open_pdk_tech_dir.joinpath("ngspice")
spice_corners = ("tt", "ff", "ss", "fs", "sf")
bip_spice_corners = {"t", "f", "s"}
spice_model_files = {
    **{
        f"logic_{corner}": {
            "deps": (
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__nfet_01v8__{corner}.pm3.spice",
                ),
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__pfet_01v8__{corner}.pm3.spice",
                ),
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__nfet_01v8_lvt__{corner}.pm3.spice",
                ),
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__pfet_01v8_lvt__{corner}.pm3.spice",
                ),
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__pfet_01v8_hvt__{corner}.pm3.spice",
                ),
            ),
            "targets": (
                open_pdk_spice_dir.joinpath(f"C4M.Sky130_logic_{corner}_model.spice"),
            ),
        }
        for corner in spice_corners
    },
    **{
        f"io_{corner}": {
            "deps": (
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__nfet_g5v0d10v5__{corner}.pm3.spice",
                ),
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__pfet_g5v0d10v5__{corner}.pm3.spice",
                ),
            ),
            "targets": (
                open_pdk_spice_dir.joinpath(f"C4M.Sky130_io_{corner}_model.spice"),
            ),
        }
        for corner in spice_corners
    },
    "diode": {
        "deps": tuple(
            sky130_pdk_ref_spice_dir.joinpath(f)
            for f in (
                "sky130_fd_pr__diode_pw2nd_05v5.model.spice",
                "sky130_fd_pr__diode_pd2nw_05v5.model.spice",
                # "sky130_fd_pr__diode_pd2nw_05v5_hvt.model.spice",
                # "sky130_fd_pr__diode_pd2nw_05v5_lvt.model.spice",
                # "sky130_fd_pr__diode_pd2nw_11v0.model.spice",
                # "sky130_fd_pr__diode_pd2nw_11v0_no_rs.model.spice",
                # "sky130_fd_pr__diode_pw2nd_05v5__extended_drain.model.spice",
                # "sky130_fd_pr__diode_pw2nd_05v5_lvt.model.spice",
                # "sky130_fd_pr__diode_pw2nd_05v5_nvt.model.spice",
                # "sky130_fd_pr__diode_pw2nd_11v0.model.spice",
            )
        ),
        "targets": (
            open_pdk_spice_dir.joinpath(f"C4M.Sky130_diode_model.spice"),
        ),
    },
    **{
        f"diode_{corner}": {
            "deps": (
                sky130_pdk_tech_spice_dir.joinpath("corners", corner, "nonfet.spice"),
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__pfet_01v8__{corner}.corner.spice",
                )
            ),
            "targets": (
                open_pdk_spice_dir.joinpath(f"C4M.Sky130_diode_{corner}_params.spice"),
            ),
            "params": (
                "sky130_fd_pr__nfet_01v8__ajunction_mult",
                "sky130_fd_pr__nfet_01v8__pjunction_mult",
                "sky130_fd_pr__pfet_01v8__ajunction_mult",
                "sky130_fd_pr__pfet_01v8__pjunction_mult",
                "sky130_fd_pr__model__parasitic__diode_pw2dn__ajunction_mult",
                "sky130_fd_pr__model__parasitic__diode_ps2nw__ajunction_mult",
                "sky130_fd_pr__model__parasitic__diode_ps2dn__pjunction_mult",
                "sky130_fd_pr__model__parasitic__diode_ps2nw__pjunction_mult",
            )
        }
        for corner in spice_corners
    },
    "pnp": {
        "deps": tuple(
            sky130_pdk_ref_spice_dir.joinpath(f)
            for f in (
                "sky130_fd_pr__pnp_05v5_W0p68L0p68.model.spice",
                "sky130_fd_pr__pnp_05v5_W3p40L3p40.model.spice",
            )
        ),
        "targets": (
            open_pdk_spice_dir.joinpath(f"C4M.Sky130_pnp_model.spice"),
        ),
    },
    **{
        f"pnp_{corner}": {
            "deps": (
                sky130_pdk_tech_spice_dir.joinpath("corners", corner+corner, "nonfet.spice"),
            ),
            "targets": (
                open_pdk_spice_dir.joinpath(f"C4M.Sky130_pnp_{corner}_params.spice"),
            ),
            "params": (
                "dkispp", "dkbfpp", "dknfpp",
                "dkispp5x", "dkbfpp5x", "dknfpp5x",
            )
        }
        for corner in bip_spice_corners
    },
    "npn": {
        "deps": tuple(
            sky130_pdk_ref_spice_dir.joinpath(f)
            for f in (
                "sky130_fd_pr__npn_05v5_W1p00L1p00.model.spice",
                "sky130_fd_pr__npn_05v5_W1p00L2p00.model.spice",
            )
        ),
        "targets": (
            open_pdk_spice_dir.joinpath(f"C4M.Sky130_npn_model.spice"),
        ),
    },
    **{
        f"npn_{corner}": {
            "deps": (
                sky130_pdk_ref_spice_dir.joinpath(
                    f"sky130_fd_pr__npn_05v5__{corner}.corner.spice",
                ),
            ),
            "targets": (
                open_pdk_spice_dir.joinpath(f"C4M.Sky130_npn_{corner}_params.spice"),
            ),
            "params": (
                "dkisnpn1x1", "dkbfnpn1x1",
                "dkisnpn1x2", "dkbfnpn1x2",
                "dkisnpnpolyhv", "dkbfnpnpolyhv",
            )
        }
        for corner in bip_spice_corners
    },
}
spice_logic_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_logic_lib.spice")
spice_io_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_io_lib.spice")
spice_diode_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_diode_lib.spice")
spice_pnp_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_pnp_lib.spice")
spice_npn_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_npn_lib.spice")
spice_all_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_all_lib.spice")
spice_lib_file = open_pdk_spice_dir.joinpath(f"C4M.Sky130_lib.spice")
def task_spice_models():
    """Convert Sky130 spice model files
    
    The model files are converted as the open_pdk ones are not compatible with
    HiTas/Yagle."""
    def spice_model_title(task):
        corner = task.name[13:]
        return f"Converting spice model file for corner {corner}"

    def remove_semicolon(corner):
        files = spice_model_files[corner]
        with files["targets"][0].open("w") as f_target:
            for dep in files["deps"]:
                with dep.open("r") as f_dep:
                    for l in f_dep:
                        # Yagle does not like ; comments in multiline parameter list
                        if ";" in l:
                            l = l[:l.index(";")] + "\n"
                        f_target.write(l)

    def convert_spice(corner):
        import re

        files = spice_model_files[corner]
        with files["targets"][0].open("w") as f_target:
            for dep in files["deps"]:
                with dep.open("r") as f_dep:
                    # We start with ignoring the lines
                    output = False
                    for line in f_dep:
                        # Extract only the .model decks
                        if line.startswith(".model"):
                            output = True
                        if line.startswith(".ends"):
                            output = False
                        if output:
                            # Remove l/w parameter dependency.
                            # These are only used for Monte-Carlo simulation and thus so
                            # we don't support these type of simulations yet.
                            # It is removed as the l/w dependency is the cause of HiTas/Yagle
                            # incompatibility.
                            # l/w is always used in a {} section that starts with a float;
                            # we only take first float without the rest of the section.
                            s = re.search("{(-?\d+(\.\d*)?(e(-|\+)?\d+)?).*}", line) # type: ignore
                            if s:
                                line = line[:s.start()] + s.groups()[0] + line[s.end():]
                            f_target.write(line)

    def zero_mc_switch(corner):
        import re

        files = spice_model_files[corner]
        with files["targets"][0].open("w") as f_target:
            for dep in files["deps"]:
                with dep.open("r") as f_dep:
                    for line in f_dep:
                        s = re.search(
                            "MC_MM_SWITCH\*AGAUSS\([^\)]*\)((\*[^/]*)?/sqrt\(mult\)|\*\([^\)]*\))",
                            line,
                        )
                        if s:
                            line = line[:s.start()] + "0.0" + line[s.end():]
                        if ";" in line:
                            line = line[:line.index(";")] + "\n"
                        f_target.write(line)

    def extract_params(corner):
        files = spice_model_files[corner]
        with files["targets"][0].open("w") as f_target:
            print(f"* {corner}\n.param", file=f_target)
            for dep in files["deps"]:
                dep: Path
                with dep.open("r") as f_dep:
                    for l in f_dep:
                        for param in files["params"]:
                            if (
                                l.startswith(f"+ {param} =")
                                or l.startswith(f"+ {param}=")
                            ):
                                # Remove ; part
                                if ";" in l:
                                    l = l[:l.index(";")] + "\n"
                                f_target.write(l)

    def write_libs():
        with spice_logic_lib_file.open("w") as f:
            print("* C4M.Sky130 logic transistors lib file\n", file=f)

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib {corner}
                    .include "C4M.Sky130_logic_{corner}_model.spice"
                    .endl {corner}
                """[1:]))

        with spice_io_lib_file.open("w") as f:
            print("* C4M.Sky130 IO transistors lib file\n", file=f)

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib {corner}
                    .include "C4M.Sky130_io_{corner}_model.spice"
                    .endl {corner}
                """[1:]))

        with spice_diode_lib_file.open("w") as f:
            print("* C4M.Sky130 diode lib file\n", file=f)

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib {corner}
                    .include "C4M.Sky130_diode_{corner}_params.spice"
                    .include "C4M.Sky130_diode_model.spice"
                    .endl {corner}
                """[1:]))

        with spice_pnp_lib_file.open("w") as f:
            print("* C4M.Sky130 pnp lib file\n", file=f)

            for corner in bip_spice_corners:
                f.write(dedent(f"""
                    .lib {corner}
                    .include "C4M.Sky130_pnp_{corner}_params.spice"
                    .include "C4M.Sky130_pnp_model.spice"
                    .endl {corner}
                """[1:]))

        with spice_npn_lib_file.open("w") as f:
            print("* C4M.Sky130 npn lib file\n", file=f)

            for corner in bip_spice_corners:
                f.write(dedent(f"""
                    * npn model needs also diode corner
                    .lib {corner}
                    .include "C4M.Sky130_npn_{corner}_params.spice"
                    .include "C4M.Sky130_npn_model.spice"
                    .endl {corner}
                """[1:]))

        with spice_all_lib_file.open("w") as f:
            print("* C4M.Sky130 global per device corner lib file\n", file=f)

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib logic_{corner}
                    .include "C4M.Sky130_logic_{corner}_model.spice"
                    .endl logic_{corner}
                """[1:]))

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib io_{corner}
                    .include "C4M.Sky130_io_{corner}_model.spice"
                    .endl io_{corner}
                """[1:]))

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib diode_{corner}
                    .include "C4M.Sky130_diode_{corner}_params.spice"
                    .include "C4M.Sky130_diode_model.spice"
                    .endl diode_{corner}
                """[1:]))

            for corner in bip_spice_corners:
                f.write(dedent(f"""
                    .lib pnp_{corner}
                    .include "C4M.Sky130_pnp_{corner}_params.spice"
                    .include "C4M.Sky130_pnp_model.spice"
                    .endl npn_{corner}
                """[1:]))

            for corner in bip_spice_corners:
                f.write(dedent(f"""
                    .lib npn_{corner}
                    .include "C4M.Sky130_npn_{corner}_params.spice"
                    .include "C4M.Sky130_npn_model.spice"
                    .endl npn_{corner}
                """[1:]))

        with spice_lib_file.open("w") as f:
            print("* C4M.Sky130 global lib file\n", file=f)

            for corner in spice_corners:
                f.write(dedent(f"""
                    .lib {corner}
                    .include "C4M.Sky130_logic_{corner}_model.spice"
                    .include "C4M.Sky130_io_{corner}_model.spice"
                    .include "C4M.Sky130_diode_{corner}_params.spice"
                    .include "C4M.Sky130_diode_model.spice"
                    .endl {corner}
                """[1:]))

    corner_funcs = {
        **{f"logic_{corner}": convert_spice for corner in spice_corners},
        **{f"io_{corner}": convert_spice for corner in spice_corners},
        "diode": remove_semicolon,
        **{f"diode_{corner}": extract_params for corner in spice_corners},
        "pnp":zero_mc_switch,
        **{f"pnp_{corner}": extract_params for corner in bip_spice_corners},
        "npn": zero_mc_switch,
        **{f"npn_{corner}": extract_params for corner in bip_spice_corners},
    }

    for (corner, files) in spice_model_files.items():
        yield {
            "title": spice_model_title,
            "name": corner,
            "doc": f"Converting spice model file for corner {corner}",
            "file_dep": files["deps"],
            "targets": files["targets"],
            "actions": (
                (create_folder, (open_pdk_spice_dir,)),
                (corner_funcs[corner], (corner,)),
            )
        }
    yield {
        "title": lambda _: "Writing top lib files",
        "name": "lib",
        "doc": f"Writing lib files",
        "targets": (
            spice_logic_lib_file,
            spice_io_lib_file,
            spice_diode_lib_file,
            spice_pnp_lib_file,
            spice_npn_lib_file,
            spice_all_lib_file,
            spice_lib_file,
        ),
        "actions": (
            (create_folder, (open_pdk_spice_dir,)),
            write_libs,
        ),
    }


#
# spice_models_python (copy inside pytho module)
python_models_dir = sky130_local_dir.joinpath("models")
def _repl_models_dir():
    def _repl_dir(p: Path) -> Path:
        b = basename(str(p))
        return python_models_dir.joinpath(b)
    for spec in spice_model_files.values():
        for p in spec["targets"]:
            yield (p, _repl_dir(p))
    yield(spice_logic_lib_file, _repl_dir(spice_logic_lib_file))
    yield(spice_io_lib_file, _repl_dir(spice_io_lib_file))
    yield(spice_diode_lib_file, _repl_dir(spice_diode_lib_file))
    yield(spice_pnp_lib_file, _repl_dir(spice_pnp_lib_file))
    yield(spice_npn_lib_file, _repl_dir(spice_npn_lib_file))
    yield(spice_all_lib_file, _repl_dir(spice_all_lib_file))
    yield(spice_lib_file, _repl_dir(spice_lib_file))
python_models_srctgts = tuple(_repl_models_dir())
python_models_deps = tuple(scr for (scr, _) in python_models_srctgts)
python_models_tgts = tuple(tgt for (_, tgt) in python_models_srctgts)
def task_spice_models_python():
    """Copy SPICE models inside pdk module
    
    This way they can be used by pyspicefactory without needing separate
    PDK install"""
    return {
        "file_dep": python_models_deps,
        "targets": (
            *python_models_tgts,
        ),
        "actions": (
            (create_folder, (python_models_dir,)),
            *(f"cp {str(src)} {str(tgt)}" for src, tgt in python_models_srctgts),
        )
    }


#
# manifest
manifest_file = top_dir.joinpath("MANIFEST.in")
def task_manifest():
    """Create MANIFEST.in"""
    def write_manifest():
        with manifest_file.open("w") as f:
            for tgt in python_models_tgts:
                print(f"include c4m/pdk/sky130/models/{basename(str(tgt))}", file=f)

    return {
        "file_dep": python_models_tgts,
        "targets": (
            manifest_file,
        ),
        "actions": (
            write_manifest,
        ),
    }


#
# dist
def task_dist():
    """Create distributable python module"""

    return {
        "title": lambda _: "Creating wheel",
        "file_dep": (top_dir.joinpath("setup.py"), *c4m_py_files),
        "targets": (dist_dir,),
        "actions": (f"{pdkmaster_python} -m build",)
    }


#
# install
def task_install():
    """Install the python module"""

    return {
        "title": lambda _: "Installing python module",
        "file_dep": (
            *c4m_py_files,
            *python_models_tgts,
            manifest_file,
        ),
        "targets": (sky130_inst_dir,),
        "actions": (
            f"{pdkmaster_pip} install {top_dir}",
        ),
    }


#
# open_pdk
def task_open_pdk():
    """Create open_pdk dir"""
    # This is separate task so we can clean up full open_pdk directory

    return {
        "title": lambda _: "Creating open_pdk directory",
        "targets": (open_pdk_dir,),
        "actions": (
            (create_folder, (open_pdk_dir,)),
        ),
        "clean": (f"rm -fr {str(open_pdk_dir)}",),
    }


#
# coriolis
def task_coriolis():
    """Generate coriolis support files"""

    coriolis_dir = open_pdk_tech_dir.joinpath("coriolis")
    corio_dir = coriolis_dir.joinpath("techno", "etc", "coriolis2")
    corio_node130_dir = corio_dir.joinpath("node130")
    corio_sky130_dir = corio_node130_dir.joinpath("sky130")

    corio_nda_init_file = corio_dir.joinpath("__init__.py")
    corio_node130_init_file = corio_node130_dir.joinpath("__init__.py")
    corio_sky130_init_file = corio_sky130_dir.joinpath("__init__.py")
    corio_sky130_techno_file = corio_sky130_dir.joinpath("techno.py")
    corio_sky130_lib_files = tuple(
        corio_sky130_dir.joinpath(f"{lib}.py") for lib in cell_list.keys()
    ) + (corio_sky130_dir.joinpath("StdCellLib_fix.py"),)

    def gen_init():
        from doitlib import libs

        with corio_sky130_init_file.open("w") as f:
            print("from .techno import *", file=f)
            for lib in libs.__libs__:
                print(f"from .{lib.name} import setup as {lib.name}_setup", file=f)

            print(
                "\n__lib_setups__ = [{}]".format(
                    ",".join(f"{lib.name}.setup" for lib in libs.__libs__)
                ),
                file=f,
            )

    def gen_coriolis():
        from pdkmaster.io import coriolis
        from c4m.pdk import sky130
        from doitlib import libs

        expo = coriolis.FileExporter(tech=sky130.tech, gds_layers=sky130.gds_layers)

        with corio_sky130_techno_file.open("w") as f:
            f.write(dedent("""
                # Autogenerated file
                # SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
            """))
            f.write(expo())

        for lib in libs.__libs__:
            with corio_sky130_dir.joinpath(f"{lib.name}.py").open("w") as f:
                f.write(expo(lib))

    def gen_flexlib_fix():
        with corio_sky130_dir.joinpath("StdCellLib_fix.py").open("w") as f:
            f.write(dedent("""
                from Hurricane import Net

                def fix(lib):
                    for cell in lib.getCells():
                        for net in cell.getNets():
                            if net.getName() == 'vdd':
                                net.setType( Net.Type.POWER )
                                net.setDirection( Net.Direction.IN )
                            elif net.getName() == 'vss':
                                net.setType( Net.Type.GROUND )
                                net.setDirection( Net.Direction.IN )
                            elif net.getName() == 'ck':
                                net.setType( Net.Type.CLOCK )
                                net.setDirection( Net.Direction.IN )
                            elif net.getName() in ('nq', "q", 'zero', 'one'):
                                net.setDirection( Net.Direction.OUT )
                            else:
                                net.setDirection( Net.Direction.IN )
            """[1:]))

    return {
        "title": lambda _: "Creating coriolis files",
        "file_dep": c4m_py_files,
        "uptodate": (
            check_timestamp_unchanged(str(pdkmaster_inst_dir)),
            check_timestamp_unchanged(str(flexcell_inst_dir)),
            check_timestamp_unchanged(str(flexio_inst_dir)),
            check_timestamp_unchanged(str(flexmem_inst_dir)),
        ),
        "targets": (
            corio_nda_init_file, corio_node130_init_file, corio_sky130_init_file,
            corio_sky130_techno_file, *corio_sky130_lib_files,
        ),
        "actions": (
            (create_folder, (corio_sky130_dir,)),
            corio_nda_init_file.touch, corio_node130_init_file.touch,
            gen_init, gen_coriolis, gen_flexlib_fix,
        ),
    }


#
# klayout
klayout_dir = open_pdk_tech_dir.joinpath("klayout")
klayout_tech_dir = klayout_dir.joinpath("tech", "C4M.Sky130")
klayout_bin_dir = klayout_dir.joinpath("bin")
def task_copy_convscript():
    """Copy the difftap conversion script"""
    name = "conv_c4msky130_to_sky130.py"
    script_src = scripts_dir.joinpath(name)
    script_tgt = klayout_bin_dir.joinpath(name)

    return {
        "title": lambda _: "Copy difftap conversion script",
        "file_dep": (
            script_src,
        ),
        "targets": (
            script_tgt,
        ),
        "actions": (
            (create_folder, (klayout_bin_dir,)),
            f"cp {str(script_src)} {str(script_tgt)}"
        ),
    }


klayout_lvs_script = klayout_bin_dir.joinpath("lvs_Sky130")
klayout_drc_script = klayout_bin_dir.joinpath("drc_Sky130")
def task_klayout():
    """Generate klayout files"""

    klayout_drc_dir = klayout_tech_dir.joinpath("drc")
    klayout_lvs_dir = klayout_tech_dir.joinpath("lvs")
    klayout_share_dir = klayout_dir.joinpath("share")

    klayout_lyt_file = klayout_tech_dir.joinpath("C4M.Sky130.lyt")
    klayout_drc_lydrc_file = klayout_drc_dir.joinpath("DRC.lydrc")
    klayout_extract_lylvs_file = klayout_lvs_dir.joinpath("Extract.lylvs")
    klayout_drc_file = klayout_share_dir.joinpath("Sky130.drc")
    klayout_extract_file = klayout_share_dir.joinpath("Sky130_extract.lvs")
    klayout_extract_script = klayout_bin_dir.joinpath("extract_Sky130")
    klayout_lvs_file = klayout_share_dir.joinpath("Sky130.lvs")

    def gen_klayout():
        from pdkmaster.io.klayout import FileExporter
        from c4m.pdk import sky130
        from xml.etree.ElementTree import ElementTree

        expo = FileExporter(
            tech=sky130.tech, gds_layers=sky130.gds_layers,
            export_name=f"C4M.{sky130.tech.name}",
        )()

        # DRC
        with klayout_drc_file.open("w") as f:
            f.write(expo["drc"])
        with klayout_drc_script.open("w") as f:
            relfile = relpath(klayout_drc_file, klayout_bin_dir)
            f.write(dedent(f"""
                #!/bin/sh
                d=`dirname $0`
                deck=`realpath $d/{relfile}`

                if [ $# -ne 2 ]
                then
                    echo "Usage `basename $0` input report"
                    exit 20
                fi

                export SOURCE_FILE=$1 REPORT_FILE=$2
                klayout -b -r ${{deck}}
            """[1:]))
        klayout_drc_script.chmod(0o755)

        # Extract
        with klayout_extract_file.open("w") as f:
            f.write(expo["extract"])
        with klayout_extract_script.open("w") as f:
            relfile = relpath(klayout_extract_file, klayout_bin_dir)
            f.write(dedent(f"""
                #!/bin/sh
                d=`dirname $0`
                deck=`realpath $d/{relfile}`

                if [ $# -ne 2 ]
                then
                    echo "Usage `basename $0` input spice_out"
                    exit 20
                fi

                export SOURCE_FILE=$1 SPICE_FILE=$2
                klayout -b -r ${{deck}}
            """[1:]))
        klayout_extract_script.chmod(0o755)

        # LVS
        with klayout_lvs_file.open("w") as f:
            f.write(expo["lvs"])
        with klayout_lvs_script.open("w") as f:
            relfile = relpath(klayout_lvs_file, klayout_bin_dir)
            f.write(dedent(f"""
                #!/bin/sh
                d=`dirname $0`
                deck=`realpath $d/{relfile}`

                if [ $# -ne 3 ]
                then
                    echo "Usage `basename $0` gds spice report"
                    exit 20
                fi

                export SOURCE_FILE=`realpath $1` SPICE_FILE=`realpath $2` REPORT_FILE=$3
                klayout -b -r ${{deck}}
            """[1:]))
        klayout_lvs_script.chmod(0o755)

        # klayout technology
        et = ElementTree(expo["ly_drc"])
        et.write(klayout_drc_lydrc_file, encoding="utf-8", xml_declaration=True)
        et = ElementTree(expo["ly_extract"])
        et.write(klayout_extract_lylvs_file, encoding="utf-8", xml_declaration=True)
        et = ElementTree(expo["ly_tech"])
        et.write(klayout_lyt_file, encoding="utf-8", xml_declaration=True)

    return {
        "title": lambda _: "Creating klayout files",
        "file_dep": c4m_py_files,
        "uptodate": (
            check_timestamp_unchanged(str(pdkmaster_inst_dir)),
        ),
        "task_dep": (
            "copy_convscript",
        ),
        "targets": (
            klayout_lyt_file, klayout_drc_lydrc_file, klayout_extract_lylvs_file,
            klayout_drc_file, klayout_drc_script, klayout_extract_file,
            klayout_extract_script, klayout_lvs_file, klayout_lvs_script,
        ),
        "actions": (
            (create_folder, (klayout_share_dir,)),
            (create_folder, (klayout_bin_dir,)),
            (create_folder, (klayout_drc_dir,)),
            (create_folder, (klayout_lvs_dir,)),
            gen_klayout,
        ),
    }


#
# spice
def task_spice():
    """Generate SPICE files"""

    spice_dirs = tuple(
        open_pdk_ref_dir.joinpath(lib, "spice") for lib in cell_list.keys()
    )
    spice_files = {}
    for lib, cells in cell_list.items():
        lib_spice_files = []
        lib_spice_files.append(open_pdk_ref_dir.joinpath(lib, "spice", f"{lib}.spi"))
        for cell in cells:
            lib_spice_files.append(open_pdk_ref_dir.joinpath(lib, "spice", f"{cell}.spi"))
            lib_spice_files.append(open_pdk_ref_dir.joinpath(lib, "spice", f"{cell}_hier.spi"))
        spice_files[lib] = lib_spice_files

    def gen_spice(libname):
        from pdkmaster.design import circuit as _ckt
        from c4m.pdk import sky130
        from doitlib import libs

        lib = None
        for lib2 in libs.__libs__:
            if lib2.name == libname:
                lib = lib2
                break
        assert lib is not None

        lib_spice_dir = open_pdk_ref_dir.joinpath(lib.name, "spice")
        with lib_spice_dir.joinpath(f"{lib.name}.spi").open("w") as f_lib:
            f_lib.write(f"* {lib.name}\n")
            for cell in lib.cells:
                # Write cell only to spice file
                pyspicesubckt = sky130.pyspicefab.new_pyspicesubcircuit(
                    circuit=cell.circuit
                )
                s = f"* {cell.name}\n" + str(pyspicesubckt)
                f_lib.write("\n" + s)
                with lib_spice_dir.joinpath(f"{cell.name}.spi").open("w") as f_cell:
                    f_cell.write(s)

                # Write cell hierarchy to file; make order so that each cell is in
                # the file before is is being used.
                with lib_spice_dir.joinpath(f"{cell.name}_hier.spi").open("w") as f_cell:
                    todo = [cell]
                    seen = {cell}

                    s_cell = ""
                    while todo:
                        subblock = todo.pop(0)

                        pyspicesubckt = sky130.pyspicefab.new_pyspicesubcircuit(
                            circuit=subblock.circuit, lvs=True,
                        )
                        s = f"* {subblock.name}\n"
                        s_ckt = str(pyspicesubckt)
                        s_ckt = s_ckt.replace("Ohm", "")
                        # s_ckt = s_ckt.replace("(", "[").replace(")", "]")
                        s += s_ckt
                        s_cell = s + s_cell

                        for inst in subblock.circuit.instances.__iter_type__(_ckt._CellInstance):
                            if inst.cell not in seen:
                                todo.append(inst.cell)
                                seen.add(inst.cell)

                    f_cell.write(f"* {cell.name}\n{s_cell}")


    for lib in cell_list.keys():
        yield {
            "name": lib,
            "doc": f"Creating spice files for library {lib}",
            "file_dep": c4m_py_files,
            "uptodate": tuple(
                check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[lib]
            ),
            "targets": spice_files[lib],
            "actions": (
                *(
                    (create_folder, (dir_,)) for dir_ in spice_dirs
                ),
                (gen_spice, (lib,)),
            ),
        }


#
# gds
def task_gds():
    """Generate GDSII files"""

    gds_dirs = tuple(
        open_pdk_ref_dir.joinpath(lib, "gds") for lib in cell_list.keys()
    )
    gds_files: Dict[str, Tuple[Path, ...]] = {}
    for lib, cells in cell_list.items():
        gds_files[lib] = tuple(
            open_pdk_ref_dir.joinpath(lib, "gds", f"{cell}.gds")
            for cell in cells
        )

    def gen_gds(libname):
        from pdkmaster.io.klayout import export2db
        from c4m.pdk import sky130
        from doitlib import libs

        lib = None
        for lib2 in libs.__libs__:
            if lib2.name == libname:
                lib = lib2
                break
        assert lib is not None

        out_dir = open_pdk_ref_dir.joinpath(libname, "gds")
        layout = export2db(
            lib, gds_layers=sky130.gds_layers, cell_name=None, merge=False,
            add_pin_label=True,
        )
        layout.write(str(out_dir.joinpath(f"{libname}.gds")))
        for cell in layout.each_cell():
            assert cell.name != libname
            cell.write(str(out_dir.joinpath(f"{cell.name}.gds")))

    for libname in cell_list.keys():
        yield {
            "name": libname,
            "doc": f"Creating gds files for {libname}",
            "file_dep": c4m_py_files,
            "uptodate": tuple(
                check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[libname]
            ),
            "targets": gds_files[libname],
            "actions": (
                *(
                    (create_folder, (dir_,)) for dir_ in gds_dirs
                ),
                (gen_gds, (libname,)),
            ),
        }


#
# VHDL/Verilog
def task_rtl():
    """Generate VHDL/verilog files"""
    langs = ("vhdl", "verilog")

    def rtl_targets(lib, lang):
        suffix = {
            "vhdl": "vhdl",
            "verilog": "v",
        }[lang]

        tgts = []
        cells = cell_list[lib]
        for cell in cells:
            if (lib == "IOLib") and not cell.startswith("IOPad"):
                continue
            tgts.append(open_pdk_ref_dir.joinpath(lib, lang, f"{cell}.{suffix}"))
        return tuple(tgts)

    def rtl_dirs(lang):
        return (tmp_dir, *(
            open_pdk_ref_dir.joinpath(lib, lang)
            for lib in cell_list.keys()
        ))

    def rtl_title(task):
        return (
            f"Creating {task.name[4:]} files" if avt_shell is not None
            else f"missing avt_shell; no {task.name[4:]} files created"
        )

    def rtl_script(lib, lang):
        avt_shell_script = dedent(f"""
            avt_config simToolModel hspice
            avt_LoadFile "{python_models_dir.joinpath("C4M.Sky130_logic_tt_model.spice")}" spice
            avt_LoadFile "{python_models_dir.joinpath("C4M.Sky130_io_tt_model.spice")}" spice
            avt_LoadFile "{python_models_dir.joinpath("C4M.Sky130_diode_tt_params.spice")}" spice
            avt_LoadFile "{python_models_dir.joinpath("C4M.Sky130_diode_model.spice")}" spice
            avt_config avtVddName "vdd:iovdd"
            avt_config avtVssName "vss:iovss"
            avt_config yagNoSupply "yes"
        """[1:])

        if lang == "verilog":
            avt_shell_script += dedent("""
                avt_config avtOutputBehaviorFormat "vlg"
                set map {spice verilog _hier.spi .v}
                set suffix v
                set comment "//"
            """[1:])
        elif lang == "vhdl":
            avt_shell_script += dedent("""
                avt_config avtOutputBehaviorFormat "vhd"
                set map {spice vhdl _hier.spi .vhdl}
                set suffix vhd
                set comment "--"
            """[1:])
        else:
            raise NotImplementedError(f"rtl lang {lang}")

        avt_shell_script += "foreach spice_file {\n"
        cells = cell_list[lib]
        for cell in cells:
            if (lib == "IOLib") and not cell.startswith("IOPad"):
                continue
            avt_shell_script += (
                f'    "{str(open_pdk_ref_dir.joinpath(lib, "spice", f"{cell}_hier.spi"))}"'
            ) + "\n"
        avt_shell_script += dedent("""
            } {
                avt_LoadFile $spice_file spice
                set rtl_file [string map $map $spice_file]
                set cell [string map {_hier.spi ""} [file tail $spice_file]]
                if {[string match "sff1*" $cell]} {
                    inf_SetFigureName $cell
                    inf_MarkSignal sff_m "FLIPFLOP+MASTER"
                    inf_MarkSignal sff_s SLAVE
                }
                set out_file "$cell.$suffix"
                yagle $cell
                if [file exists $out_file] {
                    file copy -force $out_file $rtl_file
                } else {
                    set f [open $rtl_file w]
                    puts $f "$comment no model for $cell"
                }
            }
        """[1:])

        return avt_shell_script

    def rtl_override(lib, lang):
        """Override some of the verilog file with some hard coded ones.

        Needed as Yagle does not seem to understand the zero/one cell.
        """
        override_lang_dir = override_dir.joinpath(lib, lang)
        if override_lang_dir.exists():
            rtl_lang_dir = open_pdk_ref_dir.joinpath(lib, lang)
            os.system(f"cp {str(override_lang_dir)}/* {str(rtl_lang_dir)}")

    rtl_libs = tuple(filter(lambda l: l not in ("ExampleSRAMs", "MacroLib"), cell_list.keys()))
    for lib in rtl_libs:
        docstrings = {
            "vhdl": f"Generate VHDL files for lib {lib}",
            "verilog": f"Generate Verilog files for lib {lib}",
        }
        for lang in langs:
            yield {
                "name": f"{lib}:{lang}",
                "doc": docstrings[lang],
                "title": rtl_title,
                "file_dep": c4m_py_files,
                "uptodate": tuple(
                    check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[lib]
                ),
                "task_dep": (f"spice:{lib}", "spice_models"),
                "targets": rtl_targets(lib, lang),
                "actions": (
                    *(
                        (create_folder, (dir_,)) for dir_ in rtl_dirs(lang)
                    ),
                    AVTScriptAction(rtl_script(lib, lang)),
                    (rtl_override, (lib, lang))
                )
            }
        yield {
            "name": lib,
            "doc": f"Generate RTL files for lib {lib}",
            "task_dep": tuple(f"rtl:{lib}:{lang}" for lang in langs),
            "actions": None,
        }
    docstrings = {
        "vhdl": f"Generate VHDL files for all libs",
        "verilog": f"Generate Verilog files for all libs",
    }
    for lang in langs:
        yield {
            "name": lang,
            "doc": docstrings[lang],
            "task_dep": tuple(f"rtl:{lib}:{lang}" for lib in rtl_libs),
            "actions": None,
        }


#
# liberty
def task_liberty():
    """Generate liberty files"""

    liberty_libs = ("StdCellLib",)
    liberty_spice_corners = {
        "nom": "tt", "fast": "ff", "slow": "ss",
    }

    def liberty_target(lib, corner):
        return open_pdk_ref_dir.joinpath(lib, "liberty", f"{lib}_{corner}.lib")

    def liberty_dir(lib):
        return open_pdk_ref_dir.joinpath(lib, "liberty")

    def liberty_title(task):
        lib, corner = task.name[8:].split("_")
        return (
            f"Creating liberty files for library {lib}, corner {corner}" if avt_shell is not None
            else "missing avt_shell; no liberty files created for library {lib}, corner {corner}"
        )

    def liberty_script(lib, corner):
        assert lib in ("StdCellLib",), "Unsupported lib"

        avt_script = dedent("""
            avt_config simToolModel hspice
            avt_config avtVddName "vdd:iovdd"
            avt_config avtVssName "vss:iovss"
            avt_config tasBefig yes
            avt_config tmaDriveCapaout yes
            avt_config avtPowerCalculation yes
            avt_config simSlope 20e-12
        """[1:])

        if corner == "nom":
            avt_script += dedent(f"""
                avt_config simPowerSupply 1.8
                avt_config simTemperature 25
            """[1:])
        elif corner == "fast":
            avt_script += dedent(f"""
                avt_config simPowerSupply 1.98
                avt_config simTemperature -20
            """[1:])
        elif corner == "slow":
            avt_script += dedent(f"""
                avt_config simPowerSupply 1.62
                avt_config simTemperature 85
            """[1:])
        else:
            raise NotImplementedError(f"corner {corner}")

        spice_file = open_pdk_ref_dir.joinpath(lib, "spice", f"{lib}.spi")
        spice_corner = liberty_spice_corners[corner]
        avt_script += dedent(f"""
            avt_LoadFile "{open_pdk_spice_dir}/C4M.Sky130_logic_{spice_corner}_model.spice" spice
            avt_LoadFile "{open_pdk_spice_dir}/C4M.Sky130_io_{spice_corner}_model.spice" spice
            avt_config tmaLibraryName {lib}_{corner}
            avt_LoadFile {spice_file} spice
            
            foreach cell {{
        """[1:])
        avt_script += "".join(f"    {cell}\n" for cell in cell_list[lib])
        verilog_dir = open_pdk_ref_dir.joinpath(lib, "verilog")
        liberty_file_raw = open_pdk_ref_dir.joinpath(
            lib, "liberty", f"{lib}_{corner}_raw.lib",
        )
        avt_script += dedent(f"""
            }} {{
                set verilogfile {verilog_dir}/$cell.v

                if {{[string match "sff1*" $cell]}} {{
                    # TODO: make these settings configurable
                    set beh_fig NULL
                    inf_SetFigureName $cell
                    inf_MarkSignal sff_m "MASTER"
                    inf_MarkSignal sff_s "FLIPFLOP+SLAVE"
                    create_clock -period 3000 ck
                }} elseif {{[string match "*latch*" $cell]}} {{
                    set beh_fig NULL
                }} else {{
                    set beh_fig [avt_LoadBehavior $verilogfile verilog]
                }}
                set tma_fig [tma_abstract [hitas $cell] $beh_fig]

                lappend tma_list $tma_fig
                lappend beh_list $beh_fig
            }}

            lib_drivefile $tma_list $beh_list "{liberty_file_raw}" max
        """[1:])

        return avt_script

    def fix_lib(lib, corner):
        import re

        cell_pattern = re.compile(r'\s*cell\s*\((?P<cell>\w+)\)\s*\{')
        # area_pattern = re.compile(r'(?P<area>\s*area\s*:\s*)\d+.\d+\s*;')
        qpin_pattern = re.compile(r'\s*pin\s*\(q\)\s*\{')
        ckpin_pattern = re.compile(r'\s*pin\s*\(ck\)\s*\{')

        liberty_file_raw = open_pdk_ref_dir.joinpath(
            lib, "liberty", f"{lib}_{corner}_raw.lib",
        )
        tgt = liberty_target(lib, corner)
        with liberty_file_raw.open("r") as fin:
            with tgt.open("w") as fout:
                is_flipflop = False
                for line in fin:

                    # In current one/zero cells output pins are wrongly seen as inout
                    # TODO: Check if we can fix that during HiTAS/Yagle run
                    line = line.replace("direction : inout", "direction : output")

                    m = cell_pattern.match(line)
                    if m:
                        cell = m.group("cell")
                        is_flipflop = cell.startswith("sff")
                        has_reset = cell.startswith("sff1r")
                        if is_flipflop:
                            fout.write(line)
                            fout.write('        ff (IQ,IQN) {\n')
                            fout.write('            next_state : "i" ;\n')
                            fout.write('            clocked_on : "ck" ;\n')
                            if has_reset:
                                fout.write('            clear : "nrst\'" ;\n')
                            fout.write('        }\n')
                            continue
                    elif is_flipflop:
                        m = qpin_pattern.match(line)
                        if m:
                            fout.write(line)
                            fout.write('            function : "IQ" ;\n')
                            continue

                        m = ckpin_pattern.match(line)
                        if m:
                            fout.write(line)
                            fout.write('            clock : true ;\n')
                            continue

                    fout.write(line)

    for lib in liberty_libs:
        for corner in ("nom", "fast", "slow"):
            spice_corner = liberty_spice_corners[corner]
            tmp = tmp_dir.joinpath(f"{lib}_{corner}")
            yield {
                "name": f"{lib}_{corner}",
                "doc": f"Generate liberty file for {lib}; {corner} corner",
                "title": liberty_title,
                "file_dep": c4m_py_files,
                "uptodate": tuple(
                    check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[lib]
                ),
                "task_dep": (
                    f"spice:{lib}", f"rtl:{lib}:verilog",
                    f"spice_models:logic_{spice_corner}",
                    f"spice_models:io_{spice_corner}",
                    f"spice_models:diode_{spice_corner}",
                ),
                "targets": (liberty_target(lib, corner),),
                "actions": (
                    (create_folder, (liberty_dir(lib),)),
                    (create_folder, (tmp,)),
                    AVTScriptAction(liberty_script(lib, corner), tmp=tmp),
                    (fix_lib, (lib, corner)),
                ),
            }


#
# release
def task_tarball():
    """Create a tarball"""
    from datetime import datetime

    tarballs_dir = top_dir.joinpath("tarballs")
    t = datetime.now()
    tarball = tarballs_dir.joinpath(f'{t.strftime("%Y%m%d_%H%M")}_c4m_pdk_sky130.tgz')

    return {
        "title": lambda _: "Create release tarball",
        "task_dep": (
            "coriolis", "klayout", "spice_models", "spice", "gds", "rtl", "liberty",
        ),
        "targets": (tarball,),
        "actions": (
            (create_folder, (tarballs_dir,)),
            f"cd {str(top_dir)}; tar czf {str(tarball)} open_pdk",
        )
    }


#
# drc
def task_drc():
    "Run drc checks"
    drc_dir = top_dir.joinpath("drc")

    def gen_rep_files(lib, cells) -> Generator[Path, None, None]:
        drc_lib_dir = drc_dir.joinpath(lib)
        if "Gallery" in cells:
            yield drc_lib_dir.joinpath(f"Gallery.rep")
        else:
            for cell in cells:
                yield drc_lib_dir.joinpath(f"{cell}.rep")
    drc_rep_files = {
        lib: tuple(gen_rep_files(lib, cells))
        for lib, cells in cell_list.items()
    }

    def run_drc(lib, cell):
        gds_dir = open_pdk_ref_dir.joinpath(lib, "gds")

        drcrep = drc_dir.joinpath(lib, f"{cell}.rep")
        gdsfile = gds_dir.joinpath(f"{cell}.gds")

        try:
            CmdAction(
                f"{str(klayout_drc_script)} {str(gdsfile)} {str(drcrep)}",
            ).execute()
            with drcrep.open("r") as f:
                # Each DRC error has an <item> section in the output XML
                ok = not any(("<item>" in line for line in f))
        except:
            ok = False
        if not ok:
            print(f"DRC of {lib}/{cell} failed!", file=sys.stderr)

    def lib_rep(lib, cells):
        with drc_dir.joinpath(f"{lib}.rep").open("w") as librep:
            for cell in cells:
                drcrep = drc_dir.joinpath(lib, f"{cell}.rep")
                with drcrep.open("r") as f:
                    # Each DRC error has an <item> section in the output XML
                    ok = not any(("<item>" in line for line in f))

                print(f"{cell}: {'OK' if ok else 'NOK'}", file=librep)

    for lib, cells in cell_list.items():
        for cell in cells:
            yield {
                "name": f"{lib}:{cell}",
                "doc": f"Running DRC check for lib {lib} cell {cell}",
                "file_dep": c4m_py_files,
                "task_dep": (f"gds:{lib}", "klayout"),
                "uptodate": tuple(
                    check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[lib]
                ),
                "targets": (drc_dir.joinpath(lib, f"{cell}.rep"),),
                "actions": (
                    (create_folder, (drc_dir.joinpath(lib),)),
                    (run_drc, (lib, cell)),
                )
            }

        # If there exist a Gallery cell then do only DRC on that cell by default
        if "Gallery" in cells:
            cells = ("Gallery",)

        yield {
            "name": f"{lib}",
            "doc": f"Assembling DRC results for lib",
            "file_dep": c4m_py_files,
            "task_dep": (
                *(f"drc:{lib}:{cell}" for cell in cells),
                "klayout",
            ),
            "uptodate": tuple(
                check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[lib]
            ),
            "targets": (drc_dir.joinpath(f"{lib}.rep"),),
            "actions": (
                (lib_rep, (lib, cells)),
            )
        }


#
# lvs
def task_lvs():
    "Run lvs checks"
    lvs_dir = top_dir.joinpath("lvs")

    def run_lvs(lib):
        cells = cell_list[lib]
        gds_dir = open_pdk_ref_dir.joinpath(lib, "gds")
        spice_dir = open_pdk_ref_dir.joinpath(lib, "spice")
        if "Gallery" in cells:
            # Only run LVS on Gallery cell if it exists
            cells = ("Gallery",)

        with lvs_dir.joinpath(f"{lib}.rep").open("w") as librep:
            for cell in cells:
                lvsrep = lvs_dir.joinpath(lib, f"{cell}.lvsdb")
                gdsfile = gds_dir.joinpath(f"{cell}.gds")
                spicefile = spice_dir.joinpath(f"{cell}_hier.spi")

                ok = CmdAction(
                    f"{str(klayout_lvs_script)} {str(gdsfile)} {str(spicefile)} {str(lvsrep)}",
                ).execute() is None

                print(f"{cell}: {'OK' if ok else 'NOK'}", file=librep)
                print(
                    f"LVS of {lib}/{cell}: {'OK' if ok else 'failed!'}",
                    file=sys.stderr,
                )

    for lib in cell_list.keys():
        yield {
            "name": lib,
            "doc": f"Running LVS check for lib {lib}",
            "file_dep": c4m_py_files,
            "task_dep": (f"gds:{lib}", f"spice:{lib}", "klayout"),
            "uptodate": tuple(
                check_timestamp_unchanged(str(dir)) for dir in lib_module_paths[lib]
            ),
            "targets": (lvs_dir.joinpath(f"{lib}.rep"),),
            "actions": (
                (create_folder, (lvs_dir.joinpath(lib),)),
                (run_lvs, (lib,)),
            )
        }


#
# sign-off
def task_signoff():
    return {
        "task_dep": ("drc", "lvs"),
        "actions": tuple(),
    }
