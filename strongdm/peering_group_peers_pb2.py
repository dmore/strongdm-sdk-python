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
# source: peering_group_peers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19peering_group_peers.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x86\x01\n\x1dPeeringGroupPeerCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12<\n\x12peering_group_peer\x18\x02 \x01(\x0b\x32\x14.v1.PeeringGroupPeerB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf9\x01\n\x1ePeeringGroupPeerCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12<\n\x12peering_group_peer\x18\x02 \x01(\x0b\x32\x14.v1.PeeringGroupPeerB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"Z\n\x1aPeeringGroupPeerGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf3\x01\n\x1bPeeringGroupPeerGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12<\n\x12peering_group_peer\x18\x02 \x01(\x0b\x32\x14.v1.PeeringGroupPeerB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"`\n\x1dPeeringGroupPeerDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbb\x01\n\x1ePeeringGroupPeerDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"`\n\x1bPeeringGroupPeerListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xde\x01\n\x1cPeeringGroupPeerListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12=\n\x13peering_group_peers\x18\x02 \x03(\x0b\x32\x14.v1.PeeringGroupPeerB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\x87\x01\n\x10PeeringGroupPeer\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12!\n\x08group_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01\x12,\n\x13peers_with_group_id\x18\x04 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xc2\x04\n\x11PeeringGroupPeers\x12~\n\x06\x43reate\x12!.v1.PeeringGroupPeerCreateRequest\x1a\".v1.PeeringGroupPeerCreateResponse\"-\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x1a\xaa\xf3\xb3\x07\x15/v1/peeringGroupPeers\x12\x85\x01\n\x06\x44\x65lete\x12!.v1.PeeringGroupPeerDeleteRequest\x1a\".v1.PeeringGroupPeerDeleteResponse\"4\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x1f\xaa\xf3\xb3\x07\x1a/v1/peeringGroupPeers/{id}\x12y\n\x03Get\x12\x1e.v1.PeeringGroupPeerGetRequest\x1a\x1f.v1.PeeringGroupPeerGetResponse\"1\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1f\xaa\xf3\xb3\x07\x1a/v1/peeringGroupPeers/{id}\x12w\n\x04List\x12\x1f.v1.PeeringGroupPeerListRequest\x1a .v1.PeeringGroupPeerListResponse\",\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1a\xaa\xf3\xb3\x07\x15/v1/peeringGroupPeers\x1a\x31\xca\xf9\xb3\x07\x15\xc2\xf9\xb3\x07\x10PeeringGroupPeer\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03gp-\xca\xf9\xb3\x07\x05\xe0\xf9\xb3\x07\x01\x42m\n\x19\x63om.strongdm.api.plumbingB\x19PeeringGroupPeersPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_PEERINGGROUPPEERCREATEREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupPeerCreateRequest']
_PEERINGGROUPPEERCREATERESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupPeerCreateResponse']
_PEERINGGROUPPEERGETREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupPeerGetRequest']
_PEERINGGROUPPEERGETRESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupPeerGetResponse']
_PEERINGGROUPPEERDELETEREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupPeerDeleteRequest']
_PEERINGGROUPPEERDELETERESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupPeerDeleteResponse']
_PEERINGGROUPPEERLISTREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupPeerListRequest']
_PEERINGGROUPPEERLISTRESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupPeerListResponse']
_PEERINGGROUPPEER = DESCRIPTOR.message_types_by_name['PeeringGroupPeer']
PeeringGroupPeerCreateRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERCREATEREQUEST,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerCreateRequest)
  })
_sym_db.RegisterMessage(PeeringGroupPeerCreateRequest)

PeeringGroupPeerCreateResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERCREATERESPONSE,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerCreateResponse)
  })
_sym_db.RegisterMessage(PeeringGroupPeerCreateResponse)

PeeringGroupPeerGetRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERGETREQUEST,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerGetRequest)
  })
_sym_db.RegisterMessage(PeeringGroupPeerGetRequest)

PeeringGroupPeerGetResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERGETRESPONSE,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerGetResponse)
  })
_sym_db.RegisterMessage(PeeringGroupPeerGetResponse)

PeeringGroupPeerDeleteRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERDELETEREQUEST,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerDeleteRequest)
  })
_sym_db.RegisterMessage(PeeringGroupPeerDeleteRequest)

PeeringGroupPeerDeleteResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERDELETERESPONSE,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerDeleteResponse)
  })
_sym_db.RegisterMessage(PeeringGroupPeerDeleteResponse)

PeeringGroupPeerListRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerListRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERLISTREQUEST,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerListRequest)
  })
_sym_db.RegisterMessage(PeeringGroupPeerListRequest)

PeeringGroupPeerListResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupPeerListResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEERLISTRESPONSE,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeerListResponse)
  })
_sym_db.RegisterMessage(PeeringGroupPeerListResponse)

PeeringGroupPeer = _reflection.GeneratedProtocolMessageType('PeeringGroupPeer', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPPEER,
  '__module__' : 'peering_group_peers_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupPeer)
  })
_sym_db.RegisterMessage(PeeringGroupPeer)

_PEERINGGROUPPEERS = DESCRIPTOR.services_by_name['PeeringGroupPeers']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\031PeeringGroupPeersPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _PEERINGGROUPPEERCREATEREQUEST.fields_by_name['peering_group_peer']._options = None
  _PEERINGGROUPPEERCREATEREQUEST.fields_by_name['peering_group_peer']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERCREATERESPONSE.fields_by_name['meta']._options = None
  _PEERINGGROUPPEERCREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERCREATERESPONSE.fields_by_name['peering_group_peer']._options = None
  _PEERINGGROUPPEERCREATERESPONSE.fields_by_name['peering_group_peer']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPPEERCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPPEERCREATERESPONSE._options = None
  _PEERINGGROUPPEERCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPPEERGETREQUEST.fields_by_name['id']._options = None
  _PEERINGGROUPPEERGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERGETRESPONSE.fields_by_name['meta']._options = None
  _PEERINGGROUPPEERGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERGETRESPONSE.fields_by_name['peering_group_peer']._options = None
  _PEERINGGROUPPEERGETRESPONSE.fields_by_name['peering_group_peer']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERGETRESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPPEERGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPPEERGETRESPONSE._options = None
  _PEERINGGROUPPEERGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPPEERDELETEREQUEST.fields_by_name['id']._options = None
  _PEERINGGROUPPEERDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERDELETERESPONSE.fields_by_name['meta']._options = None
  _PEERINGGROUPPEERDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPPEERDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPPEERDELETERESPONSE._options = None
  _PEERINGGROUPPEERDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPPEERLISTREQUEST.fields_by_name['filter']._options = None
  _PEERINGGROUPPEERLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEERLISTRESPONSE.fields_by_name['peering_group_peers']._options = None
  _PEERINGGROUPPEERLISTRESPONSE.fields_by_name['peering_group_peers']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _PEERINGGROUPPEERLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPPEERLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPPEER.fields_by_name['id']._options = None
  _PEERINGGROUPPEER.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPPEER.fields_by_name['group_id']._options = None
  _PEERINGGROUPPEER.fields_by_name['group_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _PEERINGGROUPPEER.fields_by_name['peers_with_group_id']._options = None
  _PEERINGGROUPPEER.fields_by_name['peers_with_group_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _PEERINGGROUPPEER._options = None
  _PEERINGGROUPPEER._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPPEERS._options = None
  _PEERINGGROUPPEERS._serialized_options = b'\312\371\263\007\025\302\371\263\007\020PeeringGroupPeer\312\371\263\007\010\322\371\263\007\003gp-\312\371\263\007\005\340\371\263\007\001'
  _PEERINGGROUPPEERS.methods_by_name['Create']._options = None
  _PEERINGGROUPPEERS.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\032\252\363\263\007\025/v1/peeringGroupPeers'
  _PEERINGGROUPPEERS.methods_by_name['Delete']._options = None
  _PEERINGGROUPPEERS.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\037\252\363\263\007\032/v1/peeringGroupPeers/{id}'
  _PEERINGGROUPPEERS.methods_by_name['Get']._options = None
  _PEERINGGROUPPEERS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\037\252\363\263\007\032/v1/peeringGroupPeers/{id}'
  _PEERINGGROUPPEERS.methods_by_name['List']._options = None
  _PEERINGGROUPPEERS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\032\252\363\263\007\025/v1/peeringGroupPeers'
  _PEERINGGROUPPEERCREATEREQUEST._serialized_start=61
  _PEERINGGROUPPEERCREATEREQUEST._serialized_end=195
  _PEERINGGROUPPEERCREATERESPONSE._serialized_start=198
  _PEERINGGROUPPEERCREATERESPONSE._serialized_end=447
  _PEERINGGROUPPEERGETREQUEST._serialized_start=449
  _PEERINGGROUPPEERGETREQUEST._serialized_end=539
  _PEERINGGROUPPEERGETRESPONSE._serialized_start=542
  _PEERINGGROUPPEERGETRESPONSE._serialized_end=785
  _PEERINGGROUPPEERDELETEREQUEST._serialized_start=787
  _PEERINGGROUPPEERDELETEREQUEST._serialized_end=883
  _PEERINGGROUPPEERDELETERESPONSE._serialized_start=886
  _PEERINGGROUPPEERDELETERESPONSE._serialized_end=1073
  _PEERINGGROUPPEERLISTREQUEST._serialized_start=1075
  _PEERINGGROUPPEERLISTREQUEST._serialized_end=1171
  _PEERINGGROUPPEERLISTRESPONSE._serialized_start=1174
  _PEERINGGROUPPEERLISTRESPONSE._serialized_end=1396
  _PEERINGGROUPPEER._serialized_start=1399
  _PEERINGGROUPPEER._serialized_end=1534
  _PEERINGGROUPPEERS._serialized_start=1537
  _PEERINGGROUPPEERS._serialized_end=2115
# @@protoc_insertion_point(module_scope)
