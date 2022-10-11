"""
Exceptions from treesync tool
"""


class ConfigurationError(Exception):
    """
    Exceptions caused by configuration file handling
    """


class SyncError(Exception):
    """
    Exceptions caused by rsync commands
    """
