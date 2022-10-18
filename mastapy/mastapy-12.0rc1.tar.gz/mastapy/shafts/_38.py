"""_38.py

ShaftSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SHAFT_SETTINGS = python_net_import('SMT.MastaAPI.Shafts', 'ShaftSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSettings',)


class ShaftSettings(_0.APIBase):
    """ShaftSettings

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS

    def __init__(self, instance_to_wrap: 'ShaftSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
