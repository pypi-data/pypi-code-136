"""
Documentation du module mod.
"""

__all__ = ['version']  # limite la portée de "import *"

version = "top-level module"
print("Initialisation", version)  # PAS DE PRINT dans un vrai module!

####################################################
# Extra useful tools, not for teaching purposes... #
####################################################

import os, sys

def main_addition():
    """
    Entry-point function.
    """

    try:
        args = [ int(arg) for arg in sys.argv[1:] ]
    except ValueError:
        print("Only integers accepted as command-line arguments:", sys.argv[1:])

    print(" + ".join([ str(arg) for arg in args ]), "=", sum(args))


_python_version = float(f"{sys.version_info.major}.{sys.version_info.minor:02d}")
if _python_version >= 3.10:
    from importlib.resources import files  # Python 3.10+
else:
    from importlib_resources import files  # External

pyyc_path = files("pyyc.config")  #: Path to pyyc configuration file.

def read_config(cfgname="default.cfg"):
    """
    Get config from configuration file.

    If the input filename does not specifically include a path, it will be
    looked for in the default `pyyc_path` directory.

    :param str cfgname: configuration file name
    :return: configuration object
    :rtype: configparser.ConfigParser
    """

    from configparser import ConfigParser

    if os.path.dirname(cfgname):  # cfgname includes a path
        fname = cfgname
    else:                          # use pyyc_path as default
        fname = pyyc_path.joinpath(cfgname)
    print(f"Reading configuration from {fname!s}...")

    cfg = ConfigParser()
    if not cfg.read(fname):     # It silently failed
        raise IOError(f"Could not find or parse {fname!s}")

    return cfg

def print_pkg_tree(node, offset=0, max_depth=2):
    """
    Print the package architecture.
    """

    if offset > max_depth * 2:
        return

    if hasattr(node, '__name__'):
        print(' '*offset + node.__name__)
        for name in dir(node):
            if not name.startswith('_'):
                print_pkg_tree(getattr(node, name), offset=offset+2)
