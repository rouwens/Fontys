Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.1.254 -Protocol https -User root -Password daan0409
Get-VM webserver-scaling-default| Get-HardDisk | Copy-HardDisk -DestinationPath "[Servers] scaling-webserver-3/HDD" -DestinationStorageFormat Thin
New-VM -Name scaling-webserver-3 -Datastore Servers -NumCPU 1 -MemoryGB 2 -NetworkName "Host-only" -Floppy -CD  -GuestID debian10_64Guest -DiskPath "[Servers] scaling-webserver-3/HDD.vmdk"
Start-VM -VM "scaling-webserver-3"
