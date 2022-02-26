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
# source: roles.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2
from . import tags_pb2 as tags__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='roles.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\rRolesPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0broles.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\x1a\ntags.proto\"`\n\x11RoleCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbb\x01\n\x12RoleCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"N\n\x0eRoleGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb5\x01\n\x0fRoleGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"l\n\x11RoleUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12\"\n\x04role\x18\x03 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbb\x01\n\x12RoleUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"T\n\x11RoleDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x97\x01\n\x12RoleDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"T\n\x0fRoleListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xa0\x01\n\x10RoleListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12#\n\x05roles\x18\x02 \x03(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01\"\xd3\x03\n\x04Role\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\xf1\x01\n\x0c\x61\x63\x63\x65ss_rules\x18\x05 \x01(\tB\xda\x01\xf2\xf8\xb3\x07\xd4\x01\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07M\xea\xf3\xb3\x07\x0c\x61\x63\x63\x65ss_rules\xf2\xf3\xb3\x07\x0b\x41\x63\x63\x65ssRules\xfa\xf3\xb3\x07\x10List<AccessRule>\x9a\xf4\xb3\x07\x12models.AccessRules\xb2\xf4\xb3\x07\ngo_private\xb2\xf4\xb3\x07\x02go\xb2\xf4\xb3\x07\x06python\xb2\xf4\xb3\x07\x04java\xb2\xf4\xb3\x07\x04ruby\xb2\xf4\xb3\x07\x0cjson_gateway\xb2\xf4\xb3\x07\x14json_gateway_private\xb2\xf4\xb3\x07\x07openapi\xb2\xf4\xb3\x07\x0fopenapi_private\x12$\n\tcomposite\x18\x03 \x01(\x08\x42\x11\x18\x01\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xe0\xf3\xb3\x07\x01\x12\"\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:V\xfa\xf8\xb3\x07Q\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07G\xa2\xf3\xb3\x07\x1dtf_examples/role_resource.txt\xaa\xf3\xb3\x07 tf_examples/role_data_source.txt2\xee\x03\n\x05Roles\x12Z\n\x06\x43reate\x12\x15.v1.RoleCreateRequest\x1a\x16.v1.RoleCreateResponse\"!\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x0e\xaa\xf3\xb3\x07\t/v1/roles\x12U\n\x03Get\x12\x12.v1.RoleGetRequest\x1a\x13.v1.RoleGetResponse\"%\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/roles/{id}\x12^\n\x06Update\x12\x15.v1.RoleUpdateRequest\x1a\x16.v1.RoleUpdateResponse\"%\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/roles/{id}\x12\x61\n\x06\x44\x65lete\x12\x15.v1.RoleDeleteRequest\x1a\x16.v1.RoleDeleteResponse\"(\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/roles/{id}\x12S\n\x04List\x12\x13.v1.RoleListRequest\x1a\x14.v1.RoleListResponse\" \x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x0e\xaa\xf3\xb3\x07\t/v1/roles\x1a\x1a\xca\xf9\xb3\x07\t\xc2\xf9\xb3\x07\x04Role\xca\xf9\xb3\x07\x07\xd2\xf9\xb3\x07\x02r-Ba\n\x1c\x63om.strongdm.api.v1.plumbingB\rRolesPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1b\x06proto3'
  ,
  dependencies=[options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,tags__pb2.DESCRIPTOR,])




_ROLECREATEREQUEST = _descriptor.Descriptor(
  name='RoleCreateRequest',
  full_name='v1.RoleCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleCreateRequest.role', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=154,
)


_ROLECREATERESPONSE = _descriptor.Descriptor(
  name='RoleCreateResponse',
  full_name='v1.RoleCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleCreateResponse.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleCreateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=157,
  serialized_end=344,
)


_ROLEGETREQUEST = _descriptor.Descriptor(
  name='RoleGetRequest',
  full_name='v1.RoleGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleGetRequest.id', index=1,
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
  serialized_start=346,
  serialized_end=424,
)


_ROLEGETRESPONSE = _descriptor.Descriptor(
  name='RoleGetResponse',
  full_name='v1.RoleGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleGetResponse.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleGetResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=427,
  serialized_end=608,
)


_ROLEUPDATEREQUEST = _descriptor.Descriptor(
  name='RoleUpdateRequest',
  full_name='v1.RoleUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleUpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleUpdateRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleUpdateRequest.role', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=718,
)


_ROLEUPDATERESPONSE = _descriptor.Descriptor(
  name='RoleUpdateResponse',
  full_name='v1.RoleUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleUpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleUpdateResponse.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleUpdateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=721,
  serialized_end=908,
)


_ROLEDELETEREQUEST = _descriptor.Descriptor(
  name='RoleDeleteRequest',
  full_name='v1.RoleDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleDeleteRequest.id', index=1,
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
  serialized_start=910,
  serialized_end=994,
)


