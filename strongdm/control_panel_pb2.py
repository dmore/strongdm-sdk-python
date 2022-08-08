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
# source: control_panel.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ontrol_panel.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"L\n$ControlPanelGetSSHCAPublicKeyRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\"\xdf\x01\n%ControlPanelGetSSHCAPublicKeyResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\npublic_key\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"_\n\x1c\x43ontrolPanelVerifyJWTRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x19\n\x05token\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd2\x01\n\x1d\x43ontrolPanelVerifyJWTResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05valid\x18\x02 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xb4\x02\n\x0c\x43ontrolPanel\x12\x99\x01\n\x11GetSSHCAPublicKey\x12(.v1.ControlPanelGetSSHCAPublicKeyRequest\x1a).v1.ControlPanelGetSSHCAPublicKeyResponse\"/\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1d\xaa\xf3\xb3\x07\x18/v1/control-panel/ssh/ca\x12\x87\x01\n\tVerifyJWT\x12 .v1.ControlPanelVerifyJWTRequest\x1a!.v1.ControlPanelVerifyJWTResponse\"5\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\"\xaa\xf3\xb3\x07\x1d/v1/control-panel/http/verifyBh\n\x19\x63om.strongdm.api.plumbingB\x14\x43ontrolPanelPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_CONTROLPANELGETSSHCAPUBLICKEYREQUEST = DESCRIPTOR.message_types_by_name['ControlPanelGetSSHCAPublicKeyRequest']
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE = DESCRIPTOR.message_types_by_name['ControlPanelGetSSHCAPublicKeyResponse']
_CONTROLPANELVERIFYJWTREQUEST = DESCRIPTOR.message_types_by_name['ControlPanelVerifyJWTRequest']
_CONTROLPANELVERIFYJWTRESPONSE = DESCRIPTOR.message_types_by_name['ControlPanelVerifyJWTResponse']
ControlPanelGetSSHCAPublicKeyRequest = _reflection.GeneratedProtocolMessageType('ControlPanelGetSSHCAPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELGETSSHCAPUBLICKEYREQUEST,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelGetSSHCAPublicKeyRequest)
  })
_sym_db.RegisterMessage(ControlPanelGetSSHCAPublicKeyRequest)

ControlPanelGetSSHCAPublicKeyResponse = _reflection.GeneratedProtocolMessageType('ControlPanelGetSSHCAPublicKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelGetSSHCAPublicKeyResponse)
  })
_sym_db.RegisterMessage(ControlPanelGetSSHCAPublicKeyResponse)

ControlPanelVerifyJWTRequest = _reflection.GeneratedProtocolMessageType('ControlPanelVerifyJWTRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELVERIFYJWTREQUEST,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelVerifyJWTRequest)
  })
_sym_db.RegisterMessage(ControlPanelVerifyJWTRequest)

ControlPanelVerifyJWTResponse = _reflection.GeneratedProtocolMessageType('ControlPanelVerifyJWTResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELVERIFYJWTRESPONSE,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelVerifyJWTResponse)
  })
_sym_db.RegisterMessage(ControlPanelVerifyJWTResponse)

_CONTROLPANEL = DESCRIPTOR.services_by_name['ControlPanel']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\024ControlPanelPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['meta']._options = None
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['public_key']._options = None
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['public_key']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['rate_limit']._options = None
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE._options = None
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _CONTROLPANELVERIFYJWTREQUEST.fields_by_name['token']._options = None
  _CONTROLPANELVERIFYJWTREQUEST.fields_by_name['token']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['meta']._options = None
  _CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['valid']._options = None
  _CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['valid']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['rate_limit']._options = None
  _CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _CONTROLPANELVERIFYJWTRESPONSE._options = None
  _CONTROLPANELVERIFYJWTRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _CONTROLPANEL.methods_by_name['GetSSHCAPublicKey']._options = None
  _CONTROLPANEL.methods_by_name['GetSSHCAPublicKey']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\035\252\363\263\007\030/v1/control-panel/ssh/ca'
  _CONTROLPANEL.methods_by_name['VerifyJWT']._options = None
  _CONTROLPANEL.methods_by_name['VerifyJWT']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\"\252\363\263\007\035/v1/control-panel/http/verify'
  _CONTROLPANELGETSSHCAPUBLICKEYREQUEST._serialized_start=54
  _CONTROLPANELGETSSHCAPUBLICKEYREQUEST._serialized_end=130
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE._serialized_start=133
  _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE._serialized_end=356
  _CONTROLPANELVERIFYJWTREQUEST._serialized_start=358
  _CONTROLPANELVERIFYJWTREQUEST._serialized_end=453
  _CONTROLPANELVERIFYJWTRESPONSE._serialized_start=456
  _CONTROLPANELVERIFYJWTRESPONSE._serialized_end=666
  _CONTROLPANEL._serialized_start=669
  _CONTROLPANEL._serialized_end=977
# @@protoc_insertion_point(module_scope)
