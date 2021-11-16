copy_vm = "webserver"
new_vm = "webserver-2"


cmd1 = "Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false"
cmd2 = "Connect-VIServer -Server 192.168.1.254 -Protocol https -User root -Password daan0409"
cmd3 = "Get-VM " + copy_vm + "| Get-HardDisk | Copy-HardDisk -DestinationPath '[Servers] " + new_vm +"/HDD' -DestinationStorageFormat Thin"
cmd4 = "New-VM -Name " + new_vm +" -Datastore Servers -NumCPU 1 -MemoryGB 2 -NetworkName 'Host-only' -Floppy -CD  -GuestID debian10_64Guest -DiskPath '[Servers] " + new_vm + "/HDD.vmdk'"
cmd5 = "Start-VM -VM '" + new_vm+ "'"

print (cmd1)
print (cmd2)
print (cmd3)
print (cmd4)
print (cmd5)