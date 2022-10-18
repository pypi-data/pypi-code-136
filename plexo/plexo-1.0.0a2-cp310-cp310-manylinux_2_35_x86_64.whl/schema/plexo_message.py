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
__capnpy_id__ = 0xeed5242d4faed181
__capnpy_version__ = '0.9.0'
__capnproto_version__ = '0.9.1'
_check_version(__name__, __capnpy_version__)
from capnpy.schema import CodeGeneratorRequest as _CodeGeneratorRequest
from capnpy.annotate import Options as _Options
from capnpy.reflection import ReflectionData as _ReflectionData
class _plexo_message_ReflectionData(_ReflectionData):
    request = _CodeGeneratorRequest.from_buffer(_Segment(b'\x00\x00\x00\x00\x00\x00\x04\x00\x11\x00\x00\x00\xb7\x00\x00\x00Y\x01\x00\x00\x1f\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00)\x01\x00\x007\x00\x00\x00\x00\x00\t\x01\x00\x00\x00\x00\x08\x00\x00\x00\x05\x00\x06\x00\x81\xd1\xaeO-$\xd5\xee\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x00\x00\x00*\x01\x00\x00Q\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00N\xc6p\xd8\x90 C\x83%\x00\x00\x00\x01\x00\x00\x00\x81\xd1\xaeO-$\xd5\xee\x02\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\x92\x01\x00\x00U\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Q\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00src/plexo/schema/plexo_message.capnp\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x01\x00N\xc6p\xd8\x90 C\x83\x01\x00\x00\x00j\x00\x00\x00PlexoMessage\x00\x00\x00\x00src/plexo/schema/plexo_message.capnp:PlexoMessage\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x08\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00)\x00\x00\x00J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x03\x00\x01\x004\x00\x00\x00\x02\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001\x00\x00\x00B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x03\x00\x01\x008\x00\x00\x00\x02\x00\x01\x00typeName\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00payload\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x01\x00\x02\x00N\xc6p\xd8\x90 C\x83\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x17\x00\x00\x00\x81\xd1\xaeO-$\xd5\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x02\x00\x81\xd1\xaeO-$\xd5\xee\x05\x00\x00\x00*\x01\x00\x00\x15\x00\x00\x00\x07\x00\x00\x00src/plexo/schema/plexo_message.capnp\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00'), 8, 0, 4)
    default_options = _Options.from_buffer(_Segment(b'\x03\x00\x03\x00\x01\x00\x03\x00'), 0, 1, 0)
    pyx = False
_reflection_data = _plexo_message_ReflectionData()

#### FORWARD DECLARATIONS ####

class PlexoMessage(_Struct): pass
PlexoMessage.__name__ = 'PlexoMessage'


#### DEFINITIONS ####

@PlexoMessage.__extend__
class PlexoMessage(_Struct):
    __capnpy_id__ = 0x83432090d870c64e
    __static_data_size__ = 0
    __static_ptrs_size__ = 2
    
    
    @property
    def type_name(self):
        # no union check
        return self._read_text_bytes(0)
    
    def get_type_name(self):
        return self._read_text_bytes(0, default_=b"")
    
    def has_type_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def payload(self):
        # no union check
        return self._read_data(8)
    
    def get_payload(self):
        return self._read_data(8, default_=b"")
    
    def has_payload(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @staticmethod
    def __new(type_name=None, payload=None):
        builder = _SegmentBuilder()
        pos = builder.allocate(16)
        builder.alloc_text(pos + 0, type_name)
        builder.alloc_data(pos + 8, payload)
        return builder.as_string()
    
    def __init__(self, type_name=None, payload=None):
        _buf = PlexoMessage.__new(type_name, payload)
        self._init_from_buffer(_buf, 0, 0, 2)
    
    def shortrepr(self):
        parts = []
        if self.has_type_name(): parts.append("typeName = %s" % _text_bytes_repr(self.get_type_name()))
        if self.has_payload(): parts.append("payload = %s" % _data_repr(self.get_payload()))
        return "(%s)" % ", ".join(parts)

_PlexoMessage_list_item_type = _StructItemType(PlexoMessage)


_extend_module_maybe(globals(), modname=__name__)