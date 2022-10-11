# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sarus_data_spec/protobuf/attribute.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sarus_data_spec/protobuf/attribute.proto',
  package='sarus_data_spec',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(sarus_data_spec/protobuf/attribute.proto\x12\x0fsarus_data_spec\"\x9c\x01\n\tAttribute\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12>\n\nproperties\x18\x03 \x03(\x0b\x32*.sarus_data_spec.Attribute.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)




_ATTRIBUTE_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='sarus_data_spec.Attribute.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='sarus_data_spec.Attribute.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='sarus_data_spec.Attribute.PropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=218,
)

_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='sarus_data_spec.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='sarus_data_spec.Attribute.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object', full_name='sarus_data_spec.Attribute.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='sarus_data_spec.Attribute.properties', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTE_PROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=218,
)

_ATTRIBUTE_PROPERTIESENTRY.containing_type = _ATTRIBUTE
_ATTRIBUTE.fields_by_name['properties'].message_type = _ATTRIBUTE_PROPERTIESENTRY
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _ATTRIBUTE_PROPERTIESENTRY,
    '__module__' : 'sarus_data_spec.protobuf.attribute_pb2'
    # @@protoc_insertion_point(class_scope:sarus_data_spec.Attribute.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _ATTRIBUTE,
  '__module__' : 'sarus_data_spec.protobuf.attribute_pb2'
  # @@protoc_insertion_point(class_scope:sarus_data_spec.Attribute)
  })
_sym_db.RegisterMessage(Attribute)
_sym_db.RegisterMessage(Attribute.PropertiesEntry)


_ATTRIBUTE_PROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