_ROLEDELETERESPONSE = _descriptor.Descriptor(
  name='RoleDeleteResponse',
  full_name='v1.RoleDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=997,
  serialized_end=1148,
)


_ROLELISTREQUEST = _descriptor.Descriptor(
  name='RoleListRequest',
  full_name='v1.RoleListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.RoleListRequest.filter', index=1,
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
  serialized_start=1150,
  serialized_end=1234,
)


_ROLELISTRESPONSE = _descriptor.Descriptor(
  name='RoleListResponse',
  full_name='v1.RoleListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roles', full_name='v1.RoleListResponse.roles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\270\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleListResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1237,
  serialized_end=1397,
)


_ROLE = _descriptor.Descriptor(
  name='Role',
  full_name='v1.Role',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.Role.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Role.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_rules', full_name='v1.Role.access_rules', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\324\001\260\363\263\007\001\312\363\263\007M\352\363\263\007\014access_rules\362\363\263\007\013AccessRules\372\363\263\007\020List<AccessRule>\232\364\263\007\022models.AccessRules\262\364\263\007\ngo_private\262\364\263\007\002go\262\364\263\007\006python\262\364\263\007\004java\262\364\263\007\004ruby\262\364\263\007\014json_gateway\262\364\263\007\024json_gateway_private\262\364\263\007\007openapi\262\364\263\007\017openapi_private', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='composite', full_name='v1.Role.composite', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001\362\370\263\007\n\260\363\263\007\001\340\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.Role.tags', index=4,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\372\370\263\007Q\250\363\263\007\001\302\363\263\007G\242\363\263\007\035tf_examples/role_resource.txt\252\363\263\007 tf_examples/role_data_source.txt',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1867,
)

_ROLECREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ROLECREATEREQUEST.fields_by_name['role'].message_type = _ROLE
_ROLECREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ROLECREATERESPONSE.fields_by_name['role'].message_type = _ROLE
_ROLECREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ROLEGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ROLEGETRESPONSE.fields_by_name['role'].message_type = _ROLE
_ROLEGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEUPDATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._UPDATEREQUESTMETADATA
_ROLEUPDATEREQUEST.fields_by_name['role'].message_type = _ROLE
_ROLEUPDATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._UPDATERESPONSEMETADATA
_ROLEUPDATERESPONSE.fields_by_name['role'].message_type = _ROLE
_ROLEUPDATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ROLEDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ROLEDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLELISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ROLELISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ROLELISTRESPONSE.fields_by_name['roles'].message_type = _ROLE
_ROLELISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLE.fields_by_name['tags'].message_type = tags__pb2._TAGS
DESCRIPTOR.message_types_by_name['RoleCreateRequest'] = _ROLECREATEREQUEST
DESCRIPTOR.message_types_by_name['RoleCreateResponse'] = _ROLECREATERESPONSE
DESCRIPTOR.message_types_by_name['RoleGetRequest'] = _ROLEGETREQUEST
DESCRIPTOR.message_types_by_name['RoleGetResponse'] = _ROLEGETRESPONSE
DESCRIPTOR.message_types_by_name['RoleUpdateRequest'] = _ROLEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['RoleUpdateResponse'] = _ROLEUPDATERESPONSE
DESCRIPTOR.message_types_by_name['RoleDeleteRequest'] = _ROLEDELETEREQUEST
DESCRIPTOR.message_types_by_name['RoleDeleteResponse'] = _ROLEDELETERESPONSE
DESCRIPTOR.message_types_by_name['RoleListRequest'] = _ROLELISTREQUEST
DESCRIPTOR.message_types_by_name['RoleListResponse'] = _ROLELISTRESPONSE
DESCRIPTOR.message_types_by_name['Role'] = _ROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleCreateRequest = _reflection.GeneratedProtocolMessageType('RoleCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLECREATEREQUEST,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleCreateRequest)
  })
_sym_db.RegisterMessage(RoleCreateRequest)

RoleCreateResponse = _reflection.GeneratedProtocolMessageType('RoleCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLECREATERESPONSE,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleCreateResponse)
  })
_sym_db.RegisterMessage(RoleCreateResponse)

RoleGetRequest = _reflection.GeneratedProtocolMessageType('RoleGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGETREQUEST,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGetRequest)
  })
_sym_db.RegisterMessage(RoleGetRequest)

RoleGetResponse = _reflection.GeneratedProtocolMessageType('RoleGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGETRESPONSE,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGetResponse)
  })
_sym_db.RegisterMessage(RoleGetResponse)

RoleUpdateRequest = _reflection.GeneratedProtocolMessageType('RoleUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEUPDATEREQUEST,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleUpdateRequest)
  })
