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

# This file was generated by protogen. DO NOT EDIT.

import grpc
import hmac
import random
import hashlib
import base64
import datetime
import time
from . import svc
from . import plumbing

# These defaults are taken from AWS. Customization of these values
# is a future step in the API.
DEFAULT_MAX_RETRIES = 3
DEFAULT_BASE_RETRY_DELAY = 0.0030  # 30 ms
DEFAULT_MAX_RETRY_DELAY = 300  # 300 seconds
API_VERSION = '2021-08-23'
USER_AGENT = 'strongdm-sdk-python/2.1.0'


class Client:
    '''Client interacts with the strongDM API.'''
    def __init__(self,
                 api_access_key,
                 api_secret,
                 host='api.strongdm.com:443',
                 insecure=False):
        '''
        Create a new Client.

        - api_access_key: the access key to authenticate with strongDM
        - api_secret: the secret key to authenticate with strongDM
        '''
        self.api_access_key = api_access_key.strip()
        self.api_secret = base64.b64decode(api_secret.strip())
        self.max_retries = DEFAULT_MAX_RETRIES
        self.base_retry_delay = DEFAULT_BASE_RETRY_DELAY
        self.max_retry_delay = DEFAULT_MAX_RETRY_DELAY
        self._test_options = {}

        try:
            if insecure:
                channel = grpc.insecure_channel(host)
            else:
                creds = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(host, creds)
        except Exception as e:
            raise plumbing.convert_error_to_porcelain(e) from e
        self.account_attachments = svc.AccountAttachments(channel, self)
        '''
         AccountAttachments assign an account to a role.

        See `strongdm.svc.AccountAttachments`.
        '''
        self.account_grants = svc.AccountGrants(channel, self)
        '''
         AccountGrants assign a resource directly to an account, giving the account the permission to connect to that resource.

        See `strongdm.svc.AccountGrants`.
        '''
        self.accounts = svc.Accounts(channel, self)
        '''
         Accounts are users that have access to strongDM. There are two types of accounts:
         1. **Users:** humans who are authenticated through username and password or SSO.
         2. **Service Accounts:** machines that are authenticated using a service token.

        See `strongdm.svc.Accounts`.
        '''
        self.control_panel = svc.ControlPanel(channel, self)
        '''
         ControlPanel contains all administrative controls.

        See `strongdm.svc.ControlPanel`.
        '''
        self.nodes = svc.Nodes(channel, self)
        '''
         Nodes make up the strongDM network, and allow your users to connect securely to your resources. There are two types of nodes:
         - **Gateways** are the entry points into network. They listen for connection from the strongDM client, and provide access to databases and servers.
         - **Relays** are used to extend the strongDM network into segmented subnets. They provide access to databases and servers but do not listen for incoming connections.

        See `strongdm.svc.Nodes`.
        '''
        self.resources = svc.Resources(channel, self)
        '''
         Resources are databases, servers, clusters, websites, or clouds that strongDM
         delegates access to.

        See `strongdm.svc.Resources`.
        '''
        self.role_attachments = svc.RoleAttachments(channel, self)
        '''
         RoleAttachments represent relationships between composite roles and the roles
         that make up those composite roles. When a composite role is attached to another
         role, the permissions granted to members of the composite role are augmented to
         include the permissions granted to members of the attached role.
         
         Deprecated: use multi-role via AccountAttachments instead.

        See `strongdm.svc.RoleAttachments`.
        '''
        self.role_grants = svc.RoleGrants(channel, self)
        '''
         RoleGrants represent relationships between composite roles and the roles
         that make up those composite roles. When a composite role is attached to another
         role, the permissions granted to members of the composite role are augmented to
         include the permissions granted to members of the attached role.
         
         Deprecated: use Role access rules instead.

        See `strongdm.svc.RoleGrants`.
        '''
        self.roles = svc.Roles(channel, self)
        '''
         A Role has a list of access rules which determine which Resources the members
         of the Role have access to. An Account can be a member of multiple Roles via
         AccountAttachments.

        See `strongdm.svc.Roles`.
        '''
        self.secret_stores = svc.SecretStores(channel, self)
        '''
         SecretStores are servers where resource secrets (passwords, keys) are stored.

        See `strongdm.svc.SecretStores`.
        '''

    def get_metadata(self, method_name, req):
        return [
            ('x-sdm-authentication', self.api_access_key),
            ('x-sdm-signature', self.sign(method_name,
                                          req.SerializeToString())),
            ('x-sdm-api-version', API_VERSION),
            ('x-sdm-user-agent', USER_AGENT),
        ]

    def sign(self, method_name, request_bytes):
        def hmac_digest(key, msg_byte_string):
            return hmac.new(key, msg=msg_byte_string,
                            digestmod=hashlib.sha256).digest()

        current_utc_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
        signing_key = hmac_digest(self.api_secret, current_utc_date.encode())
        signing_key = hmac_digest(signing_key, b'sdm_api_v1')

        hash = hashlib.sha256()

        hash.update(method_name.encode())
        hash.update(b'\n')
        hash.update(request_bytes)

        return base64.b64encode(hmac_digest(signing_key, hash.digest()))

    def jitterSleep(self, iter):
        dur_max = self.base_retry_delay * 2**iter
        if (dur_max > self.max_retry_delay):
            dur_max = self.max_retry_delay
        # get a value between 0 and max
        dur = random.random() * dur_max
        time.sleep(dur)

    def shouldRetry(self, iter, err):
        if (iter >= self.max_retries - 1):
            return False
        if not isinstance(err, grpc.RpcError):
            return True
        return err.code() == grpc.StatusCode.INTERNAL
