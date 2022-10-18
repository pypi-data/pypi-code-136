"""_267.py

MaterialsSettingsItem
"""


from typing import List

from mastapy.utility.property import _1805
from mastapy.materials import _268
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1792
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Materials', 'MaterialsSettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialsSettingsItem',)


class MaterialsSettingsItem(_1792.NamedDatabaseItem):
    """MaterialsSettingsItem

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS_ITEM

    def __init__(self, instance_to_wrap: 'MaterialsSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def available_material_standards(self) -> 'List[_1805.EnumWithBool[_268.MaterialStandards]]':
        """List[EnumWithBool[MaterialStandards]]: 'AvailableMaterialStandards' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AvailableMaterialStandards

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
