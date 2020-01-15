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
import mock
from vsphere_base_action_test_case import VsphereBaseActionTestCase
from vm_resource_pool_get import GetVMResourcePool


__all__ = [
    'GetVMResourcePoolTestCase'
]


class GetVMResourcePoolTestCase(VsphereBaseActionTestCase):
    __test__ = True
    action_cls = GetVMResourcePool

    @mock.patch('vmwarelib.checkinputs.one_of_two_strings')
    @mock.patch('vmwarelib.inventory.get_virtualmachine')
    def test_run(self, mock_inventory, mock_check_inputs):
        action = self.get_action_instance(self.new_config)

        # Define test variables
        test_vm_id = "vm-123"
        test_vm_name = "test.vm.name"
        test_vsphere = "vsphere"
        test_si_content = "content"

        # Mock functions and results
        expected_result = "result"
        action.si_content = test_si_content
        mock_get_vm = mock.MagicMock()
        mock_get_vm.resourcePool.config.entity._moId = expected_result

        mock_inventory.return_value = mock_get_vm

        action.establish_connection = mock.MagicMock()
        mock_check_inputs.return_value = "check"

        result = action.run(test_vm_id, test_vm_name, test_vsphere)

        # Verify results
        self.assertEqual(result, expected_result)
        mock_check_inputs.assert_called_with(test_vm_id, test_vm_name, "ID or Name")
        mock_inventory.assert_called_with(test_si_content, moid=test_vm_id, name=test_vm_name)
        action.establish_connection.assert_called_with(test_vsphere)
