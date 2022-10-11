"""
arthub_api.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of exceptions.
"""


class Error(Exception):
    """There was an ambiguous exception that occurred while call each interface.
    """


class ErrorNotLogin(Error):
    """arthub_api.OpenAPI instance not logged in
    """
