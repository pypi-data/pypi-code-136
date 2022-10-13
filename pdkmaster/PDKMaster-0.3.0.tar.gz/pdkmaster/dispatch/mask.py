# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from ..technology import mask as msk, wafer_ as wfr


class MaskDispatcher:
    """Dispatch to class method based on type of `_Mask` subclasses.

    This dispatcher follows the common way of working in the `dispatch` module.
    """
    def __call__(self, mask: msk._Mask, *args, **kwargs):
        classname = mask.__class__.__name__.split(".")[-1]
        return getattr(self, classname, self._pd_unhandled)(mask, *args, **kwargs)

    def _pd_unhandled(self, mask, *args, **kwargs):
        raise RuntimeError(
            "Internal error: unhandled dispatcher for object of type "
            f"{mask.__class__.__name__}"
        )

    def _Mask(self, mask: msk._Mask, *args, **kwargs):
        raise NotImplementedError(
            f"No dispatcher implemented for object of type {mask.__class__.__name__}"
        )

    def DesignMask(self, mask: msk.DesignMask, *args, **kwargs):
        return self._Mask(mask, *args, **kwargs)

    def _MaskAlias(self, mask: msk._MaskAlias, *args, **kwargs):
        return self._Mask(mask, *args, **kwargs)

    def _PartsWith(self, pw: msk._PartsWith, *args, **kwargs):
        return self._Mask(pw, *args, **kwargs)

    def Join(self, join: msk.Join, *args, **kwargs):
        return self._Mask(join, *args, **kwargs)

    def Intersect(self, intersect: msk.Intersect, *args, **kwargs):
        return self._Mask(intersect, *args, **kwargs)

    def _MaskRemove(self, mr: msk._MaskRemove, *args, **kwargs):
        return self._Mask(mr, *args, **kwargs)

    def _SameNet(self, same: msk._SameNet, *args, **kwargs):
        return self._Mask(same, *args, **kwargs)

    def _Wafer(self, wafer: wfr._Wafer, *args, **kwargs):
        return self._Mask(wafer, *args, **kwargs)