_sym_db.RegisterMessage(RoleUpdateRequest)

RoleUpdateResponse = _reflection.GeneratedProtocolMessageType('RoleUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEUPDATERESPONSE,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleUpdateResponse)
  })
_sym_db.RegisterMessage(RoleUpdateResponse)

RoleDeleteRequest = _reflection.GeneratedProtocolMessageType('RoleDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEDELETEREQUEST,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleDeleteRequest)
  })
_sym_db.RegisterMessage(RoleDeleteRequest)

RoleDeleteResponse = _reflection.GeneratedProtocolMessageType('RoleDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEDELETERESPONSE,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleDeleteResponse)
  })
_sym_db.RegisterMessage(RoleDeleteResponse)

RoleListRequest = _reflection.GeneratedProtocolMessageType('RoleListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLELISTREQUEST,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleListRequest)
  })
_sym_db.RegisterMessage(RoleListRequest)

RoleListResponse = _reflection.GeneratedProtocolMessageType('RoleListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLELISTRESPONSE,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleListResponse)
  })
_sym_db.RegisterMessage(RoleListResponse)

Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), {
  'DESCRIPTOR' : _ROLE,
  '__module__' : 'roles_pb2'
  # @@protoc_insertion_point(class_scope:v1.Role)
  })
_sym_db.RegisterMessage(Role)


DESCRIPTOR._options = None
_ROLECREATEREQUEST.fields_by_name['role']._options = None
_ROLECREATERESPONSE.fields_by_name['meta']._options = None
_ROLECREATERESPONSE.fields_by_name['role']._options = None
_ROLECREATERESPONSE.fields_by_name['rate_limit']._options = None
_ROLECREATERESPONSE._options = None
_ROLEGETREQUEST.fields_by_name['id']._options = None
_ROLEGETRESPONSE.fields_by_name['meta']._options = None
_ROLEGETRESPONSE.fields_by_name['role']._options = None
_ROLEGETRESPONSE.fields_by_name['rate_limit']._options = None
_ROLEGETRESPONSE._options = None
_ROLEUPDATEREQUEST.fields_by_name['role']._options = None
_ROLEUPDATERESPONSE.fields_by_name['meta']._options = None
_ROLEUPDATERESPONSE.fields_by_name['role']._options = None
_ROLEUPDATERESPONSE.fields_by_name['rate_limit']._options = None
_ROLEUPDATERESPONSE._options = None
_ROLEDELETEREQUEST.fields_by_name['id']._options = None
_ROLEDELETERESPONSE.fields_by_name['meta']._options = None
_ROLEDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ROLEDELETERESPONSE._options = None
_ROLELISTREQUEST.fields_by_name['filter']._options = None
_ROLELISTRESPONSE.fields_by_name['roles']._options = None
_ROLELISTRESPONSE.fields_by_name['rate_limit']._options = None
_ROLE.fields_by_name['id']._options = None
_ROLE.fields_by_name['name']._options = None
_ROLE.fields_by_name['access_rules']._options = None
_ROLE.fields_by_name['composite']._options = None
_ROLE.fields_by_name['tags']._options = None
_ROLE._options = None

_ROLES = _descriptor.ServiceDescriptor(
  name='Roles',
  full_name='v1.Roles',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312\371\263\007\t\302\371\263\007\004Role\312\371\263\007\007\322\371\263\007\002r-',
  create_key=_descriptor._internal_create_key,
  serialized_start=1870,
  serialized_end=2364,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.Roles.Create',
    index=0,
    containing_service=None,
    input_type=_ROLECREATEREQUEST,
    output_type=_ROLECREATERESPONSE,
    serialized_options=b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\016\252\363\263\007\t/v1/roles',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.Roles.Get',
    index=1,
    containing_service=None,
    input_type=_ROLEGETREQUEST,
    output_type=_ROLEGETRESPONSE,
    serialized_options=b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\023\252\363\263\007\016/v1/roles/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='v1.Roles.Update',
    index=2,
    containing_service=None,
    input_type=_ROLEUPDATEREQUEST,
    output_type=_ROLEUPDATERESPONSE,
    serialized_options=b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007\023\252\363\263\007\016/v1/roles/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.Roles.Delete',
    index=3,
    containing_service=None,
    input_type=_ROLEDELETEREQUEST,
    output_type=_ROLEDELETERESPONSE,
    serialized_options=b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\023\252\363\263\007\016/v1/roles/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.Roles.List',
    index=4,
    containing_service=None,
    input_type=_ROLELISTREQUEST,
    output_type=_ROLELISTRESPONSE,
    serialized_options=b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\016\252\363\263\007\t/v1/roles',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLES)

DESCRIPTOR.services_by_name['Roles'] = _ROLES

# @@protoc_insertion_point(module_scope)
