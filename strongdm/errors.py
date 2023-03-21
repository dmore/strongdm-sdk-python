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
# Code generated by protogen. DO NOT EDIT.


class RPCError(Exception):
    '''A generic RPC error'''
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


class AlreadyExistsError(RPCError):
    '''Used when an entity already exists in the system'''
    def __init__(self, msg):
        super().__init__(msg, 6)


class NotFoundError(RPCError):
    '''Used when an entity does not exist in the system'''
    def __init__(self, msg):
        super().__init__(msg, 5)


class BadRequestError(RPCError):
    '''Identifies a bad request sent by the client'''
    def __init__(self, msg):
        super().__init__(msg, 3)


class AuthenticationError(RPCError):
    '''Used to specify an authentication failure condition'''
    def __init__(self, msg):
        super().__init__(msg, 16)


class PermissionError(RPCError):
    '''Used to specify a permissions violation'''
    def __init__(self, msg):
        super().__init__(msg, 7)


class InternalError(RPCError):
    '''Used to specify an internal system error'''
    def __init__(self, msg):
        super().__init__(msg, 13)


class RateLimitError(RPCError):
    '''Used when rate limit is exceeded'''
    def __init__(self, msg, rate_limit):
        super().__init__(msg, 8)
        self.rate_limit = rate_limit


class TimeoutError(RPCError):
    '''Used when a request takes too long'''
    def __init__(self):
        super().__init__('deadline exceeded', 4)


class UnknownError(RPCError):
    '''Generic wrapper that indicates an unknown internal error in the SDK.'''
    def __init__(self, msg):
        super().__init__(msg, 2)
