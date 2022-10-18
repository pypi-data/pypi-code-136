"""_6748.py

BeltDriveLoadCase
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2527, _2537
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltDriveLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveLoadCase',)


class BeltDriveLoadCase(_6878.SpecialisedAssemblyLoadCase):
    """BeltDriveLoadCase

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_LOAD_CASE

    def __init__(self, instance_to_wrap: 'BeltDriveLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pre_tension(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PreTension' is the original name of this property."""

        temp = self.wrapped.PreTension

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @pre_tension.setter
    def pre_tension(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PreTension = value

    @property
    def assembly_design(self) -> '_2527.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        if _2527.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
