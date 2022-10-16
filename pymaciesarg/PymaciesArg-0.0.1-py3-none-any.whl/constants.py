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


DEPARTMENTS_TABLE_NAME = "departments"
LOCATIONS_TABLE_NAME = "locations"
PHARMACIES_TABLE_NAME = "pharmacies"

TABLE_NAMES = [
    DEPARTMENTS_TABLE_NAME,
    LOCATIONS_TABLE_NAME,
    PHARMACIES_TABLE_NAME,
]

URL_FARMACIAS = "http://datos.salud.gob.ar/dataset/39117f8f-e2bc-4571-a572-15a6ce7ea9e1/resource/19338ea7-a492-4af3-b212-18f8f4af9184/download/establecimientos-farmacias-enero-2021.csv"  # noqa
PROVINCIA = "FORMOSA"

farmacias_ds = {
    "name": "pharmacies",
    "url": URL_FARMACIAS,
    "province": PROVINCIA,
}
