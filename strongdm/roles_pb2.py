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

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2
from . import tags_pb2 as tags__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='roles.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.strongdm.api.v1.plumbingB\rRolesPlumbing'),
  serialized_pb=_b('\n\x0broles.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\roptions.proto\x1a\nspec.proto\x1a\ntags.proto\"`\n\x11RoleCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb1\x01\n\x12RoleCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"N\n\x0eRoleGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xab\x01\n\x0fRoleGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"l\n\x11RoleUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12\"\n\x04role\x18\x03 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb1\x01\n\x12RoleUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04role\x18\x02 \x01(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"T\n\x11RoleDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x8d\x01\n\x12RoleDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"T\n\x0fRoleListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x96\x01\n\x10RoleListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12#\n\x05roles\x18\x02 \x03(\x0b\x32\x08.v1.RoleB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xc2\x02\n\x04Role\x12&\n\x02id\x18\x01 \x01(\tB\x1a\xf2\xf8\xb3\x07\x15\xa2\xf3\xb3\x07\x02ID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04Role\x12&\n\x04name\x18\x02 \x01(\tB\x18\xf2\xf8\xb3\x07\x13\xa2\xf3\xb3\x07\x04Name\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x30\n\tcomposite\x18\x03 \x01(\x08\x42\x1d\xf2\xf8\xb3\x07\x18\xa2\xf3\xb3\x07\tComposite\xb0\xf3\xb3\x07\x01\xe0\xf3\xb3\x07\x01\x12+\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\x13\xf2\xf8\xb3\x07\x0e\xa2\xf3\xb3\x07\x04Tags\xb0\xf3\xb3\x07\x01:\x8a\x01\xfa\xf8\xb3\x07Z\xa2\xf3\xb3\x07\x04Role\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07G\xa2\xf3\xb3\x07\x1dtf_examples/role_resource.txt\xaa\xf3\xb3\x07 tf_examples/role_data_source.txt\x92\x41(2&\x12${ \"id\": \"r-7\", \"name\": \"happy-goat\"}2\xf2\x03\n\x05Roles\x12\xa5\x01\n\x06\x43reate\x12\x15.v1.RoleCreateRequest\x1a\x16.v1.RoleCreateResponse\"l\x82\xd3\xe4\x93\x02\x0e\"\t/v1/roles:\x01*\x92\x41U\"S\n\x18Learn how to make a Role\x12\x37https://www.strongdm.com/docs/api/services/Roles#Create\x12\x46\n\x03Get\x12\x12.v1.RoleGetRequest\x1a\x13.v1.RoleGetResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/roles/{id}\x12R\n\x06Update\x12\x15.v1.RoleUpdateRequest\x1a\x16.v1.RoleUpdateResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x1a\x0e/v1/roles/{id}:\x01*\x12O\n\x06\x44\x65lete\x12\x15.v1.RoleDeleteRequest\x1a\x16.v1.RoleDeleteResponse\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v1/roles/{id}\x12\x44\n\x04List\x12\x13.v1.RoleListRequest\x1a\x14.v1.RoleListResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/roles\x1a\x0e\xca\xf9\xb3\x07\t\xc2\xf9\xb3\x07\x04RoleB-\n\x1c\x63om.strongdm.api.v1.plumbingB\rRolesPlumbingb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,tags__pb2.DESCRIPTOR,])




_ROLECREATEREQUEST = _descriptor.Descriptor(
  name='RoleCreateRequest',
  full_name='v1.RoleCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleCreateRequest.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=134,
  serialized_end=230,
)


_ROLECREATERESPONSE = _descriptor.Descriptor(
  name='RoleCreateResponse',
  full_name='v1.RoleCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleCreateResponse.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleCreateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=410,
)


_ROLEGETREQUEST = _descriptor.Descriptor(
  name='RoleGetRequest',
  full_name='v1.RoleGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleGetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=412,
  serialized_end=490,
)


_ROLEGETRESPONSE = _descriptor.Descriptor(
  name='RoleGetResponse',
  full_name='v1.RoleGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleGetResponse.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleGetResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=664,
)


_ROLEUPDATEREQUEST = _descriptor.Descriptor(
  name='RoleUpdateRequest',
  full_name='v1.RoleUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleUpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleUpdateRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleUpdateRequest.role', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=666,
  serialized_end=774,
)


_ROLEUPDATERESPONSE = _descriptor.Descriptor(
  name='RoleUpdateResponse',
  full_name='v1.RoleUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleUpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='v1.RoleUpdateResponse.role', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleUpdateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=777,
  serialized_end=954,
)


_ROLEDELETEREQUEST = _descriptor.Descriptor(
  name='RoleDeleteRequest',
  full_name='v1.RoleDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleDeleteRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=956,
  serialized_end=1040,
)


_ROLEDELETERESPONSE = _descriptor.Descriptor(
  name='RoleDeleteResponse',
  full_name='v1.RoleDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1043,
  serialized_end=1184,
)


_ROLELISTREQUEST = _descriptor.Descriptor(
  name='RoleListRequest',
  full_name='v1.RoleListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.RoleListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=1186,
  serialized_end=1270,
)


_ROLELISTRESPONSE = _descriptor.Descriptor(
  name='RoleListResponse',
  full_name='v1.RoleListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roles', full_name='v1.RoleListResponse.roles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\270\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleListResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=1273,
  serialized_end=1423,
)


_ROLE = _descriptor.Descriptor(
  name='Role',
  full_name='v1.Role',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.Role.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\025\242\363\263\007\002ID\260\363\263\007\001\312\363\263\007\004Role'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Role.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\023\242\363\263\007\004Name\260\363\263\007\001\300\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='composite', full_name='v1.Role.composite', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\030\242\363\263\007\tComposite\260\363\263\007\001\340\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.Role.tags', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\016\242\363\263\007\004Tags\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007Z\242\363\263\007\004Role\250\363\263\007\001\302\363\263\007G\242\363\263\007\035tf_examples/role_resource.txt\252\363\263\007 tf_examples/role_data_source.txt\222A(2&\022${ \"id\": \"r-7\", \"name\": \"happy-goat\"}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1426,
  serialized_end=1748,
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
_ROLE.fields_by_name['composite']._options = None
_ROLE.fields_by_name['tags']._options = None
_ROLE._options = None

_ROLES = _descriptor.ServiceDescriptor(
  name='Roles',
  full_name='v1.Roles',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312\371\263\007\t\302\371\263\007\004Role'),
  serialized_start=1751,
  serialized_end=2249,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.Roles.Create',
    index=0,
    containing_service=None,
    input_type=_ROLECREATEREQUEST,
    output_type=_ROLECREATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\"\t/v1/roles:\001*\222AU\"S\n\030Learn how to make a Role\0227https://www.strongdm.com/docs/api/services/Roles#Create'),
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.Roles.Get',
    index=1,
    containing_service=None,
    input_type=_ROLEGETREQUEST,
    output_type=_ROLEGETRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/roles/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='v1.Roles.Update',
    index=2,
    containing_service=None,
    input_type=_ROLEUPDATEREQUEST,
    output_type=_ROLEUPDATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\032\016/v1/roles/{id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.Roles.Delete',
    index=3,
    containing_service=None,
    input_type=_ROLEDELETEREQUEST,
    output_type=_ROLEDELETERESPONSE,
    serialized_options=_b('\202\323\344\223\002\020*\016/v1/roles/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.Roles.List',
    index=4,
    containing_service=None,
    input_type=_ROLELISTREQUEST,
    output_type=_ROLELISTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\013\022\t/v1/roles'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLES)

DESCRIPTOR.services_by_name['Roles'] = _ROLES

# @@protoc_insertion_point(module_scope)
