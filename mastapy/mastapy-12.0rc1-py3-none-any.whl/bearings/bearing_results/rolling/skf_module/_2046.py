"""_2046.py

LifeModel
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2052
from mastapy._internal.python_net import python_net_import

_LIFE_MODEL = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'LifeModel')


__docformat__ = 'restructuredtext en'
__all__ = ('LifeModel',)


class LifeModel(_2052.SKFCalculationResult):
    """LifeModel

    This is a mastapy class.
    """

    TYPE = _LIFE_MODEL

    def __init__(self, instance_to_wrap: 'LifeModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic(self) -> 'float':
        """float: 'Basic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Basic

        if temp is None:
            return 0.0

        return temp

    @property
    def skf(self) -> 'float':
        """float: 'SKF' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKF

        if temp is None:
            return 0.0

        return temp

    @property
    def skfgblm(self) -> 'float':
        """float: 'SKFGBLM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFGBLM

        if temp is None:
            return 0.0

        return temp
