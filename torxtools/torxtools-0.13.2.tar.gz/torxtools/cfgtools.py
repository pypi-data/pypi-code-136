"""
Functions for working with configuration file selection and reading.

The :func:`which` convenience function returns the first file that should be used as configuration file from a list.
"""

import os
import typing as t

from boltons.iterutils import first

__all__ = [
    "which",
]


def which(
    cfgfile: str = None,
    candidates: t.List[str] = None,
    default: str = "/dev/null",
    verify: t.Callable = os.path.exists,
) -> t.Optional[str]:
    """
    Convenience function to return the configuration file to read.

    Parameters
    ----------
    cfgfile: str, None
        a single path. If not None, then it will be returned without calling the verify function.

    candidates: t.List[str], None
        a list of paths. If cfgfile is None, then the verify function will be
        called for each of these paths and the first one for which verify
        returns True will be returned.

        If no file is matched, then :file:`/dev/null` will be returned.

    verify: t.Callable
        callable that will be called for every file in candidate. Defaults to os.path.exists.

    default: str, None
        value to be returned if cfgfile is None and no match from candidates was found

    Returns
    -------
    str:
        cfgfile, a value from candidates, or default

    Example
    -------

    .. code-block:: python

        import argparse, sys
        from torxtools import cfgtools, pathtools

        defaults = pathtools.expandpath(["~/.my-cfgfile"], ["/etc/cfgfile"])
        parser = argparse.ArgumentParser()
        parser.add_argument('--cfgfile')

        args = parser.parse_args(sys.argv[:1])
        print(cfgtools.which(args.cfgfile, defaults))

    """
    if not callable(verify):
        raise TypeError(f"expected verify to be a callable, not: {verify}")

    if cfgfile:
        return cfgfile
    return first(candidates or [], default=default, key=verify)
