"""_863.py

ConicalMeshLoadDistributionAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.conical import _880
from mastapy.gears.load_case.bevel import _885
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel import _777
from mastapy.gears.ltca.conical import _862
from mastapy.gears.ltca import _834
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalMeshLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshLoadDistributionAnalysis',)


class ConicalMeshLoadDistributionAnalysis(_834.GearMeshLoadDistributionAnalysis):
    """ConicalMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOAD_DISTRIBUTION_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConicalMeshLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_roll_angles(self) -> 'int':
        """int: 'NumberOfRollAngles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRollAngles

        if temp is None:
            return 0

        return temp

    @property
    def pinion_mean_te(self) -> 'float':
        """float: 'PinionMeanTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionMeanTE

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_peak_to_peak_te(self) -> 'float':
        """float: 'PinionPeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionPeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_peak_to_peak_te(self) -> 'float':
        """float: 'WheelPeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelPeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def conical_mesh_load_case(self) -> '_880.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        if _880.ConicalMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_mesh_load_case to ConicalMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_mesh_manufacturing_analysis(self) -> '_777.ConicalMeshManufacturingAnalysis':
        """ConicalMeshManufacturingAnalysis: 'ConicalMeshManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshManufacturingAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_862.ConicalMeshedGearLoadDistributionAnalysis]':
        """List[ConicalMeshedGearLoadDistributionAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
