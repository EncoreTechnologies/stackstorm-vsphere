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
from vm_shutdown import VMShutdownGuest

__all__ = [
    'VMShutdownGuestTestCase'
]


class VMShutdownGuestTestCase(VsphereBaseActionTestCase):
    __test__ = True
    action_cls = VMShutdownGuest

    def test_normal(self):
        (action, mock_vm) = self.mock_one_vm('vm-12345')
        mock_vm.ShutdownGuest = mock.Mock()
        action.run(id=['vm-12345'])
        mock_vm.ShutdownGuest.assert_called_once_with()
