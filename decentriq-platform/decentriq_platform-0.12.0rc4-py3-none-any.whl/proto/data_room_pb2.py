# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_room.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import attestation_pb2 as attestation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64\x61ta_room.proto\x12\tdata_room\x1a\x11\x61ttestation.proto\"\xb8\x01\n\x08\x44\x61taRoom\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x12\n\nownerEmail\x18\x08 \x01(\t\x12\x39\n\x12governanceProtocol\x18\t \x01(\x0b\x32\x1d.data_room.GovernanceProtocol\x12\x18\n\x0b\x64\x63rSecretId\x18\n \x01(\x0cH\x00\x88\x01\x01\x42\x0e\n\x0c_dcrSecretIdJ\x04\x08\x02\x10\x06\"\xb6\x01\n\x12GovernanceProtocol\x12?\n\x14staticDataRoomPolicy\x18\x01 \x01(\x0b\x32\x1f.data_room.StaticDataRoomPolicyH\x00\x12U\n\x1f\x61\x66\x66\x65\x63tedDataOwnersApprovePolicy\x18\x02 \x01(\x0b\x32*.data_room.AffectedDataOwnersApprovePolicyH\x00\x42\x08\n\x06policy\"\x16\n\x14StaticDataRoomPolicy\"!\n\x1f\x41\x66\x66\x65\x63tedDataOwnersApprovePolicy\"\xab\x01\n\x15\x44\x61taRoomConfiguration\x12@\n\x08\x65lements\x18\x01 \x03(\x0b\x32..data_room.DataRoomConfiguration.ElementsEntry\x1aP\n\rElementsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.data_room.ConfigurationElement:\x02\x38\x01\"\x91\x02\n\x14\x43onfigurationElement\x12-\n\x0b\x63omputeNode\x18\x01 \x01(\x0b\x32\x16.data_room.ComputeNodeH\x00\x12I\n\x18\x61ttestationSpecification\x18\x02 \x01(\x0b\x32%.attestation.AttestationSpecificationH\x00\x12\x33\n\x0euserPermission\x18\x03 \x01(\x0b\x32\x19.data_room.UserPermissionH\x00\x12?\n\x14\x61uthenticationMethod\x18\x04 \x01(\x0b\x32\x1f.data_room.AuthenticationMethodH\x00\x42\t\n\x07\x65lement\"\xb8\x01\n\x19\x43onfigurationModification\x12)\n\x03\x61\x64\x64\x18\x01 \x01(\x0b\x32\x1a.data_room.AddModificationH\x00\x12/\n\x06\x63hange\x18\x02 \x01(\x0b\x32\x1d.data_room.ChangeModificationH\x00\x12/\n\x06\x64\x65lete\x18\x03 \x01(\x0b\x32\x1d.data_room.DeleteModificationH\x00\x42\x0e\n\x0cmodification\"O\n\x0f\x41\x64\x64Modification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x07\x65lement\x18\x02 \x01(\x0b\x32\x1f.data_room.ConfigurationElement\"R\n\x12\x43hangeModification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x07\x65lement\x18\x02 \x01(\x0b\x32\x1f.data_room.ConfigurationElement\" \n\x12\x44\x65leteModification\x12\n\n\x02id\x18\x01 \x01(\t\"\x82\x01\n\x13\x43onfigurationCommit\x12\x12\n\ndataRoomId\x18\x01 \x01(\x0c\x12\x1a\n\x12\x64\x61taRoomHistoryPin\x18\x02 \x01(\x0c\x12;\n\rmodifications\x18\x03 \x03(\x0b\x32$.data_room.ConfigurationModification\"\x83\x01\n\x0b\x43omputeNode\x12\x10\n\x08nodeName\x18\x01 \x01(\t\x12*\n\x04leaf\x18\x02 \x01(\x0b\x32\x1a.data_room.ComputeNodeLeafH\x00\x12.\n\x06\x62ranch\x18\x03 \x01(\x0b\x32\x1c.data_room.ComputeNodeBranchH\x00\x42\x06\n\x04node\"%\n\x0f\x43omputeNodeLeaf\x12\x12\n\nisRequired\x18\x01 \x01(\x08\"&\n\x13\x43omputeNodeProtocol\x12\x0f\n\x07version\x18\x01 \x01(\r\"\xc9\x01\n\x11\x43omputeNodeBranch\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\x0c\x12\x14\n\x0c\x64\x65pendencies\x18\x02 \x03(\t\x12\x32\n\x0coutputFormat\x18\x04 \x01(\x0e\x32\x1c.data_room.ComputeNodeFormat\x12\x30\n\x08protocol\x18\x05 \x01(\x0b\x32\x1e.data_room.ComputeNodeProtocol\x12\"\n\x1a\x61ttestationSpecificationId\x18\x06 \x01(\tJ\x04\x08\x03\x10\x04\"q\n\x0eUserPermission\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12*\n\x0bpermissions\x18\x03 \x03(\x0b\x32\x15.data_room.Permission\x12\x1e\n\x16\x61uthenticationMethodId\x18\x04 \x01(\tJ\x04\x08\x02\x10\x03\"U\n\x14\x41uthenticationMethod\x12.\n\ntrustedPki\x18\x01 \x01(\x0b\x32\x15.data_room.TrustedPkiH\x00\x88\x01\x01\x42\r\n\x0b_trustedPki\"(\n\nTrustedPki\x12\x1a\n\x12rootCertificatePem\x18\x01 \x01(\x0c\"\x95\x07\n\nPermission\x12G\n\x18\x65xecuteComputePermission\x18\x01 \x01(\x0b\x32#.data_room.ExecuteComputePermissionH\x00\x12;\n\x12leafCrudPermission\x18\x02 \x01(\x0b\x32\x1d.data_room.LeafCrudPermissionH\x00\x12K\n\x1aretrieveDataRoomPermission\x18\x03 \x01(\x0b\x32%.data_room.RetrieveDataRoomPermissionH\x00\x12K\n\x1aretrieveAuditLogPermission\x18\x04 \x01(\x0b\x32%.data_room.RetrieveAuditLogPermissionH\x00\x12W\n retrieveDataRoomStatusPermission\x18\x05 \x01(\x0b\x32+.data_room.RetrieveDataRoomStatusPermissionH\x00\x12S\n\x1eupdateDataRoomStatusPermission\x18\x06 \x01(\x0b\x32).data_room.UpdateDataRoomStatusPermissionH\x00\x12]\n#retrievePublishedDatasetsPermission\x18\x07 \x01(\x0b\x32..data_room.RetrievePublishedDatasetsPermissionH\x00\x12\x37\n\x10\x64ryRunPermission\x18\x08 \x01(\x0b\x32\x1b.data_room.DryRunPermissionH\x00\x12W\n generateMergeSignaturePermission\x18\t \x01(\x0b\x32+.data_room.GenerateMergeSignaturePermissionH\x00\x12]\n#executeDevelopmentComputePermission\x18\n \x01(\x0b\x32..data_room.ExecuteDevelopmentComputePermissionH\x00\x12[\n\"mergeConfigurationCommitPermission\x18\x0b \x01(\x0b\x32-.data_room.MergeConfigurationCommitPermissionH\x00\x42\x0c\n\npermission\"3\n\x18\x45xecuteComputePermission\x12\x17\n\x0f\x63omputeNodeName\x18\x01 \x01(\t\"*\n\x12LeafCrudPermission\x12\x14\n\x0cleafNodeName\x18\x01 \x01(\t\"\x1c\n\x1aRetrieveDataRoomPermission\"\x1c\n\x1aRetrieveAuditLogPermission\"\"\n RetrieveDataRoomStatusPermission\" \n\x1eUpdateDataRoomStatusPermission\"%\n#RetrievePublishedDatasetsPermission\"\x12\n\x10\x44ryRunPermission\"\"\n GenerateMergeSignaturePermission\"%\n#ExecuteDevelopmentComputePermission\"$\n\"MergeConfigurationCommitPermission*%\n\x11\x43omputeNodeFormat\x12\x07\n\x03RAW\x10\x00\x12\x07\n\x03ZIP\x10\x01\x62\x06proto3')

