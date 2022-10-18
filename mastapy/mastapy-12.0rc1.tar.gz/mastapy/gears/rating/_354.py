"""_354.py

GearMeshRating
"""


from mastapy._internal import constructor
from mastapy.gears.load_case import _868
from mastapy.gears.load_case.worm import _871
from mastapy._internal.cast_exception import CastException
from mastapy.gears.load_case.face import _874
from mastapy.gears.load_case.cylindrical import _877
from mastapy.gears.load_case.conical import _880
from mastapy.gears.load_case.concept import _883
from mastapy.gears.load_case.bevel import _885
from mastapy.gears.rating import _347
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshRating',)


class GearMeshRating(_347.AbstractGearMeshRating):
    """GearMeshRating

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_RATING

    def __init__(self, instance_to_wrap: 'GearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driving_gear(self) -> 'str':
        """str: 'DrivingGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DrivingGear

        if temp is None:
            return ''

        return temp

    @property
    def energy_loss(self) -> 'float':
        """float: 'EnergyLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def is_loaded(self) -> 'bool':
        """bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def mesh_efficiency(self) -> 'float':
        """float: 'MeshEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_name(self) -> 'str':
        """str: 'PinionName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionName

        if temp is None:
            return ''

        return temp

    @property
    def pinion_torque(self) -> 'float':
        """float: 'PinionTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_pinion_torque(self) -> 'float':
        """float: 'SignedPinionTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedPinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_wheel_torque(self) -> 'float':
        """float: 'SignedWheelTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedWheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self) -> 'float':
        """float: 'TotalEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_name(self) -> 'str':
        """str: 'WheelName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelName

        if temp is None:
            return ''

        return temp

    @property
    def wheel_torque(self) -> 'float':
        """float: 'WheelTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_load_case(self) -> '_868.MeshLoadCase':
        """MeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _868.MeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to MeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case_of_type_worm_mesh_load_case(self) -> '_871.WormMeshLoadCase':
        """WormMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _871.WormMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to WormMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case_of_type_face_mesh_load_case(self) -> '_874.FaceMeshLoadCase':
        """FaceMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _874.FaceMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to FaceMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case_of_type_cylindrical_mesh_load_case(self) -> '_877.CylindricalMeshLoadCase':
        """CylindricalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _877.CylindricalMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to CylindricalMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case_of_type_conical_mesh_load_case(self) -> '_880.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _880.ConicalMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to ConicalMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case_of_type_concept_mesh_load_case(self) -> '_883.ConceptMeshLoadCase':
        """ConceptMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _883.ConceptMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to ConceptMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case_of_type_bevel_mesh_load_case(self) -> '_885.BevelMeshLoadCase':
        """BevelMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        if _885.BevelMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to BevelMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
