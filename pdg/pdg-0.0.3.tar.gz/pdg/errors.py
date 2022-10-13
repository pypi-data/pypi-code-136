"""
PDG API exception classes.
"""

class PdgApiError(Exception):
    """PDG API base exception."""
    pass

class PdgNoDataError(Exception):
    """Exception raised if no data is found."""
    pass
