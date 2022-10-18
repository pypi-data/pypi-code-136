"""_986.py

FaceGearMicroGeometry
"""


from mastapy.gears.gear_designs.face import _982, _987, _990
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093, _1092, _1096
from mastapy.gears.analysis import _1211
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMicroGeometry',)


class FaceGearMicroGeometry(_1211.GearImplementationDetail):
    """FaceGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MICRO_GEOMETRY

    def __init__(self, instance_to_wrap: 'FaceGearMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear(self) -> '_982.FaceGearDesign':
        """FaceGearDesign: 'FaceGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGear

        if temp is None:
            return None

        if _982.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast face_gear to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry(self) -> '_1093.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        if _1093.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast micro_geometry to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_of_type_cylindrical_gear_micro_geometry(self) -> '_1092.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        if _1092.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast micro_geometry to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1096.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        if _1096.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast micro_geometry to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
