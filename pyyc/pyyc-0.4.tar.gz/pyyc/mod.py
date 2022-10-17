"""
Documentation for module `mod`.
"""

__all__ = ['version']  # limits the content of "import *"

version = "top-level module"
print("Initialization", version)  # NO PRINT in a true module!

####################################################

import os, sys


def addition(*args):
    """
    Addition function (undefined type).

    .. Note:: just a wrapper to :py:func:`sum`.

    :param args: parameters
    :return: python addition of args

    >>> addition(1, 2, 3)
    6
    >>> addition("titi", "toto")
    'tititoto'
    """

    return sum(args)


def addition_int(*args):
    """
    Addition function for integers (includes cast to integer).

    :param int args: arguments to be casted to integer
    :return: integer addition of args
    :rtype: int
    :raise ValueError: if arguments cannot be casted to integer.

    >>> addition_int(1, 2, 3)
    6
    >>> addition_int("titi", "toto")
    Traceback (most recent call last):
        ...
    ValueError: Arguments must cast to integer.
    """

    try:
        iargs = [ int(arg) for arg in args ]
    except ValueError:
        raise ValueError("Arguments must cast to integer.")

    return sum(iargs)


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

def format_pkg_tree(node, max_depth=2, printout=False, depth=0):
    """
    Format the package architecture.

    :param module node: name of the top-level module
    :param int max_depth: maximum depth of recursion
    :param bool printout: print out the resulting string
    :param int depth: used for recursion
    :return: structure as a list of strings (without newlines)
    :rtype: list

    >>> format_pkg_tree(pyyc, max_depth=1)
    ['pyyc',
     '  pyyc.config',
     '  pyyc.mod',
     '  pyyc.subpkgA',
     '  pyyc.subpkgB']
    """

    if depth > max_depth:
        return []

    s = []
    if hasattr(node, '__name__'):
        s.append('  ' * depth + node.__name__)
        for name in dir(node):
            if not name.startswith('_'):
                s.extend(format_pkg_tree(getattr(node, name),
                                         max_depth=max_depth,
                                         depth=depth + 1))

    if printout:
        print('\n'.join(s))

    return s
