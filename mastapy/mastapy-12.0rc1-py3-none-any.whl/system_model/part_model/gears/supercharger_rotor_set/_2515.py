"""_2515.py

SuperchargerRotorSetDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2514
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'SuperchargerRotorSetDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('SuperchargerRotorSetDatabase',)


class SuperchargerRotorSetDatabase(_1791.NamedDatabase['_2514.SuperchargerRotorSet']):
    """SuperchargerRotorSetDatabase

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET_DATABASE

    def __init__(self, instance_to_wrap: 'SuperchargerRotorSetDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
