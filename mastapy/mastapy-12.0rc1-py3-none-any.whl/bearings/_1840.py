"""_1840.py

BearingSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettings',)


class BearingSettings(_0.APIBase):
    """BearingSettings

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS

    def __init__(self, instance_to_wrap: 'BearingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
