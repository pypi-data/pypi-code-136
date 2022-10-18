"""list_with_selected_item.py

Implementations of 'ListWithSelectedItem' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""


from typing import List, Generic, TypeVar

from mastapy._internal import mixins, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.ltca.cylindrical import _849, _850
from mastapy.gears.manufacturing.cylindrical import _618
from mastapy.gears.manufacturing.bevel import _784
from mastapy.electric_machines import (
    _1252, _1276, _1249, _1235,
    _1259, _1267, _1270, _1283,
    _1285
)
from mastapy.electric_machines.results import _1299, _1315, _1316
from mastapy._internal.cast_exception import CastException
from mastapy.utility import _1565
from mastapy.utility.units_and_measurements import (
    _1575, _1567, _1568, _1569,
    _1573, _1574, _1576, _1570
)
from mastapy.utility.units_and_measurements.measurements import (
    _1577, _1578, _1579, _1580,
    _1581, _1582, _1583, _1584,
    _1585, _1586, _1587, _1588,
    _1589, _1590, _1591, _1592,
    _1593, _1594, _1595, _1596,
    _1597, _1598, _1599, _1600,
    _1601, _1602, _1603, _1604,
    _1605, _1606, _1607, _1608,
    _1609, _1610, _1611, _1612,
    _1613, _1614, _1615, _1616,
    _1617, _1618, _1619, _1620,
    _1621, _1622, _1623, _1624,
    _1625, _1626, _1627, _1628,
    _1629, _1630, _1631, _1632,
    _1633, _1634, _1635, _1636,
    _1637, _1638, _1639, _1640,
    _1641, _1642, _1643, _1644,
    _1645, _1646, _1647, _1648,
    _1649, _1650, _1651, _1652,
    _1653, _1654, _1655, _1656,
    _1657, _1658, _1659, _1660,
    _1661, _1662, _1663, _1664,
    _1665, _1666, _1667, _1668,
    _1669, _1670, _1671, _1672,
    _1673, _1674, _1675, _1676,
    _1677, _1678, _1679, _1680,
    _1681, _1682, _1683, _1684,
    _1685, _1686, _1687, _1688,
    _1689, _1690, _1691, _1692,
    _1693, _1694, _1695, _1696,
    _1697, _1698, _1699, _1700,
    _1701, _1702, _1703
)
from mastapy.utility.file_access_helpers import _1780
from mastapy.system_model.part_model import (
    _2424, _2396, _2388, _2389,
    _2392, _2394, _2399, _2400,
    _2404, _2405, _2407, _2414,
    _2415, _2416, _2418, _2421,
    _2423, _2429, _2431
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5615, _5668, _5669, _5670,
    _5671, _5672, _5673, _5674,
    _5675, _5676, _5677, _5678,
    _5688, _5690, _5691, _5693,
    _5722, _5739, _5764
)
from mastapy._internal.tuple_with_name import TupleWithName
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2705, _2640, _2647, _2652,
    _2666, _2670, _2685, _2686,
    _2687, _2700, _2709, _2714,
    _2717, _2720, _2753, _2759,
    _2762, _2782, _2785, _2691,
    _2692, _2693, _2696
)
from mastapy.system_model.part_model.gears import (
    _2483, _2465, _2467, _2471,
    _2473, _2475, _2477, _2480,
    _2486, _2488, _2490, _2492,
    _2493, _2495, _2497, _2499,
    _2503, _2505, _2464, _2466,
    _2468, _2469, _2470, _2472,
    _2474, _2476, _2478, _2479,
    _2481, _2485, _2487, _2489,
    _2491, _2494, _2496, _2498,
    _2500, _2501, _2502, _2504
)
from mastapy.system_model.fe import _2336, _2334, _2325
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.cycloidal import _2520, _2521
from mastapy.system_model.part_model.couplings import (
    _2530, _2533, _2535, _2538,
    _2540, _2541, _2547, _2549,
    _2552, _2555, _2556, _2557,
    _2559, _2561
)
from mastapy.system_model.fe.links import (
    _2369, _2370, _2372, _2373,
    _2374, _2375, _2376, _2377,
    _2378, _2379, _2380, _2381,
    _2382, _2383
)
from mastapy.system_model.part_model.part_groups import _2439
from mastapy.gears.gear_designs import _943
from mastapy.gears.gear_designs.zerol_bevel import _947
from mastapy.gears.gear_designs.worm import _952
from mastapy.gears.gear_designs.straight_bevel import _956
from mastapy.gears.gear_designs.straight_bevel_diff import _960
from mastapy.gears.gear_designs.spiral_bevel import _964
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _968
from mastapy.gears.gear_designs.klingelnberg_hypoid import _972
from mastapy.gears.gear_designs.klingelnberg_conical import _976
from mastapy.gears.gear_designs.hypoid import _980
from mastapy.gears.gear_designs.face import _988
from mastapy.gears.gear_designs.cylindrical import _1021, _1033
from mastapy.gears.gear_designs.conical import _1146
from mastapy.gears.gear_designs.concept import _1168
from mastapy.gears.gear_designs.bevel import _1172
from mastapy.gears.gear_designs.agma_gleason_conical import _1185
from mastapy.system_model.analyses_and_results.load_case_groups import _5599, _5600
from mastapy.nodal_analysis.component_mode_synthesis import _219, _220
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5780
from mastapy.system_model.analyses_and_results.static_loads import _6731, _6738
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4329

_ARRAY = python_net_import('System', 'Array')
_LIST_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.Utility.Property', 'ListWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = (
    'ListWithSelectedItem_str', 'ListWithSelectedItem_int',
    'ListWithSelectedItem_T', 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis',
    'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis', 'ListWithSelectedItem_CylindricalSetManufacturingConfig',
    'ListWithSelectedItem_ConicalSetManufacturingConfig', 'ListWithSelectedItem_ElectricMachineSetup',
    'ListWithSelectedItem_float', 'ListWithSelectedItem_ElectricMachineResults',
    'ListWithSelectedItem_RotorSkewSlice', 'ListWithSelectedItem_SystemDirectory',
    'ListWithSelectedItem_Unit', 'ListWithSelectedItem_MeasurementBase',
    'ListWithSelectedItem_ColumnTitle', 'ListWithSelectedItem_PowerLoad',
    'ListWithSelectedItem_AbstractPeriodicExcitationDetail', 'ListWithSelectedItem_TupleWithName',
    'ListWithSelectedItem_GearMeshSystemDeflection', 'ListWithSelectedItem_GearSet',
    'ListWithSelectedItem_FESubstructureNode', 'ListWithSelectedItem_Component',
    'ListWithSelectedItem_Datum', 'ListWithSelectedItem_FELink',
    'ListWithSelectedItem_FESubstructure', 'ListWithSelectedItem_CylindricalGear',
    'ListWithSelectedItem_ElectricMachineDetail', 'ListWithSelectedItem_GuideDxfModel',
    'ListWithSelectedItem_ConcentricPartGroup', 'ListWithSelectedItem_CylindricalGearSet',
    'ListWithSelectedItem_GearSetDesign', 'ListWithSelectedItem_ShaftHubConnection',
    'ListWithSelectedItem_TSelectableItem', 'ListWithSelectedItem_CylindricalGearSystemDeflection',
    'ListWithSelectedItem_DesignState', 'ListWithSelectedItem_FEPart',
    'ListWithSelectedItem_TPartAnalysis', 'ListWithSelectedItem_CMSElementFaceGroup',
    'ListWithSelectedItem_ResultLocationSelectionGroup', 'ListWithSelectedItem_StaticLoadCase',
    'ListWithSelectedItem_DutyCycle', 'ListWithSelectedItem_ElectricMachineDataSet',
    'ListWithSelectedItem_PointLoad'
)


T = TypeVar('T')
TSelectableItem = TypeVar('TSelectableItem')
TPartAnalysis = TypeVar('TPartAnalysis')


class ListWithSelectedItem_str(str, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_str

    A specific implementation of 'ListWithSelectedItem' for 'str' types.
    """
    __qualname__ = 'str'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        return str.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else '')

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'str':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return str

    @property
    def selected_value(self) -> 'str':
        """str: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return ''

        return temp

    @property
    def available_values(self) -> 'List[str]':
        """List[str]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value


