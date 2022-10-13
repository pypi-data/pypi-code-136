# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from ..technology import rule as rle, property_ as prp, mask as msk


class RuleDispatcher:
    """Dispatch to class method based on type of `_Rule` subclasses.

    This dispatcher follows the common way of working in the `dispatch` module.
    """
    def __call__(self, rule: rle._Rule, *args, **kwargs):
        classname = rule.__class__.__name__.split(".")[-1]
        return getattr(self, classname, self._pd_unhandled)(rule, *args, **kwargs)

    def _pd_unhandled(self, rule, *args, **kwargs):
        raise RuntimeError(
            "Internal error: unhandled dispatcher for object of type "
            f"{rule.__class__.__name__}"
        )

    def _Rule(self, rule: rle._Rule, *args, **kwargs):
        raise NotImplementedError(
            f"No dispatcher implemented for object of type {rule.__class__.__name__}"
        )

    def _Condition(self, cond: rle._Condition, *args, **kwargs):
        return self._Rule(cond, *args, **kwargs)

    def _Comparison(self, cond: prp._Comparison, *args, **kwargs):
        return self._Condition(cond, *args, **kwargs)

    def Greater(self, gt: prp.Operators.Greater, *args, **kwargs):
        return self._Comparison(gt, *args, **kwargs)

    def GreaterEqual(self, ge: prp.Operators.GreaterEqual, *args, **kwargs):
        return self._Comparison(ge, *args, **kwargs)

    def Smaller(self, st: prp.Operators.Smaller, *args, **kwargs):
        return self._Comparison(st, *args, **kwargs)

    def SmallerEqual(self, se: prp.Operators.SmallerEqual, *args, **kwargs):
        return self._Comparison(se, *args, **kwargs)

    def Equal(self, eq: prp.Operators.Equal, *args, **kwargs):
        return self._Comparison(eq, *args, **kwargs)

    def _MultiMaskCondition(self, cond: msk._MultiMaskCondition, *args, **kwargs):
        return self._Condition(cond, *args, **kwargs)

    def _InsideCondition(self, cond: msk._InsideCondition, *args, **kwargs):
        return self._MultiMaskCondition(cond, *args, **kwargs)

    def _OutsideCondition(self, cond: msk._OutsideCondition, *args, **kwargs):
        return self._MultiMaskCondition(cond, *args, **kwargs)

    def DesignMask(self, mask: msk.DesignMask, *args, **kwargs):
        return self._Rule(mask, *args, **kwargs)

    def _MaskAlias(self, alias: msk._MaskAlias, *args, **kwargs):
        return self._Rule(alias, *args, **kwargs)

    def Connect(self, conn: msk.Connect, *args, **kwargs):
        return self._Rule(conn)
