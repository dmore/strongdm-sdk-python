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
# source: account_attachments.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='account_attachments.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\032AccountAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x61\x63\x63ount_attachments.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x9b\x01\n\x1e\x41\x63\x63ountAttachmentCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x11\xfa\xf8\xb3\x07\x0c\xba\xf3\xb3\x07\x07options\"\xdf\x02\n\x1f\x41\x63\x63ountAttachmentCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"[\n\x1b\x41\x63\x63ountAttachmentGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd9\x02\n\x1c\x41\x63\x63ountAttachmentGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"a\n\x1e\x41\x63\x63ountAttachmentDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xa0\x02\n\x1f\x41\x63\x63ountAttachmentDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"a\n\x1c\x41\x63\x63ountAttachmentListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xc4\x02\n\x1d\x41\x63\x63ountAttachmentListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12>\n\x13\x61\x63\x63ount_attachments\x18\x02 \x03(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript\"\xe6\x01\n\x11\x41\x63\x63ountAttachment\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12#\n\naccount_id\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12 \n\x07role_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01:r\xfa\xf8\xb3\x07m\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07\x63\xa2\xf3\xb3\x07+tf_examples/account_attachment_resource.txt\xaa\xf3\xb3\x07.tf_examples/account_attachment_data_source.txt2\xcb\x04\n\x12\x41\x63\x63ountAttachments\x12\x82\x01\n\x06\x43reate\x12\".v1.AccountAttachmentCreateRequest\x1a#.v1.AccountAttachmentCreateResponse\"/\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-attachments\x12}\n\x03Get\x12\x1f.v1.AccountAttachmentGetRequest\x1a .v1.AccountAttachmentGetResponse\"3\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07!\xaa\xf3\xb3\x07\x1c/v1/account-attachments/{id}\x12\x89\x01\n\x06\x44\x65lete\x12\".v1.AccountAttachmentDeleteRequest\x1a#.v1.AccountAttachmentDeleteResponse\"6\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07!\xaa\xf3\xb3\x07\x1c/v1/account-attachments/{id}\x12{\n\x04List\x12 .v1.AccountAttachmentListRequest\x1a!.v1.AccountAttachmentListResponse\".\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-attachments\x1a(\xca\xf9\xb3\x07\x16\xc2\xf9\xb3\x07\x11\x41\x63\x63ountAttachment\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03\x61\x61-Bq\n\x1c\x63om.strongdm.api.v1.plumbingB\x1a\x41\x63\x63ountAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1b\x06proto3'
  ,
  dependencies=[options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_ACCOUNTATTACHMENTCREATEREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentCreateRequest',
  full_name='v1.AccountAttachmentCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_attachment', full_name='v1.AccountAttachmentCreateRequest.account_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\014\272\363\263\007\007options',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=216,
)


_ACCOUNTATTACHMENTCREATERESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentCreateResponse',
  full_name='v1.AccountAttachmentCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_attachment', full_name='v1.AccountAttachmentCreateResponse.account_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentCreateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=570,
)


_ACCOUNTATTACHMENTGETREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentGetRequest',
  full_name='v1.AccountAttachmentGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountAttachmentGetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=572,
  serialized_end=663,
)


_ACCOUNTATTACHMENTGETRESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentGetResponse',
  full_name='v1.AccountAttachmentGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_attachment', full_name='v1.AccountAttachmentGetResponse.account_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentGetResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=1011,
)


_ACCOUNTATTACHMENTDELETEREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentDeleteRequest',
  full_name='v1.AccountAttachmentDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountAttachmentDeleteRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1013,
  serialized_end=1110,
)


_ACCOUNTATTACHMENTDELETERESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentDeleteResponse',
  full_name='v1.AccountAttachmentDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1113,
  serialized_end=1401,
)


_ACCOUNTATTACHMENTLISTREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentListRequest',
  full_name='v1.AccountAttachmentListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.AccountAttachmentListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1403,
  serialized_end=1500,
)


_ACCOUNTATTACHMENTLISTRESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentListResponse',
  full_name='v1.AccountAttachmentListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_attachments', full_name='v1.AccountAttachmentListResponse.account_attachments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\270\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentListResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1503,
  serialized_end=1827,
)


