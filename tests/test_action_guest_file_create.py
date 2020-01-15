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
from guest_file_create import CreateTemporaryFileInGuest

__all__ = [
    'CreateTemporaryFileInGuestTestCase'
]


class CreateTemporaryFileInGuestTestCase(VsphereBaseActionTestCase):
    __test__ = True
    action_cls = CreateTemporaryFileInGuest

    def test_normal(self):
        (action, mock_vm) = self.mock_one_vm('vm-12345')
        mockFileMgr = mock.Mock()
        mockFileMgr.CreateTemporaryFileInGuest = mock.Mock()
        mockFileMgr.CreateTemporaryFileInGuest.return_value = '/tmp/foo.txt'
        action.si_content.guestOperationsManager = mock.Mock()
        action.si_content.guestOperationsManager.fileManager = mockFileMgr
        result = action.run(vm_id='vm-12345', username='u', password='p',
                            guest_directory='d', prefix='p', suffix='s')
        mockFileMgr.CreateTemporaryFileInGuest.assert_called_once_with(
            mock_vm, action.guest_credentials, 'p', 's', 'd'
        )
        self.assertEqual(result, '/tmp/foo.txt')
