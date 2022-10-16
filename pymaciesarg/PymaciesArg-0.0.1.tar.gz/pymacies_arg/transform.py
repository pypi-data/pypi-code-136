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

import pandas as pd


class Transform:
    """Trasform your data into a single data frame."""

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Trasform your data into a single data frame.

        Inspect the ``df`` and renamed the columns with data related
        whit pharmmacies.

        Parameters
        ----------
        df : ``pandas.DataFrame``
            Dataframe containing all data over pharmacies
            parameters of each cell.

        Return
        ------
            df : pd.DataFrame
                An instance of ``pd.DataFrame`` containing all the
                information of pharmacies.
        """
        renamed_cols = {
            "establecimiento_id": "id",
            "establecimiento_nombre": "name",
            "domicilio": "adress",
            "localidad_id": "id_location",
            "localidad_nombre": "location",
            "provincia_id": "id_province",
            "provincia_nombre": "province",
            "departamento_id": "id_department",
            "departamento_nombre": "department",
            "cod_loc": "cod_localidad",
            "tipologia_id": "id_tipology",
            "tipologia_nombre": "tipology",
            "cp": "postal_code",
            "sitio_web": "webpage",
        }

        df = df.rename(columns=renamed_cols)

        cols = [
            "id",
            "name",
            "adress",
            "id_location",
            "location",
            "id_province",
            "province",
            "id_department",
            "department",
            "postal_code",
            "webpage",
        ]

        df = df[cols]

        return df
