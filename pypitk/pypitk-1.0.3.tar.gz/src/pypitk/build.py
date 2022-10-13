import osiotk as os
from .pypipackage import PYPIPackage as _PYPIPackage


def __build_package_dir(__basedir: str, subdir_structure, overwrite: bool = False):
    def _ensure_file(__name: str, is_abspath: bool = False, overwrite: bool = False):
        path = os.abspath(__name, is_abspath)
        _exists = os.file_exists(path, is_abspath=True)
        if (not _exists) or (_exists and overwrite):
            os.writes(path, is_abspath=True, content="")
    path = os.abspath(__basedir)
    os.mkdir(path)
    if subdir_structure is not None:
        if isinstance(subdir_structure, list) or isinstance(subdir_structure, tuple):
            for subfile in subdir_structure:
                if isinstance(subfile, str):
                    subpath = os.join_paths(path, subfile)
                    _ensure_file(subpath, is_abspath=True, overwrite=overwrite)
                elif isinstance(subfile, dict):
                    for key, value in subfile.items():
                        p = os.join_paths(path, key)
                        __build_package_dir(p, subdir_structure=value)
        elif isinstance(subdir_structure, str):
            subpath = os.join_paths(path, subdir_structure)
            _ensure_file(subpath, is_abspath=True, overwrite=overwrite)

        elif isinstance(subdir_structure, dict):
            for key, value in subdir_structure.items():
                p = os.join_paths(path, key)
                __build_package_dir(p, subdir_structure=value)
        else:
            print("unable to make folder structure:", subdir_structure)

def __build_package_content(__package:_PYPIPackage):
    for key in ("pyproject_toml", "readme", "private"):
        path = getattr(__package.paths, key)
        content = getattr(__package.content, key)
        os.writes(path, content=content, is_abspath=True)

def __process_package_installation(__package:_PYPIPackage):

    config = __package.config
    if config.autoinstall:
        install_locally = __package.content.commands.install_locally
        if install_locally is not None:
            install_locally = install_locally.private_command
            os.system(install_locally)


def build_package():

    package = _PYPIPackage()

    if package is not None:

        __build_package_dir(package.package_dir, subdir_structure=package.subdir_structure)

        __build_package_content(package)

        __process_package_installation(package)


        
