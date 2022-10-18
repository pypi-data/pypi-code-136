"""_3970.py

RotorDynamicsDrawStyle
"""


from mastapy._internal import constructor
from mastapy.system_model.drawing import _2197
from mastapy._internal.python_net import python_net_import

_ROTOR_DYNAMICS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'RotorDynamicsDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorDynamicsDrawStyle',)


class RotorDynamicsDrawStyle(_2197.ContourDrawStyle):
    """RotorDynamicsDrawStyle

    This is a mastapy class.
    """

    TYPE = _ROTOR_DYNAMICS_DRAW_STYLE

    def __init__(self, instance_to_wrap: 'RotorDynamicsDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_whirl_orbits(self) -> 'bool':
        """bool: 'ShowWhirlOrbits' is the original name of this property."""

        temp = self.wrapped.ShowWhirlOrbits

        if temp is None:
            return False

        return temp

    @show_whirl_orbits.setter
    def show_whirl_orbits(self, value: 'bool'):
        self.wrapped.ShowWhirlOrbits = bool(value) if value else False
