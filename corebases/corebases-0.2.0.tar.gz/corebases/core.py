from . import interface as i
from .backends import asyncpg


def database(url: str, **options) -> i.Database:
    """Now Support Just asyncpg"""

    return asyncpg.AsyncPGDatabase(url, **options)
