"""_3972.py

ShaftForcedComplexShape
"""


from mastapy.system_model.analyses_and_results.rotor_dynamics import _3971
from mastapy.utility.units_and_measurements.measurements import _1635, _1580
from mastapy._internal.python_net import python_net_import

_SHAFT_FORCED_COMPLEX_SHAPE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'ShaftForcedComplexShape')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftForcedComplexShape',)


class ShaftForcedComplexShape(_3971.ShaftComplexShape['_1635.LengthVeryShort', '_1580.AngleSmall']):
    """ShaftForcedComplexShape

    This is a mastapy class.
    """

    TYPE = _SHAFT_FORCED_COMPLEX_SHAPE

    def __init__(self, instance_to_wrap: 'ShaftForcedComplexShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
