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

# import yaml
# from mock import Mock, MagicMock

from vsphere_base_action_test_case import VsphereBaseActionTestCase

from vm_hw_details_get import GetVMDetails


__all__ = [
    'GetVMDetailsTestCase'
]


class GetVMDetailsTestCase(VsphereBaseActionTestCase):
    __test__ = True
    action_cls = GetVMDetails

    def test_run_blank_input(self):
        action = self.get_action_instance(self.new_config)

        self.assertRaises(ValueError, action.run, vm_ids=None,
                          vm_names=None, vsphere="default")
