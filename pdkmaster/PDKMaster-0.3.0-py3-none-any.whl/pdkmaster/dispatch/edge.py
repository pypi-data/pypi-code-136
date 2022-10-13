# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from ..technology import edge as edg


class EdgeDispatcher:
    """Dispatch to class method based on type of `_Edge` subclasses.

    This dispatcher follows the common way of working in the `dispatch` module.
    """
    def __call__(self, edge: edg._Edge, *args, **kwargs):
        classname = edge.__class__.__name__.split(".")[-1]
        return getattr(self, classname, self._pd_unhandled)(edge, *args, **kwargs)

    def _pd_unhandled(self, edge, *args, **kwargs):
        raise RuntimeError(
            "Internal error: unhandled dispatcher for object of type "
            f"{edge.__class__.__name__}"
        )

    def _Edge(self, edge: edg._Edge, *args, **kwargs):
        raise NotImplementedError(
            f"No dispatcher implemented for object of type {edge.__class__.__name__}"
        )

    def _DualEdgeOperation(self, op: edg._DualEdgeOperation, *args, **kwargs):
        return self._Edge(op, *args, **kwargs)

    def MaskEdge(self, edge: edg.MaskEdge, *args, **kwargs):
        return self._Edge(edge, *args, **kwargs)

    def Join(self, join: edg.Join, *args, **kwargs):
        return self._Edge(join, *args, **kwargs)

    def Intersect(self, intersect: edg.Intersect, *args, **kwargs):
        return self._Edge(intersect, *args, **kwargs)
