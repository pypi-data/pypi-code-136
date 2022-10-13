# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from typing import cast

from pdkmaster.technology import primitive as _prm
from pdkmaster.io.klayout import merge

from c4m.flexcell.library import CellCanvas, Library

from .pdkmaster import tech, cktfab, layoutfab

__all__ = ["stdcelllib"]

prims = tech.primitives
_canvas = CellCanvas(
    tech=tech, lambda_=0.05,
    nmos=cast(_prm.MOSFET, prims.nfet_01v8), pmos=cast(_prm.MOSFET, prims.pfet_01v8),
    nimplant=cast(_prm.Implant, prims.nsdm), pimplant=cast(_prm.Implant, prims.psdm),
)
stdcelllib = Library(
    name="StdCellLib", canvas=_canvas, cktfab=cktfab, layoutfab=layoutfab,
)
merge(stdcelllib)
