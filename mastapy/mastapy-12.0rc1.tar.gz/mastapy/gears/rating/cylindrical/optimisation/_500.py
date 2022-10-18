"""_500.py

SafetyFactorOptimisationStepResultShortLength
"""


from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.optimisation import _497
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_SHORT_LENGTH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation', 'SafetyFactorOptimisationStepResultShortLength')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorOptimisationStepResultShortLength',)


class SafetyFactorOptimisationStepResultShortLength(_497.SafetyFactorOptimisationStepResult):
    """SafetyFactorOptimisationStepResultShortLength

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_SHORT_LENGTH

    def __init__(self, instance_to_wrap: 'SafetyFactorOptimisationStepResultShortLength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp
