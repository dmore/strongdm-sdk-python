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
# source: access_requests_history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import access_requests_pb2 as access__requests__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61\x63\x63\x65ss_requests_history.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15\x61\x63\x63\x65ss_requests.proto\x1a\roptions.proto\x1a\nspec.proto\"\x8e\x01\n\x1f\x41\x63\x63\x65ssRequestHistoryListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x84\x02\n AccessRequestHistoryListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x35\n\x07history\x18\x02 \x03(\x0b\x32\x18.v1.AccessRequestHistoryB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x99\x02\n\x14\x41\x63\x63\x65ssRequestHistory\x12\x1f\n\x0b\x61\x63tivity_id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x39\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\x0e\x61\x63\x63\x65ss_request\x18\x03 \x01(\x0b\x32\x11.v1.AccessRequestB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12:\n\ndeleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider2\xf1\x01\n\x15\x41\x63\x63\x65ssRequestsHistory\x12\x85\x01\n\x04List\x12#.v1.AccessRequestHistoryListRequest\x1a$.v1.AccessRequestHistoryListResponse\"2\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07 \xaa\xf3\xb3\x07\x1b/v1/access-requests-history\x1aP\xca\xf9\xb3\x07\x19\xc2\xf9\xb3\x07\x14\x41\x63\x63\x65ssRequestHistory\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-providerB\x99\x01\n\x19\x63om.strongdm.api.plumbingB\x1d\x41\x63\x63\x65ssRequestsHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\xc2\x92\xb4\x07\x06\xa2\x8c\xb4\x07\x01*\xc2\x92\xb4\x07\x18\xa2\x8c\xb4\x07\x13!terraform-providerb\x06proto3')



_ACCESSREQUESTHISTORYLISTREQUEST = DESCRIPTOR.message_types_by_name['AccessRequestHistoryListRequest']
_ACCESSREQUESTHISTORYLISTRESPONSE = DESCRIPTOR.message_types_by_name['AccessRequestHistoryListResponse']
_ACCESSREQUESTHISTORY = DESCRIPTOR.message_types_by_name['AccessRequestHistory']
AccessRequestHistoryListRequest = _reflection.GeneratedProtocolMessageType('AccessRequestHistoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSREQUESTHISTORYLISTREQUEST,
  '__module__' : 'access_requests_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccessRequestHistoryListRequest)
  })
_sym_db.RegisterMessage(AccessRequestHistoryListRequest)

AccessRequestHistoryListResponse = _reflection.GeneratedProtocolMessageType('AccessRequestHistoryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSREQUESTHISTORYLISTRESPONSE,
  '__module__' : 'access_requests_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccessRequestHistoryListResponse)
  })
_sym_db.RegisterMessage(AccessRequestHistoryListResponse)

AccessRequestHistory = _reflection.GeneratedProtocolMessageType('AccessRequestHistory', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSREQUESTHISTORY,
  '__module__' : 'access_requests_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccessRequestHistory)
  })
_sym_db.RegisterMessage(AccessRequestHistory)

_ACCESSREQUESTSHISTORY = DESCRIPTOR.services_by_name['AccessRequestsHistory']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\035AccessRequestsHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\302\222\264\007\006\242\214\264\007\001*\302\222\264\007\030\242\214\264\007\023!terraform-provider'
  _ACCESSREQUESTHISTORYLISTREQUEST.fields_by_name['filter']._options = None
  _ACCESSREQUESTHISTORYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCESSREQUESTHISTORYLISTREQUEST._options = None
  _ACCESSREQUESTHISTORYLISTREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACCESSREQUESTHISTORYLISTRESPONSE.fields_by_name['history']._options = None
  _ACCESSREQUESTHISTORYLISTRESPONSE.fields_by_name['history']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ACCESSREQUESTHISTORYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCESSREQUESTHISTORYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCESSREQUESTHISTORYLISTRESPONSE._options = None
  _ACCESSREQUESTHISTORYLISTRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACCESSREQUESTHISTORY.fields_by_name['activity_id']._options = None
  _ACCESSREQUESTHISTORY.fields_by_name['activity_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCESSREQUESTHISTORY.fields_by_name['timestamp']._options = None
  _ACCESSREQUESTHISTORY.fields_by_name['timestamp']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCESSREQUESTHISTORY.fields_by_name['access_request']._options = None
  _ACCESSREQUESTHISTORY.fields_by_name['access_request']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCESSREQUESTHISTORY.fields_by_name['deleted_at']._options = None
  _ACCESSREQUESTHISTORY.fields_by_name['deleted_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCESSREQUESTHISTORY._options = None
  _ACCESSREQUESTHISTORY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACCESSREQUESTSHISTORY._options = None
  _ACCESSREQUESTSHISTORY._serialized_options = b'\312\371\263\007\031\302\371\263\007\024AccessRequestHistory\312\371\263\007\005\330\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider'
  _ACCESSREQUESTSHISTORY.methods_by_name['List']._options = None
  _ACCESSREQUESTSHISTORY.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007 \252\363\263\007\033/v1/access-requests-history'
  _ACCESSREQUESTHISTORYLISTREQUEST._serialized_start=121
  _ACCESSREQUESTHISTORYLISTREQUEST._serialized_end=263
  _ACCESSREQUESTHISTORYLISTRESPONSE._serialized_start=266
  _ACCESSREQUESTHISTORYLISTRESPONSE._serialized_end=526
  _ACCESSREQUESTHISTORY._serialized_start=529
  _ACCESSREQUESTHISTORY._serialized_end=810
  _ACCESSREQUESTSHISTORY._serialized_start=813
  _ACCESSREQUESTSHISTORY._serialized_end=1054
# @@protoc_insertion_point(module_scope)