_COMPUTENODEFORMAT = DESCRIPTOR.enum_types_by_name['ComputeNodeFormat']
ComputeNodeFormat = enum_type_wrapper.EnumTypeWrapper(_COMPUTENODEFORMAT)
RAW = 0
ZIP = 1


_DATAROOM = DESCRIPTOR.message_types_by_name['DataRoom']
_GOVERNANCEPROTOCOL = DESCRIPTOR.message_types_by_name['GovernanceProtocol']
_STATICDATAROOMPOLICY = DESCRIPTOR.message_types_by_name['StaticDataRoomPolicy']
_AFFECTEDDATAOWNERSAPPROVEPOLICY = DESCRIPTOR.message_types_by_name['AffectedDataOwnersApprovePolicy']
_DATAROOMCONFIGURATION = DESCRIPTOR.message_types_by_name['DataRoomConfiguration']
_DATAROOMCONFIGURATION_ELEMENTSENTRY = _DATAROOMCONFIGURATION.nested_types_by_name['ElementsEntry']
_CONFIGURATIONELEMENT = DESCRIPTOR.message_types_by_name['ConfigurationElement']
_CONFIGURATIONMODIFICATION = DESCRIPTOR.message_types_by_name['ConfigurationModification']
_ADDMODIFICATION = DESCRIPTOR.message_types_by_name['AddModification']
_CHANGEMODIFICATION = DESCRIPTOR.message_types_by_name['ChangeModification']
_DELETEMODIFICATION = DESCRIPTOR.message_types_by_name['DeleteModification']
_CONFIGURATIONCOMMIT = DESCRIPTOR.message_types_by_name['ConfigurationCommit']
_COMPUTENODE = DESCRIPTOR.message_types_by_name['ComputeNode']
_COMPUTENODELEAF = DESCRIPTOR.message_types_by_name['ComputeNodeLeaf']
_COMPUTENODEPROTOCOL = DESCRIPTOR.message_types_by_name['ComputeNodeProtocol']
_COMPUTENODEBRANCH = DESCRIPTOR.message_types_by_name['ComputeNodeBranch']
_USERPERMISSION = DESCRIPTOR.message_types_by_name['UserPermission']
_AUTHENTICATIONMETHOD = DESCRIPTOR.message_types_by_name['AuthenticationMethod']
_TRUSTEDPKI = DESCRIPTOR.message_types_by_name['TrustedPki']
_PERMISSION = DESCRIPTOR.message_types_by_name['Permission']
_EXECUTECOMPUTEPERMISSION = DESCRIPTOR.message_types_by_name['ExecuteComputePermission']
_LEAFCRUDPERMISSION = DESCRIPTOR.message_types_by_name['LeafCrudPermission']
_RETRIEVEDATAROOMPERMISSION = DESCRIPTOR.message_types_by_name['RetrieveDataRoomPermission']
_RETRIEVEAUDITLOGPERMISSION = DESCRIPTOR.message_types_by_name['RetrieveAuditLogPermission']
_RETRIEVEDATAROOMSTATUSPERMISSION = DESCRIPTOR.message_types_by_name['RetrieveDataRoomStatusPermission']
_UPDATEDATAROOMSTATUSPERMISSION = DESCRIPTOR.message_types_by_name['UpdateDataRoomStatusPermission']
_RETRIEVEPUBLISHEDDATASETSPERMISSION = DESCRIPTOR.message_types_by_name['RetrievePublishedDatasetsPermission']
_DRYRUNPERMISSION = DESCRIPTOR.message_types_by_name['DryRunPermission']
_GENERATEMERGESIGNATUREPERMISSION = DESCRIPTOR.message_types_by_name['GenerateMergeSignaturePermission']
_EXECUTEDEVELOPMENTCOMPUTEPERMISSION = DESCRIPTOR.message_types_by_name['ExecuteDevelopmentComputePermission']
_MERGECONFIGURATIONCOMMITPERMISSION = DESCRIPTOR.message_types_by_name['MergeConfigurationCommitPermission']
DataRoom = _reflection.GeneratedProtocolMessageType('DataRoom', (_message.Message,), {
  'DESCRIPTOR' : _DATAROOM,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.DataRoom)
  })
