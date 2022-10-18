"""_627.py

MicroGeometryInputsLead
"""


from mastapy.math_utility import _1453
from mastapy._internal import constructor
from mastapy.math_utility.measured_ranges import _1529
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical import _626, _625
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS_LEAD = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'MicroGeometryInputsLead')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryInputsLead',)


class MicroGeometryInputsLead(_626.MicroGeometryInputs['_625.LeadModificationSegment']):
    """MicroGeometryInputsLead

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_INPUTS_LEAD

    def __init__(self, instance_to_wrap: 'MicroGeometryInputsLead.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_micro_geometry_range(self) -> '_1453.Range':
        """Range: 'LeadMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadMicroGeometryRange

        if temp is None:
            return None

        if _1453.Range.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast lead_micro_geometry_range to Range. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_lead_segments(self) -> 'int':
        """int: 'NumberOfLeadSegments' is the original name of this property."""

        temp = self.wrapped.NumberOfLeadSegments

        if temp is None:
            return 0

        return temp

    @number_of_lead_segments.setter
    def number_of_lead_segments(self, value: 'int'):
        self.wrapped.NumberOfLeadSegments = int(value) if value else 0
