Import-Module VMware.VimAutomation.Core
$vmName = 'Daan'
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.251.2 -Protocol https -User sa_gns3 -Password C9jZF3wEttlzrcqflxJZ
New-VM -Name $vmName -Datastore ESX03-Datastore1 -NumCPU 2 -MemoryGB 4 -DiskGB 100 -NetworkName 'OTA-VNR' -Floppy -CD -DiskStorageFormat Thin -GuestID ubuntu64Guest 

$vm = Get-VM -Name $vmName
$spec = New-Object VMware.Vim.VirtualMachineConfigSpec
$spec.nestedHVEnabled = $true
$vm.ExtensionData.ReconfigVM($spec)
Disconnect-VIServer -Server * -Force