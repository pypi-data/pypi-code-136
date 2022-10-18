"""_747.py

ConventionalShavingDynamicsViewModel
"""


from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _763, _744
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ConventionalShavingDynamicsViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ConventionalShavingDynamicsViewModel',)


class ConventionalShavingDynamicsViewModel(_763.ShavingDynamicsViewModel['_744.ConventionalShavingDynamics']):
    """ConventionalShavingDynamicsViewModel

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS_VIEW_MODEL

    def __init__(self, instance_to_wrap: 'ConventionalShavingDynamicsViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
