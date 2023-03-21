# Copyright 2020 StrongDM Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_identities_history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import remote_identities_pb2 as remote__identities__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fremote_identities_history.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17remote_identities.proto\x1a\roptions.proto\x1a\nspec.proto\"\x8f\x01\n RemoteIdentityHistoryListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x86\x02\n!RemoteIdentityHistoryListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x36\n\x07history\x18\x02 \x03(\x0b\x32\x19.v1.RemoteIdentityHistoryB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x9c\x02\n\x15RemoteIdentityHistory\x12\x1f\n\x0b\x61\x63tivity_id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x39\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x0fremote_identity\x18\x03 \x01(\x0b\x32\x12.v1.RemoteIdentityB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12:\n\ndeleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider2\xf8\x01\n\x17RemoteIdentitiesHistory\x12\x89\x01\n\x04List\x12$.v1.RemoteIdentityHistoryListRequest\x1a%.v1.RemoteIdentityHistoryListResponse\"4\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\"\xaa\xf3\xb3\x07\x1d/v1/remote-identities-history\x1aQ\xca\xf9\xb3\x07\x1a\xc2\xf9\xb3\x07\x15RemoteIdentityHistory\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-providerB\x9b\x01\n\x19\x63om.strongdm.api.plumbingB\x1fRemoteIdentitiesHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\xc2\x92\xb4\x07\x06\xa2\x8c\xb4\x07\x01*\xc2\x92\xb4\x07\x18\xa2\x8c\xb4\x07\x13!terraform-providerb\x06proto3')



_REMOTEIDENTITYHISTORYLISTREQUEST = DESCRIPTOR.message_types_by_name['RemoteIdentityHistoryListRequest']
_REMOTEIDENTITYHISTORYLISTRESPONSE = DESCRIPTOR.message_types_by_name['RemoteIdentityHistoryListResponse']
_REMOTEIDENTITYHISTORY = DESCRIPTOR.message_types_by_name['RemoteIdentityHistory']
RemoteIdentityHistoryListRequest = _reflection.GeneratedProtocolMessageType('RemoteIdentityHistoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEIDENTITYHISTORYLISTREQUEST,
  '__module__' : 'remote_identities_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.RemoteIdentityHistoryListRequest)
  })
_sym_db.RegisterMessage(RemoteIdentityHistoryListRequest)

RemoteIdentityHistoryListResponse = _reflection.GeneratedProtocolMessageType('RemoteIdentityHistoryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEIDENTITYHISTORYLISTRESPONSE,
  '__module__' : 'remote_identities_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.RemoteIdentityHistoryListResponse)
  })
_sym_db.RegisterMessage(RemoteIdentityHistoryListResponse)

RemoteIdentityHistory = _reflection.GeneratedProtocolMessageType('RemoteIdentityHistory', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEIDENTITYHISTORY,
  '__module__' : 'remote_identities_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.RemoteIdentityHistory)
  })
_sym_db.RegisterMessage(RemoteIdentityHistory)

_REMOTEIDENTITIESHISTORY = DESCRIPTOR.services_by_name['RemoteIdentitiesHistory']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\037RemoteIdentitiesHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\302\222\264\007\006\242\214\264\007\001*\302\222\264\007\030\242\214\264\007\023!terraform-provider'
  _REMOTEIDENTITYHISTORYLISTREQUEST.fields_by_name['filter']._options = None
  _REMOTEIDENTITYHISTORYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _REMOTEIDENTITYHISTORYLISTREQUEST._options = None
  _REMOTEIDENTITYHISTORYLISTREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _REMOTEIDENTITYHISTORYLISTRESPONSE.fields_by_name['history']._options = None
  _REMOTEIDENTITYHISTORYLISTRESPONSE.fields_by_name['history']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _REMOTEIDENTITYHISTORYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _REMOTEIDENTITYHISTORYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _REMOTEIDENTITYHISTORYLISTRESPONSE._options = None
  _REMOTEIDENTITYHISTORYLISTRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _REMOTEIDENTITYHISTORY.fields_by_name['activity_id']._options = None
  _REMOTEIDENTITYHISTORY.fields_by_name['activity_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _REMOTEIDENTITYHISTORY.fields_by_name['timestamp']._options = None
  _REMOTEIDENTITYHISTORY.fields_by_name['timestamp']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _REMOTEIDENTITYHISTORY.fields_by_name['remote_identity']._options = None
  _REMOTEIDENTITYHISTORY.fields_by_name['remote_identity']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _REMOTEIDENTITYHISTORY.fields_by_name['deleted_at']._options = None
  _REMOTEIDENTITYHISTORY.fields_by_name['deleted_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _REMOTEIDENTITYHISTORY._options = None
  _REMOTEIDENTITYHISTORY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _REMOTEIDENTITIESHISTORY._options = None
  _REMOTEIDENTITIESHISTORY._serialized_options = b'\312\371\263\007\032\302\371\263\007\025RemoteIdentityHistory\312\371\263\007\005\330\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider'
  _REMOTEIDENTITIESHISTORY.methods_by_name['List']._options = None
  _REMOTEIDENTITIESHISTORY.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\"\252\363\263\007\035/v1/remote-identities-history'
  _REMOTEIDENTITYHISTORYLISTREQUEST._serialized_start=125
  _REMOTEIDENTITYHISTORYLISTREQUEST._serialized_end=268
  _REMOTEIDENTITYHISTORYLISTRESPONSE._serialized_start=271
  _REMOTEIDENTITYHISTORYLISTRESPONSE._serialized_end=533
  _REMOTEIDENTITYHISTORY._serialized_start=536
  _REMOTEIDENTITYHISTORY._serialized_end=820
  _REMOTEIDENTITIESHISTORY._serialized_start=823
  _REMOTEIDENTITIESHISTORY._serialized_end=1071
# @@protoc_insertion_point(module_scope)
