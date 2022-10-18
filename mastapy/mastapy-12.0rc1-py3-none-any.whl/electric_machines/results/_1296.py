"""_1296.py

DynamicForceResults
"""


from typing import List

from mastapy.math_utility import _1476
from mastapy._internal import constructor, conversion
from mastapy.electric_machines.harmonic_load_data import _1346
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'DynamicForceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceResults',)


class DynamicForceResults(_1346.ElectricMachineHarmonicLoadDataBase):
    """DynamicForceResults

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_RESULTS

    def __init__(self, instance_to_wrap: 'DynamicForceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations(self) -> 'List[_1476.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
