import asyncio
from attrs import define
import logging
from pathlib import Path
from typing import List, Tuple, Dict
import yaml

# from .config import ATOPILE_DIR
from . import options

log = logging.getLogger(__name__)

def generate_table(table_type: str, libs: List[Dict[str, str]]) -> str:
    table = f'({table_type}\n'
    for lib in libs:
        name = lib['name'].replace('/', '{slash}')
        path = lib['path']
        table += f'  (lib (name "{name}")(type "KiCad")(uri "{path}")(options "")(descr ""))\n'
    table += ')\n'
    return table

def generate_mod_lib_table(libs: List[Path], where: Path):
    path = where / 'fp-lib-table'
    with path.open('w') as f:
        f.write(generate_table('fp_lib_table', libs))

def generate_sym_lib_table(libs: List[Path], where: Path):
    path = where / 'sym-lib-table'
    with path.open('w') as f:
        f.write(generate_table('sym_lib_table', libs))

def dump_kicad_lib_tables(config_data: dict):
    project_dir =  options.project_dir.value
    listed_kicad_projects = list(config_data.get('libs', {}).keys())
    unique_kicad_pro_dirs = []
    for lib in listed_kicad_projects:
        unique_kicad_pro_dirs += [Path(lib).parent]
    unique_kicad_pro_dirs = list(set(unique_kicad_pro_dirs))
    libs_by_dir = {dir: [] for dir in unique_kicad_pro_dirs}
    for kicad_project, libs in config_data.get('libs', {}).items():
        libs_by_dir[Path(kicad_project).parent].extend(libs)
    libs_by_dir = {dir: list(set(libs)) for dir, libs in libs_by_dir.items()}

    for dir, libs in libs_by_dir.items():
        # get a list of the libs by type
        def kicad_project_libs_with_suffix(suffix):
            return [{'name': str(lib), 'path': (project_dir / lib).absolute()} for lib in libs if Path(lib).suffix == suffix]

        # update the symbol and component linking files
        # we're just gonna assume all the listed dirs might have modules in them for now
        mods_libs = [{'name': str(lib), 'path': (project_dir / lib).absolute()} for lib in libs if (project_dir / lib).is_dir()]
        sym_libs = kicad_project_libs_with_suffix('.kicad_sym')
        generate_mod_lib_table(mods_libs, project_dir / dir)
        generate_sym_lib_table(sym_libs, project_dir / dir)

def index_kicad_libs(config_data: dict, indexing_path: Path, kicad_project: Path):
    all_libs = config_data.get('libs') or {}

    project_dir =  options.project_dir.value

    # get the current project's libs
    kicad_project_reference = str(kicad_project)
    prj_libs = all_libs.get(kicad_project_reference) or []

    # index the libs
    new_kicad_mod = list(set(mod.parent for mod in (project_dir / indexing_path).glob('**/*.kicad_mod')))
    new_kicad_sym = list((project_dir / indexing_path).glob('**/*.kicad_sym'))

    for lib in new_kicad_mod + new_kicad_sym:
        prj_libs.append(lib.relative_to(project_dir))

    # remove duplicates
    prj_libs = list(set(map(str, prj_libs)))

    # add the lib to the project
    all_libs[kicad_project_reference] = prj_libs
