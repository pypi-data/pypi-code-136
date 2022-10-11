# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sarus_data_spec/protobuf/constraint.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sarus_data_spec/protobuf/constraint.proto',
  package='sarus_data_spec',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)sarus_data_spec/protobuf/constraint.proto\x12\x0fsarus_data_spec\"\x82\x02\n\x11VariantConstraint\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61taspec\x18\x02 \x01(\t\x12\x38\n\x0f\x63onstraint_kind\x18\x03 \x01(\x0e\x32\x1f.sarus_data_spec.ConstraintKind\x12\x18\n\x10required_context\x18\x04 \x03(\t\x12\x46\n\nproperties\x18\x05 \x03(\x0b\x32\x32.sarus_data_spec.VariantConstraint.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*<\n\x0e\x43onstraintKind\x12\r\n\tSYNTHETIC\x10\x00\x12\x06\n\x02\x44P\x10\x01\x12\n\n\x06PUBLIC\x10\x02\x12\x07\n\x03PEP\x10\x03\x62\x06proto3'
)

_CONSTRAINTKIND = _descriptor.EnumDescriptor(
  name='ConstraintKind',
  full_name='sarus_data_spec.ConstraintKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYNTHETIC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUBLIC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=323,
  serialized_end=383,
)
_sym_db.RegisterEnumDescriptor(_CONSTRAINTKIND)

ConstraintKind = enum_type_wrapper.EnumTypeWrapper(_CONSTRAINTKIND)
SYNTHETIC = 0
DP = 1
PUBLIC = 2
PEP = 3



_VARIANTCONSTRAINT_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='sarus_data_spec.VariantConstraint.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='sarus_data_spec.VariantConstraint.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='sarus_data_spec.VariantConstraint.PropertiesEntry.value', index=1,
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
  serialized_start=272,
  serialized_end=321,
)

_VARIANTCONSTRAINT = _descriptor.Descriptor(
  name='VariantConstraint',
  full_name='sarus_data_spec.VariantConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='sarus_data_spec.VariantConstraint.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataspec', full_name='sarus_data_spec.VariantConstraint.dataspec', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraint_kind', full_name='sarus_data_spec.VariantConstraint.constraint_kind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='required_context', full_name='sarus_data_spec.VariantConstraint.required_context', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='sarus_data_spec.VariantConstraint.properties', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VARIANTCONSTRAINT_PROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=321,
)

_VARIANTCONSTRAINT_PROPERTIESENTRY.containing_type = _VARIANTCONSTRAINT
_VARIANTCONSTRAINT.fields_by_name['constraint_kind'].enum_type = _CONSTRAINTKIND
_VARIANTCONSTRAINT.fields_by_name['properties'].message_type = _VARIANTCONSTRAINT_PROPERTIESENTRY
DESCRIPTOR.message_types_by_name['VariantConstraint'] = _VARIANTCONSTRAINT
DESCRIPTOR.enum_types_by_name['ConstraintKind'] = _CONSTRAINTKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VariantConstraint = _reflection.GeneratedProtocolMessageType('VariantConstraint', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _VARIANTCONSTRAINT_PROPERTIESENTRY,
    '__module__' : 'sarus_data_spec.protobuf.constraint_pb2'
    # @@protoc_insertion_point(class_scope:sarus_data_spec.VariantConstraint.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _VARIANTCONSTRAINT,
  '__module__' : 'sarus_data_spec.protobuf.constraint_pb2'
  # @@protoc_insertion_point(class_scope:sarus_data_spec.VariantConstraint)
  })
_sym_db.RegisterMessage(VariantConstraint)
_sym_db.RegisterMessage(VariantConstraint.PropertiesEntry)


_VARIANTCONSTRAINT_PROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
