"""_1584.py

AngularJerk
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_ANGULAR_JERK = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'AngularJerk')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularJerk',)


class AngularJerk(_1570.MeasurementBase):
    """AngularJerk

    This is a mastapy class.
    """

    TYPE = _ANGULAR_JERK

    def __init__(self, instance_to_wrap: 'AngularJerk.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
