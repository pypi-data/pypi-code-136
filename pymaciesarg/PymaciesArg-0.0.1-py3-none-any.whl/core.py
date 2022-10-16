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
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd


from .constants import farmacias_ds
from .extractor import UrlExtractor
from .transform import Transform

log = logging.getLogger()

data_extractors = {
    "pharmacies": UrlExtractor(farmacias_ds["name"], farmacias_ds["url"]),
}


def extract_raws(date_str: str, base_file_dir: Path) -> Dict[str, Path]:
    """
    Read files from `source <datos.gob.ar>`_ and extract the data.

    Create a dataframe with the data and rewrite headers format.
    Save all dataframes as `.csv` file.

    Parameters
    ----------
    date_str : str
        The date on run with format YYYY-mm-dd.
    base_file_dir : Path
            A base file directory.

    Return
    ------
    file_paths : dict[str]
        A dict of stored data file paths.
    """
    file_paths = dict()
    for name, extractor in data_extractors.items():
        file_path = extractor.extract(
            date_str=date_str, base_file_dir=base_file_dir
        )
        file_paths[name] = file_path

    return file_paths


def trasform_raws(
    date_str: str, file_paths: Path, province: str, base_file_dir: Path
) -> List[Path]:
    """
    Read files from `source <datos.gob.ar>`_ and extract the data.

    Create a dataframe with the data and rewrite headers format.
    Save all dataframes as `.csv` file.

    Parameters
    ----------
    date_str : str
        The date on run with format YYYY-mm-dd.
    file_paths : str
        The destination location.
    province : str
        The province name in UPPERCASE.
    base_file_dir : Path
        A base file directory.
    Return
    ------
    data_paths : list[str]
        The destination location of data trasform.
    """
    for name, extractor in data_extractors.items():
        df = pd.read_csv(file_paths[name])
        trasform = Transform()
        dft = trasform.transform(df)

    df = dft[dft["province"] == province]

    df_fixed = df[
        [
            "id",
            "name",
            "id_location",
            "id_department",
            "postal_code",
            "adress",
        ]
    ].set_index("id")

    df_localidades = (
        df.groupby(["id_location", "location"], as_index=False)
        .count()[["id_location", "location"]]
        .set_index("id_location")
    )

    df_departamentos = (
        df.groupby(["id_department", "department"], as_index=False)
        .count()[["id_department", "department"]]
        .set_index("id_department")
    )

    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    file_path_crib = (
        "data"
        + "/{full_category}"
        + "/{year}-{month:02d}"
        + "/{category}"
        + "/{full_category}-{day:02d}-{month:02d}-{year}.csv"
    )  # noqa: E501
    data_paths = []
    for name in [
        f"pharmacies_{province.lower().replace(' ', '_')}",
        f"locations_{province.lower().replace(' ', '_')}",
        f"departments_{province.lower().replace(' ', '_')}",
    ]:
        full_category = name.split("_")
        category = "_".join(full_category[1:])
        file_path = file_path_crib.format(
            full_category=full_category[0],
            category=category,
            year=date.year,
            month=date.month,
            day=date.day,
        )

        f_path = base_file_dir / file_path
        data_paths.append(f_path)
        f_path.parent.mkdir(parents=True, exist_ok=True)

    df_fixed.to_csv(data_paths[0])
    df_localidades.to_csv(data_paths[1])
    df_departamentos.to_csv(data_paths[2])
    return data_paths


class PymaciesArg:
    """Extension class for different of PymaciesArg versions.

    Initilize the extension in `pipeline.py`::

        import datetime
        import os
        import pathlib

        from pymacies_arg import (
            PymaciesArg,
            PharmaciesLoader,
            LocationsLoader,
            DepartmentsLoader,
        )

        from sqlalchemy import create_engine

        # this path is pointing to project/
        PATH = os.path.abspath(os.path.dirname(__file__))

        SQLALCHEMY_DATABASE_URI = "sqlite:///" + PATH + "db_data.db"

        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        now = datetime.datetime.now()
        date = f"{now.year}-{now.month}-{now.day}"

        pymacies = PymaciesArg(date, pathlib.Path(PATH))

        # Extract
        file_paths = pymacies.extract_raws()

        # Transform
        provinces = [
            "BUENOS AIRES",
            "SANTA FE",
            "CABA",
            "TUCUMÁN",
            "MISIONES",
            "CÓRDOBA",
            "ENTRE RÍOS",
            "CHACO",
            "SALTA",
            "CORRIENTES",
            "RÍO NEGRO",
            "LA PAMPA",
            "SANTIAGO DEL ESTERO",
            "SAN LUIS",
            "SAN JUAN",
            "NEUQUÉN",
            "CHUBUT",
            "JUJUY",
            "CATAMARCA",
            "FORMOSA",
            "LA RIOJA",
            "SANTA CRUZ",
            "TIERRA DEL FUEGO",
            "MENDOZA",
        ]
        paths = [
            pymacies.trasform_raws(file_paths, p) for p in provinces
        ]

        # Load
        for path in paths:
            PharmaciesLoader(engine).load_table(path[0])
            LocationsLoader(engine).load_table(path[1])
            DepartmentsLoader(engine).load_table(path[2])

    Attributes
    ----------
    date_str : str
        The date on run with format YYYY-mm-dd.
    base_file_dir : Path
            A base file directory.
    """

    def __init__(self, date_str: str, base_file_dir: Path) -> None:
        self.date_str = date_str
        self.base_file_dir = base_file_dir

    def extract_raws(self) -> Dict[str, Path]:
        """
        Read files from `source <datos.gob.ar>`_ and extract the data.

        Create a dataframe with the data and rewrite headers format.
        Save all dataframes as `.csv` file.

        Return
        ------
        file_paths : dict[str,  Path]
            A dict of stored data file paths.
        """
        file_paths = extract_raws(self.date_str, self.base_file_dir)
        return file_paths

    def trasform_raws(self, file_paths: Path, province: str) -> List[Path]:
        """
        Read files from `source <datos.gob.ar>`_ and extract the data.

        Create a dataframe with the data and rewrite headers format.
        Save all dataframes as `.csv` file.

        Parameters
        ----------
        file_paths : str
            The destination location.
        province : str
            The province name in UPPERCASE.

        Return
        ------
        data_paths : list[Path]
            The destination location of data trasform.
        """
        data_paths = trasform_raws(
            self.date_str, file_paths, province, self.base_file_dir
        )
        return data_paths
