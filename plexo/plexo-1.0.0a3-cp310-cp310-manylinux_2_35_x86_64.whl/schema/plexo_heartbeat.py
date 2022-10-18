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
__capnpy_id__ = 0x99587877bc520e62
__capnpy_version__ = '0.9.0'
__capnproto_version__ = '0.9.1'
_check_version(__name__, __capnpy_version__)
from capnpy.schema import CodeGeneratorRequest as _CodeGeneratorRequest
from capnpy.annotate import Options as _Options
from capnpy.reflection import ReflectionData as _ReflectionData
class _plexo_heartbeat_ReflectionData(_ReflectionData):
    request = _CodeGeneratorRequest.from_buffer(_Segment(b"\x00\x00\x00\x00\x00\x00\x04\x00\x11\x00\x00\x00\xb7\x00\x00\x00\x19\x01\x00\x00\x1f\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\xed\x00\x00\x007\x00\x00\x00\x00\x00\t\x01\x00\x00\x00\x00\x08\x00\x00\x00\x05\x00\x06\x00b\x0eR\xbcwxX\x99!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x00\x00\x00:\x01\x00\x00Q\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6D\t\x83\x91\rL\xca'\x00\x00\x00\x01\x00\x01\x00b\x0eR\xbcwxX\x99\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\xb2\x01\x00\x00U\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Q\x00\x00\x00?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00src/plexo/schema/plexo_heartbeat.capnp\x00\x00\x04\x00\x00\x00\x01\x00\x01\x00\xa6D\t\x83\x91\rL\xca\x01\x00\x00\x00z\x00\x00\x00PlexoHeartbeat\x00\x00src/plexo/schema/plexo_heartbeat.capnp:PlexoHeartbeat\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x04\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x01\x00\x18\x00\x00\x00\x02\x00\x01\x00instanceId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x01\x00\x02\x00\xa6D\t\x83\x91\rL\xca\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x0f\x00\x00\x00b\x0eR\xbcwxX\x99\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x02\x00b\x0eR\xbcwxX\x99\x05\x00\x00\x00:\x01\x00\x00\x15\x00\x00\x00\x07\x00\x00\x00src/plexo/schema/plexo_heartbeat.capnp\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00"), 8, 0, 4)
    default_options = _Options.from_buffer(_Segment(b'\x03\x00\x03\x00\x01\x00\x03\x00'), 0, 1, 0)
    pyx = False
_reflection_data = _plexo_heartbeat_ReflectionData()

#### FORWARD DECLARATIONS ####

class PlexoHeartbeat(_Struct): pass
PlexoHeartbeat.__name__ = 'PlexoHeartbeat'


#### DEFINITIONS ####

@PlexoHeartbeat.__extend__
class PlexoHeartbeat(_Struct):
    __capnpy_id__ = 0xca4c0d91830944a6
    __static_data_size__ = 1
    __static_ptrs_size__ = 0
    
    
    @property
    def instance_id(self):
        # no union check
        value = self._read_primitive(0, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @staticmethod
    def __new(instance_id=0):
        builder = _SegmentBuilder()
        pos = builder.allocate(8)
        builder.write_uint64(pos + 0, instance_id)
        return builder.as_string()
    
    def __init__(self, instance_id=0):
        _buf = PlexoHeartbeat.__new(instance_id)
        self._init_from_buffer(_buf, 0, 1, 0)
    
    def shortrepr(self):
        parts = []
        parts.append("instanceId = %s" % self.instance_id)
        return "(%s)" % ", ".join(parts)

_PlexoHeartbeat_list_item_type = _StructItemType(PlexoHeartbeat)


_extend_module_maybe(globals(), modname=__name__)