"""_2035.py

BearingRatingLife
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2046, _2052
from mastapy._internal.python_net import python_net_import

_BEARING_RATING_LIFE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'BearingRatingLife')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingRatingLife',)


class BearingRatingLife(_2052.SKFCalculationResult):
    """BearingRatingLife

    This is a mastapy class.
    """

    TYPE = _BEARING_RATING_LIFE

    def __init__(self, instance_to_wrap: 'BearingRatingLife.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contamination_factor(self) -> 'float':
        """float: 'ContaminationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContaminationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def skf_life_modification_factor(self) -> 'float':
        """float: 'SKFLifeModificationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFLifeModificationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def life_model(self) -> '_2046.LifeModel':
        """LifeModel: 'LifeModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