_sym_db.RegisterMessage(DataRoom)

GovernanceProtocol = _reflection.GeneratedProtocolMessageType('GovernanceProtocol', (_message.Message,), {
  'DESCRIPTOR' : _GOVERNANCEPROTOCOL,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.GovernanceProtocol)
  })
_sym_db.RegisterMessage(GovernanceProtocol)

StaticDataRoomPolicy = _reflection.GeneratedProtocolMessageType('StaticDataRoomPolicy', (_message.Message,), {
  'DESCRIPTOR' : _STATICDATAROOMPOLICY,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.StaticDataRoomPolicy)
  })
_sym_db.RegisterMessage(StaticDataRoomPolicy)

AffectedDataOwnersApprovePolicy = _reflection.GeneratedProtocolMessageType('AffectedDataOwnersApprovePolicy', (_message.Message,), {
  'DESCRIPTOR' : _AFFECTEDDATAOWNERSAPPROVEPOLICY,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.AffectedDataOwnersApprovePolicy)
  })
_sym_db.RegisterMessage(AffectedDataOwnersApprovePolicy)

DataRoomConfiguration = _reflection.GeneratedProtocolMessageType('DataRoomConfiguration', (_message.Message,), {

  'ElementsEntry' : _reflection.GeneratedProtocolMessageType('ElementsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATAROOMCONFIGURATION_ELEMENTSENTRY,
    '__module__' : 'data_room_pb2'
    # @@protoc_insertion_point(class_scope:data_room.DataRoomConfiguration.ElementsEntry)
    })
  ,
  'DESCRIPTOR' : _DATAROOMCONFIGURATION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.DataRoomConfiguration)
  })
