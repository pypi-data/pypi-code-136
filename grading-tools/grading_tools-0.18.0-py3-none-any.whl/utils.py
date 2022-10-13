"""Utils."""

import os
import traceback
from functools import reduce
from pathlib import Path


def get_fixture_path(fixture):
    """Given the name of a fixture file, returns path to `../fixtures/fixture`."""
    stack = traceback.extract_stack()
    # Name of file where function was called
    filename = stack[-2].filename
    # Get path to dir two levels up
    my_dir = str(Path(filename).parents[1].resolve())
    # Create absolute path to fixture file
    fixture_path = os.path.join(my_dir, "fixtures", fixture)
    return fixture_path


# https://tinyurl.com/ybsguzpm
def nested_get(dictionary, keys, default=None):
    """Return value from nested dictionary.

    Parameters
    ----------
    dictionary: dict
        The dictionary you want to get the value from.
    keys: list
        List of sequencial keys to locate value.
    default: default=None
        Value to return if key not in dictionary.
    """
    result = reduce(
        lambda d, key: d.get(key, default) if isinstance(d, dict) else default,
        keys,
        dictionary,
    )
    return result


# https://tinyurl.com/y8vfb3oq
def nested_set(dictionary, keys, value):
    """Update value in nested dictionary.

    Parameters
    ----------
    dictionary: dict
        The dictionary you want to update.
    keys: list
        List of sequencial keys to locate value.
    value:
        The new value.
    """
    for key in keys[:-1]:
        dictionary = dictionary.setdefault(key, {})
    dictionary[keys[-1]] = value