_ACCOUNTATTACHMENT = _descriptor.Descriptor(
  name='AccountAttachment',
  full_name='v1.AccountAttachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountAttachment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='v1.AccountAttachment.account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='v1.AccountAttachment.role_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007m\250\363\263\007\001\302\363\263\007c\242\363\263\007+tf_examples/account_attachment_resource.txt\252\363\263\007.tf_examples/account_attachment_data_source.txt',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1830,
  serialized_end=2060,
)

_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['account_attachment'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['account_attachment'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTATTACHMENTGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['account_attachment'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTATTACHMENTDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTATTACHMENTLISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['account_attachments'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
DESCRIPTOR.message_types_by_name['AccountAttachmentCreateRequest'] = _ACCOUNTATTACHMENTCREATEREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentCreateResponse'] = _ACCOUNTATTACHMENTCREATERESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachmentGetRequest'] = _ACCOUNTATTACHMENTGETREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentGetResponse'] = _ACCOUNTATTACHMENTGETRESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachmentDeleteRequest'] = _ACCOUNTATTACHMENTDELETEREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentDeleteResponse'] = _ACCOUNTATTACHMENTDELETERESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachmentListRequest'] = _ACCOUNTATTACHMENTLISTREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentListResponse'] = _ACCOUNTATTACHMENTLISTRESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachment'] = _ACCOUNTATTACHMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountAttachmentCreateRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATEREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateRequest)

AccountAttachmentCreateResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATERESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateResponse)

AccountAttachmentGetRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTGETREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentGetRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentGetRequest)

AccountAttachmentGetResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTGETRESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentGetResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentGetResponse)

AccountAttachmentDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTDELETEREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentDeleteRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentDeleteRequest)

AccountAttachmentDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTDELETERESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentDeleteResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentDeleteResponse)

AccountAttachmentListRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTLISTREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentListRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentListRequest)

AccountAttachmentListResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTLISTRESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentListResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentListResponse)

AccountAttachment = _reflection.GeneratedProtocolMessageType('AccountAttachment', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENT,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachment)
  })
_sym_db.RegisterMessage(AccountAttachment)


DESCRIPTOR._options = None
_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['account_attachment']._options = None
_ACCOUNTATTACHMENTCREATEREQUEST._options = None
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['account_attachment']._options = None
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENTCREATERESPONSE._options = None
_ACCOUNTATTACHMENTGETREQUEST.fields_by_name['id']._options = None
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['meta']._options = None
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['account_attachment']._options = None
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENTGETRESPONSE._options = None
_ACCOUNTATTACHMENTDELETEREQUEST.fields_by_name['id']._options = None
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENTDELETERESPONSE._options = None
_ACCOUNTATTACHMENTLISTREQUEST.fields_by_name['filter']._options = None
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['account_attachments']._options = None
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENT.fields_by_name['id']._options = None
_ACCOUNTATTACHMENT.fields_by_name['account_id']._options = None
_ACCOUNTATTACHMENT.fields_by_name['role_id']._options = None
_ACCOUNTATTACHMENT._options = None

_ACCOUNTATTACHMENTS = _descriptor.ServiceDescriptor(
  name='AccountAttachments',
  full_name='v1.AccountAttachments',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312\371\263\007\026\302\371\263\007\021AccountAttachment\312\371\263\007\010\322\371\263\007\003aa-',
  create_key=_descriptor._internal_create_key,
  serialized_start=2063,
  serialized_end=2650,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.AccountAttachments.Create',
    index=0,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTCREATEREQUEST,
    output_type=_ACCOUNTATTACHMENTCREATERESPONSE,
    serialized_options=b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\034\252\363\263\007\027/v1/account-attachments',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.AccountAttachments.Get',
    index=1,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTGETREQUEST,
    output_type=_ACCOUNTATTACHMENTGETRESPONSE,
    serialized_options=b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007!\252\363\263\007\034/v1/account-attachments/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.AccountAttachments.Delete',
    index=2,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTDELETEREQUEST,
    output_type=_ACCOUNTATTACHMENTDELETERESPONSE,
    serialized_options=b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007!\252\363\263\007\034/v1/account-attachments/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.AccountAttachments.List',
    index=3,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTLISTREQUEST,
    output_type=_ACCOUNTATTACHMENTLISTRESPONSE,
    serialized_options=b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\034\252\363\263\007\027/v1/account-attachments',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTATTACHMENTS)

DESCRIPTOR.services_by_name['AccountAttachments'] = _ACCOUNTATTACHMENTS

# @@protoc_insertion_point(module_scope)
