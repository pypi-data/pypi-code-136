"""One Half color scheme for Pygments."""

from .onehalf import OneHalfDark, OneHalfLight

# Attempt to expose the package version as __version__ (see PEP 396).
try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution(__package__).version
except Exception:  # pylint: disable=broad-except
    pass  # pragma: no cover


__all__ = ["OneHalfDark", "OneHalfLight"]
