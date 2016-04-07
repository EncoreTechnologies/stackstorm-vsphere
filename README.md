# VSphere Integration Pack

This pack integrates with vsphere and allows for the creation and management of Virtual Machines.

## Connection Configuration

You will need to specificy the details of the vcenter instance you will be connecting to within the `config.yaml` file.

```yaml
  host:
  port:
  user:
  passwd:
```

## Actions

* `vsphere.vm_hw_basic_build` - Minstral Flow to Build Basic Server and power it on.
* `vsphere.vm_hw_cpu_mem_edit` - Adjust the CPU and RAM values assigned to a Virtual Machine
* `vsphere.vm_hw_detail_get` - Retrieve Vsphere Data about a virtual machine
* `vsphere.vm_hw_hdd_add` - Add a HardDrive Object to a Virtual Machine
* `vsphere.vm_hw_nic_add` - Add a Network Device to VM and attach to designated network.
* `vsphere.vm_hw_nic_edit` - Edit Network Device on Virtual machine (V0.2 only allows to switch network)
* `vsphere.vm_hw_power_off` - Perform VM Power off - Equivilant of Holding power button
* `vsphere.vm_hw_power_on` - Power on Virtual Machine
* `vsphere.vm_hw_scsi_controller_add` - Add SCSI HDD Controller device to VM
* `vsphere.vm_hw_uuid_get` - Retrieve VM UUID

