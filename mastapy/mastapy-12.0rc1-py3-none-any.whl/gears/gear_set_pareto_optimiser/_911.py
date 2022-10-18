"""_911.py

MicroGeometryDesignSpaceSearchChartInformation
"""


from mastapy.gears.gear_set_pareto_optimiser import (
    _909, _912, _897, _910
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.ltca.cylindrical import _853
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryDesignSpaceSearchChartInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryDesignSpaceSearchChartInformation',)


class MicroGeometryDesignSpaceSearchChartInformation(_897.ChartInfoBase['_853.CylindricalGearSetLoadDistributionAnalysis', '_910.MicroGeometryDesignSpaceSearchCandidate']):
    """MicroGeometryDesignSpaceSearchChartInformation

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION

    def __init__(self, instance_to_wrap: 'MicroGeometryDesignSpaceSearchChartInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def optimiser(self) -> '_909.MicroGeometryDesignSpaceSearch':
        """MicroGeometryDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimiser

        if temp is None:
            return None

        if _909.MicroGeometryDesignSpaceSearch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryDesignSpaceSearch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimiser_of_type_micro_geometry_gear_set_design_space_search(self) -> '_912.MicroGeometryGearSetDesignSpaceSearch':
        """MicroGeometryGearSetDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimiser

        if temp is None:
            return None

        if _912.MicroGeometryGearSetDesignSpaceSearch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryGearSetDesignSpaceSearch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
