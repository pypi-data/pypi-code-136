"""Module to assist in retrieving package metadata."""
from importlib.metadata import PackageNotFoundError, metadata


def get_metadata():
    """Try to get the package metadata."""
    try:
        meta = metadata(__package__)
    except PackageNotFoundError:
        meta = {
            "Name": __package__,
            "Summary": "description",
            "Author": "author",
            "Version": "version",
            "License": "license",
            "Home-page": "homepage",
        }
    return meta