_sym_db.RegisterMessage(DataRoomConfiguration)
_sym_db.RegisterMessage(DataRoomConfiguration.ElementsEntry)

ConfigurationElement = _reflection.GeneratedProtocolMessageType('ConfigurationElement', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONELEMENT,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ConfigurationElement)
  })
_sym_db.RegisterMessage(ConfigurationElement)

ConfigurationModification = _reflection.GeneratedProtocolMessageType('ConfigurationModification', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONMODIFICATION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ConfigurationModification)
  })
_sym_db.RegisterMessage(ConfigurationModification)

AddModification = _reflection.GeneratedProtocolMessageType('AddModification', (_message.Message,), {
  'DESCRIPTOR' : _ADDMODIFICATION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.AddModification)
  })
_sym_db.RegisterMessage(AddModification)

ChangeModification = _reflection.GeneratedProtocolMessageType('ChangeModification', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEMODIFICATION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ChangeModification)
  })
_sym_db.RegisterMessage(ChangeModification)

DeleteModification = _reflection.GeneratedProtocolMessageType('DeleteModification', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODIFICATION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.DeleteModification)
  })
_sym_db.RegisterMessage(DeleteModification)

ConfigurationCommit = _reflection.GeneratedProtocolMessageType('ConfigurationCommit', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONCOMMIT,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ConfigurationCommit)
  })
_sym_db.RegisterMessage(ConfigurationCommit)

ComputeNode = _reflection.GeneratedProtocolMessageType('ComputeNode', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTENODE,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ComputeNode)
  })
_sym_db.RegisterMessage(ComputeNode)

ComputeNodeLeaf = _reflection.GeneratedProtocolMessageType('ComputeNodeLeaf', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTENODELEAF,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ComputeNodeLeaf)
  })
_sym_db.RegisterMessage(ComputeNodeLeaf)

ComputeNodeProtocol = _reflection.GeneratedProtocolMessageType('ComputeNodeProtocol', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTENODEPROTOCOL,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ComputeNodeProtocol)
  })
_sym_db.RegisterMessage(ComputeNodeProtocol)

ComputeNodeBranch = _reflection.GeneratedProtocolMessageType('ComputeNodeBranch', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTENODEBRANCH,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ComputeNodeBranch)
  })
_sym_db.RegisterMessage(ComputeNodeBranch)

UserPermission = _reflection.GeneratedProtocolMessageType('UserPermission', (_message.Message,), {
  'DESCRIPTOR' : _USERPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.UserPermission)
  })
_sym_db.RegisterMessage(UserPermission)

AuthenticationMethod = _reflection.GeneratedProtocolMessageType('AuthenticationMethod', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONMETHOD,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.AuthenticationMethod)
  })
