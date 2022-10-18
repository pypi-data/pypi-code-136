"""_265.py

MaterialsSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS = python_net_import('SMT.MastaAPI.Materials', 'MaterialsSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialsSettings',)


class MaterialsSettings(_0.APIBase):
    """MaterialsSettings

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS

    def __init__(self, instance_to_wrap: 'MaterialsSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
