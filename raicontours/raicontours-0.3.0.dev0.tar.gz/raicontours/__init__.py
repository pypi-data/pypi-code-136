# Copyright (C) 2022 Radiotherapy AI Holdings Pty Ltd

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# pylint: disable = invalid-name

from __future__ import annotations

from enum import Enum
import pathlib

from typing_extensions import TypedDict

from ._version import __version__ as __version__, version_info as version_info

_HERE = pathlib.Path(__file__).parent.resolve()
_model_path = _HERE / "model.h5"


class TG263(str, Enum):
    """TG263 naming.

    Based on the spreadsheet downloadable from
    https://www.aapm.org/pubs/reports/rpt_263_supplemental/TG263_Nomenclature_Worksheet_20170815.xls
    """

    Eye_L = "Eye_L"
    Eye_R = "Eye_R"
    Glnd_Lacrimal_L = "Glnd_Lacrimal_L"
    Glnd_Lacrimal_R = "Glnd_Lacrimal_R"
    Lens_L = "Lens_L"
    Lens_R = "Lens_R"
    OpticChiasm = "OpticChiasm"
    OpticNrv_L = "OpticNrv_L"
    OpticNrv_R = "OpticNrv_R"


class Config(TypedDict):
    """The model configuration"""

    model_path: pathlib.Path
    structures: list[TG263]
    patch_dimensions: tuple[int, int, int]
    encoding_filter_counts: list[int]
    decoding_filter_counts: list[int]
    rescale_slope: float
    rescale_intercept: float
    reduce_block_sizes: list[tuple[int, int, int]]


cfg: Config = {
    "model_path": _model_path,
    "structures": [
        TG263.Eye_L,
        TG263.Eye_R,
        TG263.Glnd_Lacrimal_L,
        TG263.Glnd_Lacrimal_R,
        TG263.Lens_L,
        TG263.Lens_R,
        # TG263.OpticChiasm,
        TG263.OpticNrv_L,
        TG263.OpticNrv_R,
    ],
    "patch_dimensions": (64, 64, 64),
    "encoding_filter_counts": [32, 64, 128, 256],
    "decoding_filter_counts": [128, 64, 32, 16],
    "rescale_slope": 4000.0,
    "rescale_intercept": -1024.0,
    "reduce_block_sizes": [(2, 4, 4), (1, 2, 2), (1, 1, 1)],
}

# TODO: Add a "uids used for training" list and use it to verify a DICOM
# file can be used for metric calculation.
