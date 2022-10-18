# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2022-10-17 22:48
# cython: language_level=2

from capnpy import ptr as _ptr
from capnpy.struct_ import Struct as _Struct
from capnpy.struct_ import check_tag as _check_tag
from capnpy.struct_ import undefined as _undefined
from capnpy.enum import enum as _enum, fill_enum as _fill_enum
from capnpy.enum import BaseEnum as _BaseEnum
from capnpy.type import Types as _Types
from capnpy.segment.segment import Segment as _Segment
from capnpy.segment.segment import MultiSegment as _MultiSegment
from capnpy.segment.builder import SegmentBuilder as _SegmentBuilder
from capnpy.list import List as _List
from capnpy.list import PrimitiveItemType as _PrimitiveItemType
from capnpy.list import BoolItemType as _BoolItemType
from capnpy.list import TextItemType as _TextItemType
from capnpy.list import TextUnicodeItemType as _TextUnicodeItemType
from capnpy.list import StructItemType as _StructItemType
from capnpy.list import EnumItemType as _EnumItemType
from capnpy.list import VoidItemType as _VoidItemType
from capnpy.list import ListItemType as _ListItemType
from capnpy.anypointer import AnyPointer as _AnyPointer
from capnpy.util import text_bytes_repr as _text_bytes_repr
from capnpy.util import text_unicode_repr as _text_unicode_repr
from capnpy.util import data_repr as _data_repr
from capnpy.util import float32_repr as _float32_repr
from capnpy.util import float64_repr as _float64_repr
from capnpy.util import extend_module_maybe as _extend_module_maybe
from capnpy.util import check_version as _check_version
from capnpy.util import encode_maybe as _encode_maybe
__capnpy_id__ = 0xa2849a07964d7b1b
__capnpy_version__ = '0.9.0'
__capnproto_version__ = '0.9.1'
_check_version(__name__, __capnpy_version__)
from capnpy.schema import CodeGeneratorRequest as _CodeGeneratorRequest
from capnpy.annotate import Options as _Options
from capnpy.reflection import ReflectionData as _ReflectionData
class _plexo_rejection_ReflectionData(_ReflectionData):
    request = _CodeGeneratorRequest.from_buffer(_Segment(b"\x00\x00\x00\x00\x00\x00\x04\x00\x11\x00\x00\x00\xb7\x00\x00\x00\xa1\x01\x00\x00\x1f\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00m\x01\x00\x007\x00\x00\x00\x00\x00\t\x01\x00\x00\x00\x00\x08\x00\x00\x00\x05\x00\x06\x00\x1b{M\x96\x07\x9a\x84\xa2!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x00\x00\x00:\x01\x00\x00Q\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x99^@g\xb5\x9c\xf6'\x00\x00\x00\x01\x00\x02\x00\x1b{M\x96\x07\x9a\x84\xa2\x01\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\xb2\x01\x00\x00U\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Q\x00\x00\x00\xaf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00src/plexo/schema/plexo_rejection.capnp\x00\x00\x04\x00\x00\x00\x01\x00\x01\x00\x90\x99^@g\xb5\x9c\xf6\x01\x00\x00\x00z\x00\x00\x00PlexoRejection\x00\x00src/plexo/schema/plexo_rejection.capnp:PlexoRejection\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x0c\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00E\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x00\x00\x03\x00\x01\x00P\x00\x00\x00\x02\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00\x03\x00\x01\x00X\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T\x00\x00\x00\x03\x00\x01\x00`\x00\x00\x00\x02\x00\x01\x00instanceId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00proposalId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00typeName\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x01\x00\x02\x00\x90\x99^@g\xb5\x9c\xf6\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x1f\x00\x00\x00\x1b{M\x96\x07\x9a\x84\xa2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x02\x00\x1b{M\x96\x07\x9a\x84\xa2\x05\x00\x00\x00:\x01\x00\x00\x15\x00\x00\x00\x07\x00\x00\x00src/plexo/schema/plexo_rejection.capnp\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00"), 8, 0, 4)
    default_options = _Options.from_buffer(_Segment(b'\x03\x00\x03\x00\x01\x00\x03\x00'), 0, 1, 0)
    pyx = False
_reflection_data = _plexo_rejection_ReflectionData()

#### FORWARD DECLARATIONS ####

class PlexoRejection(_Struct): pass
PlexoRejection.__name__ = 'PlexoRejection'


#### DEFINITIONS ####

@PlexoRejection.__extend__
class PlexoRejection(_Struct):
    __capnpy_id__ = 0xf69cb567405e9990
    __static_data_size__ = 2
    __static_ptrs_size__ = 1
    
    
    @property
    def instance_id(self):
        # no union check
        value = self._read_primitive(0, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def proposal_id(self):
        # no union check
        value = self._read_primitive(8, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def type_name(self):
        # no union check
        return self._read_text_bytes(0)
    
    def get_type_name(self):
        return self._read_text_bytes(0, default_=b"")
    
    def has_type_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(instance_id=0, proposal_id=0, type_name=None):
        builder = _SegmentBuilder()
        pos = builder.allocate(24)
        builder.write_uint64(pos + 0, instance_id)
        builder.write_uint64(pos + 8, proposal_id)
        builder.alloc_text(pos + 16, type_name)
        return builder.as_string()
    
    def __init__(self, instance_id=0, proposal_id=0, type_name=None):
        _buf = PlexoRejection.__new(instance_id, proposal_id, type_name)
        self._init_from_buffer(_buf, 0, 2, 1)
    
    def shortrepr(self):
        parts = []
        parts.append("instanceId = %s" % self.instance_id)
        parts.append("proposalId = %s" % self.proposal_id)
        if self.has_type_name(): parts.append("typeName = %s" % _text_bytes_repr(self.get_type_name()))
        return "(%s)" % ", ".join(parts)

_PlexoRejection_list_item_type = _StructItemType(PlexoRejection)


_extend_module_maybe(globals(), modname=__name__)