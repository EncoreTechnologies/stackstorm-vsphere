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

from vmwarelib.guest import GuestAction
from pyVmomi import vim  # pylint: disable-msg=E0611


class StartProgramInGuest(GuestAction):

    def run(self, vm_id, username, password, command, arguments, workdir,
            envvar, vsphere=None):
        """
        Execute a program inside a guest.

        Args:
        - vm_id: MOID of the Virtual Machine
        - username: username to perform the operation
        - password: password of that user
        - command: command to run
        - arguments: [optional] command argument(s)
        - workdir: [optional] working directory
        - envvar: [optional] [array] environment variable(s)
        - vsphere: Pre-configured vsphere connection details (config.yaml)
        """
        self.prepare_guest_operation(vsphere, vm_id, username, password)
        cmdargs = arguments
        if not cmdargs:
            cmdargs = ''
        cmdspec = vim.vm.guest.ProcessManager.ProgramSpec(
            arguments=cmdargs,
            envVariables=envvar,
            programPath=command,
            workingDirectory=workdir)
        print(cmdspec)
        return self.guest_process_manager.StartProgramInGuest(
            self.vm, self.guest_credentials, cmdspec)