class ListWithSelectedItem_int(int, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_int

    A specific implementation of 'ListWithSelectedItem' for 'int' types.
    """
    __qualname__ = 'int'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        return int.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'int':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def selected_value(self) -> 'int':
        """int: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0

        return temp

    @property
    def available_values(self) -> 'List[int]':
        """List[int]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)
        return value


class ListWithSelectedItem_T(Generic[T], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_T

    A specific implementation of 'ListWithSelectedItem' for 'T' types.
    """
    __qualname__ = 'T'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_T.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'T':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return T

    @property
    def selected_value(self) -> 'T':
        """T: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[T]':
        """List[T]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis(_849.CylindricalGearLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearLoadDistributionAnalysis' types.
    """
    __qualname__ = 'CylindricalGearLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_849.CylindricalGearLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _849.CylindricalGearLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_849.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_849.CylindricalGearLoadDistributionAnalysis]':
        """List[CylindricalGearLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis(_850.CylindricalGearMeshLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearMeshLoadDistributionAnalysis' types.
    """
    __qualname__ = 'CylindricalGearMeshLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_850.CylindricalGearMeshLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _850.CylindricalGearMeshLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_850.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_850.CylindricalGearMeshLoadDistributionAnalysis]':
        """List[CylindricalGearMeshLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalSetManufacturingConfig(_618.CylindricalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalSetManufacturingConfig' types.
    """
    __qualname__ = 'CylindricalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_618.CylindricalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _618.CylindricalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_618.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_618.CylindricalSetManufacturingConfig]':
        """List[CylindricalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConicalSetManufacturingConfig(_784.ConicalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConicalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'ConicalSetManufacturingConfig' types.
    """
    __qualname__ = 'ConicalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConicalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_784.ConicalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _784.ConicalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_784.ConicalSetManufacturingConfig':
        """ConicalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_784.ConicalSetManufacturingConfig]':
        """List[ConicalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineSetup(_1252.ElectricMachineSetup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineSetup

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineSetup' types.
    """
    __qualname__ = 'ElectricMachineSetup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineSetup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1252.ElectricMachineSetup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1252.ElectricMachineSetup.TYPE

    @property
    def selected_value(self) -> '_1252.ElectricMachineSetup':
        """ElectricMachineSetup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1252.ElectricMachineSetup]':
        """List[ElectricMachineSetup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_float(float, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_float

    A specific implementation of 'ListWithSelectedItem' for 'float' types.
    """
    __qualname__ = 'float'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        return float.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0.0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'float':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return float

    @property
    def selected_value(self) -> 'float':
        """float: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0.0

        return temp

    @property
    def available_values(self) -> 'List[float]':
        """List[float]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value


class ListWithSelectedItem_ElectricMachineResults(_1299.ElectricMachineResults, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineResults

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineResults' types.
    """
    __qualname__ = 'ElectricMachineResults'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineResults.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1299.ElectricMachineResults.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1299.ElectricMachineResults.TYPE

    @property
    def selected_value(self) -> '_1299.ElectricMachineResults':
        """ElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1299.ElectricMachineResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_on_load_electric_machine_results(self) -> '_1315.OnLoadElectricMachineResults':
        """OnLoadElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1315.OnLoadElectricMachineResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OnLoadElectricMachineResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_open_circuit_electric_machine_results(self) -> '_1316.OpenCircuitElectricMachineResults':
        """OpenCircuitElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1316.OpenCircuitElectricMachineResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OpenCircuitElectricMachineResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1299.ElectricMachineResults]':
        """List[ElectricMachineResults]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_RotorSkewSlice(_1276.RotorSkewSlice, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_RotorSkewSlice

    A specific implementation of 'ListWithSelectedItem' for 'RotorSkewSlice' types.
    """
    __qualname__ = 'RotorSkewSlice'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_RotorSkewSlice.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1276.RotorSkewSlice.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1276.RotorSkewSlice.TYPE

    @property
    def selected_value(self) -> '_1276.RotorSkewSlice':
        """RotorSkewSlice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1276.RotorSkewSlice]':
        """List[RotorSkewSlice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_SystemDirectory(_1565.SystemDirectory, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_SystemDirectory

    A specific implementation of 'ListWithSelectedItem' for 'SystemDirectory' types.
    """
    __qualname__ = 'SystemDirectory'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_SystemDirectory.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1565.SystemDirectory.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1565.SystemDirectory.TYPE

    @property
    def selected_value(self) -> '_1565.SystemDirectory':
        """SystemDirectory: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1565.SystemDirectory]':
        """List[SystemDirectory]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Unit(_1575.Unit, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Unit

    A specific implementation of 'ListWithSelectedItem' for 'Unit' types.
    """
    __qualname__ = 'Unit'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Unit.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1575.Unit.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1575.Unit.TYPE

    @property
    def selected_value(self) -> '_1575.Unit':
        """Unit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1575.Unit.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Unit. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1575.Unit]':
        """List[Unit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_MeasurementBase(_1570.MeasurementBase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_MeasurementBase

    A specific implementation of 'ListWithSelectedItem' for 'MeasurementBase' types.
    """
    __qualname__ = 'MeasurementBase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_MeasurementBase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1570.MeasurementBase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1570.MeasurementBase.TYPE

    @property
    def selected_value(self) -> '_1570.MeasurementBase':
        """MeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1570.MeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_acceleration(self) -> '_1577.Acceleration':
        """Acceleration: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1577.Acceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Acceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle(self) -> '_1578.Angle':
        """Angle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1578.Angle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Angle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle_per_unit_temperature(self) -> '_1579.AnglePerUnitTemperature':
        """AnglePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1579.AnglePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AnglePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle_small(self) -> '_1580.AngleSmall':
        """AngleSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1580.AngleSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngleSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle_very_small(self) -> '_1581.AngleVerySmall':
        """AngleVerySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1581.AngleVerySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngleVerySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_acceleration(self) -> '_1582.AngularAcceleration':
        """AngularAcceleration: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1582.AngularAcceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularAcceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_compliance(self) -> '_1583.AngularCompliance':
        """AngularCompliance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1583.AngularCompliance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularCompliance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_jerk(self) -> '_1584.AngularJerk':
        """AngularJerk: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1584.AngularJerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularJerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_stiffness(self) -> '_1585.AngularStiffness':
        """AngularStiffness: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1585.AngularStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_velocity(self) -> '_1586.AngularVelocity':
        """AngularVelocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1586.AngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_area(self) -> '_1587.Area':
        """Area: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1587.Area.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Area. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_area_small(self) -> '_1588.AreaSmall':
        """AreaSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1588.AreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_carbon_emission_factor(self) -> '_1589.CarbonEmissionFactor':
        """CarbonEmissionFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1589.CarbonEmissionFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CarbonEmissionFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_current_density(self) -> '_1590.CurrentDensity':
        """CurrentDensity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1590.CurrentDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CurrentDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_current_per_length(self) -> '_1591.CurrentPerLength':
        """CurrentPerLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1591.CurrentPerLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CurrentPerLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cycles(self) -> '_1592.Cycles':
        """Cycles: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1592.Cycles.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Cycles. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_damage(self) -> '_1593.Damage':
        """Damage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1593.Damage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Damage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_damage_rate(self) -> '_1594.DamageRate':
        """DamageRate: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1594.DamageRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to DamageRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_data_size(self) -> '_1595.DataSize':
        """DataSize: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1595.DataSize.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to DataSize. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_decibel(self) -> '_1596.Decibel':
        """Decibel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1596.Decibel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Decibel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_density(self) -> '_1597.Density':
        """Density: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1597.Density.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Density. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electrical_resistance(self) -> '_1598.ElectricalResistance':
        """ElectricalResistance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1598.ElectricalResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricalResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electrical_resistivity(self) -> '_1599.ElectricalResistivity':
        """ElectricalResistivity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1599.ElectricalResistivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricalResistivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_current(self) -> '_1600.ElectricCurrent':
        """ElectricCurrent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1600.ElectricCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy(self) -> '_1601.Energy':
        """Energy: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1601.Energy.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Energy. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy_per_unit_area(self) -> '_1602.EnergyPerUnitArea':
        """EnergyPerUnitArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1602.EnergyPerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergyPerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy_per_unit_area_small(self) -> '_1603.EnergyPerUnitAreaSmall':
        """EnergyPerUnitAreaSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1603.EnergyPerUnitAreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergyPerUnitAreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy_small(self) -> '_1604.EnergySmall':
        """EnergySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1604.EnergySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_enum(self) -> '_1605.Enum':
        """Enum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1605.Enum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Enum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_flow_rate(self) -> '_1606.FlowRate':
        """FlowRate: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1606.FlowRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FlowRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force(self) -> '_1607.Force':
        """Force: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1607.Force.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Force. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force_per_unit_length(self) -> '_1608.ForcePerUnitLength':
        """ForcePerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1608.ForcePerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force_per_unit_pressure(self) -> '_1609.ForcePerUnitPressure':
        """ForcePerUnitPressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1609.ForcePerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force_per_unit_temperature(self) -> '_1610.ForcePerUnitTemperature':
        """ForcePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1610.ForcePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fraction_measurement_base(self) -> '_1611.FractionMeasurementBase':
        """FractionMeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1611.FractionMeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FractionMeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fraction_per_temperature(self) -> '_1612.FractionPerTemperature':
        """FractionPerTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1612.FractionPerTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FractionPerTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_frequency(self) -> '_1613.Frequency':
        """Frequency: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1613.Frequency.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Frequency. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fuel_consumption_engine(self) -> '_1614.FuelConsumptionEngine':
        """FuelConsumptionEngine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1614.FuelConsumptionEngine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FuelConsumptionEngine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fuel_efficiency_vehicle(self) -> '_1615.FuelEfficiencyVehicle':
        """FuelEfficiencyVehicle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1615.FuelEfficiencyVehicle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FuelEfficiencyVehicle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gradient(self) -> '_1616.Gradient':
        """Gradient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1616.Gradient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Gradient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_conductivity(self) -> '_1617.HeatConductivity':
        """HeatConductivity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1617.HeatConductivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatConductivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_transfer(self) -> '_1618.HeatTransfer':
        """HeatTransfer: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1618.HeatTransfer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransfer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1619.HeatTransferCoefficientForPlasticGearTooth':
        """HeatTransferCoefficientForPlasticGearTooth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1619.HeatTransferCoefficientForPlasticGearTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_transfer_resistance(self) -> '_1620.HeatTransferResistance':
        """HeatTransferResistance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1620.HeatTransferResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransferResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_impulse(self) -> '_1621.Impulse':
        """Impulse: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1621.Impulse.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Impulse. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_index(self) -> '_1622.Index':
        """Index: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1622.Index.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Index. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_inductance(self) -> '_1623.Inductance':
        """Inductance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1623.Inductance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Inductance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_integer(self) -> '_1624.Integer':
        """Integer: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1624.Integer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Integer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_inverse_short_length(self) -> '_1625.InverseShortLength':
        """InverseShortLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1625.InverseShortLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InverseShortLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_inverse_short_time(self) -> '_1626.InverseShortTime':
        """InverseShortTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1626.InverseShortTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InverseShortTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_jerk(self) -> '_1627.Jerk':
        """Jerk: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1627.Jerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Jerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_kinematic_viscosity(self) -> '_1628.KinematicViscosity':
        """KinematicViscosity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1628.KinematicViscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KinematicViscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_long(self) -> '_1629.LengthLong':
        """LengthLong: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1629.LengthLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_medium(self) -> '_1630.LengthMedium':
        """LengthMedium: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1630.LengthMedium.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthMedium. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_per_unit_temperature(self) -> '_1631.LengthPerUnitTemperature':
        """LengthPerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1631.LengthPerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthPerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_short(self) -> '_1632.LengthShort':
        """LengthShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1632.LengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_to_the_fourth(self) -> '_1633.LengthToTheFourth':
        """LengthToTheFourth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1633.LengthToTheFourth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthToTheFourth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_very_long(self) -> '_1634.LengthVeryLong':
        """LengthVeryLong: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1634.LengthVeryLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_very_short(self) -> '_1635.LengthVeryShort':
        """LengthVeryShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1635.LengthVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_very_short_per_length_short(self) -> '_1636.LengthVeryShortPerLengthShort':
        """LengthVeryShortPerLengthShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1636.LengthVeryShortPerLengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryShortPerLengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_angular_damping(self) -> '_1637.LinearAngularDamping':
        """LinearAngularDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1637.LinearAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_angular_stiffness_cross_term(self) -> '_1638.LinearAngularStiffnessCrossTerm':
        """LinearAngularStiffnessCrossTerm: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1638.LinearAngularStiffnessCrossTerm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_damping(self) -> '_1639.LinearDamping':
        """LinearDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1639.LinearDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_flexibility(self) -> '_1640.LinearFlexibility':
        """LinearFlexibility: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1640.LinearFlexibility.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearFlexibility. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_stiffness(self) -> '_1641.LinearStiffness':
        """LinearStiffness: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1641.LinearStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_field_strength(self) -> '_1642.MagneticFieldStrength':
        """MagneticFieldStrength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1642.MagneticFieldStrength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticFieldStrength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_flux(self) -> '_1643.MagneticFlux':
        """MagneticFlux: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1643.MagneticFlux.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticFlux. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_flux_density(self) -> '_1644.MagneticFluxDensity':
        """MagneticFluxDensity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1644.MagneticFluxDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticFluxDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_vector_potential(self) -> '_1645.MagneticVectorPotential':
        """MagneticVectorPotential: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1645.MagneticVectorPotential.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticVectorPotential. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetomotive_force(self) -> '_1646.MagnetomotiveForce':
        """MagnetomotiveForce: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1646.MagnetomotiveForce.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagnetomotiveForce. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass(self) -> '_1647.Mass':
        """Mass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1647.Mass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Mass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass_per_unit_length(self) -> '_1648.MassPerUnitLength':
        """MassPerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1648.MassPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass_per_unit_time(self) -> '_1649.MassPerUnitTime':
        """MassPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1649.MassPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_moment_of_inertia(self) -> '_1650.MomentOfInertia':
        """MomentOfInertia: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1650.MomentOfInertia.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentOfInertia. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_moment_of_inertia_per_unit_length(self) -> '_1651.MomentOfInertiaPerUnitLength':
        """MomentOfInertiaPerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1651.MomentOfInertiaPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentOfInertiaPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_moment_per_unit_pressure(self) -> '_1652.MomentPerUnitPressure':
        """MomentPerUnitPressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1652.MomentPerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentPerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_number(self) -> '_1653.Number':
        """Number: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1653.Number.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Number. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_percentage(self) -> '_1654.Percentage':
        """Percentage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1654.Percentage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Percentage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power(self) -> '_1655.Power':
        """Power: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1655.Power.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Power. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_per_small_area(self) -> '_1656.PowerPerSmallArea':
        """PowerPerSmallArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1656.PowerPerSmallArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerPerSmallArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_per_unit_time(self) -> '_1657.PowerPerUnitTime':
        """PowerPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1657.PowerPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small(self) -> '_1658.PowerSmall':
        """PowerSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1658.PowerSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_area(self) -> '_1659.PowerSmallPerArea':
        """PowerSmallPerArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1659.PowerSmallPerArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_mass(self) -> '_1660.PowerSmallPerMass':
        """PowerSmallPerMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1660.PowerSmallPerMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1661.PowerSmallPerUnitAreaPerUnitTime':
        """PowerSmallPerUnitAreaPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1661.PowerSmallPerUnitAreaPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_unit_time(self) -> '_1662.PowerSmallPerUnitTime':
        """PowerSmallPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1662.PowerSmallPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_volume(self) -> '_1663.PowerSmallPerVolume':
        """PowerSmallPerVolume: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1663.PowerSmallPerVolume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerVolume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure(self) -> '_1664.Pressure':
        """Pressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1664.Pressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Pressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure_per_unit_time(self) -> '_1665.PressurePerUnitTime':
        """PressurePerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1665.PressurePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressurePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure_velocity_product(self) -> '_1666.PressureVelocityProduct':
        """PressureVelocityProduct: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1666.PressureVelocityProduct.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressureVelocityProduct. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure_viscosity_coefficient(self) -> '_1667.PressureViscosityCoefficient':
        """PressureViscosityCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1667.PressureViscosityCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressureViscosityCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_price(self) -> '_1668.Price':
        """Price: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1668.Price.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Price. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_price_per_unit_mass(self) -> '_1669.PricePerUnitMass':
        """PricePerUnitMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1669.PricePerUnitMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PricePerUnitMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_quadratic_angular_damping(self) -> '_1670.QuadraticAngularDamping':
        """QuadraticAngularDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1670.QuadraticAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to QuadraticAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_quadratic_drag(self) -> '_1671.QuadraticDrag':
        """QuadraticDrag: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1671.QuadraticDrag.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to QuadraticDrag. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rescaled_measurement(self) -> '_1672.RescaledMeasurement':
        """RescaledMeasurement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1672.RescaledMeasurement.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RescaledMeasurement. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rotatum(self) -> '_1673.Rotatum':
        """Rotatum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1673.Rotatum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Rotatum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_safety_factor(self) -> '_1674.SafetyFactor':
        """SafetyFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1674.SafetyFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SafetyFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_specific_acoustic_impedance(self) -> '_1675.SpecificAcousticImpedance':
        """SpecificAcousticImpedance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1675.SpecificAcousticImpedance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpecificAcousticImpedance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_specific_heat(self) -> '_1676.SpecificHeat':
        """SpecificHeat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1676.SpecificHeat.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpecificHeat. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1677.SquareRootOfUnitForcePerUnitArea':
        """SquareRootOfUnitForcePerUnitArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1677.SquareRootOfUnitForcePerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_stiffness_per_unit_face_width(self) -> '_1678.StiffnessPerUnitFaceWidth':
        """StiffnessPerUnitFaceWidth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1678.StiffnessPerUnitFaceWidth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StiffnessPerUnitFaceWidth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_stress(self) -> '_1679.Stress':
        """Stress: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1679.Stress.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Stress. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_temperature(self) -> '_1680.Temperature':
        """Temperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1680.Temperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Temperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_temperature_difference(self) -> '_1681.TemperatureDifference':
        """TemperatureDifference: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1681.TemperatureDifference.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TemperatureDifference. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_temperature_per_unit_time(self) -> '_1682.TemperaturePerUnitTime':
        """TemperaturePerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1682.TemperaturePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TemperaturePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_text(self) -> '_1683.Text':
        """Text: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1683.Text.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Text. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_thermal_contact_coefficient(self) -> '_1684.ThermalContactCoefficient':
        """ThermalContactCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1684.ThermalContactCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermalContactCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_thermal_expansion_coefficient(self) -> '_1685.ThermalExpansionCoefficient':
        """ThermalExpansionCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1685.ThermalExpansionCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermalExpansionCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_thermo_elastic_factor(self) -> '_1686.ThermoElasticFactor':
        """ThermoElasticFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1686.ThermoElasticFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermoElasticFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_time(self) -> '_1687.Time':
        """Time: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1687.Time.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Time. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_time_short(self) -> '_1688.TimeShort':
        """TimeShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1688.TimeShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TimeShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_time_very_short(self) -> '_1689.TimeVeryShort':
        """TimeVeryShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1689.TimeVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TimeVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque(self) -> '_1690.Torque':
        """Torque: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1690.Torque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Torque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_inverse_k(self) -> '_1691.TorqueConverterInverseK':
        """TorqueConverterInverseK: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1691.TorqueConverterInverseK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterInverseK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_k(self) -> '_1692.TorqueConverterK':
        """TorqueConverterK: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1692.TorqueConverterK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_per_current(self) -> '_1693.TorquePerCurrent':
        """TorquePerCurrent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1693.TorquePerCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_per_square_root_of_power(self) -> '_1694.TorquePerSquareRootOfPower':
        """TorquePerSquareRootOfPower: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1694.TorquePerSquareRootOfPower.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerSquareRootOfPower. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_per_unit_temperature(self) -> '_1695.TorquePerUnitTemperature':
        """TorquePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1695.TorquePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_velocity(self) -> '_1696.Velocity':
        """Velocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1696.Velocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Velocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_velocity_small(self) -> '_1697.VelocitySmall':
        """VelocitySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1697.VelocitySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VelocitySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_viscosity(self) -> '_1698.Viscosity':
        """Viscosity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1698.Viscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Viscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_voltage(self) -> '_1699.Voltage':
        """Voltage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1699.Voltage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Voltage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_voltage_per_angular_velocity(self) -> '_1700.VoltagePerAngularVelocity':
        """VoltagePerAngularVelocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1700.VoltagePerAngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VoltagePerAngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_volume(self) -> '_1701.Volume':
        """Volume: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1701.Volume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Volume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_wear_coefficient(self) -> '_1702.WearCoefficient':
        """WearCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1702.WearCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WearCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_yank(self) -> '_1703.Yank':
        """Yank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1703.Yank.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Yank. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1570.MeasurementBase]':
        """List[MeasurementBase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ColumnTitle(_1780.ColumnTitle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ColumnTitle

    A specific implementation of 'ListWithSelectedItem' for 'ColumnTitle' types.
    """
    __qualname__ = 'ColumnTitle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ColumnTitle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1780.ColumnTitle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1780.ColumnTitle.TYPE

    @property
    def selected_value(self) -> '_1780.ColumnTitle':
        """ColumnTitle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1780.ColumnTitle]':
        """List[ColumnTitle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PowerLoad(_2424.PowerLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PowerLoad

    A specific implementation of 'ListWithSelectedItem' for 'PowerLoad' types.
    """
    __qualname__ = 'PowerLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PowerLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2424.PowerLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2424.PowerLoad.TYPE

    @property
    def selected_value(self) -> '_2424.PowerLoad':
        """PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2424.PowerLoad]':
        """List[PowerLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_AbstractPeriodicExcitationDetail(_5615.AbstractPeriodicExcitationDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_AbstractPeriodicExcitationDetail

    A specific implementation of 'ListWithSelectedItem' for 'AbstractPeriodicExcitationDetail' types.
    """
    __qualname__ = 'AbstractPeriodicExcitationDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_AbstractPeriodicExcitationDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5615.AbstractPeriodicExcitationDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5615.AbstractPeriodicExcitationDetail.TYPE

    @property
    def selected_value(self) -> '_5615.AbstractPeriodicExcitationDetail':
        """AbstractPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5615.AbstractPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_periodic_excitation_detail(self) -> '_5668.ElectricMachinePeriodicExcitationDetail':
        """ElectricMachinePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5668.ElectricMachinePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachinePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_x_force_periodic_excitation_detail(self) -> '_5669.ElectricMachineRotorXForcePeriodicExcitationDetail':
        """ElectricMachineRotorXForcePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5669.ElectricMachineRotorXForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorXForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_x_moment_periodic_excitation_detail(self) -> '_5670.ElectricMachineRotorXMomentPeriodicExcitationDetail':
        """ElectricMachineRotorXMomentPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5670.ElectricMachineRotorXMomentPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorXMomentPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_y_force_periodic_excitation_detail(self) -> '_5671.ElectricMachineRotorYForcePeriodicExcitationDetail':
        """ElectricMachineRotorYForcePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5671.ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorYForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_y_moment_periodic_excitation_detail(self) -> '_5672.ElectricMachineRotorYMomentPeriodicExcitationDetail':
        """ElectricMachineRotorYMomentPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5672.ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorYMomentPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_z_force_periodic_excitation_detail(self) -> '_5673.ElectricMachineRotorZForcePeriodicExcitationDetail':
        """ElectricMachineRotorZForcePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5673.ElectricMachineRotorZForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorZForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_axial_loads_excitation_detail(self) -> '_5674.ElectricMachineStatorToothAxialLoadsExcitationDetail':
        """ElectricMachineStatorToothAxialLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5674.ElectricMachineStatorToothAxialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothAxialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_loads_excitation_detail(self) -> '_5675.ElectricMachineStatorToothLoadsExcitationDetail':
        """ElectricMachineStatorToothLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5675.ElectricMachineStatorToothLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_radial_loads_excitation_detail(self) -> '_5676.ElectricMachineStatorToothRadialLoadsExcitationDetail':
        """ElectricMachineStatorToothRadialLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5676.ElectricMachineStatorToothRadialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothRadialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_tangential_loads_excitation_detail(self) -> '_5677.ElectricMachineStatorToothTangentialLoadsExcitationDetail':
        """ElectricMachineStatorToothTangentialLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5677.ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothTangentialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_torque_ripple_periodic_excitation_detail(self) -> '_5678.ElectricMachineTorqueRipplePeriodicExcitationDetail':
        """ElectricMachineTorqueRipplePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5678.ElectricMachineTorqueRipplePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineTorqueRipplePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_excitation_detail(self) -> '_5688.GearMeshExcitationDetail':
        """GearMeshExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5688.GearMeshExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_misalignment_excitation_detail(self) -> '_5690.GearMeshMisalignmentExcitationDetail':
        """GearMeshMisalignmentExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5690.GearMeshMisalignmentExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshMisalignmentExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_te_excitation_detail(self) -> '_5691.GearMeshTEExcitationDetail':
        """GearMeshTEExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5691.GearMeshTEExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshTEExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_general_periodic_excitation_detail(self) -> '_5693.GeneralPeriodicExcitationDetail':
        """GeneralPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5693.GeneralPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GeneralPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_periodic_excitation_with_reference_shaft(self) -> '_5722.PeriodicExcitationWithReferenceShaft':
        """PeriodicExcitationWithReferenceShaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5722.PeriodicExcitationWithReferenceShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PeriodicExcitationWithReferenceShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_single_node_periodic_excitation_with_reference_shaft(self) -> '_5739.SingleNodePeriodicExcitationWithReferenceShaft':
        """SingleNodePeriodicExcitationWithReferenceShaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5739.SingleNodePeriodicExcitationWithReferenceShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SingleNodePeriodicExcitationWithReferenceShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_unbalanced_mass_excitation_detail(self) -> '_5764.UnbalancedMassExcitationDetail':
        """UnbalancedMassExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _5764.UnbalancedMassExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to UnbalancedMassExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5615.AbstractPeriodicExcitationDetail]':
        """List[AbstractPeriodicExcitationDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TupleWithName(TupleWithName, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TupleWithName

    A specific implementation of 'ListWithSelectedItem' for 'TupleWithName' types.
    """
    __qualname__ = 'TupleWithName'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TupleWithName.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TupleWithName.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TupleWithName.TYPE

    @property
    def selected_value(self) -> 'TupleWithName':
        """TupleWithName: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        value = conversion.pn_to_mp_tuple_with_name(temp, (None))
        return constructor.new_from_mastapy_type(TupleWithName)(value) if value is not None else None

    @property
    def available_values(self) -> 'TupleWithName':
        """TupleWithName: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return constructor.new_from_mastapy_type(TupleWithName)(value) if value is not None else None


class ListWithSelectedItem_GearMeshSystemDeflection(_2705.GearMeshSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearMeshSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'GearMeshSystemDeflection' types.
    """
    __qualname__ = 'GearMeshSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearMeshSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2705.GearMeshSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2705.GearMeshSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2705.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2705.GearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_mesh_system_deflection(self) -> '_2640.AGMAGleasonConicalGearMeshSystemDeflection':
        """AGMAGleasonConicalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2640.AGMAGleasonConicalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_gear_mesh_system_deflection(self) -> '_2647.BevelDifferentialGearMeshSystemDeflection':
        """BevelDifferentialGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2647.BevelDifferentialGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear_mesh_system_deflection(self) -> '_2652.BevelGearMeshSystemDeflection':
        """BevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2652.BevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear_mesh_system_deflection(self) -> '_2666.ConceptGearMeshSystemDeflection':
        """ConceptGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2666.ConceptGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear_mesh_system_deflection(self) -> '_2670.ConicalGearMeshSystemDeflection':
        """ConicalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2670.ConicalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_mesh_system_deflection(self) -> '_2685.CylindricalGearMeshSystemDeflection':
        """CylindricalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2685.CylindricalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2686.CylindricalGearMeshSystemDeflectionTimestep':
        """CylindricalGearMeshSystemDeflectionTimestep: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2686.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2687.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        """CylindricalGearMeshSystemDeflectionWithLTCAResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2687.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear_mesh_system_deflection(self) -> '_2700.FaceGearMeshSystemDeflection':
        """FaceGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2700.FaceGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear_mesh_system_deflection(self) -> '_2709.HypoidGearMeshSystemDeflection':
        """HypoidGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2709.HypoidGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self) -> '_2714.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2714.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self) -> '_2717.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2717.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self) -> '_2720.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2720.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear_mesh_system_deflection(self) -> '_2753.SpiralBevelGearMeshSystemDeflection':
        """SpiralBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2753.SpiralBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_mesh_system_deflection(self) -> '_2759.StraightBevelDiffGearMeshSystemDeflection':
        """StraightBevelDiffGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2759.StraightBevelDiffGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear_mesh_system_deflection(self) -> '_2762.StraightBevelGearMeshSystemDeflection':
        """StraightBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2762.StraightBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear_mesh_system_deflection(self) -> '_2782.WormGearMeshSystemDeflection':
        """WormGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2782.WormGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear_mesh_system_deflection(self) -> '_2785.ZerolBevelGearMeshSystemDeflection':
        """ZerolBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2785.ZerolBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2705.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSet(_2483.GearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSet

    A specific implementation of 'ListWithSelectedItem' for 'GearSet' types.
    """
    __qualname__ = 'GearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2483.GearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2483.GearSet.TYPE

    @property
    def selected_value(self) -> '_2483.GearSet':
        """GearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2483.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_set(self) -> '_2465.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2465.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_gear_set(self) -> '_2467.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2467.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear_set(self) -> '_2471.BevelGearSet':
        """BevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2471.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear_set(self) -> '_2473.ConceptGearSet':
        """ConceptGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2473.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear_set(self) -> '_2475.ConicalGearSet':
        """ConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2475.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_set(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear_set(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2480.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear_set(self) -> '_2486.HypoidGearSet':
        """HypoidGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2486.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2488.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2488.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planetary_gear_set(self) -> '_2493.PlanetaryGearSet':
        """PlanetaryGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2493.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear_set(self) -> '_2495.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2495.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_set(self) -> '_2497.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2497.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear_set(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2499.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear_set(self) -> '_2503.WormGearSet':
        """WormGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2503.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear_set(self) -> '_2505.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2505.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2483.GearSet]':
        """List[GearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructureNode(_2336.FESubstructureNode, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructureNode

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructureNode' types.
    """
    __qualname__ = 'FESubstructureNode'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructureNode.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2336.FESubstructureNode.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2336.FESubstructureNode.TYPE

    @property
    def selected_value(self) -> '_2336.FESubstructureNode':
        """FESubstructureNode: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2336.FESubstructureNode]':
        """List[FESubstructureNode]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Component(_2396.Component, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Component

    A specific implementation of 'ListWithSelectedItem' for 'Component' types.
    """
    __qualname__ = 'Component'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Component.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2396.Component.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2396.Component.TYPE

    @property
    def selected_value(self) -> '_2396.Component':
        """Component: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2396.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_abstract_shaft(self) -> '_2388.AbstractShaft':
        """AbstractShaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2388.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_abstract_shaft_or_housing(self) -> '_2389.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2389.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bearing(self) -> '_2392.Bearing':
        """Bearing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2392.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bolt(self) -> '_2394.Bolt':
        """Bolt: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2394.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_connector(self) -> '_2399.Connector':
        """Connector: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2399.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_datum(self) -> '_2400.Datum':
        """Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2400.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_external_cad_model(self) -> '_2404.ExternalCADModel':
        """ExternalCADModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2404.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fe_part(self) -> '_2405.FEPart':
        """FEPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2405.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_guide_dxf_model(self) -> '_2407.GuideDxfModel':
        """GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2407.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass_disc(self) -> '_2414.MassDisc':
        """MassDisc: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2414.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_measurement_component(self) -> '_2415.MeasurementComponent':
        """MeasurementComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2415.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mountable_component(self) -> '_2416.MountableComponent':
        """MountableComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2416.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_oil_seal(self) -> '_2418.OilSeal':
        """OilSeal: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2418.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planet_carrier(self) -> '_2421.PlanetCarrier':
        """PlanetCarrier: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2421.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_point_load(self) -> '_2423.PointLoad':
        """PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2423.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_load(self) -> '_2424.PowerLoad':
        """PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2424.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_unbalanced_mass(self) -> '_2429.UnbalancedMass':
        """UnbalancedMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2429.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_virtual_component(self) -> '_2431.VirtualComponent':
        """VirtualComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2431.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_shaft(self) -> '_2434.Shaft':
        """Shaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2434.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear(self) -> '_2464.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2464.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_gear(self) -> '_2466.BevelDifferentialGear':
        """BevelDifferentialGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2466.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_planet_gear(self) -> '_2468.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2468.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_sun_gear(self) -> '_2469.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2469.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear(self) -> '_2470.BevelGear':
        """BevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2470.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear(self) -> '_2472.ConceptGear':
        """ConceptGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2472.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear(self) -> '_2474.ConicalGear':
        """ConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2474.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_planet_gear(self) -> '_2478.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2478.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear(self) -> '_2479.FaceGear':
        """FaceGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2479.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear(self) -> '_2481.Gear':
        """Gear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2481.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear(self) -> '_2485.HypoidGear':
        """HypoidGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2485.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2487.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2487.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2489.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2489.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2491.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear(self) -> '_2494.SpiralBevelGear':
        """SpiralBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2494.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear(self) -> '_2496.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2496.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear(self) -> '_2498.StraightBevelGear':
        """StraightBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2498.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_planet_gear(self) -> '_2500.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2500.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_sun_gear(self) -> '_2501.StraightBevelSunGear':
        """StraightBevelSunGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2501.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear(self) -> '_2502.WormGear':
        """WormGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2502.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear(self) -> '_2504.ZerolBevelGear':
        """ZerolBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2504.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cycloidal_disc(self) -> '_2520.CycloidalDisc':
        """CycloidalDisc: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2520.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_ring_pins(self) -> '_2521.RingPins':
        """RingPins: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2521.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_clutch_half(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2530.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_coupling_half(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2533.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_coupling_half(self) -> '_2535.CouplingHalf':
        """CouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2535.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cvt_pulley(self) -> '_2538.CVTPulley':
        """CVTPulley: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2538.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_part_to_part_shear_coupling_half(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2540.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pulley(self) -> '_2541.Pulley':
        """Pulley: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rolling_ring(self) -> '_2547.RollingRing':
        """RollingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2547.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_shaft_hub_connection(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2549.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spring_damper_half(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2552.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchroniser_half(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2555.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchroniser_part(self) -> '_2556.SynchroniserPart':
        """SynchroniserPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2556.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchroniser_sleeve(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2557.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_pump(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2559.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_turbine(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2561.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2396.Component]':
        """List[Component]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Datum(_2400.Datum, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Datum

    A specific implementation of 'ListWithSelectedItem' for 'Datum' types.
    """
    __qualname__ = 'Datum'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Datum.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2400.Datum.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2400.Datum.TYPE

    @property
    def selected_value(self) -> '_2400.Datum':
        """Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2400.Datum]':
        """List[Datum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FELink(_2369.FELink, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FELink

    A specific implementation of 'ListWithSelectedItem' for 'FELink' types.
    """
    __qualname__ = 'FELink'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FELink.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2369.FELink.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2369.FELink.TYPE

    @property
    def selected_value(self) -> '_2369.FELink':
        """FELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2369.FELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_fe_link(self) -> '_2370.ElectricMachineStatorFELink':
        """ElectricMachineStatorFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2370.ElectricMachineStatorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_fe_link(self) -> '_2372.GearMeshFELink':
        """GearMeshFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2372.GearMeshFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_with_duplicated_meshes_fe_link(self) -> '_2373.GearWithDuplicatedMeshesFELink':
        """GearWithDuplicatedMeshesFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2373.GearWithDuplicatedMeshesFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearWithDuplicatedMeshesFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_multi_angle_connection_fe_link(self) -> '_2374.MultiAngleConnectionFELink':
        """MultiAngleConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2374.MultiAngleConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiAngleConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_multi_node_connector_fe_link(self) -> '_2375.MultiNodeConnectorFELink':
        """MultiNodeConnectorFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2375.MultiNodeConnectorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiNodeConnectorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_multi_node_fe_link(self) -> '_2376.MultiNodeFELink':
        """MultiNodeFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2376.MultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planetary_connector_multi_node_fe_link(self) -> '_2377.PlanetaryConnectorMultiNodeFELink':
        """PlanetaryConnectorMultiNodeFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2377.PlanetaryConnectorMultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetaryConnectorMultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planet_based_fe_link(self) -> '_2378.PlanetBasedFELink':
        """PlanetBasedFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2378.PlanetBasedFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetBasedFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planet_carrier_fe_link(self) -> '_2379.PlanetCarrierFELink':
        """PlanetCarrierFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2379.PlanetCarrierFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetCarrierFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_point_load_fe_link(self) -> '_2380.PointLoadFELink':
        """PointLoadFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2380.PointLoadFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PointLoadFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rolling_ring_connection_fe_link(self) -> '_2381.RollingRingConnectionFELink':
        """RollingRingConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2381.RollingRingConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RollingRingConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_shaft_hub_connection_fe_link(self) -> '_2382.ShaftHubConnectionFELink':
        """ShaftHubConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2382.ShaftHubConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ShaftHubConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_single_node_fe_link(self) -> '_2383.SingleNodeFELink':
        """SingleNodeFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2383.SingleNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SingleNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2369.FELink]':
        """List[FELink]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructure(_2334.FESubstructure, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructure

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructure' types.
    """
    __qualname__ = 'FESubstructure'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructure.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2334.FESubstructure.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2334.FESubstructure.TYPE

    @property
    def selected_value(self) -> '_2334.FESubstructure':
        """FESubstructure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2334.FESubstructure]':
        """List[FESubstructure]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGear(_2476.CylindricalGear, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGear

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGear' types.
    """
    __qualname__ = 'CylindricalGear'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGear.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2476.CylindricalGear.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2476.CylindricalGear.TYPE

    @property
    def selected_value(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2476.CylindricalGear]':
        """List[CylindricalGear]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDetail(_1249.ElectricMachineDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDetail

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDetail' types.
    """
    __qualname__ = 'ElectricMachineDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1249.ElectricMachineDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1249.ElectricMachineDetail.TYPE

    @property
    def selected_value(self) -> '_1249.ElectricMachineDetail':
        """ElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1249.ElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cad_electric_machine_detail(self) -> '_1235.CADElectricMachineDetail':
        """CADElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1235.CADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_interior_permanent_magnet_machine(self) -> '_1259.InteriorPermanentMagnetMachine':
        """InteriorPermanentMagnetMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1259.InteriorPermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InteriorPermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_non_cad_electric_machine_detail(self) -> '_1267.NonCADElectricMachineDetail':
        """NonCADElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1267.NonCADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to NonCADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_permanent_magnet_assisted_synchronous_reluctance_machine(self) -> '_1270.PermanentMagnetAssistedSynchronousReluctanceMachine':
        """PermanentMagnetAssistedSynchronousReluctanceMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1270.PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PermanentMagnetAssistedSynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_surface_permanent_magnet_machine(self) -> '_1283.SurfacePermanentMagnetMachine':
        """SurfacePermanentMagnetMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1283.SurfacePermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SurfacePermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchronous_reluctance_machine(self) -> '_1285.SynchronousReluctanceMachine':
        """SynchronousReluctanceMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1285.SynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1249.ElectricMachineDetail]':
        """List[ElectricMachineDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GuideDxfModel(_2407.GuideDxfModel, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GuideDxfModel

    A specific implementation of 'ListWithSelectedItem' for 'GuideDxfModel' types.
    """
    __qualname__ = 'GuideDxfModel'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GuideDxfModel.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2407.GuideDxfModel.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2407.GuideDxfModel.TYPE

    @property
    def selected_value(self) -> '_2407.GuideDxfModel':
        """GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2407.GuideDxfModel]':
        """List[GuideDxfModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConcentricPartGroup(_2439.ConcentricPartGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConcentricPartGroup

    A specific implementation of 'ListWithSelectedItem' for 'ConcentricPartGroup' types.
    """
    __qualname__ = 'ConcentricPartGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConcentricPartGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2439.ConcentricPartGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2439.ConcentricPartGroup.TYPE

    @property
    def selected_value(self) -> '_2439.ConcentricPartGroup':
        """ConcentricPartGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2439.ConcentricPartGroup]':
        """List[ConcentricPartGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSet(_2477.CylindricalGearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSet

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSet' types.
    """
    __qualname__ = 'CylindricalGearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2477.CylindricalGearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2477.CylindricalGearSet.TYPE

    @property
    def selected_value(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2477.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSetDesign(_943.GearSetDesign, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSetDesign

    A specific implementation of 'ListWithSelectedItem' for 'GearSetDesign' types.
    """
    __qualname__ = 'GearSetDesign'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSetDesign.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_943.GearSetDesign.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _943.GearSetDesign.TYPE

    @property
    def selected_value(self) -> '_943.GearSetDesign':
        """GearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _943.GearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear_set_design(self) -> '_947.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _947.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear_set_design(self) -> '_952.WormGearSetDesign':
        """WormGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _952.WormGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear_set_design(self) -> '_956.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _956.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_set_design(self) -> '_960.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _960.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear_set_design(self) -> '_964.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _964.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_972.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _972.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_conical_gear_set_design(self) -> '_976.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _976.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear_set_design(self) -> '_980.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _980.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear_set_design(self) -> '_988.FaceGearSetDesign':
        """FaceGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _988.FaceGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_set_design(self) -> '_1021.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1021.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_planetary_gear_set_design(self) -> '_1033.CylindricalPlanetaryGearSetDesign':
        """CylindricalPlanetaryGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1033.CylindricalPlanetaryGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear_set_design(self) -> '_1146.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1146.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear_set_design(self) -> '_1168.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1168.ConceptGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear_set_design(self) -> '_1172.BevelGearSetDesign':
        """BevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1172.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_set_design(self) -> '_1185.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _1185.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_943.GearSetDesign]':
        """List[GearSetDesign]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ShaftHubConnection(_2549.ShaftHubConnection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ShaftHubConnection

    A specific implementation of 'ListWithSelectedItem' for 'ShaftHubConnection' types.
    """
    __qualname__ = 'ShaftHubConnection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ShaftHubConnection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2549.ShaftHubConnection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2549.ShaftHubConnection.TYPE

    @property
    def selected_value(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2549.ShaftHubConnection]':
        """List[ShaftHubConnection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TSelectableItem(Generic[TSelectableItem], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TSelectableItem

    A specific implementation of 'ListWithSelectedItem' for 'TSelectableItem' types.
    """
    __qualname__ = 'TSelectableItem'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TSelectableItem.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TSelectableItem':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TSelectableItem

    @property
    def selected_value(self) -> 'TSelectableItem':
        """TSelectableItem: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TSelectableItem]':
        """List[TSelectableItem]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSystemDeflection(_2691.CylindricalGearSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSystemDeflection' types.
    """
    __qualname__ = 'CylindricalGearSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2691.CylindricalGearSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2691.CylindricalGearSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2691.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2691.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2692.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2692.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2693.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2693.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2696.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _2696.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2691.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DesignState(_5599.DesignState, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DesignState

    A specific implementation of 'ListWithSelectedItem' for 'DesignState' types.
    """
    __qualname__ = 'DesignState'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DesignState.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5599.DesignState.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5599.DesignState.TYPE

    @property
    def selected_value(self) -> '_5599.DesignState':
        """DesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5599.DesignState]':
        """List[DesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FEPart(_2405.FEPart, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FEPart

    A specific implementation of 'ListWithSelectedItem' for 'FEPart' types.
    """
    __qualname__ = 'FEPart'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FEPart.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2405.FEPart.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2405.FEPart.TYPE

    @property
    def selected_value(self) -> '_2405.FEPart':
        """FEPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2405.FEPart]':
        """List[FEPart]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TPartAnalysis(Generic[TPartAnalysis], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TPartAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'TPartAnalysis' types.
    """
    __qualname__ = 'TPartAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TPartAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TPartAnalysis':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TPartAnalysis

    @property
    def selected_value(self) -> 'TPartAnalysis':
        """TPartAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TPartAnalysis]':
        """List[TPartAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CMSElementFaceGroup(_219.CMSElementFaceGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CMSElementFaceGroup

    A specific implementation of 'ListWithSelectedItem' for 'CMSElementFaceGroup' types.
    """
    __qualname__ = 'CMSElementFaceGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CMSElementFaceGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_219.CMSElementFaceGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _219.CMSElementFaceGroup.TYPE

    @property
    def selected_value(self) -> '_219.CMSElementFaceGroup':
        """CMSElementFaceGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _219.CMSElementFaceGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CMSElementFaceGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_219.CMSElementFaceGroup]':
        """List[CMSElementFaceGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ResultLocationSelectionGroup(_5780.ResultLocationSelectionGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ResultLocationSelectionGroup

    A specific implementation of 'ListWithSelectedItem' for 'ResultLocationSelectionGroup' types.
    """
    __qualname__ = 'ResultLocationSelectionGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ResultLocationSelectionGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5780.ResultLocationSelectionGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5780.ResultLocationSelectionGroup.TYPE

    @property
    def selected_value(self) -> '_5780.ResultLocationSelectionGroup':
        """ResultLocationSelectionGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5780.ResultLocationSelectionGroup]':
        """List[ResultLocationSelectionGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_StaticLoadCase(_6731.StaticLoadCase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_StaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'StaticLoadCase' types.
    """
    __qualname__ = 'StaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_StaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_6731.StaticLoadCase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6731.StaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_6731.StaticLoadCase':
        """StaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        if _6731.StaticLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StaticLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_6731.StaticLoadCase]':
        """List[StaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DutyCycle(_5600.DutyCycle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DutyCycle

    A specific implementation of 'ListWithSelectedItem' for 'DutyCycle' types.
    """
    __qualname__ = 'DutyCycle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DutyCycle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5600.DutyCycle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5600.DutyCycle.TYPE

    @property
    def selected_value(self) -> '_5600.DutyCycle':
        """DutyCycle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5600.DutyCycle]':
        """List[DutyCycle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDataSet(_2325.ElectricMachineDataSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDataSet

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDataSet' types.
    """
    __qualname__ = 'ElectricMachineDataSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDataSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2325.ElectricMachineDataSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2325.ElectricMachineDataSet.TYPE

    @property
    def selected_value(self) -> '_2325.ElectricMachineDataSet':
        """ElectricMachineDataSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2325.ElectricMachineDataSet]':
        """List[ElectricMachineDataSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PointLoad(_2423.PointLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PointLoad

    A specific implementation of 'ListWithSelectedItem' for 'PointLoad' types.
    """
    __qualname__ = 'PointLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PointLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2423.PointLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2423.PointLoad.TYPE

    @property
    def selected_value(self) -> '_2423.PointLoad':
        """PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2423.PointLoad]':
        """List[PointLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
