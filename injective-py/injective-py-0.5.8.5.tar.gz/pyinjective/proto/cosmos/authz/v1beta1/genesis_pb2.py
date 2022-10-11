# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/authz/v1beta1/genesis.proto',
  package='cosmos.authz.v1beta1',
  syntax='proto3',
  serialized_options=b'Z$github.com/cosmos/cosmos-sdk/x/authz',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"cosmos/authz/v1beta1/genesis.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x14gogoproto/gogo.proto\x1a cosmos/authz/v1beta1/authz.proto\"U\n\x0cGenesisState\x12\x45\n\rauthorization\x18\x01 \x03(\x0b\x32(.cosmos.authz.v1beta1.GrantAuthorizationB\x04\xc8\xde\x1f\x00\x42&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_authz_dot_v1beta1_dot_authz__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.authz.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authorization', full_name='cosmos.authz.v1beta1.GenesisState.authorization', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=201,
)

_GENESISSTATE.fields_by_name['authorization'].message_type = cosmos_dot_authz_dot_v1beta1_dot_authz__pb2._GRANTAUTHORIZATION
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.authz.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['authorization']._options = None
# @@protoc_insertion_point(module_scope)