_sym_db.RegisterMessage(AuthenticationMethod)

TrustedPki = _reflection.GeneratedProtocolMessageType('TrustedPki', (_message.Message,), {
  'DESCRIPTOR' : _TRUSTEDPKI,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.TrustedPki)
  })
_sym_db.RegisterMessage(TrustedPki)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.Permission)
  })
_sym_db.RegisterMessage(Permission)

ExecuteComputePermission = _reflection.GeneratedProtocolMessageType('ExecuteComputePermission', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTECOMPUTEPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ExecuteComputePermission)
  })
_sym_db.RegisterMessage(ExecuteComputePermission)

LeafCrudPermission = _reflection.GeneratedProtocolMessageType('LeafCrudPermission', (_message.Message,), {
  'DESCRIPTOR' : _LEAFCRUDPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.LeafCrudPermission)
  })
_sym_db.RegisterMessage(LeafCrudPermission)

RetrieveDataRoomPermission = _reflection.GeneratedProtocolMessageType('RetrieveDataRoomPermission', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEDATAROOMPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.RetrieveDataRoomPermission)
  })
_sym_db.RegisterMessage(RetrieveDataRoomPermission)

RetrieveAuditLogPermission = _reflection.GeneratedProtocolMessageType('RetrieveAuditLogPermission', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEAUDITLOGPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.RetrieveAuditLogPermission)
  })
_sym_db.RegisterMessage(RetrieveAuditLogPermission)

RetrieveDataRoomStatusPermission = _reflection.GeneratedProtocolMessageType('RetrieveDataRoomStatusPermission', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEDATAROOMSTATUSPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.RetrieveDataRoomStatusPermission)
  })
_sym_db.RegisterMessage(RetrieveDataRoomStatusPermission)

UpdateDataRoomStatusPermission = _reflection.GeneratedProtocolMessageType('UpdateDataRoomStatusPermission', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATAROOMSTATUSPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.UpdateDataRoomStatusPermission)
  })
_sym_db.RegisterMessage(UpdateDataRoomStatusPermission)

RetrievePublishedDatasetsPermission = _reflection.GeneratedProtocolMessageType('RetrievePublishedDatasetsPermission', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPUBLISHEDDATASETSPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.RetrievePublishedDatasetsPermission)
  })
_sym_db.RegisterMessage(RetrievePublishedDatasetsPermission)

DryRunPermission = _reflection.GeneratedProtocolMessageType('DryRunPermission', (_message.Message,), {
  'DESCRIPTOR' : _DRYRUNPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.DryRunPermission)
  })
_sym_db.RegisterMessage(DryRunPermission)

GenerateMergeSignaturePermission = _reflection.GeneratedProtocolMessageType('GenerateMergeSignaturePermission', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEMERGESIGNATUREPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.GenerateMergeSignaturePermission)
  })
_sym_db.RegisterMessage(GenerateMergeSignaturePermission)

ExecuteDevelopmentComputePermission = _reflection.GeneratedProtocolMessageType('ExecuteDevelopmentComputePermission', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEDEVELOPMENTCOMPUTEPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.ExecuteDevelopmentComputePermission)
  })
_sym_db.RegisterMessage(ExecuteDevelopmentComputePermission)

MergeConfigurationCommitPermission = _reflection.GeneratedProtocolMessageType('MergeConfigurationCommitPermission', (_message.Message,), {
  'DESCRIPTOR' : _MERGECONFIGURATIONCOMMITPERMISSION,
  '__module__' : 'data_room_pb2'
  # @@protoc_insertion_point(class_scope:data_room.MergeConfigurationCommitPermission)
  })
