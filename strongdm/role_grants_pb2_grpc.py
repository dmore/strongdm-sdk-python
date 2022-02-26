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
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import role_grants_pb2 as role__grants__pb2


class RoleGrantsStub(object):
    """RoleGrants represent relationships between composite roles and the roles
    that make up those composite roles. When a composite role is attached to another
    role, the permissions granted to members of the composite role are augmented to
    include the permissions granted to members of the attached role.

    Deprecated: use access rules instead.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.RoleGrants/Create',
                request_serializer=role__grants__pb2.RoleGrantCreateRequest.SerializeToString,
                response_deserializer=role__grants__pb2.RoleGrantCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.RoleGrants/Get',
                request_serializer=role__grants__pb2.RoleGrantGetRequest.SerializeToString,
                response_deserializer=role__grants__pb2.RoleGrantGetResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.RoleGrants/Delete',
                request_serializer=role__grants__pb2.RoleGrantDeleteRequest.SerializeToString,
                response_deserializer=role__grants__pb2.RoleGrantDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.RoleGrants/List',
                request_serializer=role__grants__pb2.RoleGrantListRequest.SerializeToString,
                response_deserializer=role__grants__pb2.RoleGrantListResponse.FromString,
                )


class RoleGrantsServicer(object):
    """RoleGrants represent relationships between composite roles and the roles
    that make up those composite roles. When a composite role is attached to another
    role, the permissions granted to members of the composite role are augmented to
    include the permissions granted to members of the attached role.

    Deprecated: use access rules instead.
    """

    def Create(self, request, context):
        """Create registers a new RoleGrant.

        Deprecated: use access rules instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one RoleGrant by ID.

        Deprecated: use access rules instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete removes a RoleGrant by ID.

        Deprecated: use access rules instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List gets a list of RoleGrants matching a given set of criteria.

        Deprecated: use access rules instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoleGrantsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=role__grants__pb2.RoleGrantCreateRequest.FromString,
                    response_serializer=role__grants__pb2.RoleGrantCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=role__grants__pb2.RoleGrantGetRequest.FromString,
                    response_serializer=role__grants__pb2.RoleGrantGetResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=role__grants__pb2.RoleGrantDeleteRequest.FromString,
                    response_serializer=role__grants__pb2.RoleGrantDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=role__grants__pb2.RoleGrantListRequest.FromString,
                    response_serializer=role__grants__pb2.RoleGrantListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.RoleGrants', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoleGrants(object):
    """RoleGrants represent relationships between composite roles and the roles
    that make up those composite roles. When a composite role is attached to another
    role, the permissions granted to members of the composite role are augmented to
    include the permissions granted to members of the attached role.

    Deprecated: use access rules instead.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.RoleGrants/Create',
            role__grants__pb2.RoleGrantCreateRequest.SerializeToString,
            role__grants__pb2.RoleGrantCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.RoleGrants/Get',
            role__grants__pb2.RoleGrantGetRequest.SerializeToString,
            role__grants__pb2.RoleGrantGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.RoleGrants/Delete',
            role__grants__pb2.RoleGrantDeleteRequest.SerializeToString,
            role__grants__pb2.RoleGrantDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.RoleGrants/List',
            role__grants__pb2.RoleGrantListRequest.SerializeToString,
            role__grants__pb2.RoleGrantListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
