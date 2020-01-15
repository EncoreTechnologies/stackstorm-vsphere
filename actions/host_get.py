#!/usr/bin/env python
# Copyright 2019 Encore Technologies
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

from vmwarelib import inventory
from vmwarelib.serialize import HostGetJSONEncoder
from vmwarelib.actions import BaseAction
import json


class GetHost(BaseAction):
    def run(self, host_ids, host_names, vsphere=None):
        """
        Retrieve summary information for given Hosts (ESXi)

        Args:
        - host_ids: Moid of Host to retrieve
        - host_names: Name of Host to retrieve
        - vsphere: Pre-configured vsphere connection details (config.yaml)


        Returns:
        - dict: Host network hints details.
        """

        # TODO review using propertspec for retrieving all Hosts's at onces.
        results = {}
        if not host_ids and not host_names:
            raise ValueError("No IDs nor Names provided.")

        self.establish_connection(vsphere)

        if host_ids:
            for hid in host_ids:
                host = inventory.get_hostsystem(self.si_content, moid=hid)
                if host:
                    if host.name not in results:
                        results[host.name] = json.loads(json.dumps(host.summary,
                                                                   cls=HostGetJSONEncoder))
        if host_names:
            for host in host_names:
                host = inventory.get_hostsystem(self.si_content, name=host)
                if host:
                    if host.name not in results:
                        results[host.name] = json.loads(json.dumps(host.summary,
                                                                   cls=HostGetJSONEncoder))
        return results
