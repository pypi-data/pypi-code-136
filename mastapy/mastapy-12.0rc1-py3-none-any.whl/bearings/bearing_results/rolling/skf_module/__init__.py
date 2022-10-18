"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2032 import AdjustedSpeed
    from ._2033 import AdjustmentFactors
    from ._2034 import BearingLoads
    from ._2035 import BearingRatingLife
    from ._2036 import DynamicAxialLoadCarryingCapacity
    from ._2037 import Frequencies
    from ._2038 import FrequencyOfOverRolling
    from ._2039 import Friction
    from ._2040 import FrictionalMoment
    from ._2041 import FrictionSources
    from ._2042 import Grease
    from ._2043 import GreaseLifeAndRelubricationInterval
    from ._2044 import GreaseQuantity
    from ._2045 import InitialFill
    from ._2046 import LifeModel
    from ._2047 import MinimumLoad
    from ._2048 import OperatingViscosity
    from ._2049 import PermissibleAxialLoad
    from ._2050 import RotationalFrequency
    from ._2051 import SKFAuthentication
    from ._2052 import SKFCalculationResult
    from ._2053 import SKFCredentials
    from ._2054 import SKFModuleResults
    from ._2055 import StaticSafetyFactors
    from ._2056 import Viscosities
