"""_1257.py

HarmonicLoadDataControlExcitationOptionForElectricMachineMode
"""


from mastapy.electric_machines.harmonic_load_data import _1349
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE = python_net_import('SMT.MastaAPI.ElectricMachines', 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataControlExcitationOptionForElectricMachineMode',)


class HarmonicLoadDataControlExcitationOptionForElectricMachineMode(_1349.HarmonicLoadDataControlExcitationOptionBase):
    """HarmonicLoadDataControlExcitationOptionForElectricMachineMode

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