_sym_db.RegisterMessage(MergeConfigurationCommitPermission)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATAROOMCONFIGURATION_ELEMENTSENTRY._options = None
  _DATAROOMCONFIGURATION_ELEMENTSENTRY._serialized_options = b'8\001'
  _COMPUTENODEFORMAT._serialized_start=3429
  _COMPUTENODEFORMAT._serialized_end=3466
  _DATAROOM._serialized_start=50
  _DATAROOM._serialized_end=234
  _GOVERNANCEPROTOCOL._serialized_start=237
  _GOVERNANCEPROTOCOL._serialized_end=419
  _STATICDATAROOMPOLICY._serialized_start=421
  _STATICDATAROOMPOLICY._serialized_end=443
  _AFFECTEDDATAOWNERSAPPROVEPOLICY._serialized_start=445
  _AFFECTEDDATAOWNERSAPPROVEPOLICY._serialized_end=478
  _DATAROOMCONFIGURATION._serialized_start=481
  _DATAROOMCONFIGURATION._serialized_end=652
  _DATAROOMCONFIGURATION_ELEMENTSENTRY._serialized_start=572
  _DATAROOMCONFIGURATION_ELEMENTSENTRY._serialized_end=652
  _CONFIGURATIONELEMENT._serialized_start=655
  _CONFIGURATIONELEMENT._serialized_end=928
  _CONFIGURATIONMODIFICATION._serialized_start=931
  _CONFIGURATIONMODIFICATION._serialized_end=1115
  _ADDMODIFICATION._serialized_start=1117
  _ADDMODIFICATION._serialized_end=1196
  _CHANGEMODIFICATION._serialized_start=1198
  _CHANGEMODIFICATION._serialized_end=1280
  _DELETEMODIFICATION._serialized_start=1282
  _DELETEMODIFICATION._serialized_end=1314
  _CONFIGURATIONCOMMIT._serialized_start=1317
  _CONFIGURATIONCOMMIT._serialized_end=1447
  _COMPUTENODE._serialized_start=1450
  _COMPUTENODE._serialized_end=1581
  _COMPUTENODELEAF._serialized_start=1583
  _COMPUTENODELEAF._serialized_end=1620
  _COMPUTENODEPROTOCOL._serialized_start=1622
  _COMPUTENODEPROTOCOL._serialized_end=1660
  _COMPUTENODEBRANCH._serialized_start=1663
  _COMPUTENODEBRANCH._serialized_end=1864
  _USERPERMISSION._serialized_start=1866
  _USERPERMISSION._serialized_end=1979
  _AUTHENTICATIONMETHOD._serialized_start=1981
  _AUTHENTICATIONMETHOD._serialized_end=2066
  _TRUSTEDPKI._serialized_start=2068
  _TRUSTEDPKI._serialized_end=2108
  _PERMISSION._serialized_start=2111
  _PERMISSION._serialized_end=3028
  _EXECUTECOMPUTEPERMISSION._serialized_start=3030
  _EXECUTECOMPUTEPERMISSION._serialized_end=3081
  _LEAFCRUDPERMISSION._serialized_start=3083
  _LEAFCRUDPERMISSION._serialized_end=3125
  _RETRIEVEDATAROOMPERMISSION._serialized_start=3127
  _RETRIEVEDATAROOMPERMISSION._serialized_end=3155
  _RETRIEVEAUDITLOGPERMISSION._serialized_start=3157
  _RETRIEVEAUDITLOGPERMISSION._serialized_end=3185
  _RETRIEVEDATAROOMSTATUSPERMISSION._serialized_start=3187
  _RETRIEVEDATAROOMSTATUSPERMISSION._serialized_end=3221
  _UPDATEDATAROOMSTATUSPERMISSION._serialized_start=3223
  _UPDATEDATAROOMSTATUSPERMISSION._serialized_end=3255
  _RETRIEVEPUBLISHEDDATASETSPERMISSION._serialized_start=3257
  _RETRIEVEPUBLISHEDDATASETSPERMISSION._serialized_end=3294
  _DRYRUNPERMISSION._serialized_start=3296
  _DRYRUNPERMISSION._serialized_end=3314
  _GENERATEMERGESIGNATUREPERMISSION._serialized_start=3316
  _GENERATEMERGESIGNATUREPERMISSION._serialized_end=3350
  _EXECUTEDEVELOPMENTCOMPUTEPERMISSION._serialized_start=3352
  _EXECUTEDEVELOPMENTCOMPUTEPERMISSION._serialized_end=3389
  _MERGECONFIGURATIONCOMMITPERMISSION._serialized_start=3391
  _MERGECONFIGURATIONCOMMITPERMISSION._serialized_end=3427
# @@protoc_insertion_point(module_scope)
