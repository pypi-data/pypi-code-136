"""_1595.py

DataSize
"""


from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.python_net import python_net_import

_DATA_SIZE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'DataSize')


__docformat__ = 'restructuredtext en'
__all__ = ('DataSize',)


class DataSize(_1570.MeasurementBase):
    """DataSize

    This is a mastapy class.
    """

    TYPE = _DATA_SIZE

    def __init__(self, instance_to_wrap: 'DataSize.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
