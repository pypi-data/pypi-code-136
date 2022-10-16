# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the PymaciesArg Project
#     https://github.com/juniors90/PymaciesArg.
#
# Copyright (c) 2022. Ferreira Juan David
# License: MIT
#   Full Text: https://github.com/juniors90/PymaciesArg/blob/main/LICENSE

# =============================================================================
# DOCS
# =============================================================================

"""
PymaciesArg.

An extension that registers all pharmacies in Argentina.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import logging

import pandas as pd

from .constants import (
    DEPARTMENTS_TABLE_NAME,
    LOCATIONS_TABLE_NAME,
    PHARMACIES_TABLE_NAME,
)


log = logging.getLogger()


class BaseLoader:
    """Base class for Load all tables in DB."""

    table_name = "Base"

    def load_table(self, df, engine):
        """Read a data frame from csv file path.

        Load ``Departamentos`` table in the database from sql query.

        Parameters
        ----------
        df: ``pandas.DataFrame``
            The dataframe must with the values.

        Return
        ------
        df.to_sql : function
            A sql query such that load all values in
            the database.
        """
        return df.to_sql(
            self.table_name, con=engine, index=False, if_exists="replace"
        )


class PharmaciesLoader(BaseLoader):
    """Load *Farmacias* table in the DB.

    Attributes
    ----------
    table_name : str, optional (default='farmacias')
        The name of table.
    """

    table_name = PHARMACIES_TABLE_NAME

    def __init__(self, engine) -> None:
        self.engine = engine

    def load_table(self, file_path):
        """Read a csv file from a file path and and load ``farmacias`` table.

        Load ``Farmacias`` table in the database from sql query.

        Parameters
        ----------
        file_path : str
            The path of csv file with all ``Farmacias``.

        Return
        ------
        super().load_table(df) : function
            A sql query such that load all ``Farmacias`` in
            the database.
        """
        df = pd.read_csv(file_path)
        return super().load_table(df, self.engine)


class LocationsLoader(BaseLoader):
    """Load *Localidades* table in the DB.

    Attributes
    ----------
    table_name : str, optional (default='localidades')
        The name of table.
    """

    table_name = LOCATIONS_TABLE_NAME

    def __init__(self, engine) -> None:
        self.engine = engine

    def load_table(self, file_path):
        """Read a csv file from a file path and and load ``localidades`` table.

        Load ``Localidades`` table in the database from sql query.

        Parameters
        ----------
        file_path : str
            The path of csv file with all ``Localidades``.

        Return
        ------
        super().load_table(df) : function
            A sql query such that load all ``Localidades`` in
            the database.
        """
        df = pd.read_csv(file_path)
        return super().load_table(df, self.engine)


class DepartmentsLoader(BaseLoader):
    """Load *Departamentos* table in the DB.

    Attributes
    ----------
    table_name : str, optional (default='departamentos')
        The name of table.
    """

    table_name = DEPARTMENTS_TABLE_NAME

    def __init__(self, engine) -> None:
        self.engine = engine

    def load_table(self, file_path):
        """Read a csv file from a file path and load ``departamentos`` table.

        Load ``Departamentos`` table in the database from sql query.

        Parameters
        ----------
        file_path : str
            The path of csv file with all ``Departamentos``.

        Return
        ------
        super().load_table(df) : function
            A sql query such that load all ``Departamentos`` in
            the database.
        """
        df = pd.read_csv(file_path)
        return super().load_table(df, self.engine)
