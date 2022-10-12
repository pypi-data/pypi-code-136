"""Module to assist with loading package data files"""
from importlib.resources import path, read_text


def load_text_resource(name):
    """Load a named resource containing text."""
    return read_text(__package__, name)


def load_file_resource(name):
    """Retrieve the file path of a named resource."""
    return path(__package__, name)
