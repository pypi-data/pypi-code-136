"""_6801.py

ElectricMachineHarmonicLoadDataFromMasta
"""


from mastapy.system_model.analyses_and_results.static_loads import _6797
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ElectricMachineHarmonicLoadDataFromMasta')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataFromMasta',)


class ElectricMachineHarmonicLoadDataFromMasta(_6797.ElectricMachineHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataFromMasta

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataFromMasta.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
