# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from typing import Iterable, Optional

from ..typing import MultiT, cast_MultiT
from . import net as net_, mask as msk


__all__ = ["wafer", "outside", "SubstrateNet"]


class _Wafer(msk._Mask):
    """Wafer is a `Mask` that represents a full wafer. Only one object
    is allowed to be created from this class and this is done through
    the wafer variable. This variable is exported from the
    `pdkmaster.technology.wafer_` module and that variable is to be used
    in user code to represenet a wafer.
    """
    generated = False

    # Class representing the whole wafer
    def __init__(self):
        if _Wafer.generated:
            raise ValueError("Creating new '_Wafer' object is not allowed. One needs to use wafer.wafer")
        else:
            _Wafer.generated = True
        super().__init__(name="wafer")

        self.grid = msk._MaskProperty(mask=self, name="grid")

    @property
    def designmasks(self) -> Iterable[msk.DesignMask]:
        return tuple()

    def __eq__(self, other: object) -> bool:
        # We only allow one _Wafer object so they are equal if other is also
        # a _Wafer object
        return self.__class__ is other.__class__

    def __hash__(self) -> int:
        return super().__hash__()
wafer = _Wafer()


def outside(masks: MultiT[msk.DesignMask], *, alias: Optional[str]=None) -> msk._Mask:
    """Return a mask representing the area on the wafer outside other mask(s).
    Optionally an alias can be given for the generated mask.
    """
    masks = cast_MultiT(masks)
    if len(masks) == 1:
        mask = wafer.remove(masks[0])
    else:
        mask = wafer.remove(msk.Join(set(masks)))
    if alias is None:
        return mask
    else:
        return mask.alias(alias)


class SubstrateNet(net_.Net):
    """SubstrateNet is a net representing the bulk of a wafer.
    """
    def __init__(self, *, name: str):
        super().__init__(name=name)

