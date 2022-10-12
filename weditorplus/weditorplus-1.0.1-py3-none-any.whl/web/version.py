# coding: utf-8
#

try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution("weditorplus").version
    print("__version__",__version__)
except pkg_resources.DistributionNotFound:
    __version__ = "1.0.0"
