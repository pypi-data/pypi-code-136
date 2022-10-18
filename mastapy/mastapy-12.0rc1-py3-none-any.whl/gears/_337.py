"""_337.py

PocketingPowerLossCoefficientsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.gears import _336
from mastapy._internal.python_net import python_net_import

_POCKETING_POWER_LOSS_COEFFICIENTS_DATABASE = python_net_import('SMT.MastaAPI.Gears', 'PocketingPowerLossCoefficientsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('PocketingPowerLossCoefficientsDatabase',)


class PocketingPowerLossCoefficientsDatabase(_1791.NamedDatabase['_336.PocketingPowerLossCoefficients']):
    """PocketingPowerLossCoefficientsDatabase

    This is a mastapy class.
    """

    TYPE = _POCKETING_POWER_LOSS_COEFFICIENTS_DATABASE

    def __init__(self, instance_to_wrap: 'PocketingPowerLossCoefficientsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
