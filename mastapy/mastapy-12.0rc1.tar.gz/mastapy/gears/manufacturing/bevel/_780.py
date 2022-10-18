"""_780.py

ConicalMeshMicroGeometryConfigBase
"""


from mastapy.gears.gear_designs.conical import _1145
from mastapy._internal import constructor
from mastapy.gears.gear_designs.zerol_bevel import _946
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _955
from mastapy.gears.gear_designs.straight_bevel_diff import _959
from mastapy.gears.gear_designs.spiral_bevel import _963
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _967
from mastapy.gears.gear_designs.klingelnberg_hypoid import _971
from mastapy.gears.gear_designs.klingelnberg_conical import _975
from mastapy.gears.gear_designs.hypoid import _979
from mastapy.gears.gear_designs.bevel import _1171
from mastapy.gears.gear_designs.agma_gleason_conical import _1184
from mastapy.gears.manufacturing.bevel import (
    _771, _769, _770, _781,
    _782, _787
)
from mastapy.gears.analysis import _1215
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshMicroGeometryConfigBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshMicroGeometryConfigBase',)


class ConicalMeshMicroGeometryConfigBase(_1215.GearMeshImplementationDetail):
    """ConicalMeshMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE

    def __init__(self, instance_to_wrap: 'ConicalMeshMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh(self) -> '_1145.ConicalGearMeshDesign':
        """ConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _1145.ConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to ConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_zerol_bevel_gear_mesh_design(self) -> '_946.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _946.ZerolBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to ZerolBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_straight_bevel_gear_mesh_design(self) -> '_955.StraightBevelGearMeshDesign':
        """StraightBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _955.StraightBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to StraightBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_straight_bevel_diff_gear_mesh_design(self) -> '_959.StraightBevelDiffGearMeshDesign':
        """StraightBevelDiffGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _959.StraightBevelDiffGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to StraightBevelDiffGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_spiral_bevel_gear_mesh_design(self) -> '_963.SpiralBevelGearMeshDesign':
        """SpiralBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _963.SpiralBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to SpiralBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self) -> '_967.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _967.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to KlingelnbergCycloPalloidSpiralBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self) -> '_971.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        """KlingelnbergCycloPalloidHypoidGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _971.KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to KlingelnbergCycloPalloidHypoidGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_klingelnberg_conical_gear_mesh_design(self) -> '_975.KlingelnbergConicalGearMeshDesign':
        """KlingelnbergConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _975.KlingelnbergConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to KlingelnbergConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_hypoid_gear_mesh_design(self) -> '_979.HypoidGearMeshDesign':
        """HypoidGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _979.HypoidGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to HypoidGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_bevel_gear_mesh_design(self) -> '_1171.BevelGearMeshDesign':
        """BevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _1171.BevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to BevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_agma_gleason_conical_gear_mesh_design(self) -> '_1184.AGMAGleasonConicalGearMeshDesign':
        """AGMAGleasonConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh

        if temp is None:
            return None

        if _1184.AGMAGleasonConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to AGMAGleasonConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config(self) -> '_771.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        if _771.ConicalGearMicroGeometryConfigBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalGearMicroGeometryConfigBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_gear_manufacturing_config(self) -> '_769.ConicalGearManufacturingConfig':
        """ConicalGearManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        if _769.ConicalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_gear_micro_geometry_config(self) -> '_770.ConicalGearMicroGeometryConfig':
        """ConicalGearMicroGeometryConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        if _770.ConicalGearMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalGearMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_pinion_manufacturing_config(self) -> '_781.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        if _781.ConicalPinionManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalPinionManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_pinion_micro_geometry_config(self) -> '_782.ConicalPinionMicroGeometryConfig':
        """ConicalPinionMicroGeometryConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        if _782.ConicalPinionMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_wheel_manufacturing_config(self) -> '_787.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        if _787.ConicalWheelManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalWheelManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
