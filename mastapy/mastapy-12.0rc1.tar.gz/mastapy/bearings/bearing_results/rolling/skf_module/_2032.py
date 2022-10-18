"""_2032.py

AdjustedSpeed
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2033, _2052
from mastapy._internal.python_net import python_net_import

_ADJUSTED_SPEED = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'AdjustedSpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AdjustedSpeed',)


class AdjustedSpeed(_2052.SKFCalculationResult):
    """AdjustedSpeed

    This is a mastapy class.
    """

    TYPE = _ADJUSTED_SPEED

    def __init__(self, instance_to_wrap: 'AdjustedSpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_reference_speed(self) -> 'float':
        """float: 'AdjustedReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def adjustment_factors(self) -> '_2033.AdjustmentFactors':
        """AdjustmentFactors: 'AdjustmentFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustmentFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
