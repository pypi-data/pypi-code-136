"""_304.py

CADFace
"""


from typing import List

from mastapy._math.vector_2d import Vector2D
from mastapy._internal import conversion, constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CAD_FACE = python_net_import('SMT.MastaAPI.Geometry.TwoD', 'CADFace')


__docformat__ = 'restructuredtext en'
__all__ = ('CADFace',)


class CADFace(_0.APIBase):
    """CADFace

    This is a mastapy class.
    """

    TYPE = _CAD_FACE

    def __init__(self, instance_to_wrap: 'CADFace.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def add_arc(self, circle_origin: 'Vector2D', radius: 'float', start_angle: 'float', sweep_angle: 'float'):
        """ 'AddArc' is the original name of this method.

        Args:
            circle_origin (Vector2D)
            radius (float)
            start_angle (float)
            sweep_angle (float)
        """

        circle_origin = conversion.mp_to_pn_vector2d(circle_origin)
        radius = float(radius)
        start_angle = float(start_angle)
        sweep_angle = float(sweep_angle)
        self.wrapped.AddArc(circle_origin, radius if radius else 0.0, start_angle if start_angle else 0.0, sweep_angle if sweep_angle else 0.0)

    def add_line(self, point_1: 'Vector2D', point_2: 'Vector2D'):
        """ 'AddLine' is the original name of this method.

        Args:
            point_1 (Vector2D)
            point_2 (Vector2D)
        """

        point_1 = conversion.mp_to_pn_vector2d(point_1)
        point_2 = conversion.mp_to_pn_vector2d(point_2)
        self.wrapped.AddLine(point_1, point_2)

    def add_poly_line(self, points: 'List[Vector2D]'):
        """ 'AddPolyLine' is the original name of this method.

        Args:
            points (List[Vector2D])
        """

        points = conversion.mp_to_pn_objects_in_list(points)
        self.wrapped.AddPolyLine(points)
