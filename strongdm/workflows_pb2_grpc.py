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

from . import workflows_pb2 as workflows__pb2


class WorkflowsStub(object):
    """Workflows are the collection of rules that define the resources to which access can be requested,
    the users that can request that access, and the mechanism for approving those requests which can either
    but automatic approval or a set of users authorized to approve the requests.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/v1.Workflows/List',
                request_serializer=workflows__pb2.WorkflowListRequest.SerializeToString,
                response_deserializer=workflows__pb2.WorkflowListResponse.FromString,
                )


class WorkflowsServicer(object):
    """Workflows are the collection of rules that define the resources to which access can be requested,
    the users that can request that access, and the mechanism for approving those requests which can either
    but automatic approval or a set of users authorized to approve the requests.
    """

    def List(self, request, context):
        """Lists existing workflows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkflowsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=workflows__pb2.WorkflowListRequest.FromString,
                    response_serializer=workflows__pb2.WorkflowListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.Workflows', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Workflows(object):
    """Workflows are the collection of rules that define the resources to which access can be requested,
    the users that can request that access, and the mechanism for approving those requests which can either
    but automatic approval or a set of users authorized to approve the requests.
    """

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
        return grpc.experimental.unary_unary(request, target, '/v1.Workflows/List',
            workflows__pb2.WorkflowListRequest.SerializeToString,
            workflows__pb2.WorkflowListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
